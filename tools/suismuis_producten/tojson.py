import json,sys,re
def slug(s): 
    s=s.lower().translate(str.maketrans('éèëêïöüà','eeeeioua')); return re.sub(r'[^a-z0-9]+','-',s).strip('-')[:40]
out={}
for l in open(sys.argv[1]).read().strip().split('\n'):
    r=l.split('#'); nr=int(r[0]); imgs=r[1].split()
    e={'img':f'sc/{nr}-v','u':[f'img/sc/{nr}-v.jpg']+[f'img/sc/{nr}-{i+1}.jpg' for i in range(len(imgs))]}
    if r[2]: e['var']=[{'n':v.split(':',1)[1],'b':f"img/sc/{nr}-{v.split(':')[0]}.jpg"} for v in r[2].split('|')]
    e['spec']=[['Materiaal',r[3]],['Afmetingen',r[4]]]
    e['m']=r[3].rstrip('.')+'.'; e['d']=r[4]
    if len(r)>5 and r[5]:
        e.update(n=r[5],p=float(r[6]),c=r[7],s=r[8],t=r[9],lt='8–15 werkdagen',nr=nr,id=f's{nr}-'+slug(r[5]))
    out[str(nr)]=e
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False); print(len(out))
