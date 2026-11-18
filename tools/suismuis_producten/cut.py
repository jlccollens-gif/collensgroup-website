import cv2, numpy as np, glob, re, sys, os
from PIL import Image, ImageFilter
O='/home/claude/collensgroup-website/src/concept/suismuis/img/sc'
def vind(path):
    img=cv2.imread(path); h,w=img.shape[:2]
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); g=cv2.GaussianBlur(g,(5,5),0)
    best=None
    for lo,hi in [(30,90),(15,60),(50,150)]:
        e=cv2.Canny(g,lo,hi); e=cv2.dilate(e,np.ones((3,3)),1)
        cs,_=cv2.findContours(e,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        for c in cs:
            a=cv2.contourArea(c)
            if a<0.06*w*h or a>0.92*w*h: continue
            p=cv2.approxPolyDP(c,0.02*cv2.arcLength(c,True),True)
            if len(p)!=4 or not cv2.isContourConvex(p): continue
            x,y,bw,bh=cv2.boundingRect(p)
            if a/(bw*bh)<0.85: continue
            if best is None or a>best[0]: best=(a,p.reshape(4,2))
        if best: break
    return img,best
def orden(p):
    s=p.sum(1); d=np.diff(p,axis=1).ravel()
    return np.array([p[s.argmin()],p[d.argmin()],p[s.argmax()],p[d.argmax()]],dtype='float32')
def maak(src,dst,bg=(239,232,222)):
    img,b=vind(src)
    if not b: return False
    q=orden(b[1]); wA=max(np.linalg.norm(q[0]-q[1]),np.linalg.norm(q[3]-q[2])); hA=max(np.linalg.norm(q[0]-q[3]),np.linalg.norm(q[1]-q[2]))
    M=cv2.getPerspectiveTransform(q,np.array([[0,0],[wA,0],[wA,hA],[0,hA]],dtype='float32'))
    war=cv2.warpPerspective(img,M,(int(wA),int(hA)))
    war=war[3:-3,3:-3]
    art=Image.fromarray(cv2.cvtColor(war,cv2.COLOR_BGR2RGB))
    L=max(art.size); f=min(1100/L,1.6); art=art.resize((int(art.width*f),int(art.height*f)),Image.LANCZOS)
    S=int(max(art.size)/0.74); m=0
    c=Image.new('RGB',(S,S),bg)
    sh=Image.new('L',(S,S),0); x=(S-art.width)//2; y=(S-art.height)//2
    sh.paste(90,(x+10,y+16,x+art.width+10,y+art.height+16)); sh=sh.filter(ImageFilter.GaussianBlur(18))
    c.paste(Image.new('RGB',(S,S),(150,130,110)),(0,0),sh); c.paste(art,(x,y))
    c.save(dst,quality=90); return art.size
if __name__=='__main__':
    for a in sys.argv[1:]:
        nr,i=a.split('-'); print(a,maak(f'{O}/{a}.jpg',f'/tmp/cut-{a}.jpg'))
