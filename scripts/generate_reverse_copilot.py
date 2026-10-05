"""Export verified V2 results as public data, SVG figures and accessible tables.

Usage: python scripts/generate_reverse_copilot.py --comparison <verified-folder>
The exporter uses only Python's standard library and never performs inference.
"""
import argparse, csv, hashlib, html, io, json, math, statistics
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MODELS = ('gpt-6.1-sol', 'opencode-go-responses/muse-spark-1.3-contributor')
APPROACHES = ('full-decompilation', 'static-summary', 'agent')
LABELS = ('Décompilation complète', 'Résumé statique', 'Agent autonome')
COLORS = ('#0072B2', '#D55E00', '#8C3FA6')

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def demand(ok, message):
    if not ok: raise ValueError(message)
def number(value): return f'{value:,.0f}'.replace(',', '\u202f')
def text(x,y,value,extra=''):
    return f'<text x="{x}" y="{y}" {extra}>{html.escape(str(value))}</text>'
def svg_start(title,description,height=750):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 {height}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(description)}</desc><rect width="920" height="{height}" fill="#fbfaf5"/><style>text{{font:16px Arial,sans-serif;fill:#17231f}}.title{{font:26px Georgia,serif}}.note{{font:14px Arial,sans-serif;fill:#56665e}}</style>'+text(38,44,title,'class="title"')
def legend(y):
    return ''.join(f'<rect x="{38+i*290}" y="{y-13}" width="14" height="14" fill="{color}"/>'+text(60+i*290,y,label,'class="note"') for i,(color,label) in enumerate(zip(COLORS,LABELS)))
def bars(groups,key,title,unit,limit=None):
    output=svg_start(title,'Deux panneaux indépendants, un par modèle. Valeurs et couvertures détaillées dans le tableau associé.')
    for mi,model in enumerate(MODELS):
        top=95+mi*310; rows=[g for g in groups if g['model']==model]
        ceiling=limit or math.ceil(max(g[key] for g in rows)/1000000)*1000000
        output+=text(38,top,'GPT · gpt-6.1-sol' if mi==0 else 'Muse Spark 1.3','class="title"')
        output+=text(38,top+25,f"Couverture : {rows[0]['token_intersection']}/20 challenges communs" if key=='tokens_sum' else 'Réponses correctes / 20 challenges','class="note"')
        for tick in range(5):
            x=280+tick*470/4; value=ceiling*tick/4
            output+=f'<path d="M{x} {top+45} V{top+205}" stroke="#d3d2c6"/>'+text(x,top+232,number(value),'text-anchor="middle" class="note"')
        for i,g in enumerate(rows):
            y=top+55+i*53
            output+=text(38,y+22,LABELS[i],'class="note"')
            output+=f'<rect x="280" y="{y}" width="{g[key]/ceiling*470:.3f}" height="31" rx="3" fill="{COLORS[i]}"/>'
            output+=text(768,y+23,number(g[key])+('/20' if key=='resolved' else ''))
        output+=text(515,top+266,unit,'text-anchor="middle" class="note"')
    return output+'</svg>'
def durations(cases):
    output=svg_start('Durées · distributions cumulées','Part des 20 cas dont la durée est inférieure ou égale au seuil. Réussites et échecs inclus, préparation exclue.',850)
    output+=legend(76)
    for mi,model in enumerate(MODELS):
        top=125+mi*345
        rows=[r for r in cases if r['model']==model]; ceiling=math.ceil(max(r['runtime_seconds'] for r in rows)/50)*50
        output+=text(38,top-8,'GPT · gpt-6.1-sol' if mi==0 else 'Muse Spark 1.3','class="title"')
        for tick in range(5):
            y=top+240-tick*55
            output+=f'<path d="M105 {y} H850" stroke="#d3d2c6"/>'+text(87,y+5,str(tick*25)+'%','text-anchor="end" class="note"')
            x=105+tick*745/4
            output+=text(x,top+265,f'{ceiling*tick/4:g}'.replace('.',','),'text-anchor="middle" class="note"')
        for ai,approach in enumerate(APPROACHES):
            values=sorted(r['runtime_seconds'] for r in rows if r['approach']==approach)
            points=[(105,top+240)]; count=len(values)
            for i,v in enumerate(values):
                x=105+v/ceiling*745;points.extend(((x,top+240-i/count*220),(x,top+240-(i+1)/count*220)))
            points.append((850,top+20))
            output+=f'<polyline points="'+ ' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="none" stroke="{COLORS[ai]}" stroke-width="3"'+'/>'
        output+=text(480,top+298,'Durée de réponse / investigation (secondes) · 20 cas par courbe','text-anchor="middle" class="note"')
    return output+'</svg>'
def table(caption,headers,rows):
    return '<div class="rc-table-scroll" tabindex="0" role="region" aria-label="'+html.escape(caption)+'"><table><caption>'+caption+'</caption><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<th scope="row">'+html.escape(str(v))+'</th>' if i==0 else '<td>'+html.escape(str(v))+'</td>' for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'
def generate(source,output):
    source=Path(source);raw=read(source/'comparison.json');validation=read(source/'validation.json');manifest=read(source/'manifest.json')
    demand(raw['status']=='completed' and validation['status']=='passed' and validation['cases']==120,'Comparison must be verified and complete.')
    demand(all(c['evaluation_matches'] and c['usage_matches'] and c['provenance_verified'] for c in validation['checks']),'Historical checks differ.')
    historical_code_changes=[]
    for filename, expected in manifest['fingerprints'].items():
        path=Path(filename)
        if not path.is_file() or sha(path)!=expected:
            if path.parent.name=='reverse_copilot' and path.suffix=='.py' and path.is_file():
                historical_code_changes.append(path.name)
            else:raise ValueError('Historical data fingerprint differs.')
    cases=[]
    for c in raw['cases']:
        usage=c['usage']; token=usage['totals']['totalTokens']
        complete=c['comparable'] and token['quality']=='reported' and token['coverage']=='complete' and token['value'] is not None
        cases.append(dict(challenge=c['challenge'],approach=c['approach'],model=c['model'],binary_sha256=c['sha256'],
            conclusion_valid=c['conclusion_valid'],answer_resolved=c['answer_resolved'],runtime_seconds=c['runtime_seconds'],
            total_tokens=token['value'] if complete else None,token_source=usage['canonical_source'],token_quality=token['quality'],
            token_coverage=token['coverage'],model_turns=c['model_turns'],corrections=c['corrections'],
            decompilations=c['decompilations'],interactive_calls=c['interactive_calls']))
    keys={(r['challenge'],r['approach'],r['model']) for r in cases}
    challenges=sorted({r['challenge'] for r in cases})
    demand(len(cases)==len(keys)==120 and len(challenges)==20,'Expected 120 unique cases.')
    demand(keys=={(c,a,m) for c in challenges for a in APPROACHES for m in MODELS},'Coverage differs.')
    cases.sort(key=lambda r:(MODELS.index(r['model']),APPROACHES.index(r['approach']),r['challenge']))
    groups=[]
    for model in MODELS:
        intersection=[c for c in challenges if all(next(r for r in cases if r['model']==model and r['approach']==a and r['challenge']==c)['total_tokens'] is not None for a in APPROACHES)]
        for approach in APPROACHES:
            rows=[r for r in cases if r['model']==model and r['approach']==approach]
            durations_values=[r['runtime_seconds'] for r in rows]
            resolved=sum(r['answer_resolved'] for r in rows)
            previous=next(g for g in raw['groups'] if g['model']==model and g['approach']==approach)
            demand(resolved==previous['answer_resolved'] and len(rows)==previous['cases'],'Score differs.')
            demand(math.isclose(statistics.median(durations_values),previous['runtime_seconds']['median']),'Duration differs.')
            groups.append(dict(model=model,approach=approach,cases=len(rows),resolved=resolved,
                valid_conclusions=sum(r['conclusion_valid'] for r in rows),token_intersection=len(intersection),
                tokens_sum=sum(r['total_tokens'] for r in rows if r['challenge'] in intersection),token_source=rows[0]['token_source'],
                seconds_median=statistics.median(durations_values),seconds_min=min(durations_values),seconds_max=max(durations_values)))
    example_case=next(c for c in raw['cases'] if c['challenge']=='password' and c['approach']=='agent' and c['model']==MODELS[0])
    finding=read(Path(example_case['report']).with_suffix('.json'))['answer']['findings'][0]
    trace=Path(example_case['trace']).read_text(encoding='utf-8')
    events=[json.loads(line) for line in trace.splitlines()]
    evidence=next(e['observation'] for e in events if e.get('event')=='tool' and e.get('evidence_id')==finding['evidence_id'])
    def strings(value):
        if isinstance(value,str):yield value
        elif isinstance(value,dict):
            for item in value.values():yield from strings(item)
        elif isinstance(value,list):
            for item in value:yield from strings(item)
    demand(evidence['status']=='success' and any(finding['excerpt'] in value for value in strings(evidence)), 'Evidence excerpt differs.')
    demand(any(finding['address'] in value for value in strings(evidence)), 'Evidence address differs.')
    public=dict(version='portfolio-v2-1',source_sha256=sha(source/'comparison.json'),validation_sha256=sha(source/'validation.json'),
        historical_code_changes=sorted(historical_code_changes),model_order=list(MODELS),approach_order=list(APPROACHES),cases=cases,groups=groups,
        evidence_example={k:finding[k] for k in ('claim','address','evidence_id','excerpt')},cost=None)
    output.mkdir(parents=True,exist_ok=True)
    files={'data.json':json.dumps(public,ensure_ascii=False,indent=2)+'\n','resolution.svg':bars(groups,'resolved','Résolution · trois approches','Réponses correctes',20),
        'tokens.svg':bars(groups,'tokens_sum','Tokens · comparaison sur les mêmes challenges','Tokens totaux rapportés'), 'durations.svg':durations(cases)}
    for name,rows in (('cases.csv',cases),('groups.csv',groups)):
        stream=io.StringIO(newline='');w=csv.DictWriter(stream,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows);files[name]=stream.getvalue()
    def short(model):return 'GPT 6.1 Sol' if model==MODELS[0] else 'Muse Spark 1.3'
    common=lambda g:[short(g['model'])+' · '+LABELS[APPROACHES.index(g['approach'])]]
    files['tables.html']=table('Résolution sur le corpus V2',['Modèle · approche','Conclusions valides','Réponses correctes'],[common(g)+[str(g['valid_conclusions'])+'/20',str(g['resolved'])+'/20'] for g in groups])
    files['tokens-table.html']=table('Tokens rapportés sur l’intersection commune',['Modèle · approche','Challenges communs','Tokens totaux','Source'],[common(g)+[str(g['token_intersection'])+'/20',number(g['tokens_sum']),g['token_source']] for g in groups])
    files['duration-table.html']=table('Durées des 20 cas par approche, échecs inclus',['Modèle · approche','Minimum s','Médiane s','Maximum s'],[common(g)+[f"{g['seconds_min']:.2f}",f"{g['seconds_median']:.2f}",f"{g['seconds_max']:.2f}"] for g in groups])
    files['duration-table.html']+= '<details><summary>Valeurs exactes des 120 cas</summary>'+table('Durées utilisées dans les courbes',['Challenge · modèle · approche','Durée s'],[[r['challenge']+' · '+short(r['model'])+' · '+LABELS[APPROACHES.index(r['approach'])],str(r['runtime_seconds'])] for r in cases])+'</details>'
    for name,content in files.items():
        demand(not any(marker in content for marker in ('C:\\','thread_id','threadId','turn_id','requestId','api_key','Bearer ')),'Private field detected.')
        if name.endswith('.svg'):ET.fromstring(content)
        (output/name).write_text(content,encoding='utf-8',newline='')
    page=ROOT/'projets/reverse-copilot.html'
    if output.resolve()==(ROOT/'assets/reverse-copilot').resolve() and page.exists():
        content=page.read_text(encoding='utf-8')
        for key,name in (('resolution','tables.html'),('tokens','tokens-table.html'),('durations','duration-table.html')):
            start='<!-- '+key+'-table:start -->';end='<!-- '+key+'-table:end -->'
            demand(start in content and end in content,'Missing table markers.')
            before,rest=content.split(start,1);_,after=rest.split(end,1)
            content=before+start+files[name]+end+after
        page.write_text(content,encoding='utf-8')
    print(json.dumps(dict(status='passed',cases=len(cases),groups=len(groups),token_intersections=[g['token_intersection'] for g in groups[::3]],files=len(files))))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--comparison',required=True,type=Path);parser.add_argument('--output-directory',type=Path,default=ROOT/'assets/reverse-copilot')
    args=parser.parse_args();generate(args.comparison,args.output_directory)
