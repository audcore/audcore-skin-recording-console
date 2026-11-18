"""Generate the skin layout illustration; optional dependency: CairoSVG."""
from pathlib import Path
import cairosvg

def rect(x,y,w,h,c,r=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>'

def line(x1,y1,x2,y2,c,w=1): return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{c}" stroke-width="{w}"/>'

def dot(x,y,r,c): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'

def mixer(bg, panel, colors, light=False, style="default"):
 s=rect(0,0,160,120,bg)+rect(0,0,160,16,panel)
 for x in [8,17,26]: s+=dot(x,8,2,"#77818a")
 s+=rect(116,5,30,5,"#50606a",2)
 for i,x in enumerate([22,47,72,97,122]):
  c=colors[i%len(colors)];s+=rect(x,23,17,92,panel,2)+rect(x+3,28,11,4,c,1)+rect(x+3,38,11,9,"#41474a",1)+rect(x+3,50,11,9,"#41474a",1)
  s+=rect(x+7,66,3,37,"#586064",1)+rect(x+4,77+(i%3)*5,9,7,"#e6e5dc",2)+rect(x+3,108,11,3,c,1)
 return s

def studio():
 s=rect(0,0,160,120,"#292c2f")+rect(0,0,160,15,"#34383c")+rect(0,15,32,105,"#24272a")
 for y in [24,36,48,60,72]:s+=rect(6,y,20,6,"#465768" if y==36 else "#34383c",1)
 for i,x in enumerate([37,61,85,109,133]):
  s+=rect(x,20,20,96,"#3b3f43",1)+rect(x+3,25,14,5,"#2197fb",1)
  for y in [35,44,53]:s+=rect(x+3,y,14,7,"#5e656c",1)
  s+=rect(x+9,66,3,32,"#202427")+rect(x+5,75+i%3*5,11,7,"#d7dcde",2)+rect(x+3,107,14,4,"#2197fb",1)
 return s

ROOT=Path(__file__).resolve().parent.parent/"assets"
ROOT.mkdir(exist_ok=True)
mark=studio()
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="160" height="120" viewBox="0 0 160 120">{mark}</svg>'
(ROOT/"preview.svg").write_text(svg+"\n",encoding="utf-8")
cairosvg.svg2png(bytestring=svg.encode(),write_to=str(ROOT/"preview.png"),output_width=160,output_height=120)
