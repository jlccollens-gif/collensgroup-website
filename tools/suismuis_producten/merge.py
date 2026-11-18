import json,sys
P='/home/claude/collensgroup-website/src/concept/suismuis/assets/scouting.js'
s=open(P).read(); head=s[:s.index('[')]; tail=s[s.rindex(']')+1:]
d=json.loads(s[s.index('['):s.rindex(']')+1])
ex=json.load(open(sys.argv[1])); have={x['nr'] for x in d}; n=a=0
for x in d:
    e=ex.get(str(x['nr']))
    if e: e={k:v for k,v in e.items() if k not in('n','p','c','s','t','id','nr','lt')}; x.update(e); x['f']=1; x['ok']=1; n+=1
for k,e in ex.items():
    if int(k) not in have and 'n' in e: e['f']=1; e['ok']=1; d.append(e); a+=1
d.sort(key=lambda x:x['nr'])
open(P,'w').write(head+json.dumps(d,ensure_ascii=False,separators=(',',':'))+tail)
print('bijgewerkt',n,'nieuw',a,'totaal',len(d))
