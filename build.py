#!/usr/bin/env python3
"""Builds Favour Ogazi's static site into ../public.
Edit the CONTENT section below, then run:  python3 build.py
"""
import html, os, shutil, pathlib

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent / "public"

# ----------------------------------------------------------------- CONTENT
EMAIL = "thefavourogazi@gmail.com"
LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/favour-ogazi",
    "Substack": "https://favoursnewsletter.substack.com",
    "Medium": "https://medium.com/@thefavourogazi",
    "Instagram": "https://www.instagram.com/favourogazii",
    "X": "https://x.com/favour_ogazi",
}

CASES = [
    dict(slug="mighty-treasury", title="Building treasury and cross-border payment operations",
         short="Treasury & cross-border payments", org="Mighty Africa", role="Operations Lead",
         year="2025 – now", kind="Fintech operations", tags="ops",
         summary="Setting up the treasury workflows, trade desk execution and payment operations behind a growing cross-border fintech.",
         context="Mighty moves money across borders. As it grew, it needed treasury, liquidity and payment operations that could scale without breaking.",
         problem="Cross-border payments depend on many moving parts: liquidity in the right place, a trade desk that executes cleanly, and teams that work from the same playbook.",
         built=["Treasury and liquidity workflows", "Trade desk processes and controls", "Cross-functional operating rhythm across teams", "Documentation and tooling, with AI and automation where they save time"],
         metrics=[("—%", "Efficiency gain"), ("—", "Markets supported"), ("—", "Team developed")],
         lesson="To be written with Favour."),
    dict(slug="dni", title="DNI", short="DNI", org="To confirm", role="To confirm", year="To confirm", kind="Project", tags="advisory",
         summary="Full story, role and outcomes coming from Favour's Notion case study.",
         context="", problem="", built=[], metrics=[("—", "Outcome"), ("—", "Outcome"), ("—", "Outcome")], lesson=""),
    dict(slug="gamp", title="GAMP", short="GAMP", org="To confirm", role="To confirm", year="To confirm", kind="Project", tags="advisory",
         summary="Full story, role and outcomes coming from Favour's Notion case study.",
         context="", problem="", built=[], metrics=[("—", "Outcome"), ("—", "Outcome"), ("—", "Outcome")], lesson=""),
    dict(slug="lagos-liga-2024", title="Lagos Liga 2024", short="Lagos Liga 2024", org="To confirm", role="To confirm", year="2024", kind="Event", tags="events",
         summary="Full story, role and outcomes coming from Favour's Notion case study.",
         context="", problem="", built=[], metrics=[("—", "Outcome"), ("—", "Outcome"), ("—", "Outcome")], lesson=""),
    dict(slug="national-msme-conference-2024", title="National MSME Conference 2024", short="National MSME Conference", org="To confirm", role="To confirm", year="2024", kind="Event", tags="events",
         summary="Full story, role and outcomes coming from Favour's Notion case study.",
         context="", problem="", built=[], metrics=[("—", "Outcome"), ("—", "Outcome"), ("—", "Outcome")], lesson=""),
    dict(slug="techunwind-fest", title="TechUnwind Fest", short="TechUnwind Fest", org="To confirm", role="To confirm", year="To confirm", kind="Event", tags="events",
         summary="Full story, role and outcomes coming from Favour's Notion case study.",
         context="", problem="", built=[], metrics=[("—", "Outcome"), ("—", "Outcome"), ("—", "Outcome")], lesson=""),
]

