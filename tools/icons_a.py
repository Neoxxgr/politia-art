import math,os,sys
N="#1e2f55";B="#3d5a8c";L="#e8edf5";G="#d4a42a";W="#fff"
GR="#5a9e4b";DG="#3f7a3a";RED="#b8433a";WD="#8a5a3c";LW="#c08a55";ST="#9aa3ad";CO="#c9ced6";SL="#7d8794";BL="#222833"
GL="#a8c8e8";WA="#3f8fd0";YE="#e8c547";OR="#d9822b";SA="#d9c39a";TU="#3fb8b0";SK="#e0b18f";BN="#4f8a5b"
A=f'stroke="{N}" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"'
def sh(d,f,sw=6): return f'<path d="{d}" fill="{f}" {A%sw}/>'
def pa(d,c=N,sw=6): return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'
def ci(cx,cy,r,f,sw=6): return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{f}" {A%sw}/>' if sw else f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{f}"/>'
def el(cx,cy,rx,ry,f,sw=6,rot=0):
    t=f' transform="rotate({rot} {cx:.1f} {cy:.1f})"' if rot else ''
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx}" ry="{ry}" fill="{f}" {A%sw}{t}/>'
def rc(x,y,w,h,f,rx=0,sw=6): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" {A%sw}/>'
def ln(x1,y1,x2,y2,c=N,sw=6): return pa(f"M{x1} {y1}L{x2} {y2}",c,sw)
def pg(pts,f,sw=6): return sh("M"+"L".join(f"{x:.1f} {y:.1f}" for x,y in pts)+"Z",f,sw)
GROUND=f'<rect x="20" y="214" width="216" height="8" fill="{N}"/>'
def P(a,r,cx=128,cy=128): return (cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))

def person(x,b,s,body,head=SK):
    bd=f"M{x-30*s} {b}C{x-30*s} {b-40*s} {x-18*s} {b-48*s} {x} {b-48*s}C{x+18*s} {b-48*s} {x+30*s} {b-40*s} {x+30*s} {b}Z"
    return sh(bd,body)+ci(x,b-48*s-12*s,15*s,head)
def stack(cx,yb,n,rx=32,ry=12,h=20):
    o=''
    for i in range(n):
        y=yb-i*h
        o+=el(cx,y,rx,ry,G)+sh(f"M{cx-rx} {y}v-{h}h{2*rx}v{h}",G)
    o+=el(cx,yb-n*h,rx,ry,G)
    return o
def star(cx,cy,ro,ri,n=5):
    pts=[]
    for i in range(2*n):
        r=ro if i%2==0 else ri
        pts.append(P(-90+i*180/n,r,cx,cy))
    return pts

I={}
I['money']=rc(40,70,150,86,BN,8)+ci(115,113,22,L)+f'<g stroke="{N}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" fill="{G}"><ellipse cx="160" cy="206" rx="52" ry="14"/><path d="M108 206v-14h104v14"/><ellipse cx="160" cy="192" rx="52" ry="14"/><path d="M108 192v-14h104v14"/><ellipse cx="160" cy="178" rx="52" ry="14"/></g>'
I['gold']=(pg([(28,216),(44,152),(108,152),(122,216)],G)+pg([(134,216),(148,152),(212,152),(228,216)],G)+pg([(80,152),(96,90),(160,90),(176,152)],G)
  +ln(56,166,98,166,L,5)+ln(160,166,202,166,L,5)+ln(104,104,146,104,L,5))
I['goods']=(rc(40,44,176,170,LW,6)+rc(40,44,34,170,WD)+rc(182,44,34,170,WD)+ln(74,100,182,100,WD,5)+ln(74,158,182,158,WD,5)
  +pa("M78 62L178 196",WD,14)+pa("M78 62L178 196",N,3))
I['food']=(ln(66,214,66,66,N,6)+''.join(el(66+dx,y,10,19,YE,5,rot) for dx,y,rot in [(-17,100,-30),(17,100,30),(-17,132,-30),(17,132,30),(-17,164,-30),(17,164,30)])+el(66,62,9,20,YE,5)
  +sh("M96 196C96 160 130 146 168 146C206 146 230 164 230 192C230 212 214 218 196 218H118C104 218 96 210 96 196Z",LW)
  +pa("M138 154L146 190M168 150L174 190M198 156L200 190",WD,6))
