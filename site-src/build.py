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
WAITLIST_URL = "https://favoursnewsletter.substack.com/subscribe"  # placeholder until the waiting list exists
LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/favour-ogazi",
    "Substack": "https://favoursnewsletter.substack.com",
    "Medium": "https://medium.com/@thefavourogazi",
    "Instagram": "https://www.instagram.com/favourogazii",
    "X": "https://x.com/favour_ogazi",
}

# ---- The record: proof at a glance (homepage)
RECORD = [
    ("95%+", "of KYC checks completed within 24 hours, after I built DNI Pay's verification workflow"),
    ("+1,868%", "growth in Lagos Liga's impressions in a single month"),
    ("70%", "email open rate for the National MSME Conference, 3.2× the industry average"),
    ("40%", "of TechUnwind Fest attendees went on to become users"),
    ("18", "businesses and institutions advised through FONO"),
    ("2+ yrs", "building DNI Pay's operations, from first hire to a live payments product"),
    ("6,000+", "readers on my newsletter"),
    ("540K", "views on a single idea I shared on X"),
]

WORKED_WITH = ["Mighty", "DNI Pay", "gamp", "Kaduna State Government", "PTDF", "Lagos Liga", "TechUnwind Fest",
               "National MSME Conference", "TOS Group", "Earna", "IMAGIO", "Gatewood Consulting"]

EXPERIENCE = [
    ("Dec 2025 – now", "Operations Lead", "Mighty", "I run operations for a B2B fintech moving money across borders: the trade desk, treasury, client onboarding with compliance, and the weekly rhythm that keeps it all accountable."),
    ("2023 – now", "Founder", "FONO Consulting", "An advisory firm for founders. We work on how a business is run, priced and grown. 18 engagements so far, from startups to state governments."),
    ("Aug 2023 – now", "Business Development Manager", "DNI Pay", "Built the company's structure, policies, hiring and budgets from the beginning, and the operations behind its live payments product."),
    ("Jan – Jul 2024", "Marketing Communications Specialist", "gamp", "Led a team of four and kept cross-functional projects moving with clear schedules and weekly check-ins."),
    ("2022 – 2023", "Co-founder", "Krieit Kulture", "Wrote the business plan, raised early capital and launched a new product line."),
    ("2022 – 2023", "Business Analyst", "Gatewood Consulting", "Gap analysis, market research and launch plans for clients."),
    ("Jan – Jun 2021", "Operations Manager", "EastPro Logistics", "Daily operations, scheduling, P&L reviews and hiring on site."),
    ("2019 – 2020", "Protocol Assistant", "National Defence College", "Protocol for senior government officials and foreign dignitaries."),
]
EDUCATION = "MSc Business and Management, Aston University · BSc Microbiology, Federal University of Agriculture, Abeokuta · Operations Management, University of Pennsylvania (online) · McKinsey Forward Program"

