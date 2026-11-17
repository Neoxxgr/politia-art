import math,os
OUT='/home/claude/artwork/sketches/icons-b/'
N='#1e2f55';B='#3d5a8c';L='#e8edf5';G='#d4a42a';GR='#5a9e4b';DG='#3f7a3a';R='#b8433a';WB='#8a5a3c';LW='#c08a55';ST='#9aa3ad';CO='#c9ced6';SS='#7d8794';K='#222833';GL='#a8c8e8';WA='#3f8fd0';Y='#e8c547';O='#d9822b';SA='#d9c39a';P='#7b5ea7'
def f(c): return f'fill="{c}"'
def rect(x,y,w,h,c,rx=0,sw=None): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" {f(c)}'+(f' stroke-width="{sw}"' if sw else '')+'/>'
def circ(x,y,r,c,sw=None): return f'<circle cx="{x}" cy="{y}" r="{r}" {f(c)}'+(f' stroke-width="{sw}"' if sw else '')+'/>'
def ell(x,y,rx,ry,c): return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" {f(c)}/>'
def path(d,c,sw=None): return f'<path d="{d}" {f(c)}'+(f' stroke-width="{sw}"' if sw else '')+'/>'
def line(x1,y1,x2,y2,sw=4,c=N): return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{c}" stroke-width="{sw}"/>'
def poly(pts,c,sw=None): return f'<polygon points="{" ".join(f"{a},{b}" for a,b in pts)}" {f(c)}'+(f' stroke-width="{sw}"' if sw else '')+'/>'
def tr(s,t): return f'<g transform="{t}">{s}</g>'
icons={}
# seasons
def flower(x,y):
    return ''.join(circ(x+14*math.cos(a*1.2566+.3),y+14*math.sin(a*1.2566+.3),11,'#f4b8c8',4) for a in range(5))+circ(x,y,7,G,4)
icons['season~0']=path('M28 206Q90 184 130 130Q170 80 224 56','none',12)+path('M28 206Q90 184 130 130Q170 80 224 56','none',6).replace(N,WB).replace('stroke-width="6"','stroke="#8a5a3c" stroke-width="6"').replace('fill="none"','fill="none"')+path('M110 150Q96 120 70 124Q84 150 110 150Z',GR,4)+flower(60,180)+flower(104,100)+flower(160,150)+flower(190,70)+flower(146,56)
icons['season~1']=''.join(line(128+68*math.cos(i*math.pi/4),128+68*math.sin(i*math.pi/4),128+98*math.cos(i*math.pi/4),128+98*math.sin(i*math.pi/4),14) for i in range(8))+circ(128,128,52,Y)+circ(128,128,52,'none',0)[:0]
leaf='<path d="M0 -62C40 -44 46 8 0 62C-46 8 -40 -44 0 -62Z" fill="%s"/><path d="M0 -40V84" fill="none" stroke-width="5"/>'
icons['season~2']=tr(leaf%O,'translate(90,110) rotate(-30) scale(.95)')+tr(leaf%R,'translate(172,100) rotate(28) scale(.9)')+tr(leaf%Y,'translate(130,160) rotate(5) scale(.75)')
sf=''
for i in range(3):
    a=i*60
    sf+=f'<g transform="rotate({a} 128 128)"><path d="M128 28V228M104 60L128 84L152 60M104 196L128 172L152 196" fill="none" stroke="{N}" stroke-width="14"/></g>'
for i in range(3):
    a=i*60
    sf+=f'<g transform="rotate({a} 128 128)"><path d="M128 28V228M104 60L128 84L152 60M104 196L128 172L152 196" fill="none" stroke="{GL}" stroke-width="5"/></g>'
icons['season~3']=sf+circ(128,128,14,L)
# products
logs=''
for x,y in [(76,178),(128,178),(180,178),(102,128),(154,128),(128,78)]:
    logs+=circ(x,y,27,LW)+circ(x,y,13,WB,4)
icons['product~wood']=logs
def boll(x,y):
    return path(f'M{x-20} {y+10}Q{x} {y+38} {x+20} {y+10}L{x+10} {y+34}H{x-10}Z',DG,4)+circ(x-14,y-4,17,'#fff',5)+circ(x+14,y-4,17,'#fff',5)+circ(x,y-18,17,'#fff',5)+circ(x,y,15,'#fff',0)