I['energy']=pg([(148,26),(66,144),(118,144),(96,230),(190,104),(138,104)],YE)
I['influence']=(ci(128,128,98,G)+person(66,196,1.3,B)+person(190,196,1.3,B)+person(128,210,1.6,N))
I['military']=(sh("M32 170A96 96 0 0 1 224 170Z",DG)+rc(24,164,208,30,DG,14)+pa("M128 78V150",N,5)+rc(112,100,32,26,G,6)+ln(70,176,70,176,L,6))
I['military']=(sh("M32 168A96 96 0 0 1 224 168Z",DG)+rc(22,162,212,30,DG,14)+ln(60,150,196,150,G,8)+pa("M104 82Q128 70 152 82",L,6))
fl=("M108 40V100L46 198Q38 216 60 216H196Q218 216 210 198L148 100V40Z")
I['research']=(sh(fl,L)+sh("M78 148H178L210 198Q218 216 196 216H60Q38 216 46 198Z",TU)+rc(96,28,64,16,L,6)+ci(112,186,7,L,4)+ci(146,170,5,L,4)+ci(156,196,8,L,4))
I['intel']=(sh("M28 128Q128 36 228 128Q128 220 28 128Z",L)+ci(128,128,42,B)+ci(128,128,18,N,4)+ci(116,116,7,W,0))
I['users']=(person(56,226,1.3,B)+person(200,226,1.3,B)+person(128,228,1.7,SL))
I['user']=person(128,226,2.2,ST)
I['happiness']=(ci(128,128,98,G)+ci(128,128,76,YE)+ci(98,106,10,N,0)+ci(158,106,10,N,0)+pa("M86 140Q128 196 170 140",N,8))
I['stability']=(sh("M128 28L212 56V124Q212 188 128 228Q44 188 44 124V56Z",B)+sh("M128 52L192 74V124Q192 172 128 204Q64 172 64 124V74Z",L,4)+ci(128,124,26,G))
I['approval']=(sh("M88 122L118 72Q124 36 150 42Q170 52 158 98H206Q226 100 224 120Q222 130 214 136Q224 148 214 160Q220 172 210 182Q214 196 200 204Q192 216 172 216H88Z",SK)
  +pa("M168 136H212M170 160H208M168 184H202",N,5)+rc(28,116,52,104,B,8)+rc(28,116,52,18,G,6))
I['home']=(GROUND+rc(60,112,136,102,SA,0)+pg([(36,120),(128,44),(220,120)],N)+rc(110,158,36,56,WD)+rc(72,134,26,26,GL,0,5)+rc(158,134,26,26,GL,0,5)+ci(138,188,3,G,0))
def globe(cx,cy,r,grid):
    o=f'<defs><clipPath id="c"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath></defs>'+ci(cx,cy,r,WA)
    o+=f'<g clip-path="url(#c)">'+sh(f"M{cx-60} {cy-40}C{cx-30} {cy-70} {cx} {cy-50} {cx-6} {cy-20}C{cx-10} {cy} {cx-40} {cy+4} {cx-66} {cy+10}C{cx-80} {cy-10} {cx-80} {cy-30} {cx-60} {cy-40}Z",GR,5)
    o+=sh(f"M{cx+20} {cy+8}C{cx+50} {cy-8} {cx+80} {cy+4} {cx+78} {cy+34}C{cx+70} {cy+66} {cx+40} {cy+84} {cx+26} {cy+60}C{cx+14} {cy+40} {cx+8} {cy+20} {cx+20} {cy+8}Z",GR,5)
    o+=sh(f"M{cx+20} {cy-60}C{cx+40} {cy-76} {cx+66} {cy-60} {cx+56} {cy-40}C{cx+44} {cy-30} {cx+24} {cy-34} {cx+20} {cy-60}Z",GR,5)+'</g>'
    if grid: o+=pa(f"M{cx-r} {cy}H{cx+r}",N,4)+f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.42:.0f}" ry="{r}" fill="none" stroke="{N}" stroke-width="4"/>'
    o+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" {A%6}/>'
    return o