# ---- Case studies (Work page). tags: "ops" or "projects"
CASES = [
    dict(slug="mighty-treasury", tags="ops", kind="Operations",
         title="Building treasury and cross-border payment operations", short="Mighty",
         org="Mighty", role="Operations Lead", year="Dec 2025 – now",
         summary="Running the operating side of a B2B fintech that moves money across borders, from the trade desk to the weekly scorecard.",
         context="Mighty gives businesses cross-border payments, foreign exchange and treasury infrastructure. When I joined, the company was growing faster than its processes. A lot of trading still happened by hand, and trading, product and compliance each had their own way of working.",
         problem="Money only moves well when everything around it is in step: liquidity in the right place, a trade desk that executes cleanly, onboarding that doesn't stall, and teams that agree on what matters this week.",
         built=["Moved manual trading onto Ramp, Mighty's in-house treasury product, working with the product team on adoption, client walkthroughs and onboarding.",
                "Run trade desk execution day to day: client transactions, liquidity sourcing, settlement follow-up and reconciliation with traders and partners.",
                "Work with compliance and legal to close documentation gaps and get new clients to their first live transaction.",
                "Set quarterly priorities, weekly reporting and scorecards for trading volume, revenue and active clients, using EOS to build the operating rhythm."],
         metrics=[("—", "Trading volume growth"), ("—", "Active clients"), ("—", "Faster settlement")],
         metrics_note="Outcomes coming soon.",
         lesson="In payments, operations is how trust becomes visible. Every settled transaction is a promise kept.",
         quote=None, video=None),
    dict(slug="dni", tags="ops", kind="Operations",
         title="Building DNI Pay's operations from the ground up", short="DNI Pay",
         org="DNI / DNI Pay", role="Business management & operations", year="2023 – 2025",
         summary="From a young security startup to a live payments platform: structure, hiring, strategy, launch, and everything needed to run it afterwards.",
         context="DNI started in August 2023 as a tech startup focused on estate and building security. By the end of 2024 it had pivoted and relaunched as DNI Pay, a payments platform built to make transactions faster, safer and easier across Africa. I was there from the start.",
         problem="A young company with a big idea and very little structure. It needed a team, a plan for the market, policies people could follow, and systems ready for real money on day one.",
         built=["Designed the team structure, set company OKRs and built the first hiring processes for design, development and sales.",
                "Wrote a 12-month market entry plan, rebuilt the digital platforms and led the company's first big public launch.",
                "Updated the pitch decks for funding conversations, introduced HR and finance policies, negotiated vendor contracts and managed budgets.",
                "When DNI Pay went live in August 2025, set up customer support, KYC verification, HR records and finance tracking, and signed five new partnerships."],
         metrics=[("95%+", "KYC checks done within 24 hours"), ("90%", "Transaction issues fixed within 24 hours"), ("<10 min", "Average response to users")],
         metrics_note="Also: 2,000+ active users within 21 days of launch, five new partnerships and two new markets researched.",
         lesson="Advising a business and running one are different jobs. This was the one where the strategy had to work on Monday morning.",
         quote=("Thank you for putting in extra effort to ensure everything goes well for DNI. Thank you for making our lives easier. I do not take anything you do for granted; I mean it.", "Olayinka Olaoye", "Co-founder & CEO, DNI Pay"),
         video=None),
    dict(slug="gamp", tags="projects", kind="Projects",
         title="Marketing and project delivery at gamp", short="gamp",
         org="gamp technology", role="Marketing Communications Specialist", year="Jan – Jul 2024",
         summary="Leading a small marketing team and keeping cross-functional projects on schedule, with campaigns shaped by data and the community.",
         context="gamp needed marketing that grew awareness and brought in customers, and projects that shipped on time across marketing, sales and communications.",
         problem="Several teams, several deadlines, and a community that only responds to content it genuinely cares about.",
         built=["Led a team of four marketers through planning and running campaigns.",
                "Read the marketing data each cycle to see what was working and adjust the next campaign.",
                "Worked with sales and communications on content that felt like it came from the community, not at it.",
                "Kept projects on track with clear schedules and weekly stakeholder check-ins."],
         metrics=[("4", "Marketers led"), ("Weekly", "Stakeholder reviews"), ("—", "Engagement growth")],
         metrics_note="Engagement figures to confirm.",
         lesson="Most project problems are communication problems. The right people knowing the right thing at the right time fixes a lot.",
         quote=("Favour, I wanted to say you were a great addition to the team. Good luck in all your future endeavors, and let me know whenever you need me or the team.", "Boluwatife Omotayo", "Co-founder & CEO, gamp technology"),
         video=None),
    dict(slug="lagos-liga-2024", tags="projects", kind="Projects",
         title="Turning Lagos Liga into a content business", short="Lagos Liga",
         org="Lagos Liga · through FONO", role="Social media & content strategy", year="2024 – 2025",
         summary="Five platforms for one of Africa's largest recreational football leagues, and a brand people kept talking about between matches.",
         context="Lagos Liga is one of Africa's largest private recreational football leagues: non-professional players, ex-players and fans competing for serious prizes. The league had real energy on the pitch, but very little of it reached the internet.",
         problem="Great matches, quiet channels. The league needed a reason for people to care on the days there was no football.",
         built=["Took over Instagram, Facebook, TikTok, YouTube and X at once, plus live coverage of events.",
                "Worked out what made Lagos Liga different from every other league, and kept saying it.",
                "Put everyone in the spotlight: club owners, coaches, players, partners and vendors. When people feel seen, they share.",
                "Treated the league as a content business that stays interesting between game days."],
         metrics=[("+1,868%", "Impressions in one month"), ("+2,098%", "New followers"), ("5.1%", "Engagement rate, up 75%")],
         metrics_note="It also trended on X organically, with no paid push.",
         lesson="The fastest growth didn't come from better content alone. It came from making every person in the league feel important.",
         quote=("I knew you were good at your stuff, but I saw how that competence got matched with personality, character and street depth. I don't think I ever want to do any venture without going with you.", "JJ Omojuwa", "Convener, Lagos Liga"),
         video=None),
    dict(slug="techunwind-fest", tags="projects", kind="Projects",
         title="Filling TechUnwind Fest, three times", short="TechUnwind Fest",
         org="TechUnwind Fest · through FONO", role="Marketing & partnerships", year="2023 – 2024",
         summary="Marketing and partnerships for three editions of a lifestyle-meets-tech festival, with partnerships built as real activations.",
         context="TechUnwind Fest gives Nigeria's tech community, from founders and creatives to investors, a relaxed place to meet and learn. FONO led marketing and partnerships across three editions.",
         problem="Get the right people in the room, and make the event worth it for the brands supporting it.",
         built=["Ran digital campaigns alongside volunteers who reached tech communities in person.",
                "Brought in and managed 18+ brand partnerships, each set up as a shared activation rather than a logo on a banner.",
                "Built the content around three ideas: educate, entertain, sell. Spaces, lives, radio, street interviews and a talent hunt.",
                "Chose influencers for their record of converting people, not their follower counts."],
         metrics=[("40%", "Attendees who became users"), ("3,000+", "Attendees across 3 editions"), ("18+", "Brand partnerships")],
         metrics_note="45% of the audience were mid-level professionals and 25% senior experts.",
         lesson="Event marketing works when it serves a business goal, from the first invite to the last follow-up.",
         quote=None, video="h-46PNFo1wQ"),
    dict(slug="national-msme-conference-2024", tags="projects", kind="Projects",
         title="Communications for the National MSME Conference", short="National MSME Conference",
         org="National MSME Conference · through FONO", role="Strategic communications", year="2024",
         summary="Communications for one of Nigeria's biggest small-business gatherings, from the first invitation to the follow-up after.",
         context="The National MSME Conference is one of Nigeria's most important gatherings for small and medium businesses. FONO handled the communications, from early awareness to live coverage and follow-up.",
         problem="Fill a full-capacity venue, get people to show up online, and keep every message personal at national scale.",
         built=["Ran one plan across LinkedIn, X, Instagram, email and business community voices.",
                "Made email the engine: daily recaps and personal reminders that brought people back.",
                "Handled live coverage, press, interviews and media releases with one consistent voice."],
         metrics=[("70%", "Email open rate, 3.2× industry"), ("16%", "Click-through rate"), ("8,000+", "Applications received")],
         metrics_note="800 people attended in person, at full capacity, and 600+ joined online.",
         lesson="A 70% open rate is really a measure of trust. People open what they've learned to expect something useful from.",
         quote=None, video=None),
]