icons['product~cotton']=''.join(line(128,226,x,y+30,7,WB) for x,y in[(70,100),(128,70),(186,100)])+boll(70,92)+boll(128,62)+boll(186,92)
icons['product~rubber']=rect(28,168,140,32,K,6)+rect(36,134,124,32,K,6)+rect(44,100,108,32,K,6)+line(44,184,150,184,4,SS)+line(52,150,140,150,4,SS)+line(60,116,132,116,4,SS)+path('M170 116H230Q230 200 200 200Q170 200 170 116Z',LW)+ell(200,116,30,9,'#fff')
icons['product~stone']=rect(30,140,72,60,ST,4)+rect(106,140,60,60,CO,4)+rect(54,84,80,56,ST,4)+path('M126 214Q176 100 232 214Z',SA)+line(168,196,186,196,4,'#b8a47a')
icons['product~iron']=poly([(40,170),(52,110),(104,68),(168,62),(214,108),(222,170),(170,206),(90,210)],'#6b565c')+poly([(104,68),(168,62),(150,110),(98,112)],'#8a747a',4)+poly([(150,110),(214,108),(222,170),(176,160)],SS,4)+poly([(70,152),(110,150),(100,184)],SS,4)
icons['product~copper']=circ(90,112,66,O)+circ(90,112,28,L)+circ(90,112,48,'none',4)+poly([(94,214),(110,166),(220,166),(236,214)],O)+line(124,182,196,182,4,'#f0b070')
icons['product~bauxite']=circ(88,150,54,'#c8653a')+circ(168,142,50,'#a8452e')+circ(128,92,44,'#d9822b')+circ(112,76,9,SA,4)+circ(80,142,8,SA,4)+circ(176,130,8,SA,4)
fl=''.join(poly([(x,y),(x+14,y+4),(x+8,y+16)],c,4) for x,y,c in[(88,126,K),(126,100,P),(150,140,K),(110,152,P),(80,150,K)])
icons['product~rareEarth']=path('M66 158Q128 40 190 158Z','#8b7d72')+fl+path('M36 150H220Q220 214 128 214Q36 214 36 150Z',GL)+line(64,170,90,196,4,'#fff')
icons['product~coal']=''.join(poly(p,K)+poly(h,SS,3) for p,h in[([(30,206),(40,150),(86,132),(120,170),(110,206)],[(48,156),(70,142),(66,160)]),([(110,206),(120,160),(164,140),(206,166),(196,206)],[(136,162),(160,152),(150,170)]),([(70,150),(84,96),(134,80),(170,118),(150,160),(100,166)],[(96,102),(130,92),(116,114)])])
icons['product~lithium']=path('M26 214Q80 90 150 214Z',L)+path('M150 214V150L184 130L226 150V214Z',ST)+poly([(184,130),(226,150),(184,170),(150,150)],CO,4)
icons['product~phosphate']=poly([(40,168),(56,100),(110,60),(176,66),(220,120),(214,184),(150,214),(80,208)],SA)+''.join(circ(x,y,r,'#b8a47a',3) for x,y,r in[(90,110,10),(150,100,12),(180,160,10),(110,170,12),(70,160,7)])
icons['product~oil']=path('M64 96Q54 150 64 214H192Q202 150 192 96Z','#4b5563')+rect(60,118,136,12,SS,4)+rect(60,184,136,12,SS,4)+path('M62 98Q60 66 96 70Q104 34 140 50Q176 44 194 98Q160 112 128 104Q92 112 62 98Z',K)+path('M92 108Q96 150 110 128Q112 112 104 108Z',K)+line(110,66,134,58,5,'#8a93a0')
icons['product~gas']=path('M80 214V110Q80 70 128 70Q176 70 176 110V214Z',GL)+rect(112,40,32,34,SS,4)+rect(90,36,76,14,SS,4)+rect(60,200,136,16,SS,4)+line(100,110,100,180,6,'#fff')+circ(172,44,0,SS)[:0]
icons['product~uranium']=path('M44 160H212L190 212H66Z',SS)+path('M56 160Q128 50 200 160Z',Y)+''.join(circ(x,y,5,O,3) for x,y in[(110,130),(146,120),(128,148),(170,150)])
icons['product~precious']=poly([(24,206),(40,140),(110,140),(126,206)],G)+poly([(132,206),(148,140),(218,140),(234,206)],CO)+line(58,158,98,158,5,'#f0d878')+line(166,158,206,158,5,'#fff')+poly([(70,140),(82,100),(136,100),(124,140)],G)[:0]
icons['product~steel']=path('M24 70H124V104H92V176H124V210H24V176H56V104H24Z',SS)+circ(184,140,48,SS)+circ(184,140,18,L)+circ(184,140,34,'none',4)
ing=lambda x,y,c: poly([(x,y+54),(x+12,y),(x+88,y),(x+100,y+54)],c)+line(x+26,y+14,x+70,y+14,4,'#fff')
icons['product~aluminium']=ing(30,150,CO)+ing(126,150,CO)+ing(78,90,CO)
pel=''
cols=['#fff',WA,R]
k=0
for row,(n,y) in enumerate([(5,196),(4,160),(3,124),(2,88)]):
    for i in range(n):
        x=128+(i-(n-1)/2)*38
        pel+=circ(x,y,17,cols[k%3],5);k+=1