ESSAYS = [
    ("What Do You Have In Your Hands?", "Jun 2026", "Medium", "ambition", "Ambition", "On building from what you already have, before chasing what you lack.", "https://medium.com/@thefavourogazi/what-do-you-have-in-your-hands-84d61900e5d2"),
    ("Have Hobbies That Do Not Scale.", "Jan 2026", "Medium", "life", "Life", "A case for private joys that can't be measured, monetised or posted.", "https://medium.com/@thefavourogazi/have-hobbies-that-do-not-scale-c2be5e06cc0a"),
    ("Slow Death.", "Nov 2025", "Medium", "life", "Life", "How we quietly lose ourselves, and how choosing yourself turns it around.", "https://medium.com/@thefavourogazi/slow-death-34ce5e1d343a"),
    ("You Want More Than I Can Give.", "Oct 2025", "Medium", "friendship", "Friendship", "On the weight of friendship, and giving your fullest self to a few.", "https://medium.com/@thefavourogazi/you-want-more-than-i-can-give-ccfd6936a4b8"),
    ("You Are Running Away Again.", "Jul 2025", "Medium", "life", "Life", "When retreat feels like rest, and the courage it takes to come back.", "https://medium.com/@thefavourogazi/you-are-running-away-again-18275b6b5e1c"),
    ("They Don't Tell You How It Feels To Be A Christian Girl In Nigeria.", "May 2025", "Substack", "faith womanhood", "Faith", "An honest reflection on faith, setbacks and grace as a young woman.", "https://favoursnewsletter.substack.com/p/they-dont-tell-you-how-it-feels-to"),
    ("Bad Girls Of The Bible.", "Apr 2025", "Substack", "faith womanhood", "Faith", "Ten flawed women of scripture, and what their stories say about grace.", "https://favoursnewsletter.substack.com/p/bad-girls-of-the-bible"),
    ("They Say Your Twenties Are The Most Important Years Of Your Life.", "Mar 2025", "Medium", "life", "Growing up", "All the contradictory advice about your twenties, and how tiring it is.", "https://medium.com/@thefavourogazi/my-dear-i-am-trying-109839ba8daf"),
    ("Short Skirt.", "Jan 2025", "Medium", "womanhood life", "Womanhood", "A party-game nickname, and how the labels we choose shape how we're seen.", "https://medium.com/@thefavourogazi/short-skirt-3a386754d9fb"),
]

TOPICS = [
    ("Business operations", "Turning strategy into systems, structure and execution."),
    ("Leadership and ownership", "Building accountable teams and thinking like a business partner."),
    ("Entrepreneurship", "Helping founders build businesses that can grow beyond them."),
    ("Fintech operations", "Cross-border payments, treasury workflows and trade desk execution."),
    ("AI for business", "Practical ways to improve workflows and everyday operations."),
    ("Career growth", "Navigating career transitions and building career capital."),
    ("Writing and storytelling", "Finding your voice and communicating ideas with clarity."),
]

SERVICES = [
    ("Business & pricing systems", "Pricing, unit economics and the systems that make a business run on purpose."),
    ("Operations advisory", "Processes, structure and operating rhythm that free founders from the day-to-day."),
    ("AI implementation", "Practical automation that saves your team time, without the hype."),
    ("Growth strategy", "Clear priorities and plans that move you from idea to execution."),
    ("Leadership", "Helping leaders build accountable teams and lead with clarity."),
]

PRINCIPLES = [
    ("Documentation", "If it isn't written down, it didn't happen. I capture what was done, why, and what came of it, so work outlives the moment."),
    ("Communication", "Strategy only becomes reality when the people carrying it understand it. Clear, early and often."),
    ("AI-forward thinking", "Using automation and AI to simplify operations and give people more time for meaningful work."),
]

# ----------------------------------------------------------------- TEMPLATE
e = html.escape
NAV = [("Work", "work.html"), ("FONO", "fono.html"), ("Writing", "writing.html"), ("Speaking", "speaking.html"), ("About", "about.html")]

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true" fill="currentColor">'
        '<rect x="3" y="8" width="4.2" height="24"/><rect x="3" y="8" width="14" height="4.2"/><rect x="3" y="18.2" width="10.5" height="3.8"/>'
        '<circle cx="28.5" cy="20" r="8.6" fill="none" stroke="currentColor" stroke-width="4"/></svg>')

def head(title, desc):
    t = "Favour Ogazi" if title == "Home" else f"{title} · Favour Ogazi"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(t)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0A0A0A">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Instrument+Serif:ital@0;1&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
"""

def nav(active):
    items = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if l == active else ""}>{l}</a></li>' for l, h in NAV)
    cur = ' aria-current="page"' if active == "Contact" else ""
    return f"""<div class="progress" aria-hidden="true"></div>
<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Favour Ogazi, home">{LOGO}<span class="name">Favour Ogazi</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
    <ul class="nav-links" id="nav-links">{items}<li><a class="nav-cta" href="contact.html"{cur}>Work with me</a></li></ul>
  </div>
</header>
<main>
"""

def footer():
    soc = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in LINKS.items())
    pages = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in NAV)
    return f"""</main>
<footer class="footer dark">
  <div class="wrap">
    <div class="footer-top">
      <a href="contact.html" class="footer-big">Let's build<br><em>something.</em></a>
      <div class="footer-cols">
        <div><p class="label muted" style="margin-bottom:14px">Pages</p><ul>{pages}<li><a href="contact.html">Work with me</a></li></ul></div>
        <div><p class="label muted" style="margin-bottom:14px">Elsewhere</p><ul>{soc}</ul></div>
        <div><p class="label muted" style="margin-bottom:14px">Email</p><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
      </div>
    </div>
    <div class="footer-bottom"><span class="logo" style="color:var(--paper)">{LOGO}</span><span>© <span id="yr">2026</span> Favour Ogazi · Lagos</span></div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""