FONO_PROJECTS = [
    dict(name="DNI / DNI Pay", year="2023 – 2025", sector="Fintech", service="Business management & operations",
         context="A young security startup that pivoted into DNI Pay, a payments platform for Africa. FONO was its operating and strategy partner from the first month.",
         did="Team structure, OKRs and hiring; a 12-month market entry plan; the launch event; pitch decks and policies; and, at go-live, support, KYC, finance tracking and five partnerships.",
         results="2,000+ active users within 21 days of launch · 95%+ of KYC checks done within 24 hours · 90% of issues fixed within 24 hours · our longest engagement, 2+ years.",
         insight="Building a business and then running it after launch is the clearest test of strategy."),
    dict(name="Lagos Liga", year="2024 – 2025", sector="Sports & entertainment", service="Growth & communications",
         context="One of Africa's largest recreational football leagues, with real energy on the pitch and very little online.",
         did="Five platforms and live coverage at once, a spotlight on every stakeholder in the league, and a new position as a content business between matches.",
         results="In one month: +1,868% impressions · +7,929% profile visits · +2,098% followers · engagement up 75% to 5.1% · trending on X without paid promotion.",
         insight="When people feel important, they amplify for free."),
    dict(name="TechUnwind Fest", year="2023 – 2024", sector="Tech events & community", service="Growth & partnerships",
         context="A lifestyle-meets-tech festival for Nigeria's tech community, across three editions.",
         did="Digital and on-the-ground campaigns, 18+ partnerships set up as shared activations, an educate–entertain–sell content plan, press and creator collaborations.",
         results="3,000+ attendees across three editions · 40% of attendees became users · 650,000+ impressions · 75,000+ people engaged on social.",
         insight="Event marketing only works when it's tied to a business goal."),
    dict(name="National MSME Conference 2024", year="2024", sector="Government / SME development", service="Strategic communications",
         context="One of Nigeria's most important gatherings for small business.",
         did="One communications plan across social, email and community voices; daily recaps and personal reminders; live coverage, press and media.",
         results="8,000+ applications · 800 in person at full capacity · 600+ online · 70% email open rate, 3.2× the industry average · 16% click-through.",
         insight="A high open rate is proof of trust. The audience wanted to hear from us."),
    dict(name="Kaduna State Government", year="2024", sector="Government / public sector", service="Public communications",
         context="The state wanted to share real progress in healthcare and education without it sounding like a political advert.",
         did="A strict brief (no hashtags, no campaign language), six credible voices across X and Instagram, and a full report at the end.",
         results="65,000+ people reached · every post live within 48 hours of the brief · 100% of posts on tone.",
         insight="The best government communication doesn't look like government communication."),
    dict(name="Petroleum Technology Development Fund (PTDF)", year="2024", sector="Federal government / STEM education", service="Project leadership & production",
         context="PTDF needed a STEM film that made complex science feel simple and exciting for young Nigerians, without losing accuracy.",
         did="Led the proposal that won the project, then managed the script, crew, shoot and every stakeholder through to delivery.",
         results="Delivered “Empowering the Future: PTDF STEM in Action” on a tight timeline, with warm feedback from every stakeholder.",
         insight="Federal projects need precision: many stakeholders, real sensitivities, no room for misalignment."),
    dict(name="TOS Group: Reserved Seats Bill for Women", year="2025", sector="Civic advocacy", service="Public affairs & campaigns",
         context="A campaign to get people talking about guaranteed seats for women in Nigeria's legislature.",
         did="Ten days across four platforms: daily content, live engagement, 10+ creators, two new pages built from scratch, and content in English, Yoruba and Igbo.",
         results="145,000+ views in 10 days · 12,200 TikTok views on a brand-new page · 10+ creators · 3 languages.",
         insight="Treat every day of a campaign as its own small launch."),
    dict(name="IMAGIO", year="2025", sector="Home & lifestyle", service="Growth advisory",
         context="An Abuja home furnishings brand. FONO looked after its growth on Instagram and TikTok for two quarters.",
         did="Social media, influencer campaigns for a sale and a product launch, weekly content, quarterly reports and an email plan.",
         results="Q2: 608,000+ Instagram views and 244,000+ people reached · Q3 reported honestly, with a clear reason for the dip.",
         insight="Honest reports that name the cause, not just the number, are what let a strategy get better."),
    dict(name="Study Abroad Manuel (SAM)", year="2024", sector="Education", service="Growth advisory",
         context="A Nigerian consultancy helping students apply to universities abroad.",
         did="100+ posts, live events, ads, influencers and monthly explainer videos; a tuition campaign and a #StudyAbroadChallenge; a new student partnership and webinar.",
         results="36,000+ accounts reached in a month · 43,500+ views on the challenge · audiences in Nigeria, Ghana, the UK, Tanzania and the US.",
         insight="Speaking to five countries at once needs content that is local and global at the same time."),
    dict(name="Mide Lawal & Co.", year="2025", sector="Personal brand / coaching", service="Brand & go-to-market",
         context="A business operations coach who needed a clear brand and a launch.",
         did="Positioned her as a 'Business Midwife', built her content on three platforms, then changed course mid-sprint to launch her masterclass with a webinar funnel.",
         results="+684% month-on-month impressions on X · 67 webinar attendees · 33 masterclass sign-ups with the campaign still running.",
         insight="The best plan is one you're willing to change."),
    dict(name="Earna", year="2024", sector="Fintech & insurance", service="Growth advisory",
         context="A fintech and insurance platform for health, group, senior and retirement plans.",
         did="Content across five platforms, explainer videos, a flagship campaign, two plan relaunches, a retirement launch and a webinar.",
         results="The flagship campaign was the top content on every platform · strong diaspora reach in the UK.",
         insight="With money, trust comes first. Educate, then sell."),
    dict(name="Grey Cleaning Solutions", year="2025", sector="Home services", service="Brand & market launch",
         context="A working business without a clear identity. The brief: build the brand and launch it properly.",
         did="A brand audit, a full brand book, a marketing plan and rebuilt Instagram and TikTok, ending in a relaunch.",
         results="+2,784% Instagram reach after relaunch · +609% TikTok viewers within a week · audit to relaunch in under two months.",
         insight="Give people something worth discovering and the algorithm does the rest."),
    dict(name="HC Studios", year="2025", sector="Photography", service="Brand & communication",
         context="An Abuja photographer whose brand didn't yet match the feeling in his work.",
         did="A voice built on peace, warmth and quiet confidence, a storytelling plan, and a content system shaped around the client's journey.",
         results="One clear identity across platforms, and a content system the founder actually uses.",
         insight="The brief was never 'make it look nice'. It was 'make it feel like something'."),
    dict(name="Dee Dorhcas", year="2024 – 2025", sector="Fashion", service="Brand & growth",
         context="A fashion brand with a following, but no consistency or clear identity.",
         did="An audit, a new visual identity, a public relaunch and creator partnerships.",
         results="In two weeks: 76.5% of top-post views from new people · 63% non-follower views overall.",
         insight="A brand loved by its followers and found by strangers is built to grow."),
    dict(name="HyTaste", year="2023", sector="Food & hospitality", service="Launch strategy",
         context="A healthy fast food restaurant in Wuse II, Abuja, opening after an expansion.",
         did="A full opening plan: flyers, a roadshow and local partnerships; an Instagram campaign and influencers; a tasting event; email and SMS to bring people back.",
         results="One plan with traditional, digital, in-person and retention channels working together from day one.",
         insight="A grand opening is a first impression at scale."),
    dict(name="ASIKA", year="2024", sector="Fashion", service="Brand identity",
         context="A women's clothing brand blending style and quality.", did="Logo and brand mock-ups built around confidence and self-expression.", results="", insight=""),
    dict(name="The Stylish Room", year="2024", sector="Interior decoration", service="Brand identity",
         context="A boutique interior decoration company.", did="Logo and brand mock-ups across its range of styles.", results="", insight=""),
    dict(name="QiQi", year="2025", sector="Home care", service="Brand identity",
         context="An eco-friendly detergent brand for colourful fabrics.", did="Logo and packaging mock-ups.", results="", insight=""),
]

