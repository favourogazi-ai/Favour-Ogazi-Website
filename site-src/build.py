#!/usr/bin/env python3
"""Builds Favour Ogazi's static site into ../public.
Edit the CONTENT section, then run:  python3 site-src/build.py
Works with Python 3.8+ (including the Python that ships with macOS).
"""
import html, pathlib, shutil

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent / "public"

# ======================================================================= CONTENT
EMAIL = "thefavourogazi@gmail.com"
NEWSLETTER = "https://favoursnewsletter.substack.com/subscribe"
WAITLIST_URL = NEWSLETTER  # placeholder until the anthology list exists
LINKS = [
    ("LinkedIn", "https://www.linkedin.com/in/favour-ogazi"),
    ("Substack", "https://favoursnewsletter.substack.com"),
    ("Medium", "https://medium.com/@thefavourogazi"),
    ("X", "https://x.com/favour_ogazi"),
    ("Instagram", "https://www.instagram.com/favourogazii"),
]

PARTS = [
    ("Operations", "By day, I'm Operations Lead at Mighty, a company that moves money across borders for businesses. My job is the running of things: making sure money moves when it should, clients are set up properly, and the team knows what matters this week.",
     "https://www.linkedin.com/in/favour-ogazi", "Find me on LinkedIn", True),
    ("FONO", "FONO Consulting is an advisory firm focused on helping business owners run their businesses with clarity, structure and purpose. I started it for founders whose business has outgrown the way it's being run.",
     "index.html#contact", "Talk to FONO", False),
    ("Writing", "I read a lot and think slowly. Writing is how I work out what I believe about people, work, love and faith, and I share it with readers on Substack, Medium and X.",
     "writing.html", "Read my writing", False),
]

# (title, date, source, filter tags, label, one line, url) — newest first
ESSAYS = [
    ("What Do You Have In Your Hands?", "Jun 2026", "Medium", "productivity psychology", "Productivity", "On starting with what you already have, instead of waiting for what you don't.", "https://medium.com/@thefavourogazi/what-do-you-have-in-your-hands-84d61900e5d2"),
    ("Have Hobbies That Do Not Scale.", "Jan 2026", "Medium", "productivity psychology", "Productivity", "A case for small joys you never measure, sell or post.", "https://medium.com/@thefavourogazi/have-hobbies-that-do-not-scale-c2be5e06cc0a"),
    ("Slow Death.", "Nov 2025", "Medium", "psychology relationships", "Psychology", "How we lose ourselves a little at a time, and how we come back.", "https://medium.com/@thefavourogazi/slow-death-34ce5e1d343a"),
    ("You Want More Than I Can Give.", "Oct 2025", "Medium", "relationships", "Relationships", "On friendship, limits, and giving your whole self to a few people.", "https://medium.com/@thefavourogazi/you-want-more-than-i-can-give-ccfd6936a4b8"),
    ("You Are Running Away Again.", "Jul 2025", "Medium", "psychology", "Psychology", "When hiding feels like rest, and what it takes to come back.", "https://medium.com/@thefavourogazi/you-are-running-away-again-18275b6b5e1c"),
    ("They Don't Tell You How It Feels To Be A Christian Girl In Nigeria.", "May 2025", "Substack", "faith womanhood", "Faith", "Faith, setbacks and grace, honestly.", "https://favoursnewsletter.substack.com/p/they-dont-tell-you-how-it-feels-to"),
    ("Bad Girls Of The Bible.", "Apr 2025", "Substack", "faith womanhood", "Faith", "Ten imperfect women of scripture, and what they teach about grace.", "https://favoursnewsletter.substack.com/p/bad-girls-of-the-bible"),
    ("They Say Your Twenties Are The Most Important Years Of Your Life.", "Mar 2025", "Medium", "psychology productivity", "Psychology", "All the conflicting advice about your twenties, and how tiring it gets.", "https://medium.com/@thefavourogazi/my-dear-i-am-trying-109839ba8daf"),
    ("Short Skirt.", "Jan 2025", "Medium", "womanhood psychology", "Womanhood", "A nickname from a party game, and how labels shape how we're seen.", "https://medium.com/@thefavourogazi/short-skirt-3a386754d9fb"),
]