icons['product~plastic']=pel
icons['product~cement']=path('M36 72Q80 56 120 72V206H36Z',SA)+rect(36,72,84,24,'#c2ab80',4)+path('M96 214Q170 70 232 214Z',ST)+line(150,190,180,190,4,SS)
icons['product~glass']=rect(26,60,90,148,GL,4)+line(44,80,96,130,6,'#fff')+rect(50,40,90,148,GL,4)[:0]+path('M170 50H200V90Q222 110 222 140V210H148V140Q148 110 170 90Z',GL)+line(166,150,166,196,6,'#fff')
icons['product~paper']=rect(28,170,106,30,'#fff',4)+rect(28,138,106,30,L,4)+rect(28,106,106,30,'#fff',4)+line(40,184,120,184,4,CO)+circ(184,134,50,'#fff')+circ(184,134,17,LW,5)+circ(184,134,34,'none',3)
def bolt(y,c,w): return rect(40,y,w,46,c,10)+line(40+w-30,y+8,40+w-30,y+38,4)
icons['product~textiles']=bolt(164,B,176)+bolt(112,R,160)+bolt(60,Y,176)
icons['product~fertilizer']=path('M54 112H202L212 214H44Z',SA)+rect(48,152,160,30,GR,4)+path('M62 112Q128 24 194 112Z','#e8edf5')+''.join(circ(x,y,6,c,3) for x,y,c in[(110,92,ST),(140,80,ST),(150,100,ST),(100,106,ST),(128,100,ST)])
cell=lambda x:rect(x,100,54,112,ST,8)+rect(x+14,84,26,18,SS,4)+rect(x,140,54,36,GR,0)+line(x+14,120,x+14,134,5,'#fff')
icons['product~batteries']=cell(30)+cell(101)+cell(172)
chips=''.join(rect(x,y,w,h,K,4)+''.join(line(x+6+i*(w-12)/3,y-8,x+6+i*(w-12)/3,y,3)+line(x+6+i*(w-12)/3,y+h,x+6+i*(w-12)/3,y+h+8,3) for i in range(4)) for x,y,w,h in[(54,90,64,48),(142,110,52,44),(84,164,48,34)])
icons['product~electronics']=rect(30,56,196,150,GR,10)+line(130,80,200,80,4,DG)+line(200,80,200,98,4,DG)+line(56,150,56,190,4,DG)+chips
icons['product~fuel']=rect(52,76,152,140,R,14)+path('M72 76V50Q72 40 82 40H128Q138 40 138 50V76',R)+rect(88,52,34,24,L,6)[:0]+rect(150,48,40,28,Y,4)+rect(160,34,20,16,SS,4)+line(66,96,190,196,5,'#8a2e28')+line(190,96,66,196,5,'#8a2e28')+ell(100,62,14,7,L)
icons['product~chemicals']=path('M44 80H72V110Q92 126 92 150V210H24V150Q24 126 44 110Z',GL)+rect(26,170,64,38,P,0)+rect(40,64,30,18,SS,4)+rect(112,90,112,124,WA,12)+rect(112,114,112,10,B,3)+rect(112,176,112,10,B,3)+rect(150,70,36,22,B,5)
def gear(cx,cy,r,n,c):
    pts=[]
    for i in range(n):
        a=i*2*math.pi/n
        for da,rr in[(-.22,r-12),(-.14,r),(.14,r),(.22,r-12)]:
            pts.append((cx+rr*math.cos(a+da*2*math.pi/n*1.9),cy+rr*math.sin(a+da*2*math.pi/n*1.9)))
    return poly([(round(x,1),round(y,1)) for x,y in pts],c)+circ(cx,cy,r-30,L)