TESTIMONIALS = [
    ("I knew you were good at your stuff, but I saw how that competence got matched with personality, character and street depth. You couldn't have impressed me more.", "JJ Omojuwa", "Convener, Lagos Liga"),
    ("Working with Favour was honestly one of the best decisions I made for my personal brand. She doesn't just know what to do, she gets it done swiftly and with so much precision.", "Itunu Olatunde", "Fashion, beauty and lifestyle creator"),
    ("I have worked with many people for two years, but these few months with you were one of the best times I've had with a staff. You are very intelligent, and I love how you connect all things.", "Nkem Ukwa", "Lead Consultant, Gatewood Consulting"),
    ("Thank you for anticipating my needs even before I knew what I wanted. It's inspiring to see your determination and hunger for excellence.", "Kayode Akinwunmi", "CEO, CSL Pay"),
    ("Thank you for putting in extra effort to ensure everything goes well for DNI. Thank you for making our lives easier.", "Olayinka Olaoye", "Co-founder & CEO, DNI Pay"),
    ("You were a great addition to the team. Let me know whenever you need me or the team.", "Boluwatife Omotayo", "Co-founder & CEO, gamp technology"),
]

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

TOPICS = [
    ("Business operations", "How strategy becomes structure, routines and work that actually ships."),
    ("Leadership and ownership", "Building teams that own outcomes, and thinking like a partner in the business."),
    ("Entrepreneurship", "Helping founders build companies that can grow beyond them."),
    ("Fintech operations", "What it really takes to run cross-border payments and treasury day to day."),
    ("AI at work", "Practical, unglamorous ways AI gives teams their time back."),
    ("Career growth", "Changing direction, building career capital, and the courage in between."),
    ("Writing and storytelling", "Finding your voice and saying what you mean, clearly."),
]

FONO_AREAS = [
    ("Strategy & operations", "How the business really runs: structure, processes, decision rights and the weekly rhythm that keeps a team honest."),
    ("Pricing & business models", "What you charge, why, and whether the numbers actually work as you grow."),
    ("Growth & go-to-market", "Who you're for, how they find you, and the campaigns and partnerships that bring them in."),
    ("AI & automation", "Where automation saves real time in your operations, and where it would just add noise."),
    ("Leadership & team design", "Who does what, how people are hired and developed, and how a founder steps back without things falling apart."),
]

FONO_MODES = [
    ("Diagnostic", "A focused look at where the business is stuck. You get an honest written assessment and a clear plan you can act on."),
    ("Advisory retainer", "Ongoing counsel for founders and leadership teams: regular working sessions, a thinking partner for big decisions, and accountability."),
    ("Embedded delivery", "When a plan needs carrying through, we join for a defined project and run it alongside your team until it holds."),
]

PRINCIPLES = [
    ("I write things down.", "Work you can't explain is work that can't be repeated. I document what was done, why, and what happened, so the next person doesn't start from zero."),
    ("I talk early and often.", "Most problems I've fixed were communication problems first. Plans only work when the people carrying them understand them."),
    ("I let tools do the boring parts.", "Automation and AI should give people their time back for the work that needs judgement."),
]

NOW = [("At work", "Building treasury and cross-border payment operations at Mighty."), ("At FONO", "Taking on a small number of new advisory clients."),
       ("Writing", "My first anthology."), ("Learning", "Operations, AI and automation.")]

# ======================================================================= TEMPLATE
e = html.escape
NAV = [("Work", "work.html"), ("FONO", "fono.html"), ("Writing", "writing.html"), ("Speaking", "speaking.html"), ("About", "about.html")]
AC = ' aria-current="page"'

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
<meta name="theme-color" content="#FAF9F6">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
""".format(t=e(t), d=e(desc))

def nav(active):
    items = "".join('<li><a href="{h}"{c}>{l}</a></li>'.format(h=h, l=l, c=AC if l == active else "") for l, h in NAV)
    return """<header class="nav">
  <div class="wrap">
    <a class="wordmark" href="index.html">Favour Ogazi</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
    <ul class="nav-links" id="nav-links">{items}<li><a class="nav-cta" href="contact.html"{cc}>Work with me</a></li></ul>
  </div>
</header>
<main id="top">
""".format(items=items, cc=AC if active == "Contact" else "")

def footer():
    soc = "".join('<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>'.format(n=n, u=u) for n, u in LINKS.items())
    pages = "".join('<li><a href="{h}">{l}</a></li>'.format(h=h, l=l) for l, h in NAV)
    return """</main>
<footer class="footer dark">
  <div class="wrap">
    <div class="footer-top">
      <a href="contact.html" class="footer-big">Let's build <em>something.</em></a>
      <div class="footer-cols">
        <div><p class="label" style="margin-bottom:12px">Pages</p><ul>{pages}<li><a href="fono-projects.html">FONO engagements</a></li><li><a href="contact.html">Work with me</a></li></ul></div>
        <div><p class="label" style="margin-bottom:12px">Elsewhere</p><ul>{soc}</ul></div>
        <div><p class="label" style="margin-bottom:12px">Stay in touch</p><ul><li><a href="{wl}" target="_blank" rel="noopener">The newsletter</a></li><li><a href="mailto:{em}">Email me</a></li></ul></div>
      </div>
    </div>
    <div class="footer-bottom"><span>Favour Ogazi · Abuja, Nigeria</span><span>© <span id="yr">2026</span></span></div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
""".format(pages=pages, soc=soc, wl=WAITLIST_URL, em=EMAIL)

def page(name, title, desc, body, active):
    (OUT / name).write_text(head(title, desc) + nav(active) + body + footer(), encoding="utf-8")

def img(src, alt, cls="", eager=False):
    return '<img class="{c}" src="{s}" alt="{a}"{l}>'.format(c=cls, s=src, a=e(alt), l="" if eager else ' loading="lazy"')

def quotes(items):
    return "".join('<figure class="quote"><blockquote><p>“{q}”</p></blockquote><figcaption><cite><b>{n}</b>{r}</cite></figcaption></figure>'.format(q=e(q), n=e(n), r=e(r)) for q, n, r in items)

def xp_list():
    return "".join('<li><span class="when">{w}</span><div><h3>{r} <span>· {o}</span></h3><p>{d}</p></div></li>'.format(w=e(w), r=e(r), o=e(o), d=e(d)) for w, r, o, d in EXPERIENCE)

def case_img(c):
    if c["video"]:
        return img("https://img.youtube.com/vi/%s/maxresdefault.jpg" % c["video"], c["short"])
    p = OUT / "assets" / "img" / ("work-%s.jpg" % c["slug"])
    if p.exists():
        return img("assets/img/work-%s.jpg" % c["slug"], c["short"])
    return ""

# ======================================================================= PAGES
def home():
    record = "".join("<div><b>%s</b><span>%s</span></div>" % (e(n), e(t)) for n, t in RECORD)
    names = "".join("<span>%s</span>" % e(n) for n in WORKED_WITH)
    roles = [("Operations", "I run the operating side of a fintech that moves money across borders.", "work.html", "See the work"),
             ("Advisory", "Through FONO, I help founders get their business working as well as their idea does.", "fono.html", "About FONO"),
             ("Writing", "Unconventional ideas about people, work, love and faith, read by thousands.", "writing.html", "Read my ideas"),
             ("Speaking", "Talks, panels and classes on operations, leadership, careers and storytelling.", "speaking.html", "Speaking & teaching")]
    cards = "".join('<a href="%s"><p class="label">%02d</p><p class="h3">%s</p><p>%s</p><span class="go">%s →</span></a>' % (h, i, e(t), e(d), e(c)) for i, (t, d, h, c) in enumerate(roles, 1))
    pr = "".join('<div><p class="h3">%s</p><p>%s</p></div>' % (e(t), e(d)) for t, d in PRINCIPLES)
    body = """