I['globe']=globe(128,112,84,True)+rc(120,196,16,16,G,0,5)+rc(88,210,80,14,B,5)
I['world']=globe(128,128,98,False)
I['columns']=(GROUND+ln(128,22,128,48,N,5)+pg([(128,26),(166,36),(128,46)],G,4)
  +pg([(28,112),(128,54),(228,112)],L)+ci(128,92,10,G,5)+rc(34,112,188,18,CO)+''.join(rc(x,130,24,58,L,4) for x in (48,86,130,168)[:0])
  +''.join(rc(x,130,22,60,L,4) for x in (46,82,118,154,190))+rc(34,190,188,12,CO)+rc(24,202,208,12,CO))
I['bank']=(GROUND+pg([(28,106),(128,48),(228,106)],ST)+ci(128,88,16,G)+rc(34,106,188,18,CO)
  +''.join(rc(x,124,32,68,ST,4) for x in (52,112,172))+rc(34,192,188,12,CO)+rc(24,204,208,10,CO,0,5))
I['ballot']=(rc(96,34,66,80,L,4)+pa("M112 70L126 84L148 56",GR,8)+rc(48,106,160,108,B,8)+rc(38,96,180,22,N,8)+rc(48,148,160,14,G,0,5))
I['handshake']=(rc(24,80,50,100,N,8)+rc(24,148,50,18,G,4)+rc(182,80,50,100,B,8)+rc(182,148,50,18,G,4)
  +sh("M70 96H140Q150 96 158 104L184 126V170H110Q100 170 92 164L70 150Z",SK)+sh("M186 94H150Q136 94 130 104Q124 114 138 120L166 136L186 156Z",SK)
  +''.join(ln(x,132,x,160,N,5) for x in (112,126,140))+ln(166,140,166,140,N,4))
I['chat']=(sh("M56 44H200Q228 44 228 72V132Q228 160 200 160H120L72 204V160H56Q28 160 28 132V72Q28 44 56 44Z",B)+''.join(ci(x,102,11,L,0) for x in (82,128,174)))
I['mail']=(rc(28,56,200,144,L,12)+pa("M32 68L128 140L224 68",N,6)+ci(128,148,15,G))
I['bell']=(ci(128,38,12,G)+sh("M128 54C80 54 76 100 72 140C70 164 52 176 52 186H204C204 176 186 164 184 140C180 100 176 54 128 54Z",G)+rc(48,184,160,14,B,6)+ci(128,214,14,B)+pa("M96 80Q84 110 84 140",L,5))
I['wrench']=(rc(100,110,126,36,SL,16)+ci(210,128,7,L,4)+sh("M28.9 112A46 46 0 1 1 28.9 144H72V112Z",SL))
I['clock']=(ci(128,128,98,B)+ci(128,128,78,L)+''.join(pa(f"M{P(a*30,66)[0]:.1f} {P(a*30,66)[1]:.1f}L{P(a*30,(52 if a%3==0 else 58))[0]:.1f} {P(a*30,(52 if a%3==0 else 58))[1]:.1f}",N,(6 if a%3==0 else 4)) for a in range(12))
  +ln(128,128,128,70,N,8)+ln(128,128,168,150,N,8)+ci(128,128,9,G,5))
I['alert']=pg([(128,32),(230,208),(26,208)],YE)+ln(128,96,128,150,N,15)+ci(128,180,9,N,4)
I['info']=ci(128,128,98,B)+ci(128,128,80,B,0).replace('fill="'+B+'"','fill="none" stroke="'+G+'" stroke-width="5"')+ci(128,78,12,L,0)+ln(128,110,128,178,L,22)
bars=[(40,50,B),(88,86,B),(136,124,B),(184,166,GR)]
I['chart']=''.join(rc(x,214-h,36,h,c,4) for x,h,c in bars)+rc(24,214,208,10,N,0,4)
I['coins']=stack(58,214,3)+stack(128,214,6)+stack(198,214,4)
def chev(x0,f): return sh(f"M{x0} 44H{x0+38}L{x0+120} 128L{x0+38} 212H{x0}L{x0+82} 128Z",f)
I['chev']=chev(34,G)+chev(80,B)
I['crown']=(sh("M42 190L32 88L88 136L128 72L168 136L224 88L214 190Z",G)+rc(38,186,180,30,G,6)+''.join(ci(x,y,11,G) for x,y in ((32,84),(128,66),(224,84)))+ci(78,201,8,RED,4)+ci(128,201,8,WA,4)+ci(178,201,8,RED,4))
I['star']=pg(star(128,134,100,42),G)
rays=''
for k in range(12):
    a=k*30
    p1=P(a-9,66);p2=P(a+9,66);t=P(a,102)
    rays+=pg([p1,t,p2],OR if False else G,5)