icons['product~machinery']=gear(100,96,66,10,SS)+rect(118,150,108,62,ST,10)+''.join(line(x,158,x,204,5,SS) for x in (140,160,180))+rect(210,168,16,26,SS,3)
icons['product~vehicles']=path('M24 176V150Q24 136 40 132L82 128L112 90Q118 84 128 84H178Q190 84 196 94L214 130Q232 136 232 154V176Z',R)+path('M96 128L118 98H178L196 128Z',GL)+line(148,100,148,128,5)+circ(78,182,26,K)+circ(78,182,9,CO,4)+circ(184,182,26,K)+circ(184,182,9,CO,4)
icons['product~pharma']=rect(100,92,100,124,O,12)+rect(106,70,88,30,L,6)+rect(116,134,68,56,'#fff',4)+rect(144,142,12,40,R,0)[:0]+path('M142 146h16v12h12v16h-12v12h-16v-12h-12v-16h12z',R,3)+tr(rect(26,142,60,26,R,13)+rect(56,142,30,26,'#fff',13)+path('M56 142V168',  'none'),'rotate(-30 56 155)')
icons['product~consumer']=rect(36,130,184,82,LW,6)+rect(112,130,32,82,'#e8c88e',0)+rect(48,96,70,34,GL,8)+line(64,98,64,128,4,WA)[:0]+circ(168,104,28,R)+line(150,92,168,84,4,'#fff')+path('M60 96L66 70H98L104 96',ST,5)[:0]+rect(48,96,70,34,TL:='#3fb8b0',8)
icons['product~luxury']=rect(68,34,34,52,G,6)+rect(68,176,34,46,G,6)+circ(85,130,44,G)+circ(85,130,31,L,4)+line(85,130,85,108,5)+line(85,130,102,138,5)+rect(138,150,90,62,P,6)+rect(138,150,90,16,G,4)+circ(160,134,13,'#fff',4)+circ(186,134,13,'#fff',4)+circ(212,134,13,'#fff',4)
cart=lambda x:rect(x,140,22,66,G,3)+path(f'M{x} 140V126Q{x+11} 90 {x+22} 126V140Z',LW,5)+line(x,196,x+22,196,4)
icons['product~munitions']=cart(30)+cart(58)+cart(86)+rect(124,116,106,94,'#6b7a48',6)+rect(124,142,106,10,'#4d5a34',3)+rect(124,176,106,10,'#4d5a34',3)+rect(160,104,34,16,SS,4)
rods=''.join(rect(x,44,26,130,SS,12)+rect(x,44,26,28,Y,12)+line(x+8,90,x+8,160,4,CO) for x in (44,80,116,152,188)[:4] )
icons['product~nuclearFuel']=''.join(rect(x,44,32,134,SS,12)+rect(x,44,32,30,Y,12)+line(x+9,96,x+9,164,4,CO) for x in (40,88,136,184)[:4])+rect(26,172,204,46,SS,8)+circ(128,195,18,Y,4)+circ(128,195,5,K,0)
# icons
icons['product~wool']=''.join(circ(x,y,r,'#f3ece0') for x,y,r in [(70,150,40),(186,150,40),(100,100,42),(156,100,42),(128,150,50),(128,70,34),(80,190,26),(176,190,26)])+''.join(path(f'M{x} {y}q10 -12 20 0',"none",4) for x,y in [(90,100),(140,90),(112,160),(60,150),(170,150)])
pip=lambda x,y:circ(x,y,7,N,0)
icons['icon~dice']=rect(26,108,100,100,LW,16)+pip(52,134)+pip(100,134)+pip(76,158)+pip(52,182)+pip(100,182)+rect(136,50,92,92,LW,16)+pip(160,74)+pip(204,118)+pip(182,96)
sw=lambda: rect(-9,-118,18,0,SS)[:0]+path('M0 -118L10 -92V20H-10V-92Z',CO)+line(0,-100,0,14,4,SS)+rect(-28,20,56,12,G,4)+rect(-6,32,12,44,WB,3)+circ(0,86,10,G,5)
icons['icon~swords']=tr(sw(),'translate(128,128) rotate(45) translate(0,-11)')+tr(sw(),'translate(128,128) rotate(-45) translate(0,-11)')
icons['icon~fire']=path('M128 28C150 72 192 92 192 142C192 182 162 196 128 196C94 196 64 182 64 142C64 112 90 100 98 68C112 92 122 80 128 28Z',O)+path('M128 98C142 124 164 130 164 156C164 178 148 188 128 188C108 188 92 178 92 156C92 136 116 128 128 98Z',Y)+tr(rect(30,196,150,28,WB,12),'rotate(-8 105 210)')+tr(rect(76,196,150,28,LW,12),'rotate(8 150 210)')
icons['icon~pin']=rect(88,28,80,34,R,12)+path('M100 62H156L170 132H86Z',R)+rect(60,132,136,22,R,10)+line(106,76,100,118,6,'#e08a80')+path('M122 154H134L128 226Z',SS)
icons['icon~sprout']=rect(121,120,14,100,GR,3)+path('M124 150C70 160 36 118 44 66C96 66 128 100 124 150Z',GR)+path('M132 124C140 70 180 46 220 56C226 106 190 140 132 124Z',DG)+path('M44 224Q128 164 212 224Z',WB)+line(60,76,106,128,4,DG)[:0]
icons['icon~language']=circ(128,100,62,WA)+path('M128 38V162','none')+f'<ellipse cx="128" cy="100" rx="26" ry="62" fill="none"/>'+line(66,100,190,100)+path('M72 64H184M72 136H184','none',4)+rect(26,150,100,56,'#fff',14)+path('M48 206L40 228L72 206Z','#fff',5)+rect(130,138,100,56,G,14)+path('M206 194L216 218L184 194Z',G,5)+''.join(circ(x,178,5,N,0) for x in (50,76,102))+''.join(circ(x,166,5,N,0) for x in (156,180,204))
icons['icon~mapflag']=rect(92,34,12,182,SS,4)+path('M104 40H212L184 80L212 120H104Z',R)+path('M36 224Q98 168 160 224Z',GR)[:0]+path('M30 226Q100 160 170 226Z',GR)+path('M120 226Q180 178 232 226Z',DG)
st=''
for x,cy in[(52,92),(90,66),(128,54),(166,66),(204,92)]:
    st+=rect(x-4,cy+20,8,190-cy,LW,2)+ell(x,cy,13,32,Y)+line(x,cy-10,x-8,cy-2,4)+line(x,cy+4,x+8,cy+12,4)