<section class="hero">
  <div class="wrap">
    <div class="hero-text">
      <p class="label">Operations Leader · Founder · Writer</p>
      <h1>I'm the person founders call when the idea is working and the business hasn't caught up yet.</h1>
      <p class="lead">I'm Favour. I run operations at a cross-border payments company, advise founders through my firm FONO, and write about the human side of ambition. My work is the unglamorous middle: the structure, routines and people that let a good idea become a business that lasts.</p>
      <div class="btns"><a class="btn" href="work.html">See my work</a><a class="btn ghost" href="contact.html">Work with me</a></div>
    </div>
    {portrait}
  </div>
</section>

<section class="section tight white">
  <div class="wrap">
    <p class="statement">I take ideas, businesses, teams and messy situations, and make them <em>work better.</em></p>
  </div>
</section>

<section class="section dark" id="record">
  <div class="wrap">
    <div class="head"><p class="label">The record</p><h2>Some of what that has looked like.</h2></div>
    <div class="record">{record}</div>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="head"><p class="label">Companies, clients and institutions</p></div>
    <p class="names">{names}</p>
  </div>
</section>

<section class="section white" id="what-i-do">
  <div class="wrap">
    <div class="head"><p class="label">What I do</p><h2>One person, four ways of doing the same job.</h2><p class="lead">Running a business, advising one, writing about the people in it, and teaching what I learn. Pick where you'd like to start.</p></div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="section" id="experience">
  <div class="wrap two">
    <div class="head" style="margin:0"><p class="label">Experience</p><h2>Where I've done the work.</h2><p class="muted" style="font-size:15px">{edu}</p><a class="more" href="about.html">More about me</a></div>
    <ul class="xp">{xp}</ul>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="head-row"><div class="head"><p class="label">In their words</p><h2>What working with me is like.</h2></div><a class="more" href="work.html#testimonials">More testimonials</a></div>
    <div class="quotes">{q}</div>
  </div>
</section>

<section class="section white" id="how-i-work">
  <div class="wrap">
    <div class="head"><p class="label">How I work</p><h2>Three habits I don't compromise on.</h2></div>
    <div class="cards three">{pr}</div>
  </div>
</section>
""".format(portrait=img("assets/img/portrait.jpg", "Favour Ogazi", "portrait", eager=True), record=record, names=names, cards=cards,
           edu=e(EDUCATION), xp=xp_list(), q=quotes(TESTIMONIALS[:3]), pr=pr)
    page("index.html", "Home", "Favour Ogazi runs operations in fintech, advises founders through FONO, and writes about the human side of ambition.", body, "Home")

def work():
    cards = "".join("""<article class="case-card" data-c="{tags}">
      <a class="img{ph}" href="work-{slug}.html">{im}</a>
      <p class="label">{kind}</p>
      <h2 class="h3"><a href="work-{slug}.html">{title}</a></h2>
      <p>{summary}</p>
      <a class="more" href="work-{slug}.html">Read the case study</a>
    </article>""".format(tags=c["tags"], slug=c["slug"], im=case_img(c) or "Photo coming", ph="" if case_img(c) else " placeholder", kind=e(c["kind"]), title=e(c["title"]), summary=e(c["summary"])) for c in CASES)
    body = """
<section class="page-hero">
  <div class="wrap">
    <p class="label">Selected work</p>
    <h1>The work, and what changed because of it.</h1>
    <p class="lead">A few things I've built or helped build, in companies I worked for and through FONO. Each one starts with what was going on, then what I actually did, and what happened next.</p>
    <div class="chips" data-filter-group="#cases" role="group" aria-label="Filter work"><button type="button" aria-pressed="true" data-f="all">All</button><button type="button" aria-pressed="false" data-f="ops">Operations</button><button type="button" aria-pressed="false" data-f="projects">Projects</button></div>
  </div>
</section>
<section style="padding-bottom:clamp(72px,9vw,128px)">
  <div class="wrap"><div class="work-grid" id="cases">{cards}</div></div>
</section>
<section class="section white">
  <div class="wrap two">
    <div class="head" style="margin:0"><p class="label">Work history</p><h2>The full path.</h2><a class="more" href="fono-projects.html">See all 18 FONO engagements</a></div>
    <ul class="xp">{xp}</ul>
  </div>
</section>
<section class="section dark" id="testimonials">
  <div class="wrap">
    <div class="head"><p class="label">Testimonials</p><h2>In their words.</h2></div>
    <div class="quotes">{q}</div>
  </div>
</section>
""".format(cards=cards, xp=xp_list(), q=quotes(TESTIMONIALS))
    page("work.html", "Work", "Case studies and work history: operations at Mighty and DNI Pay, and projects delivered through FONO.", body, "Work")

def case_pages():
    for i, c in enumerate(CASES):
        nxt = CASES[(i + 1) % len(CASES)]
        built = "".join("<li>%s</li>" % e(b) for b in c["built"])
        results = "".join("<div><b>%s</b><span>%s</span></div>" % (e(v), e(l)) for v, l in c["metrics"])
        chapters = [("What was going on", "<p>%s</p>" % e(c["context"])),
                    ("The challenge", "<p>%s</p>" % e(c["problem"])),
                    ("What I did", "<ul>%s</ul>" % built),
                    ("What changed", '<div class="results">%s</div><p class="muted" style="font-size:15px">%s</p>' % (results, e(c["metrics_note"]))),
                    ("What I took from it", '<p class="h3" style="font-style:italic">%s</p>' % e(c["lesson"]))]
        if c["quote"]:
            q, n, r = c["quote"]
            chapters.append(("In their words", '<figure class="quote" style="border:0;padding:0"><blockquote><p>“%s”</p></blockquote><figcaption><cite><b>%s</b>%s</cite></figcaption></figure>' % (e(q), e(n), e(r))))
        ch = "".join('<section class="chapter"><h2>%s</h2><div class="prose">%s</div></section>' % (t, b) for t, b in chapters)
        if c["video"]:
            media = '<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0" title="%s video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>' % (c["video"], e(c["short"]))
        elif (OUT / "assets" / "img" / ("work-%s.jpg" % c["slug"])).exists():
            media = img("assets/img/work-%s.jpg" % c["slug"], c["short"], "cover", eager=True)
        else:
            media = ""
        body = """