I['sun']=rays+ci(128,128,56,YE)
I['anchor']=(pa("M46 150Q60 214 128 214Q196 214 210 150",N,32)+pa("M46 150Q60 214 128 214Q196 214 210 150",SL,20)
  +pg([(22,160),(46,128),(72,162)],SL)+pg([(234-0,160),(210,128),(184,162)],SL).replace('234.0','230.0')
  +rc(118,62,20,146,SL,4)+rc(84,86,88,16,SL,8)+rc(118,134,20,14,G,0,4)+ci(128,46,20,SL)+ci(128,46,8,W,4))
leaf=''
stem=''
for side in (-1,1):
    arc=[]
    for i in range(8):
        a=100+i*18 if side==-1 else 80-i*18
        # left branch uses angles 100..226 ; right mirrored
        px,py=P(a,76)
        tang=a+(90 if side==-1 else -90)
        leaf+=el(px+(-0)*0,py,22,10,GR if i%2 else DG,5,tang+30 if side==-1 else tang-30)
        ox,oy=P(a,100)
        leaf+=el((px+ox)/2+ (ox-px)*0.0 ,(py+oy)/2,0.1,0.1,GR,0)
I['laurel']=pa(f"M{P(100,76)[0]:.1f} {P(100,76)[1]:.1f}A76 76 0 0 1 {P(235,76)[0]:.1f} {P(235,76)[1]:.1f}",DG,6)+pa(f"M{P(80,76)[0]:.1f} {P(80,76)[1]:.1f}A76 76 0 0 0 {P(-55,76)[0]:.1f} {P(-55,76)[1]:.1f}",DG,6)
lv=''
for side in (-1,1):
    for i in range(7):
        a=100+i*20 if side==-1 else 80-i*20
        px,py=P(a,76)
        out=P(a,95); inn=P(a,57)
        rot=a+90 if side==-1 else a-90
        for pt,rr in ((out,rot-40*side*-1),(inn,rot+40*side*-1)):
            lv+=el(pt[0],pt[1],22,10,GR if i%2 else DG,5,a+(0 if True else 0)+ (35 if pt is out else -35)*(1 if side==-1 else -1)+90*(0))
I['laurel']+=lv+ci(128,206,12,G)+ci(110,222,0.1,G,0)
I['flame']=sh("M128 28C140 80 200 100 200 160C200 204 168 228 128 228C88 228 56 204 56 160C56 130 76 112 88 92C92 114 104 124 112 124C100 90 108 56 128 28Z",OR)+sh("M128 124C140 150 168 164 168 192C168 212 150 222 128 222C106 222 88 212 88 192C88 160 118 150 128 124Z",YE,5)
I['key']=rc(120,114,106,26,G,6)+rc(186,138,14,32,G,4)+rc(208,138,18,24,G,4)+ci(78,128,48,G)+ci(78,128,17,W,5)
cr=[(128,90,58),(76,132,42),(180,132,42),(128,140,52)]
I['tree']=(rc(112,140,32,78,WD)+''.join(ci(x,y,r+0,N,12) for x,y,r in cr)+''.join(ci(x,y,r,GR,0) for x,y,r in cr)+ci(150,160,20,DG,0)+ci(98,128,12,DG,0)+ci(142,92,12,DG,0))
I['compass']=(ci(128,30,13,SL,5).replace('fill="'+SL+'"','fill="none"')+rc(112,38,32,16,G,4)+ci(128,138,88,SL)+ci(128,138,68,L)
  +''.join(ln(*[round(v,1) for v in (*P(a*45,62,128,138),*P(a*45,(50 if a%2==0 else 54),128,138))],N,5) for a in range(8))
  +'<g transform="rotate(35 128 138)">'+pg([(128,76),(142,138),(114,138)],RED,5)+pg([(142,138),(128,200),(114,138)],L,5)+'</g>'+ci(128,138,8,G,4))