TWEETS = [
    ("x-1.png", "https://x.com/Favour_Ogazi/status/2089991110009516113", "I think one of my favourite things about life is still meeting someone and immediately knowing: oh, you are going to matter."),
    ("x-2.png", "https://x.com/Favour_Ogazi/status/2096610437399773338", "Money buys a lot of extremely underrated things. Convenience. Time. Options. Privacy. Distance from nonsense."),
    ("x-3.png", "https://x.com/Favour_Ogazi/status/2092571639879708870", "Some opportunities arrive because you are talented. Others arrive because someone remembered you were reliable."),
    ("x-4.png", "https://x.com/Favour_Ogazi/status/2103749188030730630", "Good friendships make ordinary life feel important."),
    ("x-5.png", "https://x.com/Favour_Ogazi/status/2100671115118997524", "At some point, you have to let yourself be witnessed."),
]

# ======================================================================= TEMPLATE
e = html.escape
NAV = [("About", "index.html#about"), ("FONO", "index.html#fono"), ("Writing", "writing.html"), ("Contact", "index.html#contact")]

def head(title, desc):
    t = "Favour Ogazi" if title == "Home" else title + " · Favour Ogazi"
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/portrait.jpg">
<meta name="theme-color" content="#FAF8F4">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;1,400&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
""".format(t=e(t), d=e(desc))

def nav(active):
    items = "".join('<li><a href="{h}"{c}>{l}</a></li>'.format(h=h, l=l, c=' aria-current="page"' if l == active else "") for l, h in NAV)
    return """<header class="nav">
  <div class="wrap">
    <a class="wordmark" href="index.html">Favour Ogazi</a>
    <nav aria-label="Main"><ul>{items}</ul></nav>
  </div>
</header>
<main>
""".format(items=items)

def contact_block():
    soc = "".join('<a class="link" href="%s" target="_blank" rel="noopener">%s</a>' % (u, n) for n, u in LINKS)
    return """
<section class="section dark" id="contact">
  <div class="wrap contact">
    <p class="kicker">Get in touch</p>
    <h2>Say hello.</h2>
    <p class="lead" style="max-width:52ch">Whether it's about FONO, something I wrote, or you'd simply like to talk, email is the best way to reach me.</p>
    <a class="email" href="mailto:{em}">{em}</a>
    <div class="btns"><a class="btn" href="mailto:{em}">Send an email</a><button class="btn ghost" type="button" data-copy="{em}">Copy address</button></div>
    <div class="socials">{soc}</div>
  </div>
</section>
""".format(em=EMAIL, soc=soc)

def footer():
    return """</main>
<footer class="footer dark">
  <div class="wrap"><span>Favour Ogazi · Abuja, Nigeria</span><span>© <span id="yr">2026</span></span></div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""

def page(name, title, desc, body, active):
    (OUT / name).write_text(head(title, desc) + nav(active) + body + footer(), encoding="utf-8")

def essay_items(items):
    return "".join('<li data-c="{c}"><a href="{u}" target="_blank" rel="noopener"><span class="d">{d}</span><span class="t"><h3>{t}</h3><span>{s}</span></span><span class="src">{src}</span></a></li>'.format(
        c=c, u=u, d=e(d), t=e(t), s=e(s), src=e(src)) for t, d, src, c, tag, s, u in items)

# ======================================================================= PAGES
def home():
    parts = "".join('<div{id}><h3>{t}</h3><p>{d}</p><a class="link" href="{h}"{tgt}>{l}</a></div>'.format(
        id=' id="fono"' if t == "FONO" else "", t=e(t), d=e(d), h=h, l=e(l), tgt=' target="_blank" rel="noopener"' if ext else "") for t, d, h, l, ext in PARTS)
    body = """
<section class="hero">
  <div class="wrap">
    <div class="hero-text">
      <p class="kicker">Operations · FONO · Writing</p>
      <h1>Hi, I'm Favour.</h1>
      <p class="lead">Most of my week goes to my 9-to-5 in operations. I also run FONO, a small advisory firm, and in the time that's left, I write.</p>
      <div class="btns"><a class="btn" href="writing.html">Read my writing</a><a class="btn ghost" href="#contact">Say hello</a></div>
    </div>
    <img class="portrait" src="assets/img/portrait.jpg" alt="Favour Ogazi">
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <p class="statement">I take ideas, businesses, teams and messy situations, and make them <em>work better.</em></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head"><p class="kicker">What I do</p><h2>Three things take up most of my time.</h2></div>
    <div class="parts">{parts}</div>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <div class="head-row"><div class="head"><p class="kicker">Recent writing</p><h2>Things I've been thinking about.</h2></div><a class="link" href="writing.html">All my writing</a></div>
    <ul class="essays">{essays}</ul>
    <div class="btns" style="margin-top:36px"><a class="btn" href="{nl}" target="_blank" rel="noopener">Get new essays by email</a></div>
  </div>
</section>

<section class="section" id="about">
  <div class="wrap two center">
    <img class="photo" src="assets/img/about.jpg" alt="Favour Ogazi" loading="lazy">
    <div class="prose">
      <p class="kicker">A little more about me</p>
      <h2>I never planned to work in operations.</h2>
      <p>I studied microbiology, then went back for a master's in Business and Management. A mix of chance and curiosity took me into operations, and I found I liked the part most people find boring: getting things to run properly.</p>
      <p>Outside work, I'm a woman of faith and I serve in Children's Church. I treasure my friends, love a good story, travel when I can, and watch more movies than I should. I'm based in Abuja.</p>
    </div>
  </div>
</section>
{contact}""".format(parts=parts, essays=essay_items(ESSAYS[:4]), nl=NEWSLETTER, contact=contact_block())
    page("index.html", "Home", "Favour Ogazi works in operations, runs the advisory firm FONO, and writes about people, work, love and faith.", body, "")