<section class="page-hero">
  <div class="wrap">
    <a class="back" href="work.html">← All work</a>
    <p class="label">{kind}</p>
    <h1 style="max-width:20ch">{title}</h1>
    <p class="lead">{summary}</p>
    <div class="facts"><div><span>Organisation</span><b>{org}</b></div><div><span>My role</span><b>{role}</b></div><div><span>Type</span><b>{kind}</b></div><div><span>When</span><b>{year}</b></div></div>
  </div>
</section>
<section><div class="wrap">{media}</div></section>
<section class="section" style="padding-top:clamp(40px,5vw,64px)"><div class="wrap">{ch}</div></section>
<section class="section tight white"><div class="wrap next"><p class="label">Next case study</p><a class="h2" href="work-{ns}.html">{nt} →</a></div></section>
""".format(kind=e(c["kind"]), title=e(c["title"]), summary=e(c["summary"]), org=e(c["org"]), role=e(c["role"]), year=e(c["year"]), media=media, ch=ch, ns=nxt["slug"], nt=e(nxt["short"]))
        page("work-%s.html" % c["slug"], c["short"], c["summary"], body, "Work")

def fono():
    areas = "".join('<li><p class="h3">%s</p><p>%s</p></li>' % (e(t), e(d)) for t, d in FONO_AREAS)
    modes = "".join('<div><p class="h3">%s</p><p>%s</p></div>' % (e(t), e(d)) for t, d in FONO_MODES)
    steps = [("Listen", "We learn the business, the people and what's actually in the way."), ("Diagnose", "We name the real problem, which is rarely the first one mentioned."),
             ("Build", "We design the plan and the systems, and work with your team to put them in place."), ("Review", "We measure what changed, and adjust until it holds.")]
    st = "".join('<li><h3>%s</h3><p>%s</p></li>' % (e(t), e(d)) for t, d in steps)
    names = " · ".join(e(p["name"]) for p in FONO_PROJECTS[:8])
    body = """
<section class="page-hero">
  <div class="wrap two" style="align-items:end">
    <div style="display:grid;gap:22px">
      <p class="label">FONO Consulting · Advisory</p>
      <h1>FONO</h1>
      <p class="lead">FONO Consulting is an advisory firm focused on helping business owners run their businesses with clarity, structure and purpose.</p>
    </div>
    <div style="display:grid;gap:22px">
      <p>We work with founders and leadership teams on the parts of a business that decide whether it can grow: how it runs, how it's priced, how it reaches customers, and how the team works together. We give honest advice, and when it helps, we stay to see it through.</p>
      <div class="btns"><a class="btn" href="contact.html">Start a conversation</a><a class="btn ghost" href="fono-projects.html">See our engagements</a></div>
    </div>
  </div>
</section>
<section class="section tight white">
  <div class="wrap">
    <p class="label" style="margin-bottom:18px">Why we exist</p>
    <p class="statement" style="max-width:26ch">Too many founders are passionate, dedicated but overwhelmed. We take the overwhelm away and reinforce <em>clarity.</em></p>
  </div>
</section>
<section class="section dark" id="engagements">
  <div class="wrap">
    <div class="head"><p class="label">Selected engagements</p><h2>18 businesses and institutions, from fintech startups to state governments.</h2><p>{names}, and more.</p></div>
    <a class="btn" href="fono-projects.html">See all engagements</a>
  </div>
</section>
<section class="section">
  <div class="wrap two">
    <div class="head" style="margin:0"><p class="label">How we think</p><h2>Advice that holds up on Monday morning.</h2></div>
    <div class="prose">
      <p>Every business is different, so we don't arrive with a template. We start by listening: to the founder, the team, the customers and the numbers.</p>
      <p>Then we tell you what we see, plainly, and build a plan grounded in your data and your reality. We care less about a beautiful strategy deck and more about whether things are working better three months later.</p>
    </div>
  </div>
</section>
<section class="section white" id="areas">
  <div class="wrap">
    <div class="head"><p class="label">Where we advise</p><h2>Five areas founders bring to us most.</h2></div>
    <ul class="rows">{areas}</ul>
  </div>
</section>
<section class="section" id="how-we-engage">
  <div class="wrap">
    <div class="head"><p class="label">How we engage</p><h2>Three ways to work with us.</h2></div>
    <div class="engage">{modes}</div>
  </div>
</section>
<section class="section dark">
  <div class="wrap">
    <div class="head"><p class="label">How an engagement runs</p><h2>Listen, diagnose, build, review.</h2></div>
    <ol class="steps">{st}</ol>
  </div>
</section>
<section class="section tight white">
  <div class="wrap"><div class="head-row" style="margin:0;align-items:center"><div class="head" style="margin:0"><h2>Have a business that's outgrowing how it's run?</h2></div><a class="btn" href="contact.html">Talk to FONO</a></div></div>
</section>
""".format(names=names, areas=areas, modes=modes, st=st)
    page("fono.html", "FONO", "FONO Consulting is an advisory firm helping business owners run their businesses with clarity, structure and purpose.", body, "FONO")

def slugify(s):
    out = "".join(ch.lower() if ch.isalnum() else "-" for ch in s)
    while "--" in out: out = out.replace("--", "-")
    return out.strip("-")

def fono_projects():
    jump = "".join('<a href="#%s">%s</a>' % (slugify(p["name"]), e(p["name"])) for p in FONO_PROJECTS)
    rows = []
    for p in FONO_PROJECTS:
        dl = "<dt>The situation</dt><dd>%s</dd><dt>What we did</dt><dd>%s</dd>" % (e(p["context"]), e(p["did"]))
        if p["results"]:
            dl += "<dt>Results</dt><dd>%s</dd>" % e(p["results"])
        ins = "<blockquote>“%s”</blockquote>" % e(p["insight"]) if p["insight"] else ""
        rows.append('<article class="engagement" id="{id}"><div class="meta"><p class="label">{y} · {s}</p><h2 class="h3" style="font-size:clamp(26px,2.4vw,34px)">{n}</h2><p class="muted" style="font-size:15px">{sv}</p></div><div style="display:grid;gap:14px"><dl>{dl}</dl>{ins}</div></article>'.format(
            id=slugify(p["name"]), y=e(p["year"]), s=e(p["sector"]), n=e(p["name"]), sv=e(p["service"]), dl=dl, ins=ins))
    body = """