icons['icon~crops']=st+rect(24,196,208,30,WB,12)
def tl(y0,sh): return ''
hm=lambda: rect(-7,-70,14,150,WB,4)+rect(-36,-100,72,32,SS,6)+rect(-36,-100,24,32,CO,6)
tw=lambda: path('M0 -108C26 -80 34 -52 24 -40H-24C-34 -52 -26 -80 0 -108Z',CO)+rect(-4,-40,8,22,SS,2)+rect(-9,-18,18,76,WB,6)
icons['icon~builders']=tr(hm(),'translate(128,128) rotate(45) scale(1.15) translate(0,-5)')+tr(tw(),'translate(128,128) rotate(-45) scale(1.15) translate(0,25)')
ah=lambda x,y,rot: f'<g transform="translate({x},{y}) rotate({rot})"><polygon points="-20,0 20,0 0,26" fill="{B}" stroke-width="5"/></g>'
icons['icon~exchange']=circ(88,92,40,G)+circ(88,92,24,'none',4)+circ(168,164,40,G)+circ(168,164,24,'none',4)+'<path d="M150 46Q214 48 212 104" fill="none" stroke="'+B+'" stroke-width="14"/>'+ah(212,112,0)+'<path d="M106 210Q42 208 44 152" fill="none" stroke="'+B+'" stroke-width="14"/>'+ah(44,144,180)
icons['icon~location']=path('M128 226C62 150 52 130 52 100A76 76 0 0 1 204 100C204 130 194 150 128 226Z',B)+circ(128,100,28,L)
icons['icon~search']=tr(rect(-12,58,24,86,B,8),'translate(106,106) rotate(-45)')+circ(106,106,64,GL,8)+path('M66 100A42 42 0 0 1 100 66','none',7).replace(N,'#fff')

hdr='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256"><rect width="256" height="256" fill="#ffffff"/><g stroke="#1e2f55" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">'
for k,v in icons.items():
    open(OUT+k+'.svg','w').write(hdr+v+'</g></svg>\n')
print(len(icons))
