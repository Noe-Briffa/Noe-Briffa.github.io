"""Verify public data, charts, page links and deterministic export output."""
import importlib.util,json,re,sys,tempfile,unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets/reverse-copilot'
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.cards=[];self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag in ('a','link') and a.get('href'):self.links.append(a['href'])
        if tag in ('img','script','source') and a.get('src'):self.links.append(a['src'])
        if tag=='a' and 'featured-link' in a.get('class','').split():self.cards.append(a['href'])
        if tag=='img':self.images.append(a)
def parse(path):
    page=Page();page.feed(path.read_text(encoding='utf-8'));return page

class PortfolioTests(unittest.TestCase):
    def test_coverage_scores_and_missing_tokens(self):
        data=json.loads((ASSETS/'data.json').read_text(encoding='utf-8'));cases=data['cases'];groups=data['groups']
        self.assertEqual(len(cases),120);self.assertEqual(len({(c['challenge'],c['model'],c['approach']) for c in cases}),120)
        self.assertEqual([g['resolved'] for g in groups],[19,18,19,19,18,19])
        self.assertEqual([g['token_intersection'] for g in groups],[20,20,20,19,19,19])
        self.assertEqual(sum(c['total_tokens'] is None for c in cases),1)
        for g in groups:
            models=[r for r in cases if r['model']==g['model']]
            ids={r['challenge'] for r in models if r['total_tokens'] is None}
            self.assertEqual(g['tokens_sum'],sum(r['total_tokens'] for r in models if r['approach']==g['approach'] and r['challenge'] not in ids))
    def test_order_and_unaffected_catalog_entries(self):
        self.assertEqual(parse(ROOT/'index.html').cards,['projets/reverse-copilot.html','projets/colorisation.html','projets/local-rag.html'])
        self.assertEqual(parse(ROOT/'projets/index.html').cards,['reverse-copilot.html','colorisation.html','local-rag.html','warungfit.html','local-second-brain.html'])
        self.assertNotRegex((ROOT/'styles.css').read_text(encoding='utf-8'),r'featured-link:nth-child')
        self.assertNotIn("cards[",(ROOT/'index.html').read_text(encoding='utf-8'))
    def test_links_images_and_anchor_targets(self):
        for path in [ROOT/'index.html',*sorted((ROOT/'projets').glob('*.html'))]:
            page=parse(path)
            for link in page.links:
                url=urlsplit(link)
                if url.scheme or url.netloc:continue
                target=(path.parent/unquote(url.path)).resolve() if url.path else path
                with self.subTest(page=path.name,link=link):
                    self.assertTrue(target.is_relative_to(ROOT));self.assertTrue(target.exists())
                    if url.fragment and target.suffix=='.html':self.assertIn(url.fragment,parse(target).ids)
            self.assertTrue(all('alt' in image for image in page.images),path.name)
    def test_svg_validity_and_no_private_data(self):
        for name in ('thumbnail.svg','architecture.svg','resolution.svg','tokens.svg','durations.svg'):
            doc=ET.parse(ASSETS/name);self.assertTrue(doc.getroot().find('{http://www.w3.org/2000/svg}title') is not None)
        for name in ('data.json','cases.csv','groups.csv','method.md'):
            content=(ASSETS/name).read_text(encoding='utf-8')
            for marker in ('C:\\','requestId','thread_id','Bearer ','api_key'):self.assertNotIn(marker,content)
        data=json.loads((ASSETS/'data.json').read_text(encoding='utf-8'))
        self.assertEqual(data['evidence_example']['evidence_id'],'E003')
        self.assertIn('strcmp',data['evidence_example']['excerpt'])
    def test_accessible_tables_match_figures(self):
        page=(ROOT/'projets/reverse-copilot.html').read_text(encoding='utf-8')
        for marker in ('resolution','tokens','durations'):
            fragment=page.split('<!-- '+marker+'-table:start -->')[1].split('<!-- '+marker+'-table:end -->')[0]
            self.assertIn('<caption>',fragment);self.assertIn('scope="col"',fragment);self.assertIn('scope="row"',fragment)
        self.assertEqual(page.count('class="rc-chart"'),3)
        self.assertTrue((ASSETS/'share.png').is_file())
    def test_repeat_generation(self):
        if not SOURCE:self.skipTest('Pass --comparison to verify original-source replay.')
        spec=importlib.util.spec_from_file_location('exporter',ROOT/'scripts/generate_reverse_copilot.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            first=Path(directory)/'a';second=Path(directory)/'b';module.generate(SOURCE,first);module.generate(SOURCE,second)
            for file in first.iterdir():self.assertEqual(file.read_bytes(),(second/file.name).read_bytes());self.assertEqual(file.read_bytes(),(ASSETS/file.name).read_bytes())
    def test_modified_historical_data_is_rejected(self):
        spec=importlib.util.spec_from_file_location('exporter',ROOT/'scripts/generate_reverse_copilot.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            source=Path(directory)/'source';source.mkdir();artifact=source/'report.json';artifact.write_text('altered')
            for name,value in (('comparison.json',{'status':'completed'}),('validation.json',{'status':'passed','cases':120,'checks':[]}),('manifest.json',{'fingerprints':{str(artifact):'0'*64}})):
                (source/name).write_text(json.dumps(value))
            output=Path(directory)/'out'
            with self.assertRaisesRegex(ValueError,'Historical data fingerprint differs'):module.generate(source,output)
            self.assertFalse(output.exists())
    def test_bad_source_fails_closed(self):
        spec=importlib.util.spec_from_file_location('exporter',ROOT/'scripts/generate_reverse_copilot.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            source=Path(directory)/'source';source.mkdir()
            for name,value in (('comparison.json',{'status':'error'}),('validation.json',{'status':'passed'}),('manifest.json',{})):(source/name).write_text(json.dumps(value))
            output=Path(directory)/'out'
            with self.assertRaises(ValueError):module.generate(source,output)
            self.assertFalse(output.exists())

SOURCE=None
if __name__=='__main__':
    if '--comparison' in sys.argv:
        i=sys.argv.index('--comparison');SOURCE=Path(sys.argv[i+1]);del sys.argv[i:i+2]
    unittest.main()