def writing():
    tw = "".join('<a href="{u}" target="_blank" rel="noopener"><img src="assets/img/{f}" alt="Post by Favour Ogazi: {t}" loading="lazy"></a>'.format(u=u, f=f, t=e(t)) for f, u, t in TWEETS)
    chips = "".join('<button type="button" aria-pressed="%s" data-f="%s">%s</button>' % ("true" if f == "all" else "false", f, l) for f, l in
                    [("all", "All"), ("psychology", "Psychology"), ("relationships", "Relationships"), ("productivity", "Productivity"), ("faith", "Faith"), ("womanhood", "Womanhood")])
    body = """
<section class="page-top">
  <div class="wrap">
    <p class="kicker">Writing</p>
    <h1>Ideas I've been turning over for a while.</h1>
    <p class="lead">I write about people, work, love and faith. Some of it is a little unconventional, and most of it started as a question I couldn't stop asking.</p>
  </div>
</section>
<section style="padding-bottom:clamp(72px,10vw,136px)">
  <div class="wrap">
    <div class="chips" data-filter-group="#essays" role="group" aria-label="Filter by topic">{chips}</div>
    <ul class="essays" id="essays">{items}</ul>
  </div>
</section>
<section class="section white">
  <div class="wrap">
    <div class="head"><p class="kicker">Shorter thoughts</p><h2>Sometimes an idea is only a sentence long.</h2></div>
    <div class="tweets">{tw}</div>
    <p style="margin-top:28px"><a class="link" href="https://x.com/favour_ogazi" target="_blank" rel="noopener">More on X</a></p>
  </div>
</section>
<section class="section">
  <div class="wrap two">
    <div class="prose">
      <p class="kicker">The newsletter</p>
      <h2>New essays, straight to your inbox.</h2>
      <p>Whenever a new essay is ready, I send it out. Nothing in between.</p>
      <div class="btns"><a class="btn" href="{nl}" target="_blank" rel="noopener">Subscribe on Substack</a><a class="btn ghost" href="https://medium.com/@thefavourogazi" target="_blank" rel="noopener">Read on Medium</a></div>
    </div>
    <div class="prose">
      <p class="kicker">Coming soon</p>
      <h2>My first <em>anthology.</em></h2>
      <p>A collection of the ideas I keep coming back to. Join the list and you'll hear first when it's out.</p>
      <div class="btns"><a class="btn ghost" href="{wl}" target="_blank" rel="noopener">Join the list</a></div>
    </div>
  </div>
</section>
{contact}""".format(chips=chips, items=essay_items(ESSAYS), tw=tw, nl=NEWSLETTER, wl=WAITLIST_URL, contact=contact_block())
    page("writing.html", "Writing", "Essays and short thoughts by Favour Ogazi on people, work, love and faith.", body, "Writing")

def notfound():
    body = """
<section class="page-top" style="min-height:55vh"><div class="wrap"><p class="kicker">404</p><h1>This page doesn't exist.</h1><div class="btns"><a class="btn" href="index.html">Back home</a></div></div></section>"""
    page("404.html", "Page not found", "Page not found.", body, "")

def favicon():
    (OUT / "assets" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="8" fill="#161514"/>'
        '<text x="20" y="27" text-anchor="middle" font-family="Montserrat, Arial, sans-serif" font-size="20" fill="#FAF8F4">F</text></svg>', encoding="utf-8")

PAGES = {"index.html", "writing.html", "404.html"}

if __name__ == "__main__":
    (OUT / "assets" / "img").mkdir(parents=True, exist_ok=True)
    for f in ("site.css", "site.js"):
        shutil.copy(SRC / "assets" / f, OUT / "assets" / f)
    favicon()
    home(); writing(); notfound()
    print("Built", sorted(PAGES))