def photo(src, label, cls=""):
    return f'<figure class="photo {cls}" data-label="{e(label)}"><img src="{src}" alt="{e(label)}" loading="lazy"></figure>'

def page(name, title, desc, body, active):
    (OUT / name).write_text(head(title, desc) + nav(active) + body + footer(), encoding="utf-8")

# ----------------------------------------------------------------- PAGES
def home():
    featured = CASES[:4]
    cards = "".join(f"""
      <a class="card" href="work-{c['slug']}.html">
        {photo(f"assets/img/work-{c['slug']}.jpg", c['short'], "wide")}
        <div class="meta"><span class="label muted">{e(c['kind'])}</span><span class="label muted">{e(c['year'])}</span></div>
        <h3>{e(c['title'])}</h3>
        <p>{e(c['summary'])}</p>
      </a>""" for c in featured)
    pr = "".join(f'<div{" class=\"no-js-hide\"" if i else ""}><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(PRINCIPLES))
    latest = "".join(f'<li><a href="{u}" target="_blank" rel="noopener"><span class="k">{e(tag)}</span><h3>{e(t)}<span class="sub">{e(s)}</span></h3><span class="d">{e(d)}</span></a></li>' for t, d, src, c, tag, s, u in ESSAYS[:3])
    body = f"""
<section class="hero dark" aria-label="Introduction">
  <div class="wrap">
    <div>
      <p class="label muted rv">Operations leader · Founder · Writer</p>
      <h1 class="rv" style="margin-top:28px">Favour<span>Ogazi</span></h1>
      <div class="roles label rv"><span>Operations Lead, Mighty Africa</span><span class="muted">Founder, FONO</span></div>
    </div>
    <div class="hero-side">
      {photo("assets/img/portrait.jpg", "Portrait")}
      <p class="lead rv">I bring clarity to complex problems, build systems that work, and turn strategy into measurable results.</p>
      <span class="scroll-cue">Scroll</span>
    </div>
  </div>
</section>

<section class="scrolly light" style="height:240vh" aria-label="What I do">
  <div class="stage"><div class="wrap">
    <p class="label muted" style="margin-bottom:28px">The thread</p>
    <p class="reveal-text" data-words>I take ideas, businesses, teams and messy situations, and make them <em>work better.</em></p>
  </div></div>
</section>

<section class="scrolly dark sides-wrap" style="height:440vh" aria-label="One operator, several sides">
  <div class="stage"><div class="wrap">
    <div class="sides">
      <ul class="side-list"><li>Operator</li><li>Advisor</li><li>Writer</li><li>Speaker</li></ul>
      <div class="side-panels">
        <div><span class="label muted">01 · First, always</span><h3 class="h-md">Operator</h3><p>Operations Lead at Mighty Africa, building treasury and cross-border payment operations. Strategy, structure and execution.</p><a class="link-arrow" href="work.html">See the work</a></div>
        <div class="no-js-hide"><span class="label muted">02 · Since 2023</span><h3 class="h-md">Advisor</h3><p>Founder of FONO, helping businesses with operating systems, pricing, growth strategy and AI implementation.</p><a class="link-arrow" href="fono.html">About FONO</a></div>
        <div class="no-js-hide"><span class="label muted">03 · The heart</span><h3 class="h-md">Writer</h3><p>Essays on life, womanhood, friendship, ambition and faith, read by thousands on Substack and Medium.</p><a class="link-arrow" href="writing.html">Read the writing</a></div>
        <div class="no-js-hide"><span class="label muted">04 · In the room</span><h3 class="h-md">Speaker &amp; teacher</h3><p>Talks, panels and classes on operations, leadership, careers, content and storytelling.</p><a class="link-arrow" href="speaking.html">Speaking &amp; teaching</a></div>
        <div class="no-js-hide"><span class="label muted">One body of work</span><h3 class="h-md">Not four people. One builder.</h3><p>Running operations, advising businesses, writing to make sense of it, and teaching what I learn.</p><a class="link-arrow" href="about.html">About me</a></div>
      </div>
    </div>
  </div></div>
</section>

<section class="scrolly light reel-section" aria-label="Selected work">
  <div class="stage"><div class="wrap" style="overflow:visible">
    <div class="section-head" style="margin-bottom:36px">
      <div style="display:grid;gap:14px"><p class="label muted">Selected work</p><h2 class="h-xl">The work,<br><em>shown.</em></h2></div>
      <a class="link-arrow" href="work.html">All work</a>
    </div>
    <div class="reel">{cards}
      <a class="card end" href="work.html"><p class="label muted">Portfolio</p><h3>See every case study, with the problem, what I built and what changed.</h3><span class="link-arrow">View portfolio</span></a>
    </div>
  </div></div>
</section>

<section class="scrolly white pr-section" style="height:320vh" aria-label="How I work">
  <div class="stage"><div class="wrap">
    <p class="label muted" style="margin-bottom:26px">Three things shape how I work</p>
    <div class="pr-wrap">
      <div class="pr-num">1</div>
      <div><div class="pr-items">{pr}</div><div class="dots"><i class="on"></i><i></i><i></i></div></div>
    </div>
  </div></div>
</section>

<section class="section dark" aria-label="Latest writing">
  <div class="wrap">
    <div class="section-head">
      <div style="display:grid;gap:14px"><p class="label muted">Writing</p><h2 class="h-xl">Ideas, <em>over time.</em></h2></div>
      <a class="link-arrow" href="writing.html">All writing</a>
    </div>
    <ul class="rows">{latest}</ul>
  </div>
</section>

<section class="section light" aria-label="Now">
  <div class="wrap grid-2">
    <div style="display:grid;gap:18px;align-content:start"><p class="label muted">Updated every few months</p><h2 class="h-xl">Now</h2></div>
    <ul class="rows">
      <li><div class="row-inner"><span class="k">Building</span><h3>Treasury and cross-border payment operations at Mighty.</h3><span></span></div></li>
      <li><div class="row-inner"><span class="k">Growing</span><h3>FONO's advisory work.</h3><span></span></div></li>
      <li><div class="row-inner"><span class="k">Writing</span><h3>My first anthology.</h3><span></span></div></li>
      <li><div class="row-inner"><span class="k">Learning</span><h3>Finance, AI and automation, and how they give people time back.</h3><span></span></div></li>
    </ul>
  </div>
</section>
"""
    page("index.html", "Home", "Favour Ogazi is an operations leader who brings clarity to complex problems, builds systems that work, and turns strategy into measurable results.", body, "Home")

def work():
    idx = "".join(f'<li><a href="#p-{c["slug"]}">{e(c["short"])}</a></li>' for c in CASES)
    projects = "".join(f"""
      <article class="project rv" id="p-{c['slug']}" data-c="{c['tags']}">
        <a href="work-{c['slug']}.html">{photo(f"assets/img/work-{c['slug']}.jpg", c['short'], "wide")}</a>
        <div class="meta"><span class="label">{e(c['kind'])}</span><span class="label muted">{e(c['org'])}</span><span class="label muted">{e(c['year'])}</span></div>
        <h2><a href="work-{c['slug']}.html">{e(c['title'])}</a></h2>
        <p>{e(c['summary'])}</p>
        <a class="link-arrow" href="work-{c['slug']}.html">Read case study</a>
      </article>""" for c in CASES)
    body = f"""
<section class="page-hero light">
  <div class="wrap">
    <p class="label muted rv">Portfolio · Case studies</p>
    <h1 class="rv">Selected <em>work</em></h1>
    <div class="row"><p class="lead rv">Operations is hard to see from the outside. Each case study shows the problem, what I built, the people involved, and the results I can share.</p>
    <div class="chips rv" data-filter-group="#projects" role="group" aria-label="Filter work"><button type="button" aria-pressed="true" data-f="all">All</button><button type="button" aria-pressed="false" data-f="ops">Operations</button><button type="button" aria-pressed="false" data-f="advisory">Advisory</button><button type="button" aria-pressed="false" data-f="events">Events</button></div></div>
  </div>
</section>
<section class="light" style="padding-bottom:clamp(40px,6vw,80px)">
  <div class="wrap split">
    <div class="split-sticky"><p class="label muted">Index</p><ul class="index-list" data-spy>{idx}</ul></div>
    <div id="projects">{projects}</div>
  </div>
</section>
<section class="section dark" aria-label="Testimonials">
  <div class="wrap" style="display:grid;gap:40px">
    <p class="label muted">What people say</p>
    <p class="pull">Testimonials from Favour's portfolio go here.</p>
    <span class="note">To add from Notion portfolio</span>
  </div>
</section>
"""
    page("work.html", "Work", "Selected work and case studies by Favour Ogazi: operations, advisory and events.", body, "Work")

def case_pages():
    for i, c in enumerate(CASES):
        nxt = CASES[(i + 1) % len(CASES)]
        pending = not c["context"]
        built = "".join(f"<li>{e(b)}</li>" for b in c["built"]) or "<li>To come from the case study.</li>"
        metrics = "".join(f"<div><b>{e(v)}</b><span>{e(l)}</span></div>" for v, l in c["metrics"])
        chapters = [("context", "Context", f"<p>{e(c['context'] or 'The background: the organisation, the moment and why this work mattered.')}</p>"),
                    ("problem", "The problem", f"<p>{e(c['problem'] or 'What was broken, slow or missing, and what was at stake.')}</p>"),
                    ("built", "What I built", f'<ul class="prose" style="padding-left:20px">{built}</ul>'),
                    ("outcome", "Outcome", f'<div class="metrics">{metrics}</div><p class="muted" style="font-size:14px">Percentages and growth figures only. No partner names or exact revenue.</p>'),
                    ("lessons", "Lessons", f"<p>{e(c['lesson'] or 'What this taught me, and what I would do again.')}</p>")]
        cnav = "".join(f'<li><a href="#{k}">{t}</a></li>' for k, t, _ in chapters)
        csec = "".join(f'<section class="chapter rv" id="{k}"><p class="label muted">{n:02d}</p><h2>{t}</h2><div class="prose">{b}</div></section>' for n, (k, t, b) in enumerate(chapters, 1))
        note = '<span class="note">Draft: details to come from Favour\'s Notion case study</span>' if pending else '<span class="note">Draft: figures to confirm with Favour</span>'
        body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <a class="label muted rv" href="work.html">← All work</a>
    <h1 class="rv" style="font-size:clamp(40px,6.4vw,96px)">{e(c['title'])}</h1>
    <p class="lead rv" style="color:#CFCFCB">{e(c['summary'])}</p>
    <div class="case-meta rv"><div><span class="label muted">Organisation</span><b>{e(c['org'])}</b></div><div><span class="label muted">Role</span><b>{e(c['role'])}</b></div><div><span class="label muted">Type</span><b>{e(c['kind'])}</b></div><div><span class="label muted">When</span><b>{e(c['year'])}</b></div></div>
    <div>{note}</div>
  </div>
</section>
<section class="dark" style="padding-bottom:clamp(48px,7vw,96px)"><div class="wrap">{photo(f"assets/img/work-{c['slug']}.jpg", c['short'] + " · cover image", "wide")}</div></section>
<section class="section light">
  <div class="wrap chapters">
    <ul class="chapter-nav" data-spy>{cnav}</ul>
    <div>{csec}
      <div class="grid-2">{photo(f"assets/img/work-{c['slug']}-2.jpg", "Photo", "square")}{photo(f"assets/img/work-{c['slug']}-3.jpg", "Photo", "square")}</div>
    </div>
  </div>
</section>
<section class="white"><div class="wrap next-case"><p class="label muted">Next case study</p><a href="work-{nxt['slug']}.html">{e(nxt['short'])} →</a></div></section>
"""
        page(f"work-{c['slug']}.html", c["short"], c["summary"], body, "Work")

def fono():
    svc = "".join(f'<li><div class="row-inner"><span class="k">{n:02d}</span><h3>{e(t)}<span class="sub">{e(d)}</span></h3><span></span></div></li>' for n, (t, d) in enumerate(SERVICES, 1))
    steps = [("Understand", "We learn your business, your goals and what's getting in the way."), ("Design", "We build tailored, data-grounded strategies and systems. No templates."), ("Execute", "We work alongside you to put them in place."), ("Evaluate", "We measure what changed and keep improving.")]
    st = "".join(f'<div class="rv"><span class="label muted">{n:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for n, (t, d) in enumerate(steps, 1))
    body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <p class="label muted rv">The firm · Since 2023</p>
    <h1 class="rv" style="font-size:clamp(80px,18vw,280px)">FONO</h1>
    <div class="row"><p class="lead rv" style="color:#CFCFCB">FONO Consulting is my advisory firm. We help business owners run their businesses with clarity, structure and purpose.</p><a class="btn rv" href="contact.html?topic=fono">Work with FONO</a></div>
  </div>
</section>
<section class="scrolly light" style="height:240vh" aria-label="Why FONO exists">
  <div class="stage"><div class="wrap">
    <p class="label muted" style="margin-bottom:28px">Why we exist</p>
    <p class="reveal-text" data-words>Too many founders are passionate, dedicated, and <em>overwhelmed.</em> We help bring the joy and the clarity back.</p>
  </div></div>
</section>
<section class="section white">
  <div class="wrap grid-2">
    <div style="display:grid;gap:18px;align-content:start"><p class="label muted">How we think</p><h2 class="h-lg">Your trusted <span class="serif-i">copilots.</span></h2></div>
    <div class="prose rv">
      <p>Every business is different, so we don't do one-size-fits-all. We take the time to understand your vision, your goals and your challenges.</p>
      <p>Then we build tailored strategies, grounded in data, that take you from idea to execution and evaluation. Practical guidance, a partner who understands, and room to grow with purpose.</p>
    </div>
  </div>
</section>
<section class="section light">
  <div class="wrap">
    <div class="section-head"><div style="display:grid;gap:14px"><p class="label muted">What we do</p><h2 class="h-xl">Services</h2></div></div>
    <ul class="rows">{svc}</ul>
  </div>
</section>
<section class="section dark">
  <div class="wrap" style="display:grid;gap:48px">
    <div style="display:grid;gap:14px"><p class="label muted">How we work</p><h2 class="h-xl">Idea to <em>execution.</em></h2></div>
    <div class="grid-3" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">{st}</div>
  </div>
</section>
<section class="section white">
  <div class="wrap" style="display:grid;gap:28px">
    <p class="label muted">Clients &amp; results</p>
    <p class="pull" style="font-style:normal;font-family:var(--sans);font-weight:700;letter-spacing:-.03em">Selected FONO projects and client testimonials.</p>
    <span class="note">To add from Favour's portfolio</span>
    <a class="link-arrow" href="work.html">See case studies</a>
  </div>
</section>
"""
    page("fono.html", "FONO", "FONO Consulting helps business owners with operating systems, pricing, growth strategy, AI implementation and leadership.", body, "FONO")

def writing():
    items = "".join(f'<li data-c="{c}"><a href="{u}" target="_blank" rel="noopener"><span class="k">{e(tag)} · {e(src)}</span><h3>{e(t)}<span class="sub">{e(s)}</span></h3><span class="d">{e(d)}</span></a></li>' for t, d, src, c, tag, s, u in ESSAYS)
    body = f"""
<section class="page-hero light">
  <div class="wrap">
    <p class="label muted rv">Writing · Essays &amp; notes</p>
    <h1 class="rv">Ideas, <em>over time</em></h1>
    <p class="lead rv">I write through my sensitivity, hoping to see myself better in my work. These are some of the pieces I keep coming back to.</p>
  </div>
</section>
<section class="light" style="padding-bottom:clamp(80px,11vw,160px)">
  <div class="wrap" style="display:grid;gap:32px">
    <div class="chips" data-filter-group="#essays" role="group" aria-label="Filter essays">
      <button type="button" aria-pressed="true" data-f="all">All</button><button type="button" aria-pressed="false" data-f="life">Life</button><button type="button" aria-pressed="false" data-f="womanhood">Womanhood</button><button type="button" aria-pressed="false" data-f="friendship">Friendship</button><button type="button" aria-pressed="false" data-f="ambition">Ambition</button><button type="button" aria-pressed="false" data-f="faith">Faith</button>
    </div>
    <ul class="rows" id="essays">{items}</ul>
  </div>
</section>
<section class="section dark">
  <div class="wrap grid-2" style="align-items:end">
    <div style="display:grid;gap:18px"><p class="label muted">The newsletter</p><h2 class="h-xl">Join 6,000+ <em>readers.</em></h2><p class="lead" style="color:#CFCFCB">New essays on life, faith, ambition and work, straight to your inbox through Substack.</p></div>
    <div style="display:grid;gap:16px">
      <a class="btn" href="https://favoursnewsletter.substack.com/subscribe" target="_blank" rel="noopener">Subscribe on Substack</a>
      <div style="display:flex;gap:24px;flex-wrap:wrap"><a class="link-arrow" href="{LINKS['Medium']}" target="_blank" rel="noopener">Medium</a><a class="link-arrow" href="{LINKS['Substack']}" target="_blank" rel="noopener">Substack</a></div>
    </div>
  </div>
</section>
<section class="section white">
  <div class="wrap grid-2" style="align-items:center">
    {photo("assets/img/anthology.jpg", "Anthology cover", "")}
    <div style="display:grid;gap:18px"><p class="label muted">In the works</p><h2 class="h-xl">My first <em>anthology.</em></h2><p class="lead">Coming soon.</p></div>
  </div>
</section>
"""
    page("writing.html", "Writing", "Essays by Favour Ogazi on life, womanhood, friendship, ambition and faith.", body, "Writing")

def speaking():
    tl = "".join(f'<li><div class="row-inner"><span class="k">{n:02d}</span><h3>{e(t)}<span class="sub">{e(d)}</span></h3><span></span></div></li>' for n, (t, d) in enumerate(TOPICS, 1))
    body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <p class="label muted rv">Speaking · Teaching</p>
    <h1 class="rv">In the <em>room</em></h1>
    <div class="row"><p class="lead rv" style="color:#CFCFCB">Panels, workshops, interviews, podcasts and classes. I speak and teach on operations, leadership, careers and storytelling.</p><a class="btn rv" href="contact.html?topic=speaking">Invite me to speak</a></div>
  </div>
</section>
<section class="section light">
  <div class="wrap">
    <div class="section-head"><div style="display:grid;gap:14px"><p class="label muted">Book me for</p><h2 class="h-xl">Topics</h2></div></div>
    <ul class="rows">{tl}</ul>
  </div>
</section>
<section class="section white">
  <div class="wrap grid-2" style="align-items:center">
    <div style="display:grid;gap:18px"><p class="label muted">Teaching</p><h2 class="h-lg">Content creation &amp; digital marketing</h2><p class="lead">I teach remote cohorts at a London and Lagos tech academy: a two-month content creation course and a three-month digital marketing course.</p></div>
    {photo("assets/img/teaching.jpg", "Teaching", "wide")}
  </div>
</section>
<section class="section dark">
  <div class="wrap" style="display:grid;gap:36px">
    <div class="section-head" style="margin:0"><div style="display:grid;gap:14px"><p class="label muted">Moments</p><h2 class="h-xl">On <em>stage.</em></h2></div><span class="note">Photos to add from Favour's speaking highlights</span></div>
    <div class="grid-2" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px">{photo("assets/img/speaking-1.jpg","Event photo","square")}{photo("assets/img/speaking-2.jpg","Event photo","square")}{photo("assets/img/speaking-3.jpg","Event photo","square")}</div>
  </div>
</section>
"""
    page("speaking.html", "Speaking", "Favour Ogazi speaks and teaches on business operations, leadership, fintech, AI, careers and storytelling.", body, "Speaking")

def about():
    pr = "".join(f'<div class="rv"><span class="label muted">{n:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for n, (t, d) in enumerate(PRINCIPLES, 1))
    body = f"""
<section class="page-hero light">
  <div class="wrap">
    <p class="label muted rv">About</p>
    <h1 class="rv">One <em>builder</em></h1>
  </div>
</section>
<section class="light" style="padding-bottom:clamp(80px,11vw,160px)">
  <div class="wrap grid-2">
    {photo("assets/img/about.jpg", "Portrait")}
    <div class="prose rv" style="align-content:start">
      <p style="font-size:clamp(20px,2vw,26px);line-height:1.45;font-weight:500;letter-spacing:-.01em">I'm Favour, a commercially minded operations leader. I bring clarity to complex problems, build systems that work, and turn strategy into measurable results.</p>
      <p>I lead operations at Mighty Africa, where I'm building treasury and cross-border payment operations. Through FONO, my advisory firm, I help businesses with operating systems, pricing, growth strategy and AI implementation.</p>
      <p>I'm also a writer. Writing is how I process what I see and share it, and thousands of readers follow my essays on Substack and Medium.</p>
      <p>Outside work, I'm a woman of faith and someone who cares deeply about her people. I love good stories, thoughtful conversations, travel, movies, and finding humour in ordinary things. I serve in Children's Church, treasure my friendships, and want a full life, with room for ambition, love, curiosity and quiet.</p>
      <div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:8px"><a class="link-arrow" href="{LINKS['LinkedIn']}" target="_blank" rel="noopener">LinkedIn</a><a class="link-arrow" href="contact.html">Work with me</a></div>
    </div>
  </div>
</section>
<section class="section dark">
  <div class="wrap" style="display:grid;gap:48px">
    <div style="display:grid;gap:14px"><p class="label muted">How I work</p><h2 class="h-xl">Three <em>principles.</em></h2></div>
    <div class="grid-3">{pr}</div>
  </div>
</section>
<section class="section white">
  <div class="wrap grid-2">
    <div style="display:grid;gap:18px;align-content:start"><p class="label muted">Updated every few months</p><h2 class="h-xl">Now</h2></div>
    <ul class="rows">
      <li><div class="row-inner"><span class="k">Building</span><h3>Treasury and cross-border payment operations at Mighty.</h3><span></span></div></li>
      <li><div class="row-inner"><span class="k">Growing</span><h3>FONO's advisory work.</h3><span></span></div></li>
      <li><div class="row-inner"><span class="k">Writing</span><h3>My first anthology.</h3><span></span></div></li>
      <li><div class="row-inner"><span class="k">Learning</span><h3>Finance, AI and automation.</h3><span></span></div></li>
    </ul>
  </div>
</section>
"""
    page("about.html", "About", "About Favour Ogazi: operations leader, founder of FONO, writer and woman of faith.", body, "About")

def contact():
    ways = [("Leadership roles", "Operations Lead, Head of Operations, Strategy & Operations or Chief of Staff, especially at international fintech and technology companies."),
            ("Advisory & consulting", "Operating systems, process improvement, growth strategy or AI implementation, through FONO."),
            ("Speaking & teaching", "Panels, workshops, podcasts and classes."),
            ("Writing & bylines", "Essays and commentary on business, leadership and life."),
            ("Collaborations", "Partnerships and projects with peers and organisations."),
            ("Investment", "Later. Happy to start the conversation.")]
    w = "".join(f'<div class="rv"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in ways)
    soc = "".join(f'<a class="link-arrow" href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in LINKS.items())
    body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <p class="label muted rv">Work with me</p>
    <h1 class="rv">If we're <em>aligned</em></h1>
    <p class="lead rv" style="color:#CFCFCB">This is what I do, what I've done, and how I think. If it fits what you need, here's how to reach me.</p>
  </div>
</section>
<section class="section light">
  <div class="wrap" style="display:grid;gap:40px">
    <p class="label muted">Ways to work together</p>
    <div class="grid-3">{w}</div>
  </div>
</section>
<section class="section white">
  <div class="wrap grid-2">
    <div style="display:grid;gap:22px;align-content:start">
      <p class="label muted">Email</p>
      <p class="h-md" style="word-break:break-word">{EMAIL}</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="mailto:{EMAIL}">Send an email</a><button class="btn ghost" type="button" data-copy="{EMAIL}">Copy address</button></div>
      <p class="label muted" style="margin-top:20px">Elsewhere</p>
      <div style="display:flex;gap:22px;flex-wrap:wrap">{soc}</div>
    </div>
    <form class="form" id="contact-form">
      <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="f-org">Organisation</label><input id="f-org" name="org" autocomplete="organization"></div>
      <div class="field"><label for="f-topic">What's this about?</label><select id="f-topic" name="topic"><option>Leadership role</option><option>Advisory / FONO</option><option>Speaking or teaching</option><option>Writing</option><option>Collaboration</option><option>Something else</option></select></div>
      <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required></textarea></div>
      <button class="btn" type="submit" style="justify-self:start">Send message</button>
      <p class="form-note" id="form-note" aria-live="polite"></p>
    </form>
  </div>
</section>
"""
    page("contact.html", "Work with me", "Work with Favour Ogazi: leadership roles, advisory through FONO, speaking, teaching, writing and collaborations.", body, "Contact")

def notfound():
    body = """
<section class="hero dark" style="min-height:80vh"><div class="wrap" style="grid-template-columns:1fr"><div style="display:grid;gap:24px">
<p class="label muted">404</p><h1>Not<span>found</span></h1><p class="lead" style="color:#CFCFCB">This page doesn't exist yet.</p><a class="link-arrow" href="index.html">Back home</a></div></div></section>"""
    page("404.html", "Page not found", "Page not found.", body, "")

def favicon():
    (OUT / "assets" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" fill="#0A0A0A"/>'
        '<g fill="#FAFAF8" transform="translate(2 0) scale(.9) translate(2 2)"><rect x="3" y="8" width="4.2" height="24"/><rect x="3" y="8" width="14" height="4.2"/><rect x="3" y="18.2" width="10.5" height="3.8"/>'
        '<circle cx="28.5" cy="20" r="8.6" fill="none" stroke="#FAFAF8" stroke-width="4"/></g></svg>', encoding="utf-8")

if __name__ == "__main__":
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT / "assets" / "img").mkdir(parents=True)
    for f in ("site.css", "site.js"): shutil.copy(SRC / "assets" / f, OUT / "assets" / f)
    (OUT / "assets" / "img" / "README.txt").write_text(
        "Drop photos here with these names and they appear automatically (shown in black and white):\n"
        "portrait.jpg (homepage), about.jpg, anthology.jpg, teaching.jpg, speaking-1.jpg..speaking-3.jpg,\n"
        "work-<slug>.jpg (cover), work-<slug>-2.jpg, work-<slug>-3.jpg for each case study.\n"
        "Slugs: " + ", ".join(c["slug"] for c in CASES) + "\n", encoding="utf-8")
    favicon()
    home(); work(); case_pages(); fono(); writing(); speaking(); about(); contact(); notfound()
    print("Built", sorted(p.name for p in OUT.glob("*.html")))
