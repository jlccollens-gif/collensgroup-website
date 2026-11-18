import sys,os,io,concurrent.futures as cf,urllib.request,json
from PIL import Image
O='/home/claude/collensgroup-website/src/concept/suismuis/img/sc'
rows=[l.split('#') for l in open(sys.argv[1]).read().strip().split('\n')]
jobs=[]
for r in rows:
    nr=int(r[0])
    for i,f in enumerate(r[1].split()): jobs.append((nr,i,f))
def get(j):
    nr,i,f=j; dst=f'{O}/{nr}-{i+1}.jpg'
    if os.path.exists(dst): return 'skip'
    try:
        b=urllib.request.urlopen(urllib.request.Request(f'https://ae-pic-a1.aliexpress-media.com/kf/{f}',headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
        Image.open(io.BytesIO(b)).convert('RGB').save(dst,'JPEG',quality=90); return 'ok'
    except Exception as e: return 'ERR '+str(e)
with cf.ThreadPoolExecutor(10) as ex: res=list(ex.map(get,jobs))
print(len(res),[r for r in res if r.startswith('ERR')][:3])
