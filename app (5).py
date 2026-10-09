"""
Hritvi Maheshwari - Portfolio
Run:  pip install streamlit
      streamlit run app.py

Optional files placed next to app.py (the app works without them):
  profile.jpg            -> your photo (shown in the hero)
  resume_data.pdf        -> Data / Analytics resume
  resume_ai.pdf          -> AI / Research resume
  resume_hosting.pdf     -> Hosting / Communication resume
"""
import base64
import os

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hritvi Maheshwari | Data - AI - Research - Communication",
    page_icon="✦",
    layout="wide",
)

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------- EDIT THESE ----------------
EMAIL = "maheshwarihritvi@gmail.com"
PHONE = "+91 9315334858"
LINKEDIN_URL = "https://www.linkedin.com/in/hritvi-maheshwari-b570b224a"
GITHUB_URL = ""     # paste your GitHub link here (leave empty to hide the button)
# --------------------------------------------

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap');
:root{--navy:#EAF0FF;--navy2:#9DB4FF;--blue:#2B5BFF;--blue2:#4D7CFF;--lav:#0F1D4D;--ink:#C9D3EE;--mut:#8D9BBF;--bg:#03060F;--card:#08102A;--line:#14235A;--silver:#D9DEEB;}
html,body,[class*="css"],.stApp{font-family:'Inter',system-ui,sans-serif;color:var(--ink);}
.stApp{background:radial-gradient(900px 500px at 90% -5%,rgba(43,91,255,.18),transparent 60%),radial-gradient(700px 500px at -5% 40%,rgba(43,91,255,.10),transparent 60%),var(--bg);}
#MainMenu,footer,header{visibility:hidden;}
.block-container{max-width:1120px;padding-top:1.2rem;padding-bottom:4rem;}
h1,h2,h3,h4{font-family:'Sora',sans-serif;color:#fff;}
html{scroll-behavior:smooth;}

.nav{position:sticky;top:0;z-index:50;display:flex;gap:6px;flex-wrap:wrap;justify-content:center;
 background:rgba(5,10,30,.82);backdrop-filter:blur(12px);border:1px solid var(--line);border-radius:999px;
 padding:8px 14px;margin-bottom:22px;box-shadow:0 8px 30px rgba(0,0,0,.5),0 0 0 1px rgba(43,91,255,.12);}
.nav a{color:var(--silver);text-decoration:none;font-size:.84rem;font-weight:600;padding:6px 12px;border-radius:999px;transition:.2s;}
.nav a:hover{background:var(--blue);color:#fff;box-shadow:0 0 18px rgba(43,91,255,.7);}

.hero{position:relative;overflow:hidden;border-radius:28px;padding:56px 48px;color:#fff;border:1px solid var(--line);
 background:radial-gradient(700px 420px at 88% 10%,rgba(43,91,255,.55),transparent 62%),
 radial-gradient(600px 400px at 0% 110%,rgba(43,91,255,.25),transparent 60%),linear-gradient(135deg,#02040C,#050B22 60%,#08144A);
 display:flex;gap:40px;align-items:center;justify-content:space-between;flex-wrap:wrap;}
.hero:after{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(77,124,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(77,124,255,.07) 1px,transparent 1px);background-size:44px 44px;pointer-events:none;}
.hero-l{flex:1 1 420px;position:relative;z-index:1;}
.hero .kicker{letter-spacing:.28em;font-size:.75rem;color:#7FA0FF;font-weight:600;text-transform:uppercase;}
.hero h1{font-family:'Anton','Sora',sans-serif;text-transform:uppercase;color:#fff;font-size:4.6rem;line-height:.98;margin:.35rem 0 .6rem;font-weight:400;letter-spacing:.01em;}
.hero h1 .a{background:linear-gradient(180deg,#FFFFFF,#9AA3B8);-webkit-background-clip:text;background-clip:text;color:transparent;}
.hero h1 .b{color:var(--blue);text-shadow:0 0 40px rgba(43,91,255,.55);}
.hero .roles{font-family:'Sora';font-size:1.05rem;color:var(--silver);margin-bottom:14px;}
.hero p{color:#AEB9D8;max-width:560px;line-height:1.65;font-size:1rem;}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px;}
.btn{display:inline-block;padding:12px 22px;border-radius:999px;font-weight:600;font-size:.92rem;text-decoration:none!important;transition:.25s;}
.btn.p{background:var(--blue);color:#fff!important;box-shadow:0 0 28px rgba(43,91,255,.6);}
.btn.s{border:1.5px solid rgba(160,185,255,.4);color:#fff!important;}
.btn.s:hover{border-color:var(--blue2);box-shadow:0 0 18px rgba(43,91,255,.45);}
.btn:hover{transform:translateY(-3px);}
.meta{margin-top:20px;font-size:.82rem;color:#7E90C4;}
.avatar{position:relative;z-index:1;width:250px;height:250px;border-radius:50%;padding:5px;
 background:conic-gradient(from 180deg,#2B5BFF,#0A1A66,#7FA0FF,#2B5BFF);box-shadow:0 0 70px rgba(43,91,255,.55),0 20px 60px rgba(0,0,0,.6);}
.avatar img,.avatar .mono{width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:center 20%;background:#050B22;}
.avatar .mono{display:flex;align-items:center;justify-content:center;font-family:'Anton';font-size:4rem;color:#fff;}

.sec{margin-top:70px;}
.eyebrow{font-size:.75rem;letter-spacing:.24em;font-weight:700;color:var(--blue2);text-transform:uppercase;}
.sec h2{font-family:'Anton','Sora',sans-serif;text-transform:uppercase;font-size:2.5rem;margin:.2rem 0 .4rem;font-weight:400;letter-spacing:.02em;
 background:linear-gradient(180deg,#fff,#A9B2C7);-webkit-background-clip:text;background-clip:text;color:transparent;}
.sub{color:var(--mut);max-width:680px;margin-bottom:22px;line-height:1.6;}

.grid{display:grid;gap:18px;}
.g2{grid-template-columns:repeat(auto-fit,minmax(320px,1fr));}
.g3{grid-template-columns:repeat(auto-fit,minmax(250px,1fr));}
.g4{grid-template-columns:repeat(auto-fit,minmax(200px,1fr));}
.card{background:linear-gradient(160deg,#0A1433,#060C22);border:1px solid var(--line);border-radius:22px;padding:24px;transition:.3s;position:relative;overflow:hidden;}
.card:hover{transform:translateY(-6px);box-shadow:0 18px 44px rgba(0,0,0,.55),0 0 28px rgba(43,91,255,.28);border-color:var(--blue);}
.card h3{margin:.2rem 0 .3rem;font-size:1.15rem;}
.card p{color:var(--mut);font-size:.93rem;line-height:1.55;margin:.3rem 0;}
.card b{color:#fff;}
.ico{font-size:1.7rem;}
.chip{display:inline-block;background:rgba(43,91,255,.14);color:#A9BEFF;border:1px solid rgba(77,124,255,.28);font-size:.74rem;font-weight:600;padding:4px 10px;border-radius:999px;margin:3px 4px 0 0;}
.chip.l{background:rgba(255,255,255,.05);color:var(--silver);border-color:rgba(255,255,255,.14);}
.path:before{content:"";position:absolute;right:-40px;top:-40px;width:140px;height:140px;border-radius:50%;background:radial-gradient(var(--blue),transparent 70%);opacity:.35;}
.go{display:inline-block;margin-top:12px;font-weight:700;color:var(--blue2)!important;text-decoration:none!important;font-size:.9rem;}

.stat{background:linear-gradient(160deg,#0B1A52,#050B26);border:1px solid var(--line);color:#fff;border-radius:20px;padding:22px;text-align:center;}
.stat b{display:block;font-family:'Anton','Sora';font-weight:400;font-size:2.1rem;color:var(--blue2);text-shadow:0 0 24px rgba(43,91,255,.6);}
.stat span{font-size:.8rem;color:#93A4D3;}

.bring .tag{font-family:'Sora';font-weight:800;letter-spacing:.12em;font-size:.8rem;color:var(--blue2);}
.proj .no{font-family:'Anton';font-size:2.6rem;color:rgba(43,91,255,.28);position:absolute;right:18px;top:8px;}
.proj .q{background:rgba(43,91,255,.09);border-left:4px solid var(--blue);padding:10px 14px;border-radius:10px;margin:10px 0;font-size:.9rem;color:var(--ink);}
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:10px 0;}
.flow span{background:var(--blue);color:#fff;font-size:.74rem;padding:5px 10px;border-radius:8px;font-weight:600;}
.flow i{color:var(--blue2);font-style:normal;font-weight:800;}

.pipe{display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:center;background:linear-gradient(135deg,#050B22,#0A1A66);border:1px solid var(--line);border-radius:24px;padding:30px;}
.pipe .node{background:rgba(255,255,255,.05);border:1px solid rgba(120,150,255,.3);color:#fff;border-radius:16px;padding:14px 18px;text-align:center;min-width:130px;font-weight:600;font-size:.9rem;}
.pipe .arrow{color:var(--blue2);font-size:1.6rem;}
.pipe .outs{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.pipe .outs div{background:var(--blue);color:#fff;border-radius:10px;padding:8px 12px;font-size:.8rem;font-weight:600;text-align:center;box-shadow:0 0 16px rgba(43,91,255,.5);}

.tl{position:relative;margin-left:12px;padding-left:28px;border-left:3px solid var(--line);}
.tl .it{position:relative;background:linear-gradient(160deg,#0A1433,#060C22);border:1px solid var(--line);border-radius:18px;padding:18px 22px;margin-bottom:18px;transition:.3s;}
.tl .it:hover{box-shadow:0 0 28px rgba(43,91,255,.3);border-color:var(--blue);transform:translateX(4px);}
.tl .it:before{content:"";position:absolute;left:-39px;top:24px;width:16px;height:16px;border-radius:50%;background:var(--blue);border:3px solid var(--bg);box-shadow:0 0 14px var(--blue);}
.tl .yr{font-size:.78rem;font-weight:700;color:var(--blue2);letter-spacing:.1em;}
.tl h4{margin:.15rem 0;font-size:1.05rem;}
.tl ul{margin:.4rem 0 0 1.1rem;padding:0;color:var(--mut);font-size:.92rem;line-height:1.6;}
.hl{background:linear-gradient(135deg,#0B1A52,#070F30)!important;border-color:var(--blue)!important;}

.stage{background:radial-gradient(500px 300px at 90% 0%,rgba(43,91,255,.45),transparent 60%),linear-gradient(135deg,#050B22,#0A1A66);border:1px solid var(--line);border-radius:26px;padding:34px;color:#fff;}
.stage h3{color:#fff;font-size:1.5rem;}
.stage p{color:#B4C2EA;}
.stage .chip{background:rgba(255,255,255,.1);color:#fff;border-color:rgba(255,255,255,.18);}
.mini{background:#08102A;border:1px solid var(--line);border-radius:16px;padding:16px;text-align:center;font-weight:600;color:var(--silver);transition:.25s;}
.mini:hover{background:var(--blue);color:#fff;transform:translateY(-4px);box-shadow:0 0 24px rgba(43,91,255,.6);}

.badge{text-align:center;}
.badge .ico{font-size:2.1rem;}
.proof{display:flex;justify-content:space-between;gap:10px;padding:10px 0;border-bottom:1px dashed var(--line);font-size:.92rem;}
.proof b{color:#fff;}
.proof span{color:var(--blue2);font-weight:600;text-align:right;}

.cta{margin-top:70px;border-radius:28px;padding:50px 30px;text-align:center;color:#fff;border:1px solid var(--line);
 background:radial-gradient(600px 300px at 80% 0%,rgba(43,91,255,.5),transparent 60%),linear-gradient(135deg,#02040C,#08144A);}
.cta h2{font-family:'Anton','Sora';font-weight:400;text-transform:uppercase;font-size:3rem;color:#fff;letter-spacing:.02em;}
.cta p{color:#B4C2EA;}
.foot{text-align:center;color:var(--mut);font-size:.8rem;margin-top:30px;}

div[data-testid="stPills"] button,div[role="radiogroup"] label{font-weight:600;}
div[data-testid="stPills"] button{background:#08102A;color:var(--silver);border:1px solid var(--line);}
div[data-testid="stPills"] button[aria-checked="true"],div[data-testid="stPills"] button[aria-pressed="true"]{background:var(--blue);color:#fff;border-color:var(--blue);}
div[role="radiogroup"] label p{color:var(--silver);}
.stCaption,[data-testid="stCaptionContainer"]{color:var(--mut)!important;}
.stDownloadButton button{background:var(--blue);color:#fff;border:none;border-radius:999px;font-weight:600;}
.stDownloadButton button:hover{box-shadow:0 0 22px rgba(43,91,255,.7);color:#fff;}
/* ===== MOTION & EXTRA VISUALS ===== */
@property --p{syntax:'<number>';inherits:false;initial-value:94;}
@property --ang{syntax:'<angle>';inherits:false;initial-value:0deg;}

.avatar-wrap{position:relative;z-index:1;width:250px;height:250px;margin:30px;}
.avatar-wrap .avatar{width:250px;height:250px;animation:breathe 4s ease-in-out infinite;}
@keyframes breathe{0%,100%{box-shadow:0 0 60px rgba(43,91,255,.45),0 20px 60px rgba(0,0,0,.6)}50%{box-shadow:0 0 110px rgba(43,91,255,.85),0 20px 60px rgba(0,0,0,.6)}}
.orbit{position:absolute;border-radius:50%;pointer-events:none;}
.orbit.o1{inset:-26px;border:1px dashed rgba(127,160,255,.4);animation:spin 22s linear infinite;}
.orbit.o2{inset:-52px;border:1px dotted rgba(127,160,255,.25);animation:spin 36s linear infinite reverse;}
.orbit:after{content:"";position:absolute;top:-4px;left:50%;width:8px;height:8px;margin-left:-4px;border-radius:50%;background:#7FA0FF;box-shadow:0 0 14px 3px rgba(77,124,255,.9);}
@keyframes spin{to{transform:rotate(360deg)}}
.fchip{position:absolute;background:rgba(8,16,42,.88);border:1px solid rgba(127,160,255,.45);color:#fff;font-weight:700;font-size:.78rem;padding:7px 13px;border-radius:999px;backdrop-filter:blur(6px);box-shadow:0 0 20px rgba(43,91,255,.4);animation:floaty 5s ease-in-out infinite;white-space:nowrap;}
.fchip.f1{top:-4px;left:-46px;}
.fchip.f2{top:46%;right:-62px;animation-delay:-1.6s;}
.fchip.f3{bottom:-8px;left:-6px;animation-delay:-3.2s;}
@keyframes floaty{0%,100%{translate:0 0}50%{translate:0 -10px}}
.spark{position:absolute;color:#9DB6FF;text-shadow:0 0 14px #2B5BFF;animation:twinkle 2.6s ease-in-out infinite;pointer-events:none;}
.spark.sp1{top:-58px;right:-6px;font-size:1.6rem;}
.spark.sp2{bottom:-52px;right:30px;font-size:1rem;animation-delay:-1.3s;}
@keyframes twinkle{0%,100%{opacity:.25;transform:scale(.7) rotate(0)}50%{opacity:1;transform:scale(1.25) rotate(45deg)}}

.hero h1 .b{background:linear-gradient(90deg,#2B5BFF,#8FB0FF,#2B5BFF);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;text-shadow:none;filter:drop-shadow(0 0 18px rgba(43,91,255,.55));animation:shine 5s linear infinite;}
@keyframes shine{to{background-position:-200% 0}}
.rotline{font-family:'Sora';font-size:1rem;color:#AEB9D8;margin:0 0 14px;display:flex;gap:7px;align-items:center;flex-wrap:wrap;}
.rot{display:inline-block;height:1.6em;overflow:hidden;vertical-align:bottom;}
.rot-in{display:flex;flex-direction:column;animation:rot 9s cubic-bezier(.7,0,.2,1) infinite;}
.rot-in b{height:1.6em;line-height:1.6em;color:#7FA0FF;font-weight:700;}
@keyframes rot{0%,18%{transform:translateY(0)}25%,43%{transform:translateY(-1.6em)}50%,68%{transform:translateY(-3.2em)}75%,93%{transform:translateY(-4.8em)}100%{transform:translateY(-6.4em)}}

.marq{overflow:hidden;margin-top:26px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:14px 0;
 -webkit-mask-image:linear-gradient(90deg,transparent,#000 9%,#000 91%,transparent);mask-image:linear-gradient(90deg,transparent,#000 9%,#000 91%,transparent);}
.marq-in{display:flex;width:max-content;animation:marq 32s linear infinite;}
.marq:hover .marq-in{animation-play-state:paused;}
.marq-in span{font-family:'Anton','Sora';text-transform:uppercase;letter-spacing:.09em;font-size:1.15rem;color:#5B77C9;white-space:nowrap;margin-right:34px;}
.marq-in span.w{color:var(--silver);}
@keyframes marq{to{transform:translateX(-50%)}}

.ring{--p:94;width:96px;height:96px;border-radius:50%;margin:0 auto 8px;position:relative;display:flex;align-items:center;justify-content:center;
 background:conic-gradient(#4D7CFF calc(var(--p)*1%),#101C4A 0);box-shadow:0 0 30px rgba(43,91,255,.4);animation:fillring 2.4s ease-out both;}
.ring:before{content:"";position:absolute;inset:9px;border-radius:50%;background:#060C26;}
.stat .ring b{position:relative;z-index:1;font-size:1.9rem;}
@keyframes fillring{from{--p:0}to{--p:94}}

.card:after{content:"";position:absolute;top:0;left:-130%;width:55%;height:100%;pointer-events:none;background:linear-gradient(100deg,transparent,rgba(130,160,255,.14),transparent);transform:skewX(-20deg);transition:left .8s ease;}
.card:hover:after{left:150%;}
.ico{display:inline-block;animation:bob 3.6s ease-in-out infinite;}
@keyframes bob{0%,100%{translate:0 0}50%{translate:0 -5px}}

.tl .it:before{animation:ping 2.2s ease-out infinite;}
@keyframes ping{0%{box-shadow:0 0 0 0 rgba(77,124,255,.75)}100%{box-shadow:0 0 0 16px rgba(77,124,255,0)}}
.tl{border-image:linear-gradient(180deg,#2B5BFF,#14235A 70%,transparent) 1;}

.stage{border:2px solid transparent;background:radial-gradient(500px 300px at 90% 0%,rgba(43,91,255,.45),transparent 60%) padding-box,linear-gradient(135deg,#050B22,#0A1A66) padding-box,conic-gradient(from var(--ang),rgba(43,91,255,.08) 0%,#8FB0FF 14%,rgba(43,91,255,.08) 34%,rgba(43,91,255,.08) 100%) border-box;animation:angspin 7s linear infinite;}
@keyframes angspin{to{--ang:360deg}}

.pipe .arrow{animation:nudge 1.6s ease-in-out infinite;}
@keyframes nudge{0%,100%{translate:-4px 0;opacity:.35}50%{translate:6px 0;opacity:1}}
.pipe .node{animation:nodeglow 4.5s ease-in-out infinite;}
.pipe .node:nth-child(3){animation-delay:1.1s;}
.pipe .node:nth-child(5){animation-delay:2.2s;}
@keyframes nodeglow{0%,70%,100%{box-shadow:0 0 0 rgba(43,91,255,0);border-color:rgba(120,150,255,.3)}35%{box-shadow:0 0 26px rgba(43,91,255,.85);border-color:#7FA0FF}}
.pipe .outs div{animation:outpulse 3s ease-in-out infinite;}
.pipe .outs div:nth-child(2){animation-delay:.3s}.pipe .outs div:nth-child(3){animation-delay:.6s}.pipe .outs div:nth-child(4){animation-delay:.9s}
@keyframes outpulse{0%,100%{filter:brightness(1)}50%{filter:brightness(1.45)}}

.vizlabel{display:flex;align-items:center;gap:10px;margin:26px 0 10px;color:var(--silver);font-weight:700;font-size:.95rem;}
.vizlabel:before{content:"";width:9px;height:9px;border-radius:50%;background:#4D7CFF;box-shadow:0 0 12px #4D7CFF;animation:ping 1.8s ease-out infinite;}

@supports (animation-timeline: view()){
 .card,.mini,.stat,.tl .it,.pipe,.stage,.marq{animation-name:reveal;animation-duration:1ms;animation-timing-function:linear;animation-fill-mode:both;animation-timeline:view();animation-range:entry 0% entry 40%;}
 .ring{animation:fillring linear both;animation-timeline:view();animation-range:entry 10% cover 45%;}
 .stage{animation:reveal linear both,angspin 7s linear infinite;animation-timeline:view(),auto;animation-range:entry 0% entry 40%,normal;}
 .pipe .node,.pipe .arrow,.pipe .outs div,.ico,.tl .it:before{animation-timeline:auto;}
 @keyframes reveal{from{opacity:0;translate:0 46px;scale:.96}to{opacity:1;translate:0 0;scale:1}}
}
@media (prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important;}}
@media (max-width:700px){.hero{padding:34px 22px}.hero h1{font-size:3.2rem}.avatar-wrap{width:180px;height:180px;margin:36px auto}.avatar-wrap .avatar{width:180px;height:180px}.fchip.f1{left:-24px}.fchip.f2{right:-30px}.sec h2{font-size:2rem}}
</style>
"""


def md(s: str) -> None:
    """Render HTML safely (strip indentation / blank lines so Markdown doesn't treat it as code)."""
    clean = "\n".join(line.strip() for line in s.strip().splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


def chips(items, cls=""):
    return "".join(f'<span class="chip {cls}">{i}</span>' for i in items)


def section(anchor, eyebrow, title, sub=""):
    md(f'<div class="sec" id="{anchor}"><div class="eyebrow">{eyebrow}</div><h2>{title}</h2>'
       f'<div class="sub">{sub}</div></div>')


def photo_html():
    for name in ("profile.jpg", "profile.jpeg", "profile.png"):
        path = os.path.join(HERE, name)
        if os.path.exists(path):
            ext = "png" if name.endswith("png") else "jpeg"
            with open(path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            return f'<img src="data:image/{ext};base64,{b64}" alt="Hritvi Maheshwari"/>'
    return '<div class="mono">HM</div>'


DATA_VIZ = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{margin:0;background:transparent;font-family:Inter,system-ui,sans-serif}
.wrap{position:relative;border:1px solid #14235A;border-radius:22px;overflow:hidden;background:linear-gradient(160deg,#0A1433,#050B22)}
canvas{display:block;width:100%;height:290px}
.steps{display:flex;gap:8px;justify-content:center;padding:2px 12px 16px;flex-wrap:wrap}
.steps span{font-size:12px;font-weight:600;padding:5px 13px;border-radius:999px;color:#8D9BBF;border:1px solid #14235A;transition:.3s}
.steps span.on{background:#2B5BFF;color:#fff;border-color:#2B5BFF;box-shadow:0 0 16px rgba(43,91,255,.7)}
</style></head><body><div class="wrap"><canvas id="c"></canvas><div class="steps" id="s"></div></div>
<script>
(function(){
var cv=document.getElementById('c'),ctx=cv.getContext('2d');
var names=['Collect','Clean','Explore','Visualize','Insight'];
var caps=['Raw, messy data','Removing the noise','Finding structure','Drawing the pattern','Insight'];
var sEl=document.getElementById('s');
names.forEach(function(n){var e=document.createElement('span');e.textContent=n;sEl.appendChild(e);});
var chips=sEl.children,cur=-1;
var W=300,H=290,dpr=window.devicePixelRatio||1;
function size(){W=cv.clientWidth||300;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);}
size();window.addEventListener('resize',size);
function rnd(a,b){return a+Math.random()*(b-a);}
function ease(x){x=Math.max(0,Math.min(1,x));return x*x*(3-2*x);}
var N=66,pts=[];
for(var i=0;i<N;i++){pts.push({sx:rnd(.04,.96),sy:rnd(.06,.94),n:rnd(-1,1),out:Math.random()<.17,ph:rnd(0,6.28)});}
var T=10000;
function frame(now){
  var t=(now%T)/T;
  ctx.clearRect(0,0,W,H);
  var L=46,R=W-28,Tp=34,B=H-30;
  var gA=Math.min(1,t/.05)*Math.min(1,(1-t)/.06);
  ctx.globalAlpha=gA;
  ctx.lineWidth=1;
  for(var g=1;g<5;g++){var gy=B-(B-Tp)*g/5;ctx.beginPath();ctx.moveTo(L,gy);ctx.lineTo(R,gy);ctx.strokeStyle='rgba(120,150,255,.07)';ctx.stroke();}
  ctx.beginPath();ctx.moveTo(L,Tp);ctx.lineTo(L,B);ctx.lineTo(R,B);ctx.strokeStyle='rgba(120,150,255,.3)';ctx.stroke();
  var cleanP=ease((t-.2)/.18),moveP=ease((t-.4)/.2),lineP=ease((t-.62)/.18);
  for(var i=0;i<N;i++){
    var p=pts[i];
    var x=L+(R-L)*p.sx+Math.sin(now/700+p.ph)*3*(1-moveP);
    var yS=Tp+(B-Tp)*p.sy+Math.cos(now/800+p.ph)*3*(1-moveP);
    var yT=B-(B-Tp)*(.12+.72*p.sx)+p.n*16;
    var y=yS+(yT-yS)*moveP;
    var a=1,r=3.4,col='#7FA0FF';
    if(p.out){col='#9AA3B8';a=1-cleanP;r=3.4*(1-cleanP*.6);}
    if(a<=0.01)continue;
    ctx.globalAlpha=gA*a;
    ctx.beginPath();ctx.arc(x,y,r,0,6.2832);
    ctx.fillStyle=col;ctx.shadowColor=col;ctx.shadowBlur=p.out?0:8;ctx.fill();
  }
  ctx.shadowBlur=0;ctx.globalAlpha=gA;
  if(lineP>0){
    var x0=L,y0=B-(B-Tp)*.12,x1=R,y1=B-(B-Tp)*.84;
    var xe=x0+(x1-x0)*lineP,ye=y0+(y1-y0)*lineP;
    ctx.beginPath();ctx.moveTo(x0,y0);ctx.lineTo(xe,ye);
    ctx.strokeStyle='#4D7CFF';ctx.lineWidth=3;ctx.lineCap='round';ctx.shadowColor='#2B5BFF';ctx.shadowBlur=16;ctx.stroke();
    ctx.shadowBlur=0;
    if(t>.8){
      var pu=(Math.sin(now/260)+1)/2;
      ctx.beginPath();ctx.arc(x1,y1,8+pu*7,0,6.2832);ctx.strokeStyle='rgba(127,160,255,'+(0.7-pu*.5)+')';ctx.lineWidth=2;ctx.stroke();
      ctx.beginPath();ctx.arc(x1,y1,5,0,6.2832);ctx.fillStyle='#fff';ctx.fill();
    }
  }
  var idx=t<.2?0:t<.4?1:t<.62?2:t<.8?3:4;
  ctx.globalAlpha=gA;ctx.fillStyle=idx==4?'#fff':'#9DB4FF';
  ctx.font='700 13px Inter,system-ui,sans-serif';ctx.textAlign='left';
  ctx.fillText(caps[idx],L,20);
  ctx.globalAlpha=1;
  if(idx!==cur){cur=idx;for(var k=0;k<chips.length;k++){chips[k].className=(k===idx)?'on':'';}}
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
})();
</script></body></html>"""

NN_VIZ = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{margin:0;background:transparent;font-family:Inter,system-ui,sans-serif}
.wrap{border:1px solid #14235A;border-radius:22px;overflow:hidden;background:radial-gradient(500px 260px at 85% 0%,rgba(43,91,255,.3),transparent 60%),linear-gradient(160deg,#0A1433,#050B22)}
canvas{display:block;width:100%;height:300px}
</style></head><body><div class="wrap"><canvas id="c"></canvas></div>
<script>
(function(){
var cv=document.getElementById('c'),ctx=cv.getContext('2d');
var W=300,H=300,dpr=window.devicePixelRatio||1,layers=[3,6,6,4],nodes=[];
var inL=['Recording','Transcript','Prompt'],outL=['Summary','Key Points','Decisions','Action Items'];
function build(){
  W=cv.clientWidth||300;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
  var narrow=W<520,xs=narrow?[.24,.42,.58,.68]:[.2,.4,.58,.76];
  nodes=[];
  layers.forEach(function(n,li){var col=[];for(var i=0;i<n;i++){col.push({x:W*xs[li],y:H*(i+1)/(n+1),glow:0});}nodes.push(col);});
}
build();window.addEventListener('resize',build);
var pulses=[],last=0,spawn=0;
function ease(x){return x*x*(3-2*x);}
function newPulse(){
  var path=[],li;
  for(li=0;li<layers.length;li++){path.push(nodes[li][Math.floor(Math.random()*layers[li])]);}
  pulses.push({path:path,seg:0,t:0,sp:.9+Math.random()*.5});
}
function frame(now){
  var dt=Math.min(.05,(now-last)/1000||0.016);last=now;
  spawn-=dt;if(spawn<=0){newPulse();spawn=.28+Math.random()*.25;}
  ctx.clearRect(0,0,W,H);
  var narrow=W<520,fs=narrow?10:12;
  ctx.lineWidth=1;
  for(var li=0;li<layers.length-1;li++){
    nodes[li].forEach(function(a){nodes[li+1].forEach(function(b){
      ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.strokeStyle='rgba(110,140,255,.10)';ctx.stroke();});});
  }
  for(var i=pulses.length-1;i>=0;i--){
    var p=pulses[i];p.t+=dt*p.sp;
    if(p.t>=1){p.seg++;p.t=0;p.path[p.seg].glow=1;if(p.seg>=p.path.length-1){pulses.splice(i,1);continue;}}
    var a=p.path[p.seg],b=p.path[p.seg+1],e=ease(p.t);
    var x=a.x+(b.x-a.x)*e,y=a.y+(b.y-a.y)*e;
    ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(x,y);ctx.strokeStyle='rgba(127,160,255,.55)';ctx.lineWidth=1.6;ctx.stroke();
    ctx.beginPath();ctx.arc(x,y,3.6,0,6.2832);ctx.fillStyle='#fff';ctx.shadowColor='#4D7CFF';ctx.shadowBlur=14;ctx.fill();ctx.shadowBlur=0;
  }
  ctx.lineWidth=1;
  nodes.forEach(function(col,li){col.forEach(function(n,i){
    n.glow=Math.max(0,n.glow-dt*1.6);
    var r=li==0||li==3?7:5.5;
    ctx.beginPath();ctx.arc(n.x,n.y,r+n.glow*2.5,0,6.2832);
    ctx.fillStyle=n.glow>0.02?'rgba(127,160,255,'+(0.35+n.glow*.65)+')':'#0F1D4D';
    ctx.strokeStyle=li==3?'#4D7CFF':'rgba(127,160,255,.6)';
    ctx.shadowColor='#2B5BFF';ctx.shadowBlur=n.glow*18;ctx.fill();ctx.shadowBlur=0;ctx.stroke();
    ctx.font='600 '+fs+'px Inter,system-ui,sans-serif';ctx.textBaseline='middle';
    if(li==0){ctx.textAlign='right';ctx.fillStyle='#AEB9D8';ctx.fillText(inL[i],n.x-r-8,n.y);}
    if(li==3){ctx.textAlign='left';ctx.fillStyle=n.glow>0.1?'#fff':'#8FA3D8';ctx.fillText(outL[i],n.x+r+8,n.y);}
  });});
  ctx.textAlign='center';ctx.fillStyle='#6E87D6';ctx.font='700 '+(fs-1)+'px Inter,system-ui,sans-serif';ctx.textBaseline='alphabetic';
  ctx.fillText('AI PROCESSING',(nodes[1][0].x+nodes[2][0].x)/2,H-12);
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
})();
</script></body></html>"""


def show_canvas(html, height):
    """Run an animated canvas (JavaScript) inside a Streamlit component. Fails silently if unavailable."""
    try:
        components.html(html, height=height)
    except Exception:
        pass


md(CSS)

# =====================================================================
#  DATA
# =====================================================================
def resume_button(fname, label, key):
    path = os.path.join(HERE, fname)
    if os.path.exists(path):
        with open(path, "rb") as f:
            st.download_button(label, f.read(), file_name=fname, mime="application/pdf",
                               key=key, use_container_width=True)
    else:
        st.caption(f"Add `{fname}` next to app.py to enable this download.")


def proj_card(no, icon, title, sub, question, flow, body, stack):
    flow_html = "<i>→</i>".join(f"<span>{s}</span>" for s in flow)
    return (f'<div class="card proj"><div class="no">{no}</div><div class="ico">{icon}</div>'
            f'<h3>{title}</h3><div class="eyebrow" style="letter-spacing:.1em">{sub}</div>'
            f'<div class="q"><b>Question:</b> {question}</div>'
            f'<div class="flow">{flow_html}</div><p>{body}</p>{chips(stack, "l")}</div>')


# =====================================================================
#  NAV
# =====================================================================
md("""
<div class="nav">
<a href="#home">Home</a><a href="#about">About</a><a href="#projects">Projects</a>
<a href="#experience">Experience</a><a href="#achievements">Achievements</a>
<a href="#skills">Skills</a><a href="#contact">Contact</a>
</div>
""")

# =====================================================================
#  1. HOME
# =====================================================================
li_btn = f'<a class="btn s" href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>' if LINKEDIN_URL else ""
md(f"""
<div class="hero" id="home">
<div class="hero-l">
<div class="kicker">Portfolio · 2026</div>
<h1><span class="a">Hritvi</span><br><span class="b">Maheshwari</span></h1>
<div class="roles">Data &nbsp;|&nbsp; AI &nbsp;|&nbsp; Research &nbsp;|&nbsp; Communication</div>
<div class="rotline">I love working with <span class="rot"><span class="rot-in"><b>data</b><b>AI</b><b>research</b><b>audiences</b><b>data</b></span></span></div>
<p>A BCA student who combines analytical thinking, emerging technology, research and strong communication
to turn ideas into meaningful outcomes.</p>
<div class="btns">
<a class="btn p" href="#projects">View My Projects →</a>
<a class="btn s" href="#contact">Resumes &amp; Contact</a>
{li_btn}
</div>
<div class="meta">📍 Delhi, India &nbsp;·&nbsp; BCA, IITM Janakpuri &nbsp;·&nbsp; Expected Graduation 2027</div>
</div>
<div class="avatar-wrap"><div class="orbit o2"></div><div class="orbit o1"></div><div class="avatar">{photo_html()}</div>
<div class="fchip f1">📊 Data</div><div class="fchip f2">🤖 AI</div><div class="fchip f3">🎤 Host</div>
<div class="spark sp1">✦</div><div class="spark sp2">✦</div></div>
</div>
""")

_items = ["Python", "SQL", "Power BI", "Excel", "Statistics", "Generative AI", "Agentic AI", "NLP", "LangChain",
          "Streamlit", "Research", "Public Speaking", "Anchoring", "Leadership"]
_row = "".join(f'<span>{t}</span><span class="w">✦</span>' for t in _items)
md(f'<div class="marq"><div class="marq-in">{_row}{_row}</div></div>')

# =====================================================================
#  2. ABOUT
# =====================================================================
section("about", "About me", "Technology, with a human voice")
c1, c2 = st.columns([1.4, 1], gap="large")
with c1:
    md("""
    <div class="card"><p style="font-size:1rem;color:#C9D3EE">
    I'm <b>Hritvi Maheshwari</b>, a BCA student with a strong interest in Data Analytics,
    Artificial Intelligence and research.</p>
    <p style="font-size:1rem">My work spans AI-powered applications, data analysis and visualization,
    while my experience in event hosting and student coordination has strengthened my communication,
    leadership and problem-solving abilities.</p>
    <p style="font-size:1rem">I enjoy learning emerging technologies, simplifying complex ideas, and working on
    projects where technology creates practical value.</p></div>
    """)
with c2:
    md("""
    <div class="grid" style="grid-template-columns:1fr 1fr">
    <div class="stat"><div class="ring"><b>9.4</b></div><span>CGPA out of 10</span></div>
    <div class="stat"><b>Top 2</b><span>Project among many students</span></div>
    <div class="stat"><b>2027</b><span>Expected Graduation</span></div>
    <div class="stat"><b>100–1000+</b><span>Audience sizes hosted</span></div>
    </div>
    """)
_cert_chips = chips(["Data Analytics · ShapeMySkill", "Generative AI & Agentic AI · GRASSTech (4-week practical training)"], "l")
_course_chips = chips(["Data Analytics", "Database Management Systems", "Statistics", "Python Programming",
                       "Business Intelligence", "Generative AI", "Agentic AI"])
md(f"""
<div class="card" style="margin-top:18px">
<div class="eyebrow">Education</div>
<h3>Bachelor of Computer Applications (BCA) · CGPA 9.4/10</h3>
<p>Institute of Innovation in Technology &amp; Management (IITM), Janakpuri, Delhi · Expected 2027</p>
<div>{_course_chips}</div>
<div class="eyebrow" style="margin-top:14px">Certifications</div>
<div>{_cert_chips}</div>
</div>
""")

# =====================================================================
#  3. PROJECTS  (pick an area, see only that area)
# =====================================================================
section("projects", "Projects", "Choose an area to explore",
        "Pick one of the three areas below and the page shows only that work.")

AREAS = ["📊 Data & Analytics", "🤖 AI & Research", "🎤 Hosting & Leadership"]
if hasattr(st, "pills"):
    area = st.pills("Area", AREAS, default=AREAS[0], label_visibility="collapsed", key="area")
else:
    area = st.radio("Area", AREAS, horizontal=True, label_visibility="collapsed", key="area")
area = area or AREAS[0]

if area == AREAS[0]:
    md(f"""
    <div class="sub" style="margin-top:14px"><b style="color:#fff">I turn raw information into meaningful insights.</b></div>
    <div style="margin-bottom:14px">{chips(["Python", "SQL", "Power BI", "Excel", "Statistics", "Data Cleaning", "EDA", "Visualization"])}</div>
    <div class="grid g2">
    {proj_card("01", "📈", "Student Performance Analysis", "Python · Statistics · Visualization",
               "Which factors are most associated with how students perform?",
               ["Collect", "Clean", "Statistical Analysis", "Charts & Reports"],
               "Collected and cleaned academic data using Python, applied statistical analysis to identify factors affecting performance, and presented findings through charts and visual reports.",
               ["Python", "Statistics", "Charts"])}
    {proj_card("02", "⚖️", "The 1 in the 0's", "When Data Meets Discrimination",
               "What patterns, trends and potential bias can real-world data reveal?",
               ["Data", "Cleaning", "EDA", "Visualization", "Insights"],
               "Explored real-world datasets to identify patterns, trends and potential bias, then presented the findings through reports and dashboards in an easy-to-understand way.",
               ["EDA", "Visualization", "Dashboards"])}
    </div>
    <div class="card" style="margin-top:18px"><h3>Skill → Proof</h3>
    <div class="proof"><b>Python</b><span>Student Performance Analysis</span></div>
    <div class="proof"><b>Statistics</b><span>Student Performance Analysis</span></div>
    <div class="proof"><b>EDA &amp; Visualization</b><span>The 1 in the 0's</span></div>
    <div class="proof"><b>Data accuracy</b><span>Placement Cell records</span></div></div>
    <div class="vizlabel">Raw data to insight, in motion</div>
    """)
    show_canvas(DATA_VIZ, 350)
    resume_button("resume_data.pdf", "⬇ Download Data / Analytics resume", "dl_data_proj")

elif area == AREAS[1]:
    md(f"""
    <div class="sub" style="margin-top:14px"><b style="color:#fff">I explore AI through practical projects and research.</b></div>
    <div style="margin-bottom:14px">{chips(["Generative AI", "Agentic AI", "NLP", "LLMs", "Python", "LangChain", "Streamlit", "APIs", "Git/GitHub"])}</div>
    <div class="grid g2">
    {proj_card("01", "🤖", "MeetFlow", "AI Meeting Assistant",
               "How can a long meeting recording become something you can act on in minutes?",
               ["Recording", "Transcript", "LLM Analysis", "Summary · Decisions · Actions"],
               "Built an LLM-powered app (Streamlit, LangChain) that turns meeting recordings into transcripts, summaries, key points, decisions and action items, with an interactive interface to explore them.",
               ["Generative AI", "NLP", "Streamlit", "LangChain"])}
    {proj_card("02", "🔬", "IEEE · Research Work", "Member · Research &amp; Technical Activities",
               "How does an emerging technology move from paper to practice?",
               ["Read", "Discuss", "Workshop", "Apply"],
               "Active IEEE member taking part in research paper reading sessions, technical discussions, workshops and seminars on technology, data and AI.",
               ["Paper Reading", "Workshops", "Seminars"])}
    </div>
    <div class="pipe" style="margin-top:18px">
    <div class="node">🎙️<br>Meeting<br>Recording</div><div class="arrow">→</div>
    <div class="node">📝<br>Transcription</div><div class="arrow">→</div>
    <div class="node">🧠<br>LLM<br>Analysis</div><div class="arrow">→</div>
    <div class="outs"><div>Summary</div><div>Key Points</div><div>Decisions</div><div>Action Items</div></div>
    </div>
    <div class="vizlabel">How MeetFlow turns a meeting into action items</div>
    """)
    show_canvas(NN_VIZ, 310)
    resume_button("resume_ai.pdf", "⬇ Download AI / Research resume", "dl_ai_proj")

else:
    md(f"""
    <div class="sub" style="margin-top:14px"><b style="color:#fff">I turn events into engaging experiences.</b></div>
    <div style="margin-bottom:14px">{chips(["Anchoring", "Public Speaking", "Stage Flow", "Coordination", "Voice Modulation", "Script Writing"])}</div>
    <div class="stage">
    <div class="eyebrow" style="color:#7FA0FF">Featured event</div>
    <h3>INCEPTA HER 1.0 · Microsoft</h3>
    <p><b>Role:</b> Event Host / MC &nbsp;·&nbsp; <b>Audience:</b> ~100 &nbsp;·&nbsp; <b>Sept 2026</b></p>
    <p>Topics: Emerging AI · Cloud DevOps · AdTech · Industry Insights</p>
    <div style="margin-top:8px">{chips(["Stage Flow", "Speaker Introductions", "Audience Engagement", "Transitions", "Event Coordination"])}</div>
    </div>
    <div class="grid g4" style="margin-top:18px">
    <div class="mini">🏫 Morning Assemblies</div><div class="mini">🍎 Teachers' Day</div>
    <div class="mini">🎓 School Farewell</div><div class="mini">🎉 Freshers' Party</div>
    <div class="mini">🥂 College Farewell</div><div class="mini">🎭 Annual College Fest</div>
    <div class="mini">💻 IT &amp; Technical Events</div><div class="mini">🛠️ Workshops &amp; Hackathons</div>
    </div>
    <div class="grid g2" style="margin-top:18px">
    {proj_card("01", "🎓", "Placement Cell Coordinator", "IITM, Delhi · 2025 – Present",
               "How do recruiters, students and faculty stay perfectly in sync?",
               ["Recruiters", "Student Coordinator", "Students & Faculty"],
               "Maintained placement records with accuracy, coordinated between companies and students, and helped organise pre-placement sessions, workshops and GD/PI practice.",
               ["Coordination", "Data Accuracy", "Communication"])}
    <div class="card"><div class="ico">🎤</div><h3>On stage, under pressure</h3>
    <p>Voice modulation, script writing and calm handling of live changes in schedule and stage flow.</p>
    <p>Appreciated by faculty and organizers for audience engagement, and frequently selected to anchor major institutional events.</p></div>
    </div>
    """)
    resume_button("resume_hosting.pdf", "⬇ Download Hosting / Communication resume", "dl_host_proj")

# =====================================================================
#  4. EXPERIENCE
# =====================================================================
section("experience", "Experience", "A timeline of what I've done")
md("""
<div class="tl">
<div class="it hl"><div class="yr">SEPT 2026</div><h4>Event Host / MC · Microsoft, INCEPTA HER 1.0</h4>
<ul><li>Hosted a dynamic tech event with eminent speakers on Emerging AI, Cloud DevOps, AdTech and Industry Insights.</li>
<li>Managed stage flow and coordinated with speakers and organizers for an audience of around 100.</li></ul></div>
<div class="it"><div class="yr">2025 – PRESENT</div><h4>Student Coordinator · Placement Cell, IITM Delhi</h4>
<ul><li>Maintained placement data, schedules and records with accuracy and confidentiality.</li>
<li>Coordinated between recruiters, students and faculty; supported placement sessions, workshops and GD/PI practice.</li></ul></div>
<div class="it"><div class="yr">2025 – PRESENT</div><h4>Private Tutor · AI &amp; Information Practices</h4>
<ul><li>Taught Classes 9–12, simplifying Python, data handling, databases and AI fundamentals with practical exercises.</li>
<li>Tracked student progress and supported exam preparation.</li></ul></div>
<div class="it"><div class="yr">2023 – PRESENT</div><h4>Event Host, Anchor &amp; Student Event Coordinator · School &amp; College</h4>
<ul><li>Hosted seminars, competitions and technical programs for 100 to 1000+ attendees.</li>
<li>Adapted quickly to last-minute changes and was frequently selected to anchor institutional events.</li></ul></div>
</div>
""")

# =====================================================================
#  5. ACHIEVEMENTS
# =====================================================================
section("achievements", "Achievements", "Highlights so far")
md("""
<div class="grid g3 badge">
<div class="card"><div class="ico">🏆</div><h3>Top 2 Project</h3><p>Among many students, Generative AI &amp; Agentic AI training</p></div>
<div class="card"><div class="ico">🎤</div><h3>Microsoft Event Host</h3><p>INCEPTA HER 1.0, Sept 2026</p></div>
<div class="card"><div class="ico">🔬</div><h3>IEEE Member</h3><p>Research &amp; technical activities</p></div>
<div class="card"><div class="ico">🎓</div><h3>Placement Cell Coordinator</h3><p>Student–recruiter coordination at IITM</p></div>
<div class="card"><div class="ico">📜</div><h3>Certifications</h3><p>Data Analytics (ShapeMySkill) · Generative &amp; Agentic AI, GRASSTech (4-week practical training)</p></div>
<div class="card"><div class="ico">🌟</div><h3>Frequently selected anchor</h3><p>For major institutional events</p></div>
</div>
""")

# =====================================================================
#  6. SKILLS
# =====================================================================
section("skills", "Skills", "Organised by what they're for")
_sk_prog = chips(["Python", "SQL", "C", "Java"])
_sk_data = chips(["Power BI", "Excel", "Google Sheets", "Data Cleaning", "EDA", "Statistics", "Visualization", "Jupyter"])
_sk_ai = chips(["Generative AI", "Agentic AI", "NLP", "ML Fundamentals", "Classification", "Regression"])
_sk_tools = chips(["Streamlit", "LangChain", "APIs", "Git/GitHub", "Google Forms", "SurveyMonkey"])
_sk_pro = chips(["Communication", "Public Speaking", "Anchoring", "Stage Management", "Leadership", "Team Collaboration",
                 "Problem Solving", "Time Management", "Adaptability"], "l")
md(f"""
<div class="grid g3">
<div class="card"><h3>Programming</h3>{_sk_prog}</div>
<div class="card"><h3>Data</h3>{_sk_data}</div>
<div class="card"><h3>AI</h3>{_sk_ai}</div>
<div class="card"><h3>Tools</h3>{_sk_tools}</div>
<div class="card"><h3>Professional</h3>{_sk_pro}</div>
<div class="card"><h3>Languages</h3><p><b>Hindi</b>: Native<br><b>English</b>: Professional Working Proficiency</p></div>
</div>
""")

# =====================================================================
#  7. CONTACT
# =====================================================================
extra = ""
if LINKEDIN_URL:
    extra += f'<a class="btn s" href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>'
if GITHUB_URL:
    extra += f'<a class="btn s" href="{GITHUB_URL}" target="_blank">GitHub</a>'
md(f"""
<div class="cta" id="contact">
<div class="eyebrow" style="color:#7FA0FF">Contact</div>
<h2>Let's build something meaningful.</h2>
<p>📍 Delhi, India &nbsp;·&nbsp; ✉️ {EMAIL} &nbsp;·&nbsp; 📞 {PHONE}</p>
<div class="btns" style="justify-content:center">
<a class="btn p" href="mailto:{EMAIL}">Let's Connect →</a>{extra}
</div></div>
""")
md('<div class="sub" style="margin:26px 0 8px;text-align:center;max-width:none"><b style="color:#fff">Looking for something specific? Pick a resume.</b></div>')
rc = st.columns(3, gap="medium")
with rc[0]:
    resume_button("resume_data.pdf", "📊 Data / Analytics", "dl_data")
with rc[1]:
    resume_button("resume_ai.pdf", "🤖 AI / Research", "dl_ai")
with rc[2]:
    resume_button("resume_hosting.pdf", "🎤 Hosting / Communication", "dl_host")

md('<div class="foot">© 2026 Hritvi Maheshwari · Built with Python &amp; Streamlit</div>')