<section class="page-hero">
  <div class="wrap">
    <a class="back" href="fono.html">← FONO</a>
    <p class="label">FONO Consulting · Selected engagements</p>
    <h1>The engagements, and the story behind each one.</h1>
    <p class="lead">What was going on, what we did, and what changed. Client names are shared with permission.</p>
    <nav class="jump" aria-label="Jump to an engagement">{jump}</nav>
  </div>
</section>
<section style="padding-bottom:clamp(72px,9vw,128px)"><div class="wrap">{rows}</div></section>
""".format(jump=jump, rows="".join(rows))
    page("fono-projects.html", "FONO engagements", "Selected FONO Consulting engagements, with context and results.", body, "FONO")

def writing():
    items = "".join('<li data-c="{c}"><a href="{u}" target="_blank" rel="noopener"><span class="k">{tag} · {src}</span><span><span class="h3">{t}</span><span class="sub">{s}</span></span><span class="d">{d}</span></a></li>'.format(
        c=c, u=u, tag=e(tag), src=e(src), t=e(t), s=e(s), d=e(d)) for t, d, src, c, tag, s, u in ESSAYS)
    tw = "".join('<a class="tweet-shot" href="{u}" target="_blank" rel="noopener"><img src="assets/img/{f}" alt="Post by @Favour_Ogazi: {t}" loading="lazy"></a>'.format(u=u, f=f, t=e(t)) for f, u, t in TWEETS)
    body = """
<section class="page-hero">
  <div class="wrap">
    <p class="label">Writing</p>
    <h1>Ideas, <em>over time.</em></h1>
    <p class="lead">I read a lot, and I think slowly. What comes out can be unconventional: ideas about people, work, love and faith that I've turned over for a long time before writing them down. I write them to help people see a little differently, and to see myself better too.</p>
  </div>
</section>
<section style="padding-bottom:clamp(64px,8vw,112px)">
  <div class="wrap" style="display:grid;gap:28px">
    <div class="chips" data-filter-group="#essays" role="group" aria-label="Filter writing"><button type="button" aria-pressed="true" data-f="all">All</button><button type="button" aria-pressed="false" data-f="psychology">Psychology</button><button type="button" aria-pressed="false" data-f="relationships">Relationships</button><button type="button" aria-pressed="false" data-f="productivity">Productivity</button><button type="button" aria-pressed="false" data-f="faith">Faith</button><button type="button" aria-pressed="false" data-f="womanhood">Womanhood</button></div>
    <ul class="essays" id="essays">{items}</ul>
  </div>
</section>
<section class="section white" id="scribbles">
  <div class="wrap" style="display:grid;gap:28px">
    <div class="head-row" style="margin:0"><div class="head" style="margin:0"><p class="label">Short form</p><h2>Scribbles of <em>my thoughts.</em></h2></div><p class="muted" style="max-width:36ch">Sometimes an idea is only a sentence long. These are a few that hundreds of thousands of people read.</p></div>
    <div class="tweets">{tw}</div>
    <a class="more" href="{x}" target="_blank" rel="noopener">More on X</a>
  </div>
</section>
<section class="section dark">
  <div class="wrap two" style="align-items:end">
    <div class="head" style="margin:0"><p class="label">The newsletter</p><h2>Join 6,000+ readers.</h2><p class="lead">New essays on people, work, love and faith, whenever one is ready. No noise in between.</p></div>
    <div class="btns"><a class="btn" href="{sub}/subscribe" target="_blank" rel="noopener">Subscribe on Substack</a><a class="btn ghost" href="{med}" target="_blank" rel="noopener">Read on Medium</a></div>
  </div>
</section>
<section class="section white" id="anthology">
  <div class="wrap two" style="align-items:center">
    <div class="big-type"><span class="label">Anthology</span><p>Something big is <em>coming.</em></p></div>
    <div class="head" style="margin:0"><p class="label">Coming soon</p><h2>My first anthology.</h2><p class="lead">A collection of the ideas I keep coming back to. Join the list and you'll hear first.</p><div><a class="btn" href="{wl}" target="_blank" rel="noopener">Be the first to know</a></div></div>
  </div>
</section>
""".format(items=items, tw=tw, x=LINKS["X"], sub=LINKS["Substack"], med=LINKS["Medium"], wl=WAITLIST_URL)
    page("writing.html", "Writing", "Essays and short ideas by Favour Ogazi on psychology, relationships, productivity, faith and womanhood.", body, "Writing")

def speaking():
    tl = "".join('<li><span class="n">%02d</span><p class="h3">%s</p><p>%s</p></li>' % (n, e(t), e(d)) for n, (t, d) in enumerate(TOPICS, 1))
    body = """
<section class="page-hero">
  <div class="wrap">
    <p class="label">Speaking & teaching</p>
    <h1>In the <em>room.</em></h1>
    <p class="lead">I love a room full of people trying to figure something out. I speak on panels, run workshops, join podcasts and teach, mostly about operations, leadership, careers and finding your voice.</p>
    <div class="btns"><a class="btn" href="contact.html">Invite me to speak</a></div>
  </div>
</section>
<section class="section white" id="teaching">
  <div class="wrap two" style="align-items:center">
    <div class="head" style="margin:0"><p class="label">Teaching</p><h2>Content creation & digital marketing.</h2><p class="lead">On weekends I teach remote cohorts at a London and Lagos tech academy: a two-month content creation course and a three-month digital marketing course. Watching someone find their voice for the first time never gets old.</p></div>
    {teach}
  </div>
</section>
<section class="section dark" id="on-stage">
  <div class="wrap">
    <div class="head"><p class="label">Moments</p><h2>On stage.</h2></div>
    <div class="work-grid" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px"><div class="photo-blank"></div><div class="photo-blank"></div><div class="photo-blank"></div></div>
  </div>
</section>
<section class="section" id="topics">
  <div class="wrap">
    <div class="head-row"><div class="head" style="margin:0"><p class="label">Book me for</p><h2>Topics I speak on.</h2></div><a class="more" href="contact.html">Invite me to speak</a></div>
    <ul class="topics">{tl}</ul>
  </div>