I['flag']=(rc(60,28,12,196,SL,4)+ci(66,30,10,G,5)+sh("M72 46Q112 28 150 46T228 46V144Q190 162 150 144T72 144Z",B)+ci(150,96,22,G,5)+rc(40,214,52,12,N,4))
I['logout']=(rc(34,36,110,184,BL,8)+rc(34,36,40,184,LW,8)+ci(60,130,6,G,4)+rc(110,114,66,28,G,8)+pg([(168,88),(228,128),(168,168)],G))
gp=[]
for k in range(8):
    a=k*45
    for da,r in ((-14,70),(-9,94),(9,94),(14,70)): gp.append(P(a+da,r))
I['gear']=pg(gp,B)+ci(128,128,38,G)+ci(128,128,16,L,5)
I['book']=(sh("M26 74V198Q78 184 128 206Q178 184 230 198V74Z",B)+sh("M128 68Q84 48 38 62V180Q84 168 128 190Z",L)+sh("M128 68Q172 48 218 62V180Q172 168 128 190Z",L)
  +''.join(pa(f"M{x1} {y}Q{x1+22} {y-8} {x1+44} {y-2}",ST,4) for x1 in (60,) for y in (96,116,136))+''.join(pa(f"M{x1} {y}Q{x1+22} {y-8} {x1+44} {y-2}",ST,4) for x1 in (152,) for y in (96,116,136))+sh("M120 188V222L128 214L136 222V188Z",G,4))
I['heart']=sh("M128 214C40 150 28 100 52 70C76 42 118 56 128 88C138 56 180 42 204 70C228 100 216 150 128 214Z",RED)+pa("M62 92Q66 78 82 74",L,7)
I['scale']=(rc(80,212,96,14,B,5)+rc(120,56,16,156,B,4)+rc(44,66,168,14,G,7)+ci(128,46,12,G)
  +''.join(pa(f"M{cx} 80L{cx-22} 150M{cx} 80L{cx+22} 150",N,4) for cx in (50,206))
  +''.join(sh(f"M{cx-26} 150H{cx+26}Q{cx+26} 184 {cx} 184Q{cx-26} 184 {cx-26} 150Z",G) for cx in (50,206)))
I['leaf']=sh("M128 28C204 70 214 140 128 200C42 140 52 70 128 28Z",GR)+ln(128,200,128,226,DG,8)+pa("M128 56V200",DG,5)+pa("M128 100L98 76M128 100L158 76M128 140L92 112M128 140L164 112",DG,4)
I['megaphone']=('<g transform="translate(10 0)">'+rc(100,150,24,58,N,8)+sh("M66 100L184 52V204L66 156Z",RED)+rc(24,100,48,56,B,12)+rc(176,40,20,176,G,8)+'</g>'+pa("M218 100Q232 128 218 156",N,6))
I['hammer']=rc(84,112,144,34,WD,12)+rc(40,56,80,144,SL,12)+ln(58,76,58,180,L,7)
I['plane']=(pg([(168,112),(196,52),(224,52),(222,114)],B)+rc(26,104,196,58,L,29)+pg([(98,140),(144,140),(116,200),(82,200)],B)+''.join(ci(x,126,6,B,4) for x in (84,112,140,168))+ln(60,148,200,148,G,6)+pa("M44 120Q54 108 70 108",B,6))

def write(name,body):
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256"><rect width="256" height="256" fill="#ffffff"/>{body}</svg>\n'
    open(f"/home/claude/artwork/sketches/icons-a/icon~{name}.svg","w").write(s)
import json
ids=[j['id'].split('/')[1] for j in json.load(open('/home/claude/artwork/jobs/icons-a.json'))]
miss=[i for i in ids if i not in I]
print('missing',miss)
for i in ids: write(i,I[i])
