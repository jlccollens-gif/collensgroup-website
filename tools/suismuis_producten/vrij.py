import cv2,numpy as np
from PIL import Image
O='/home/claude/collensgroup-website/src/concept/suismuis/img/sc'
CREAM=(222,232,239) # BGR of #EFE8DE
def vrij(nr,i,tol=14):
    img=cv2.imread(f'{O}/{nr}-{i}.jpg'); h,w=img.shape[:2]
    m=np.zeros((h+2,w+2),np.uint8); out=img.copy()
    for (x,y) in [(2,2),(w-3,2),(2,h-3),(w-3,h-3),(w//2,2),(w//2,h-3)]:
        cv2.floodFill(out,m,(x,y),CREAM,(tol,)*3,(tol,)*3,cv2.FLOODFILL_FIXED_RANGE|8)
    filled=m[1:-1,1:-1].mean()
    S=max(h,w); c=np.full((S,S,3),CREAM,np.uint8); c[(S-h)//2:(S-h)//2+h,(S-w)//2:(S-w)//2+w]=out
    if S<1000: c=cv2.resize(c,(1000,1000),interpolation=cv2.INTER_LANCZOS4)
    cv2.imwrite(f'{O}/{nr}-v.jpg',c,[cv2.IMWRITE_JPEG_QUALITY,90]); return round(filled,2)
if __name__=='__main__':
    import sys
    for a in sys.argv[1:]:
        nr,i=a.split('-'); print(a,vrij(int(nr),int(i)))
