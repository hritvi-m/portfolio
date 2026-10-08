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

st.set_page_config(
    page_title="Hritvi Maheshwari | Data - AI - Research - Communication",
    page_icon="✦",
    layout="wide",
)

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------- EDIT THESE ----------------
EMAIL = "maheshwarihritvi@gmail.com"
PHONE = "+91 9315334858"
LINKEDIN_URL = ""   # paste your LinkedIn profile link here, e.g. "https://www.linkedin.com/in/your-id"
GITHUB_URL = ""     # paste your GitHub link here (leave empty to hide the button)
# --------------------------------------------

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap');
:root{--navy:#0A1F44;--navy2:#13306B;--blue:#2F6BFF;--lav:#E9E6FF;--ink:#1B2740;--mut:#5C6885;--bg:#F7F8FD;}
html,body,[class*="css"],.stApp{font-family:'Inter',system-ui,sans-serif;color:var(--ink);}
.stApp{background:var(--bg);}
#MainMenu,footer,header{visibility:hidden;}
.block-container{max-width:1120px;padding-top:1.2rem;padding-bottom:4rem;}
h1,h2,h3,h4{font-family:'Sora',sans-serif;color:var(--navy);}
html{scroll-behavior:smooth;}

.nav{position:sticky;top:0;z-index:50;display:flex;gap:6px;flex-wrap:wrap;justify-content:center;
 background:rgba(255,255,255,.85);backdrop-filter:blur(10px);border:1px solid #E3E7F5;border-radius:999px;
 padding:8px 14px;margin-bottom:22px;box-shadow:0 6px 24px rgba(10,31,68,.06);}
.nav a{color:var(--navy);text-decoration:none;font-size:.84rem;font-weight:600;padding:6px 12px;border-radius:999px;transition:.2s;}
.nav a:hover{background:var(--navy);color:#fff;}

.hero{position:relative;overflow:hidden;border-radius:28px;padding:56px 48px;color:#fff;
 background:radial-gradient(900px 400px at 85% -10%,rgba(139,123,255,.55),transparent 60%),
 radial-gradient(700px 400px at 0% 110%,rgba(47,107,255,.55),transparent 60%),linear-gradient(135deg,#071634,#0A1F44 55%,#13306B);
 display:flex;gap:40px;align-items:center;justify-content:space-between;flex-wrap:wrap;}
.hero:after{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.08) 1px,transparent 1px);background-size:22px 22px;pointer-events:none;}
.hero-l{flex:1 1 420px;position:relative;z-index:1;}
.hero .kicker{letter-spacing:.28em;font-size:.75rem;color:#B9C8FF;font-weight:600;text-transform:uppercase;}
.hero h1{color:#fff;font-size:3.3rem;line-height:1.05;margin:.35rem 0 .5rem;font-weight:800;}
.hero h1 span{background:linear-gradient(90deg,#7FA5FF,#C9BEFF);-webkit-background-clip:text;background-clip:text;color:transparent;}
.hero .roles{font-family:'Sora';font-size:1.05rem;color:#DDE5FF;margin-bottom:14px;}
.hero p{color:#C9D5F5;max-width:560px;line-height:1.65;font-size:1rem;}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px;}
.btn{display:inline-block;padding:12px 22px;border-radius:999px;font-weight:600;font-size:.92rem;text-decoration:none!important;transition:.25s;}
.btn.p{background:var(--blue);color:#fff!important;box-shadow:0 8px 24px rgba(47,107,255,.45);}
.btn.s{border:1.5px solid rgba(255,255,255,.45);color:#fff!important;}
.btn:hover{transform:translateY(-3px);}
.meta{margin-top:20px;font-size:.82rem;color:#9FB2E8;}
.avatar{position:relative;z-index:1;width:230px;height:230px;border-radius:50%;padding:6px;
 background:conic-gradient(from 180deg,#2F6BFF,#B9A8FF,#2F6BFF);box-shadow:0 20px 60px rgba(0,0,0,.4);}
.avatar img,.avatar .mono{width:100%;height:100%;border-radius:50%;object-fit:cover;background:var(--navy);}
.avatar .mono{display:flex;align-items:center;justify-content:center;font-family:'Sora';font-weight:800;font-size:4rem;color:#fff;}

.sec{margin-top:70px;}
.eyebrow{font-size:.75rem;letter-spacing:.24em;font-weight:700;color:var(--blue);text-transform:uppercase;}
.sec h2{font-size:2.1rem;margin:.2rem 0 .4rem;font-weight:800;}
.sub{color:var(--mut);max-width:680px;margin-bottom:22px;line-height:1.6;}

.grid{display:grid;gap:18px;}
.g2{grid-template-columns:repeat(auto-fit,minmax(320px,1fr));}
.g3{grid-template-columns:repeat(auto-fit,minmax(250px,1fr));}
.g4{grid-template-columns:repeat(auto-fit,minmax(200px,1fr));}
.card{background:#fff;border:1px solid #E3E7F5;border-radius:22px;padding:24px;transition:.3s;position:relative;overflow:hidden;}
.card:hover{transform:translateY(-6px);box-shadow:0 18px 40px rgba(10,31,68,.12);border-color:#C5D3FF;}
.card h3{margin:.2rem 0 .3rem;font-size:1.15rem;}
.card p{color:var(--mut);font-size:.93rem;line-height:1.55;margin:.3rem 0;}
.ico{font-size:1.7rem;}
.chip{display:inline-block;background:#EEF2FF;color:var(--navy2);font-size:.74rem;font-weight:600;padding:4px 10px;border-radius:999px;margin:3px 4px 0 0;}
.chip.l{background:var(--lav);}
.path{background:linear-gradient(160deg,#fff,#F1EFFF);}
.path:before{content:"";position:absolute;right:-40px;top:-40px;width:120px;height:120px;border-radius:50%;background:radial-gradient(var(--blue),transparent 70%);opacity:.18;}
.go{display:inline-block;margin-top:12px;font-weight:700;color:var(--blue)!important;text-decoration:none!important;font-size:.9rem;}

.stat{background:var(--navy);color:#fff;border-radius:20px;padding:22px;text-align:center;}
.stat b{display:block;font-family:'Sora';font-size:2rem;background:linear-gradient(90deg,#8FB0FF,#D4CBFF);-webkit-background-clip:text;background-clip:text;color:transparent;}
.stat span{font-size:.8rem;color:#B9C8FF;}

.bring .tag{font-family:'Sora';font-weight:800;letter-spacing:.12em;font-size:.8rem;color:var(--blue);}
.proj .no{font-family:'Sora';font-weight:800;font-size:2.4rem;color:#E3E9FF;position:absolute;right:18px;top:8px;}
.proj .q{background:#F4F6FF;border-left:4px solid var(--blue);padding:10px 14px;border-radius:10px;margin:10px 0;font-size:.9rem;color:var(--ink);}
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:10px 0;}
.flow span{background:var(--navy);color:#fff;font-size:.74rem;padding:5px 10px;border-radius:8px;font-weight:600;}
.flow i{color:var(--blue);font-style:normal;font-weight:800;}

.pipe{display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:center;background:linear-gradient(135deg,#0A1F44,#13306B);border-radius:24px;padding:30px;}
.pipe .node{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);color:#fff;border-radius:16px;padding:14px 18px;text-align:center;min-width:130px;font-weight:600;font-size:.9rem;}
.pipe .arrow{color:#8FB0FF;font-size:1.6rem;}
.pipe .outs{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.pipe .outs div{background:var(--blue);color:#fff;border-radius:10px;padding:8px 12px;font-size:.8rem;font-weight:600;text-align:center;}

.tl{position:relative;margin-left:12px;padding-left:28px;border-left:3px solid #D5DEFF;}
.tl .it{position:relative;background:#fff;border:1px solid #E3E7F5;border-radius:18px;padding:18px 22px;margin-bottom:18px;transition:.3s;}
.tl .it:hover{box-shadow:0 12px 30px rgba(10,31,68,.1);transform:translateX(4px);}
.tl .it:before{content:"";position:absolute;left:-39px;top:24px;width:16px;height:16px;border-radius:50%;background:var(--blue);border:3px solid var(--bg);}
.tl .yr{font-size:.78rem;font-weight:700;color:var(--blue);letter-spacing:.1em;}
.tl h4{margin:.15rem 0;font-size:1.05rem;}
.tl ul{margin:.4rem 0 0 1.1rem;padding:0;color:var(--mut);font-size:.92rem;line-height:1.6;}
.hl{background:linear-gradient(135deg,#EEF2FF,#F1EDFF);border-color:#C5D3FF!important;}

.stage{background:linear-gradient(135deg,#0A1F44,#13306B);border-radius:26px;padding:34px;color:#fff;}
.stage h3{color:#fff;font-size:1.5rem;}
.stage p{color:#C9D5F5;}
.stage .chip{background:rgba(255,255,255,.12);color:#fff;}
.mini{background:#fff;border:1px solid #E3E7F5;border-radius:16px;padding:16px;text-align:center;font-weight:600;color:var(--navy);transition:.25s;}
.mini:hover{background:var(--navy);color:#fff;transform:translateY(-4px);}

.badge{text-align:center;}
.badge .ico{font-size:2.1rem;}
.proof{display:flex;justify-content:space-between;gap:10px;padding:10px 0;border-bottom:1px dashed #D9DFF2;font-size:.92rem;}
.proof b{color:var(--navy);}
.proof span{color:var(--blue);font-weight:600;text-align:right;}

.cta{margin-top:70px;border-radius:28px;padding:50px 30px;text-align:center;color:#fff;
 background:radial-gradient(600px 300px at 80% 0%,rgba(139,123,255,.5),transparent 60%),linear-gradient(135deg,#071634,#13306B);}
.cta h2{color:#fff;font-size:2.2rem;}
.cta p{color:#C9D5F5;}
.foot{text-align:center;color:var(--mut);font-size:.8rem;margin-top:30px;}

div[data-testid="stPills"] button,div[role="radiogroup"] label{font-weight:600;}
@media (max-width:700px){.hero{padding:34px 22px}.hero h1{font-size:2.4rem}.avatar{width:170px;height:170px}}
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


md(CSS)

# ---------------- NAV ----------------
md("""
<div class="nav">
<a href="#home">Home</a><a href="#about">About</a><a href="#work">Work</a><a href="#data">Data</a>
<a href="#ai">AI &amp; Research</a><a href="#experience">Experience</a><a href="#stage">On Stage</a>
<a href="#achievements">Achievements</a><a href="#skills">Skills</a><a href="#resume">Resumes</a><a href="#contact">Contact</a>
</div>
""")

# ---------------- HERO ----------------
li_btn = f'<a class="btn s" href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>' if LINKEDIN_URL else ""
md(f"""
<div class="hero" id="home">
<div class="hero-l">
<div class="kicker">Portfolio · 2026</div>
<h1>Hritvi<br><span>Maheshwari</span></h1>
<div class="roles">Data &nbsp;|&nbsp; AI &nbsp;|&nbsp; Research &nbsp;|&nbsp; Communication</div>
<p>I explore the intersection of technology, data and communication, building practical projects,
contributing to research, and creating engaging experiences on and off the stage.</p>
<div class="btns">
<a class="btn p" href="#work">View My Work →</a>
<a class="btn s" href="#resume">Resumes</a>
{li_btn}
</div>
<div class="meta">📍 Delhi, India &nbsp;·&nbsp; BCA, IITM Janakpuri &nbsp;·&nbsp; Expected Graduation 2027</div>
</div>
<div class="avatar">{photo_html()}</div>
</div>
""")

# ---------------- CHOOSE YOUR PATH ----------------
section("path", "Start here", "What are you here to explore?",
        "One portfolio, three directions. Pick the one that matters to you.")
md(f"""
<div class="grid g3">
<div class="card path"><div class="ico">📊</div><h3>Data &amp; Analytics</h3>
<p>I turn raw information into meaningful insights.</p>
{chips(["Python", "SQL", "Power BI", "Excel", "Statistics"])}<br>
<a class="go" href="#data">Explore Analytics →</a></div>
<div class="card path"><div class="ico">🤖</div><h3>AI &amp; Research</h3>
<p>I explore AI through practical projects and research.</p>
{chips(["Generative AI", "Agentic AI", "NLP", "LangChain", "IEEE"])}<br>
<a class="go" href="#ai">Explore AI &amp; Research →</a></div>
<div class="card path"><div class="ico">🎤</div><h3>Hosting &amp; Leadership</h3>
<p>I turn events into engaging experiences.</p>
{chips(["Anchoring", "Public Speaking", "Stage Flow", "Coordination"])}<br>
<a class="go" href="#stage">Explore Communication →</a></div>
</div>
""")

# ---------------- ABOUT ----------------
section("about", "About me", "Technology, with a human voice")
c1, c2 = st.columns([1.4, 1], gap="large")
with c1:
    md("""
    <div class="card"><p style="font-size:1rem;color:#1B2740">
    I'm <b>Hritvi Maheshwari</b>, a BCA student with a strong interest in Data Analytics,
    Artificial Intelligence and research.</p>
    <p style="font-size:1rem">My work spans AI-powered applications, data analysis and visualization,
    while my experience in event hosting and student coordination has strengthened my communication,
    leadership and problem-solving abilities.</p>
    <p style="font-size:1rem">I enjoy learning emerging technologies, simplifying complex ideas, and working on
    projects where technology creates practical value. Right now I'm building my skills across Python, SQL,
    Power BI, Generative AI, Agentic AI and data-driven problem solving.</p></div>
    """)
with c2:
    md("""
    <div class="grid" style="grid-template-columns:1fr 1fr">
    <div class="stat"><b>9.4/10</b><span>CGPA</span></div>
    <div class="stat"><b>2027</b><span>Expected Graduation</span></div>
    <div class="stat"><b>2nd / 65</b><span>Best Project, GenAI &amp; Agentic AI</span></div>
    <div class="stat"><b>100–1000+</b><span>Audience sizes hosted</span></div>
    </div>
    """)

# ---------------- WHAT I BRING ----------------
section("bring", "What I bring", "Think. Build. Research. Connect.")
md(f"""
<div class="grid g4 bring">
<div class="card"><div class="tag">THINK</div><h3>Analytical Thinking</h3><p>Turning messy data into clear answers.</p>
{chips(["Python", "SQL", "Statistics", "EDA"])}</div>
<div class="card"><div class="tag">BUILD</div><h3>Technology &amp; AI</h3><p>LLM-powered apps with practical use.</p>
{chips(["Generative AI", "Agentic AI", "Streamlit"])}</div>
<div class="card"><div class="tag">RESEARCH</div><h3>Curiosity</h3><p>Paper reading, workshops and technical discussion.</p>
{chips(["IEEE", "AI", "Data Science"])}</div>
<div class="card"><div class="tag">CONNECT</div><h3>Communication</h3><p>Explaining ideas and leading a room.</p>
{chips(["Hosting", "Public Speaking", "Coordination"])}</div>
</div>
""")

# ---------------- FEATURED WORK (with filter) ----------------
section("work", "Featured work", "Selected projects &amp; experiences",
        "Filter by the area you care about.")

PROJECTS = [
    dict(cat=["AI & Research"], no="01", icon="🤖", title="MeetFlow",
         sub="AI Meeting Assistant", stack=["Generative AI", "NLP", "Streamlit", "LangChain"],
         q="How can a long meeting recording become something you can act on in minutes?",
         flow=["Recording", "Transcript", "LLM Analysis", "Summary · Decisions · Actions"],
         body="Built an LLM-powered app (Streamlit, LangChain) that turns meeting recordings into transcripts, "
              "summaries, key points, decisions and action items, with an interactive interface to explore them."),
    dict(cat=["Data"], no="02", icon="📈", title="Student Performance Analysis",
         sub="Python · Statistics · Visualization", stack=["Python", "Statistics", "Charts"],
         q="Which factors are most associated with how students perform?",
         flow=["Collect", "Clean", "Statistical Analysis", "Charts & Reports"],
         body="Collected and cleaned academic data using Python, applied statistical analysis to identify factors "
              "affecting performance, and presented findings through charts and visual reports."),
    dict(cat=["Data"], no="03", icon="⚖️", title="The 1 in the 0's",
         sub="When Data Meets Discrimination", stack=["EDA", "Visualization", "Dashboards"],
         q="What patterns, trends and potential bias can real-world data reveal?",
         flow=["Data", "Cleaning", "EDA", "Visualization", "Insights"],
         body="Explored real-world datasets to identify patterns, trends and potential bias, then presented the "
              "findings through reports and dashboards in an easy-to-understand way."),
    dict(cat=["Hosting", "Leadership"], no="04", icon="🎤", title="Microsoft · INCEPTA HER 1.0",
         sub="Event Host / MC · Sept 2026", stack=["Emerging AI", "Cloud DevOps", "AdTech", "Industry Insights"],
         q="How do you keep a technology event engaging for ~100 attendees?",
         flow=["Stage Flow", "Speaker Intros", "Audience Engagement", "Transitions"],
         body="Anchored a dynamic tech event featuring eminent speakers, managed stage flow and coordinated with "
              "speakers and organizers to give every attendee a smooth, engaging experience."),
    dict(cat=["AI & Research"], no="05", icon="🔬", title="IEEE · Research Work",
         sub="Member · Research &amp; Technical Activities", stack=["Paper Reading", "Workshops", "Seminars"],
         q="How does an emerging technology move from paper to practice?",
         flow=["Read", "Discuss", "Workshop", "Apply"],
         body="Active IEEE member taking part in research paper reading sessions, technical discussions, "
              "workshops and seminars on technology, data and AI."),
    dict(cat=["Leadership", "Hosting"], no="06", icon="🎓", title="Placement Cell Coordinator",
         sub="IITM, Delhi · 2025 – Present", stack=["Coordination", "Data Accuracy", "Communication"],
         q="How do recruiters, students and faculty stay perfectly in sync?",
         flow=["Recruiters", "Student Coordinator", "Students & Faculty"],
         body="Maintained placement records with accuracy, coordinated between companies and students, and "
              "helped organise pre-placement sessions, workshops and GD/PI practice."),
]

FILTERS = ["All", "Data", "AI & Research", "Hosting", "Leadership"]
if hasattr(st, "pills"):
    choice = st.pills("Filter", FILTERS, default="All", label_visibility="collapsed")
else:
    choice = st.radio("Filter", FILTERS, horizontal=True, label_visibility="collapsed")
choice = choice or "All"

shown = [p for p in PROJECTS if choice == "All" or choice in p["cat"]]
cards = ""
for p in shown:
    flow = '<i>→</i>'.join(f"<span>{s}</span>" for s in p["flow"])
    cards += f"""
    <div class="card proj"><div class="no">{p['no']}</div><div class="ico">{p['icon']}</div>
    <h3>{p['title']}</h3><div class="eyebrow" style="letter-spacing:.1em">{p['sub']}</div>
    <div class="q"><b>Question:</b> {p['q']}</div>
    <div class="flow">{flow}</div>
    <p>{p['body']}</p>{chips(p['stack'], 'l')}</div>
    """
md(f'<div class="grid g2">{cards}</div>')

# ---------------- DATA & ANALYTICS ----------------
section("data", "01 · Data &amp; Analytics", "From raw data to actionable insights",
        "Skills are only convincing with proof, so here is each tool next to where I used it.")
md(f"""
<div style="margin-bottom:16px">{chips(["Python", "SQL", "Power BI", "Excel", "Statistics", "Data Cleaning", "EDA", "Visualization"])}</div>
<div class="grid g2">
<div class="card"><h3>Skill → Proof</h3>
<div class="proof"><b>Python</b><span>Student Performance Analysis</span></div>
<div class="proof"><b>EDA &amp; Visualization</b><span>The 1 in the 0's</span></div>
<div class="proof"><b>Statistics</b><span>Student Performance Analysis</span></div>
<div class="proof"><b>Data accuracy</b><span>Placement Cell records</span></div>
<div class="proof"><b>Power BI / Excel</b><span>Reports &amp; dashboards</span></div></div>
<div class="card"><h3>My analysis approach</h3>
<div class="flow" style="margin-top:14px"><span>Collect</span><i>→</i><span>Clean</span><i>→</i><span>Explore</span><i>→</i><span>Visualize</span><i>→</i><span>Insight</span></div>
<p>Relevant coursework: Data Analytics, Database Management Systems, Statistics, Python Programming, Business Intelligence.</p>
<p>Certified: <b>Data Analytics – ShapeMySkill</b>.</p></div>
</div>
""")

# ---------------- AI & RESEARCH ----------------
section("ai", "02 · AI &amp; Research", "Exploring how intelligent systems solve practical problems")
md(f"""
<div style="margin-bottom:16px">{chips(["Generative AI", "Agentic AI", "NLP", "LLMs", "Python", "LangChain", "Streamlit", "APIs", "Git/GitHub"])}</div>
<div class="pipe">
<div class="node">🎙️<br>Meeting<br>Recording</div><div class="arrow">→</div>
<div class="node">📝<br>Transcription</div><div class="arrow">→</div>
<div class="node">🧠<br>LLM<br>Analysis</div><div class="arrow">→</div>
<div class="outs"><div>Summary</div><div>Key Points</div><div>Decisions</div><div>Action Items</div></div>
</div>
<div class="grid g2" style="margin-top:18px">
<div class="card"><h3>MeetFlow</h3><p>An LLM-powered meeting assistant with an interactive interface for exploring what was said, decided and assigned.</p></div>
<div class="card"><h3>Research · IEEE Member</h3><p>Research paper reading sessions, workshops, seminars and technical discussions on AI and Data Science. Also delivered academic and technical presentations that simplify complex information.</p></div>
</div>
""")

# ---------------- EXPERIENCE ----------------
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

# ---------------- HOSTING & LEADERSHIP ----------------
section("stage", "03 · Hosting &amp; Leadership", "On stage", "Hosting treated as the professional skill it is.")
md(f"""
<div class="stage">
<div class="eyebrow" style="color:#9FB2E8">Featured event</div>
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
<div class="grid g3" style="margin-top:18px">
<div class="card"><h3>Public speaking</h3><p>Voice modulation, script writing and simplifying complex ideas for diverse audiences.</p></div>
<div class="card"><h3>Crisis handling</h3><p>Calm, quick adjustments to live changes in schedule and stage flow.</p></div>
<div class="card"><h3>Recognition</h3><p>Appreciated by faculty and organizers for audience engagement and stage presence.</p></div>
</div>
""")

# ---------------- ACHIEVEMENTS ----------------
section("achievements", "Achievements", "Proof, not a certificate graveyard")
md("""
<div class="grid g3 badge">
<div class="card"><div class="ico">🏆</div><h3>2nd Best Project</h3><p>Among 65 students, Generative AI &amp; Agentic AI training</p></div>
<div class="card"><div class="ico">🎤</div><h3>Microsoft Event Host</h3><p>INCEPTA HER 1.0, Sept 2026</p></div>
<div class="card"><div class="ico">🔬</div><h3>IEEE Member</h3><p>Research &amp; technical activities</p></div>
<div class="card"><div class="ico">🎓</div><h3>Placement Cell Coordinator</h3><p>Student–recruiter coordination at IITM</p></div>
<div class="card"><div class="ico">📜</div><h3>Certifications</h3><p>Data Analytics (ShapeMySkill) · Generative &amp; Agentic AI, GRASSTech (4-week practical training)</p></div>
<div class="card"><div class="ico">🌟</div><h3>Frequently selected anchor</h3><p>For major institutional events</p></div>
</div>
""")

# ---------------- SKILLS ----------------
section("skills", "Skills", "Organised by what they're for")
md(f"""
<div class="grid g3">
<div class="card"><h3>Programming</h3>{chips(["Python", "SQL", "C", "Java"])}</div>
<div class="card"><h3>Data</h3>{chips(["Power BI", "Excel", "Google Sheets", "Data Cleaning", "EDA", "Statistics", "Visualization", "Jupyter"])}</div>
<div class="card"><h3>AI</h3>{chips(["Generative AI", "Agentic AI", "NLP", "ML Fundamentals", "Classification", "Regression"])}</div>
<div class="card"><h3>Tools</h3>{chips(["Streamlit", "LangChain", "APIs", "Git/GitHub", "Google Forms", "SurveyMonkey"])}</div>
<div class="card"><h3>Professional</h3>{chips(["Communication", "Public Speaking", "Leadership", "Team Collaboration", "Problem Solving", "Time Management", "Adaptability"], "l")}</div>
<div class="card"><h3>Languages</h3><p><b>Hindi</b>: Native<br><b>English</b>: Professional Working Proficiency</p></div>
</div>
""")

# ---------------- BEYOND THE SCREEN ----------------
section("beyond", "Beyond the screen", "The person behind the projects")
md("""
<div class="grid g4">
<div class="mini">🎤 Hosting</div><div class="mini">📢 Public Speaking</div>
<div class="mini">📚 Research &amp; Learning</div><div class="mini">💡 Technology Exploration</div>
</div>
""")

# ---------------- RESUMES ----------------
section("resume", "Resumes", "Looking for something specific?", "Three focused resumes, one person.")
RESUMES = [
    ("📊", "Data / Analytics", "Data Analytics · Python · SQL · Power BI", "resume_data.pdf"),
    ("🤖", "AI / Research", "Generative AI · Agentic AI · Research · Projects", "resume_ai.pdf"),
    ("🎤", "Hosting / Communication", "Anchoring · MC · Public Speaking · Events", "resume_hosting.pdf"),
]
cols = st.columns(3, gap="medium")
for col, (icon, title, desc, fname) in zip(cols, RESUMES):
    with col:
        md(f'<div class="card"><div class="ico">{icon}</div><h3>{title}</h3><p>{desc}</p></div>')
        path = os.path.join(HERE, fname)
        if os.path.exists(path):
            with open(path, "rb") as f:
                st.download_button("Download resume", f.read(), file_name=fname,
                                   mime="application/pdf", key=fname, use_container_width=True)
        else:
            st.caption(f"Add `{fname}` next to app.py to enable download.")

# ---------------- CONTACT ----------------
extra = ""
if LINKEDIN_URL:
    extra += f'<a class="btn s" href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>'
if GITHUB_URL:
    extra += f'<a class="btn s" href="{GITHUB_URL}" target="_blank">GitHub</a>'
md(f"""
<div class="cta" id="contact">
<div class="eyebrow" style="color:#B9C8FF">Contact</div>
<h2>Let's build something meaningful.</h2>
<p>📍 Delhi, India &nbsp;·&nbsp; ✉️ {EMAIL} &nbsp;·&nbsp; 📞 {PHONE}</p>
<div class="btns" style="justify-content:center">
<a class="btn p" href="mailto:{EMAIL}">Let's Connect →</a>{extra}
</div></div>
<div class="foot">© 2026 Hritvi Maheshwari · Built with Python &amp; Streamlit</div>
""")