</section>
""".format(teach=img("assets/img/teaching.jpg", "Favour Ogazi teaching", "cover"), tl=tl)
    page("speaking.html", "Speaking", "Favour Ogazi speaks and teaches on operations, leadership, fintech, AI, careers and storytelling.", body, "Speaking")

def about():
    pr = "".join('<div><p class="h3">%s</p><p>%s</p></div>' % (e(t), e(d)) for t, d in PRINCIPLES)
    now = "".join('<li><p class="h3">%s</p><p>%s</p></li>' % (e(k), e(v)) for k, v in NOW)
    body = """
<section class="page-hero">
  <div class="wrap"><p class="label">About</p><h1>Hello, I'm <em>Favour.</em></h1></div>
</section>
<section style="padding-bottom:clamp(72px,9vw,128px)">
  <div class="wrap two">
    {ph}
    <div class="prose">
      <p class="h3" style="font-size:clamp(24px,2.2vw,30px)">I never planned to work in operations. A mix of chance, curiosity and drive took me there.</p>
      <p>I studied microbiology. I sold beauty products in school, helped run a student union election campaign, started FONO, and went back for a master's in Business and Management. Somewhere along the way I realised the thing I'm best at is the part most people find boring: turning a good idea into a way of working that holds up.</p>
      <p>Most businesses don't stall for lack of ideas. They stall because nobody has built the structure, the routines and the trust that let an idea run without the founder holding it together. That's my part. Today I do it at Mighty, a cross-border payments company, and for the founders FONO works with. Before that, I helped build DNI Pay from a young startup into a live payments platform.</p>
      <p>I'm also a writer and a big reader. Writing is how I process what I see, think and feel, and thousands of people read my ideas on Substack, Medium and X.</p>
      <p>Outside work, I'm a woman of faith and I serve in Children's Church. I treasure my friends, love a good story, travel when I can, watch too many movies, and find the funny side of ordinary days. I want a full life, with room for ambition, love, curiosity and quiet.</p>
      <div class="btns" style="margin-top:6px"><a class="btn" href="contact.html">Work with me</a><a class="btn ghost" href="{li}" target="_blank" rel="noopener">LinkedIn</a></div>
    </div>
  </div>
</section>
<section class="section white" id="experience">
  <div class="wrap two">
    <div class="head" style="margin:0"><p class="label">Experience</p><h2>The path so far.</h2><p class="muted" style="font-size:15px">{edu}</p></div>
    <ul class="xp">{xp}</ul>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="head"><p class="label">How I work</p><h2>Three habits.</h2></div>
    <div class="cards three">{pr}</div>
  </div>
</section>
<section class="section dark" id="now">
  <div class="wrap two">
    <div class="head" style="margin:0"><p class="label">Now</p><h2>What I'm focused on.</h2><p class="muted" style="font-size:15px">Updated every few months.</p></div>
    <ul class="xp">{now}</ul>
  </div>
</section>
""".format(ph=img("assets/img/about.jpg", "Favour Ogazi", "portrait"), li=LINKS["LinkedIn"], edu=e(EDUCATION), xp=xp_list(), pr=pr,
           now=now.replace("<li>", '<li style="grid-template-columns:150px minmax(0,1fr)">'))
    page("about.html", "About", "About Favour Ogazi: operations leader, founder of FONO, writer, and a woman of faith who loves a good story.", body, "About")

def contact():
    ways = [("A leadership role", "Operations Lead, Head of Operations, Strategy & Operations or Chief of Staff, especially at international fintech and technology companies."),
            ("Advice for your business", "Operations, pricing, growth or AI, through FONO."),
            ("A talk or a class", "Panels, workshops, podcasts and teaching."),
            ("Writing", "Essays and commentary on business, leadership and life."),
            ("Working together", "Partnerships and projects with people and organisations I admire."),
            ("Investment", "Not yet, but I'm happy to start the conversation.")]
    w = "".join('<div><p class="h3">%s</p><p>%s</p></div>' % (e(t), e(d)) for t, d in ways)
    soc = "".join('<a class="more" href="%s" target="_blank" rel="noopener">%s</a>' % (u, n) for n, u in LINKS.items())
    body = """
<section class="page-hero">
  <div class="wrap"><p class="label">Work with me</p><h1>If something here sounds like what you need, I'd love to hear about it.</h1></div>
</section>
<section style="padding-bottom:clamp(64px,8vw,112px)">
  <div class="wrap"><div class="cards three">{w}</div></div>
</section>
<section class="section white" id="message">
  <div class="wrap two">
    <div style="display:grid;gap:18px;align-content:start">
      <p class="label">Email</p>
      <p class="h3" style="word-break:break-word">{em}</p>
      <div class="btns"><a class="btn" href="mailto:{em}">Send an email</a><button class="btn ghost" type="button" data-copy="{em}">Copy address</button></div>
      <p class="label" style="margin-top:18px">Elsewhere</p>
      <div style="display:flex;gap:18px;flex-wrap:wrap">{soc}</div>
    </div>
    <form class="form" id="contact-form">
      <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-email">Your email</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="f-org">Organisation (optional)</label><input id="f-org" name="org" autocomplete="organization"></div>
      <div class="field"><label for="f-topic">What's this about?</label><select id="f-topic" name="topic"><option>A leadership role</option><option>Advice through FONO</option><option>A talk or a class</option><option>Writing</option><option>Working together</option><option>Something else</option></select></div>
      <div class="field"><label for="f-msg">Tell me a little</label><textarea id="f-msg" name="message" required></textarea></div>
      <div><button class="btn" type="submit">Send message</button></div>
      <p class="form-note" id="form-note" aria-live="polite"></p>
    </form>
  </div>
</section>
""".format(w=w, em=EMAIL, soc=soc)
    page("contact.html", "Work with me", "Get in touch with Favour Ogazi about leadership roles, advice through FONO, speaking, writing or working together.", body, "Contact")

def notfound():
    body = """
<section class="page-hero" style="min-height:60vh"><div class="wrap"><p class="label">404</p><h1>This page doesn't exist <em>yet.</em></h1><div><a class="btn" href="index.html">Back home</a></div></div></section>"""
    page("404.html", "Page not found", "Page not found.", body, "")

def favicon():
    (OUT / "assets" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="8" fill="#141413"/>'
        '<text x="20" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="24" fill="#FAF9F6">F</text></svg>', encoding="utf-8")

if __name__ == "__main__":
    (OUT / "assets" / "img").mkdir(parents=True, exist_ok=True)
    for f in ("site.css", "site.js"):
        shutil.copy(SRC / "assets" / f, OUT / "assets" / f)
    favicon()
    home(); work(); case_pages(); fono(); fono_projects(); writing(); speaking(); about(); contact(); notfound()
    print("Built", sorted(p.name for p in OUT.glob("*.html")))
