#!/usr/bin/env python3
"""Builds Favour Ogazi's static site into ../public.
Edit the CONTENT section below, then run:  python3 build.py
Works with Python 3.8+ (including the Python that ships with macOS).
"""
import html, pathlib, shutil

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent / "public"

# ======================================================================= CONTENT
EMAIL = "thefavourogazi@gmail.com"
# Placeholder until the dedicated newsletter / waiting list is set up
WAITLIST_URL = "https://favoursnewsletter.substack.com/subscribe"
LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/favour-ogazi",
    "Substack": "https://favoursnewsletter.substack.com",
    "Medium": "https://medium.com/@thefavourogazi",
    "Instagram": "https://www.instagram.com/favourogazii",
    "X": "https://x.com/favour_ogazi",
}

# ---- Portfolio case studies (Work page). tags: "ops" or "projects"
CASES = [
    dict(slug="mighty-treasury", tags="ops", kind="Operations",
         title="Building treasury and cross-border payment operations", short="Treasury & cross-border payments",
         org="Mighty", role="Operations Lead", year="Dec 2025 – now",
         summary="Running operations for a B2B fintech in cross-border payments, foreign exchange and treasury, across trading, product and compliance.",
         context="Mighty provides cross-border payments, foreign exchange and treasury infrastructure for businesses. As the business grew, its operations needed to keep pace across trading, product and compliance.",
         problem="Manual trading processes, many moving parts across payment and liquidity corridors, and teams that needed one shared operating rhythm.",
         built=["Moved manual trading processes onto Mighty's in-house treasury platform, working with the product team on adoption, client walkthroughs and onboarding.",
                "Oversee trade desk execution: client transactions, liquidity sourcing, settlement follow-up and reconciliation.",
                "Coordinate due diligence and onboarding with compliance and legal, taking clients from documentation to live transactions.",
                "Drive quarterly priorities, weekly reporting and scorecards, with operating rhythms and accountability built on EOS."],
         metrics=[("—", "Trading volume growth"), ("—", "Active clients"), ("—", "Faster settlement")],
         metrics_note="Figures to confirm with Favour. Percentages only.",
         lesson="Operations in fintech is trust made visible. Every settled transaction is a promise kept.",
         quote=None, video=None),
    dict(slug="dni", tags="ops", kind="Operations",
         title="Building DNI Pay's operations from the ground up", short="DNI Pay",
         org="DNI / DNI Pay", role="Head of Business Management & Operations", year="2023 – 2025",
         summary="From a new security startup to a live payments platform: team structure, strategy, launch and the systems that run it.",
         context="DNI began in August 2023 as a new tech startup focused on estate and building security. By the end of 2024 it had pivoted and relaunched as DNI Pay, a digital payments platform built to make transactions faster, safer and more accessible across Africa.",
         problem="A young company needed an operational and strategic backbone: structure, hiring, a go-to-market plan, and systems ready for a live payments product.",
         built=["Redefined the team structure, set organisational OKRs and built the first hiring processes for design, development and sales.",
                "Wrote a 12-month market entry plan, overhauled every digital platform and led the company's first major public launch event.",
                "Updated pitch decks and company profiles for funding conversations, introduced HR and finance policies, negotiated vendor contracts and managed budgets.",
                "When DNI Pay went live in August 2025, built customer experience, KYC verification, HR and finance tracking systems, plus five new partnership agreements."],
         metrics=[("95%+", "KYC verified within 24 hours"), ("90%", "Issues resolved within 24 hours"), ("<10 min", "Average response time")],
         metrics_note="Also: 2,000+ active users within 21 days of launch, 5 new partnerships and 2 new markets scoped.",
         lesson="Building a business from scratch, then running it after go-live, is a different discipline from advising one. Strategy only counts when it ships.",
         quote=("Thank you for putting in extra effort to ensure everything goes well for DNI. Thank you for making our lives easier. I do not take anything you do for granted; I mean it.", "Olayinka Olaoye", "Co-founder & CEO, DNI Pay"),
         video=None),
    dict(slug="gamp", tags="projects", kind="Projects",
         title="Marketing communications and project delivery at gamp", short="gamp",
         org="gamp technology", role="Marketing Communications Specialist", year="Jan – Jul 2024",
         summary="Leading a four-person marketing team and cross-functional projects, with campaigns built on data and community.",
         context="gamp needed marketing that grew brand awareness and customer acquisition, and projects that shipped on time across marketing, sales and communications.",
         problem="Many teams, many deadlines, and a community that needed content it actually cared about.",
         built=["Led a team of four marketing professionals to plan and execute campaigns.",
                "Analysed marketing data to spot trends and shape what came next.",
                "Worked with marketing, sales and communications to create content that resonated with the community.",
                "Ran project schedules and weekly stakeholder meetings to keep cross-functional projects on track."],
         metrics=[("4", "Marketers led"), ("Weekly", "Stakeholder reviews"), ("—", "Engagement growth")],
         metrics_note="Engagement figures to confirm with Favour.",
         lesson="Good projects are mostly good communication: the right people knowing the right things at the right time.",
         quote=("Favour, I wanted to say you were a great addition to the team. Good luck in all your future endeavors, and let me know whenever you need me or the team.", "Boluwatife Omotayo", "Co-founder & CEO, gamp technology"),
         video=None),
    dict(slug="lagos-liga-2024", tags="projects", kind="Projects",
         title="Turning Lagos Liga into a content business", short="Lagos Liga",
         org="Lagos Liga · via FONO", role="Social media & content strategy", year="2024 – 2025",
         summary="Running five platforms for one of Africa's largest recreational football leagues, and growing it into a brand people talk about between matches.",
         context="Lagos Liga is one of Africa's largest private recreational football leagues, bringing together non-professional footballers, ex-players and fans. The brand had real energy, but it hadn't turned that into digital presence.",
         problem="Great matches, quiet channels. The league needed to stay relevant between game days and give its community a reason to share.",
         built=["Took over Instagram, Facebook, TikTok, YouTube and X at the same time, plus live coverage of physical and virtual events.",
                "Identified what made Lagos Liga unique among football leagues and made it impossible to ignore.",
                "Spotlighted everyone: club owners, coaches, players, partners and vendors, so each stakeholder wanted to share.",
                "Repositioned the league as a content business that stays relevant between matches."],
         metrics=[("+1,868%", "Impressions in one month"), ("+2,098%", "New followers"), ("+75%", "Engagement rate, to 5.1%")],
         metrics_note="Also trended on X organically, with no paid push.",
         lesson="When people feel seen, they amplify for free. The fastest growth came from making every stakeholder feel important.",
         quote=("I knew you were good at your stuff, but I saw how that competence got matched with personality, character and street depth. I don't think I ever want to do any venture without going with you.", "JJ Omojuwa", "Convener, Lagos Liga"),
         video=None),
    dict(slug="techunwind-fest", tags="projects", kind="Projects",
         title="Marketing and partnerships for TechUnwind Fest", short="TechUnwind Fest",
         org="TechUnwind Fest · via FONO", role="Marketing & partnerships lead", year="2023 – 2024",
         summary="Three editions of a lifestyle-meets-tech festival, filled through hybrid marketing and partnerships built as real activations.",
         context="TechUnwind Fest gives Nigeria's tech community, from founders and creatives to investors and professionals, a relaxed space to connect and learn. FONO led marketing and partnership strategy across three editions.",
         problem="Get the right people in the room, and turn attendance into real interest for the brands behind the event.",
         built=["Designed a hybrid strategy: targeted digital campaigns plus volunteers reaching tech communities on the ground.",
                "Secured and managed 18+ brand partnerships, each structured as a mutual activation rather than a logo placement.",
                "Built content around three principles: educate, entertain, sell. Spaces, lives, radio, interviews and a talent hunt.",
                "Chose influencers for proven conversion, not follower counts, and secured press features."],
         metrics=[("40%", "Attendee-to-user conversion"), ("3,000+", "Attendees across 3 editions"), ("18+", "Brand partnerships")],
         metrics_note="Audience: 45% mid-level professionals, 25% senior experts.",
         lesson="Event marketing works when it serves a business goal, from the first invite to the last follow-up.",
         quote=None, video="h-46PNFo1wQ"),
    dict(slug="national-msme-conference-2024", tags="projects", kind="Projects",
         title="Strategic communications for the National MSME Conference", short="National MSME Conference",
         org="National MSME Conference · via FONO", role="Strategic communications", year="2024",
         summary="Integrated communications for one of Nigeria's biggest small-business gatherings, from first invite to post-event follow-up.",
         context="The National MSME Conference is one of Nigeria's most significant gatherings for small and medium enterprise development. FONO handled strategic communications from pre-event awareness to live coverage and follow-up.",
         problem="Fill a full-capacity event, drive online attendance, and keep every message personal at national scale.",
         built=["Ran an integrated strategy across LinkedIn, X, Instagram, email and influencer coordination with business leaders.",
                "Made email the engine: daily recaps and personalised reminder sequences to drive virtual attendance.",
                "Managed live coverage, press, interviews and media releases with consistent messaging throughout."],
         metrics=[("70%", "Email open rate, 3.2× industry"), ("16%", "Click-through rate"), ("8,000+", "Applications received")],
         metrics_note="800 in-person attendees (full capacity) and 600+ online.",
         lesson="A 70% open rate is a measure of trust. People open what they've learned to expect value from.",
         quote=None, video=None),
]

# ---- FONO client projects (FONO Projects page), from FONO's case study database
FONO_PROJECTS = [
    dict(name="DNI / DNI Pay", year="2023 – 2025", sector="Fintech", service="Business management & operations",
         context="A new security startup that pivoted into DNI Pay, a digital payments platform for Africa. FONO was its operational and strategic backbone from day one.",
         did="Team structure, OKRs and hiring; a 12-month market entry plan; launch event; pitch decks, HR and finance policies; and, at go-live, customer experience, KYC, finance tracking and five new partnerships.",
         results="2,000+ active users within 21 days of launch · 95%+ KYC verified within 24 hours · 90% of issues resolved within 24 hours · FONO's longest engagement, 2+ years.",
         insight="Building a business from scratch and running it after launch is the clearest proof of strategy-led execution."),
    dict(name="Lagos Liga", year="2024 – 2025", sector="Sports & entertainment", service="Social media marketing",
         context="One of Africa's largest private recreational football leagues. Real energy on the pitch, but little of it online.",
         did="Took over five platforms at once with live event coverage, spotlighted every stakeholder in the league, and repositioned it as a content business that stays relevant between matches.",
         results="Within one month: +1,868% impressions · +7,929% profile visits · +2,098% new followers · engagement up 75% to 5.1% · trending on X organically.",
         insight="When people feel important, they amplify for free."),
    dict(name="TechUnwind Fest", year="2023 – 2024", sector="Tech events & community", service="Marketing & partnerships",
         context="A lifestyle-meets-tech festival for Nigeria's tech community. FONO led marketing and partnerships across three editions.",
         did="Hybrid digital and on-the-ground campaigns, 18+ brand partnerships built as mutual activations, an educate–entertain–sell content framework, press and influencer collaborations.",
         results="3,000+ attendees across 3 editions · 40% attendee-to-user conversion · 650,000+ impressions · 75,000+ social users engaged.",
         insight="That alignment between event marketing and business goals takes strategy from the first invite to the last follow-up."),
    dict(name="National MSME Conference 2024", year="2024", sector="Government / SME development", service="Strategic communications",
         context="One of Nigeria's most important gatherings for small business development.",
         did="Integrated social, email and influencer communications; daily recaps and personalised reminders; live coverage, press and media management.",
         results="8,000+ applications · 800 in-person attendees (full capacity) · 600+ online · 70% email open rate, 3.2× the industry average · 16% click-through.",
         insight="A 70% open rate is proof of trust: the audience wanted to hear from us."),
    dict(name="Kaduna State Government", year="2024", sector="Government / public sector", service="Influencer marketing & campaign management",
         context="The state needed to share progress on healthcare and education infrastructure without it feeling like a political advert.",
         did="Ran the influencer campaign end to end: a strict brief (no hashtags, no campaign language), six credible voices across X and Instagram, and a full analytics report.",
         results="65,000+ total reach · all posts live within 48 hours of briefing · 100% tone compliance.",
         insight="The most effective government communication doesn't look like government communication."),
    dict(name="Petroleum Technology Development Fund (PTDF)", year="2024", sector="Federal government / STEM education", service="Business writing & production",
         context="PTDF needed a STEM video that made complex science simple and inspiring for young Nigerians, without losing accuracy.",
         did="Led the proposal and won the project, then managed scripting, crew, shoot-day supervision and stakeholder coordination through to delivery of the film.",
         results="Delivered “Empowering the Future: PTDF STEM in Action” on a tight timeline, with positive feedback from all stakeholders.",
         insight="Federal projects demand precision: many stakeholders, institutional sensitivities and zero tolerance for misalignment."),
    dict(name="TOS Group: Reserved Seats Bill for Women", year="2025", sector="Civic advocacy", service="PR & campaign management",
         context="A campaign to spark public conversation about guaranteeing women's representation in Nigeria's legislature.",
         did="A 10-day campaign across four platforms with daily content, real-time engagement, 10+ creators, new Facebook and TikTok pages built from scratch, and content in English, Yoruba and Igbo.",
         results="145,000+ views in 10 days · 12,200 TikTok views on a brand-new page · 10+ creator collaborations · 3 languages.",
         insight="Treat every day of a campaign as its own mini-launch."),
    dict(name="IMAGIO", year="2025", sector="Home furnishings & lifestyle", service="Marketing",
         context="An Abuja home furnishings and lifestyle brand. FONO ran marketing across Instagram and TikTok for two quarters.",
         did="Social media management, influencer campaigns for a discount week and a product launch, weekly content, quarterly reporting and an email/CRM strategy.",
         results="Q2: 608,000+ Instagram views and 244,000+ combined reach · Q3 documented honestly, with a clear diagnosis of what changed.",
         insight="Honest reporting that names causes, not just outcomes, is what lets a strategy improve."),
    dict(name="Study Abroad Manuel (SAM)", year="2024", sector="Education / study abroad", service="Marketing",
         context="A Nigerian consultancy helping students apply to universities abroad.",
         did="100+ posts, live events, paid ads, influencers and monthly explainer videos; a lead-generation tuition campaign and a #StudyAbroadChallenge; a new student-network partnership and webinar.",
         results="36,000+ accounts reached in one month · 43,500+ views on the challenge campaign · audiences across Nigeria, Ghana, the UK, Tanzania and the US.",
         insight="Speaking to many countries at once takes content that is local and global at the same time."),
    dict(name="Mide Lawal & Co.", year="2025", sector="Personal brand / coaching", service="Branding & go-to-market",
         context="A business operations and customer experience coach who needed a personal brand and a launch.",
         did="Positioned her as a 'Business Midwife', built content across three platforms, and pivoted mid-sprint to launch her flagship masterclass with a webinar funnel and conversion ads.",
         results="+684% month-on-month impressions on X · 67 webinar attendees · 33 masterclass sign-ups while the campaign was still running.",
         insight="The best strategy is one you can adapt without losing clarity."),
    dict(name="Earna", year="2024", sector="Fintech & insurance", service="Marketing",
         context="A fintech and insurance platform offering health, group, senior and retirement plans.",
         did="Multi-platform social media, explainer videos, a cross-platform campaign, plan relaunches, a retirement plan launch, a webinar and partnership materials.",
         results="The flagship campaign was the top content on every platform · 31.5% of interactions came from paid · strong diaspora reach in the UK.",
         insight="In financial products, trust is the currency: educate first, sell second."),
    dict(name="Grey Cleaning Solutions", year="2025", sector="Cleaning / home services", service="Branding & market launch",
         context="An existing business without a clear identity or digital foundation. The mandate: build the brand and launch it properly.",
         did="Brand audit, a full brand book (identity, voice, messaging), marketing strategy and rebuilt Instagram and TikTok, ending in a full relaunch.",
         results="+2,784% Instagram reach after relaunch · +609% TikTok viewers within a week · audit to relaunch in under 2 months.",
         insight="Give a brand something worth discovering and the algorithm works for you."),
    dict(name="HC Studios", year="2025", sector="Photography / creative services", service="Branding & communication",
         context="An Abuja photographer with a strong body of work and a brand that didn't yet match its emotional depth.",
         did="Defined a voice built on peace, warmth and quiet confidence; a messaging and storytelling strategy; and a content system built around the client journey.",
         results="A cohesive identity, a consistent voice across platforms, and a content system the founder actually uses.",
         insight="The brief was never 'make it look nice'. It was 'make it feel like something'."),
    dict(name="Dee Dorhcas", year="2024 – 2025", sector="Fashion & lifestyle", service="Branding & marketing",
         context="A fashion brand with a following but no visual consistency or clear identity.",
         did="A page audit, a rebuilt visual identity and digital presence, a public relaunch and influencer partnerships.",
         results="First two weeks: 76.5% of top-post views from non-followers · 63% non-follower views overall · 83% of interactions from loyal followers.",
         insight="A brand loved by its followers and discovered by new people is built to grow without paid dependency."),
    dict(name="HyTaste", year="2023", sector="Food & hospitality", service="Marketing",
         context="A healthy fast food restaurant and salad bar in Wuse II, Abuja, preparing a grand opening after expanding.",
         did="A full pre- and post-opening plan: flyers, roadshow and local partnerships; an Instagram campaign, influencers and a hashtag challenge; a tasting event; and email and SMS retention.",
         results="One launch plan with traditional, digital, experiential and retention channels working together from day one.",
         insight="A grand opening is a brand's first impression at scale. It deserves a proper strategy."),
    dict(name="ASIKA", year="2024", sector="Fashion", service="Branding",
         context="A women's clothing brand blending style and quality for the modern wardrobe.",
         did="Brand identity: logo and mock-ups that speak to confidence and self-expression.", results="", insight=""),
    dict(name="The Stylish Room", year="2024", sector="Interior decoration", service="Branding",
         context="A boutique interior decoration company that turns living spaces into personal sanctuaries.",
         did="Brand identity: logo and mock-ups across contemporary, minimalist and bohemian styles.", results="", insight=""),
    dict(name="QiQi", year="2025", sector="Home care", service="Branding",
         context="A premium eco-friendly detergent brand designed to care for multicoloured fabrics.",
         did="Brand identity: logo and packaging mock-ups for the conscious Nigerian household.", results="", insight=""),
]

TESTIMONIALS = [
    ("I knew you were good at your stuff, but I saw how that competence got matched with personality, character and street depth. You couldn't have impressed me more. I don't think I ever want to do any venture without going with you.", "JJ Omojuwa", "Convener, Lagos Liga"),
    ("Working with Favour Ogazi was honestly one of the best decisions I made for my personal brand. She doesn't just know what to do, she gets it done swiftly and with so much precision.", "Itunu Olatunde", "Fashion, beauty and lifestyle creator"),
    ("Favour, I have worked with many people for 2 years, but these few months with you were one of the best times I've had with a staff. You are very intelligent, and I love how you connect all things.", "Nkem Ukwa", "Lead Consultant, Gatewood Consulting"),
    ("It's been an absolute pleasure working with you. Thank you for anticipating my needs even before I knew what I wanted. It's inspiring to see your determination and hunger for excellence.", "Kayode Akinwunmi", "CEO, CSL Pay"),
    ("Thank you for putting in extra effort to ensure everything goes well for DNI. Thank you for making our lives easier. I do not take anything you do for granted; I mean it.", "Olayinka Olaoye", "Co-founder & CEO, DNI Pay"),
    ("Favour, I wanted to say you were a great addition to the team. Good luck in all your future endeavors, and let me know whenever you need me or the team.", "Boluwatife Omotayo", "Co-founder & CEO, gamp technology"),
]

# ---- Writing. cats: psychology, relationships, productivity, faith, womanhood
ESSAYS = [
    ("What Do You Have In Your Hands?", "Jun 2026", "Medium", "productivity psychology", "Productivity", "Build from what you already have, before chasing what you lack.", "https://medium.com/@thefavourogazi/what-do-you-have-in-your-hands-84d61900e5d2"),
    ("Have Hobbies That Do Not Scale.", "Jan 2026", "Medium", "productivity psychology", "Productivity", "A case for private joys that can't be measured, monetised or posted.", "https://medium.com/@thefavourogazi/have-hobbies-that-do-not-scale-c2be5e06cc0a"),
    ("Slow Death.", "Nov 2025", "Medium", "psychology relationships", "Psychology", "How we quietly lose ourselves, and how choosing yourself turns it around.", "https://medium.com/@thefavourogazi/slow-death-34ce5e1d343a"),
    ("You Want More Than I Can Give.", "Oct 2025", "Medium", "relationships", "Relationships", "On the weight of friendship, and giving your fullest self to a few.", "https://medium.com/@thefavourogazi/you-want-more-than-i-can-give-ccfd6936a4b8"),
    ("You Are Running Away Again.", "Jul 2025", "Medium", "psychology", "Psychology", "When retreat feels like rest, and the courage it takes to come back.", "https://medium.com/@thefavourogazi/you-are-running-away-again-18275b6b5e1c"),
    ("They Don't Tell You How It Feels To Be A Christian Girl In Nigeria.", "May 2025", "Substack", "faith womanhood", "Faith", "An honest look at faith, setbacks and grace as a young woman.", "https://favoursnewsletter.substack.com/p/they-dont-tell-you-how-it-feels-to"),
    ("Bad Girls Of The Bible.", "Apr 2025", "Substack", "faith womanhood", "Faith", "Ten flawed women of scripture, and what their stories say about grace.", "https://favoursnewsletter.substack.com/p/bad-girls-of-the-bible"),
    ("They Say Your Twenties Are The Most Important Years Of Your Life.", "Mar 2025", "Medium", "psychology productivity", "Psychology", "All the contradictory advice about your twenties, and how tiring it is.", "https://medium.com/@thefavourogazi/my-dear-i-am-trying-109839ba8daf"),
    ("Short Skirt.", "Jan 2025", "Medium", "womanhood psychology", "Womanhood", "A party-game nickname, and how the labels we choose shape how we're seen.", "https://medium.com/@thefavourogazi/short-skirt-3a386754d9fb"),
]

# ---- Short-form ideas from X: screenshots in public/assets/img/x-1.png ... (from her most-liked posts)
TWEETS = [
    ("x-1.png", "https://x.com/Favour_Ogazi/status/2089991110009516113", "I think one of my favourite things about life is still meeting someone and immediately knowing: oh, you are going to matter."),
    ("x-2.png", "https://x.com/Favour_Ogazi/status/2096610437399773338", "Money buys a lot of extremely underrated things. Convenience. Time. Options. Privacy. Distance from nonsense."),
    ("x-3.png", "https://x.com/Favour_Ogazi/status/2092571639879708870", "Some opportunities arrive because you are talented. Others arrive because someone remembered you were reliable."),
    ("x-4.png", "https://x.com/Favour_Ogazi/status/2103749188030730630", "Good friendships make ordinary life feel important. A random Wednesday, one phone call, a stupid joke, dinner somewhere. That is a life too."),
    ("x-5.png", "https://x.com/Favour_Ogazi/status/2100671115118997524", "At some point, you have to let yourself be witnessed - in the work, in the mistakes, in the becoming."),
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
    ("Growth strategy", "Clear priorities, go-to-market plans and campaigns that move you from idea to execution."),
    ("Leadership", "Helping leaders build accountable teams and lead with clarity."),
]

PRINCIPLES = [
    ("Documentation", "If it isn't written down, it didn't happen. I capture what was done, why, and what came of it, so work outlives the moment."),
    ("Communication", "Strategy only becomes reality when the people carrying it understand it. Clear, early and often."),
    ("AI-forward thinking", "Using automation and AI to simplify operations and give people more time for meaningful work."),
]

EXPERIENCE = [
    ("Dec 2025 – now", "Operations Lead", "Mighty"),
    ("2023 – now", "Founder", "FONO Consulting"),
    ("2023 – 2025", "Head of Business Management & Operations", "DNI / DNI Pay"),
    ("2024", "Marketing Communications Specialist", "gamp"),
    ("2022 – 2023", "Co-founder", "Krieit Kulture"),
    ("2022 – 2023", "Business Analyst", "Gatewood Consulting"),
    ("2021", "Operations Manager", "EastPro Logistics"),
]

NOW = [("Building", "Treasury and cross-border payment operations."), ("Growing", "FONO's advisory work."),
       ("Writing", "My first anthology."), ("Learning", "Operations, AI and automation.")]

# ======================================================================= TEMPLATE
e = html.escape
NAV = [("Work", "work.html"), ("FONO", "fono.html"), ("Writing", "writing.html"), ("Speaking", "speaking.html"), ("About", "about.html")]
AC = ' aria-current="page"'
NJ = ' class="no-js-hide"'
LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true" fill="currentColor">'
        '<rect x="3" y="8" width="4.2" height="24"/><rect x="3" y="8" width="14" height="4.2"/><rect x="3" y="18.2" width="10.5" height="3.8"/>'
        '<circle cx="28.5" cy="20" r="8.6" fill="none" stroke="currentColor" stroke-width="4"/></svg>')

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
<meta name="theme-color" content="#0A0A0A">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Instrument+Serif:ital@0;1&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
""".format(t=e(t), d=e(desc))

def nav(active):
    items = "".join('<li><a href="{h}"{c}>{l}</a></li>'.format(h=h, l=l, c=AC if l == active else "") for l, h in NAV)
    home_cls = " logo-home" if active == "Home" else ""
    return """<div class="progress" aria-hidden="true"></div>
<header class="nav">
  <div class="wrap">
    <a class="logo{hc}" href="index.html" aria-label="Favour Ogazi, home">{logo}<span class="name">Favour Ogazi</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
    <ul class="nav-links" id="nav-links">{items}<li><a class="nav-cta" href="contact.html"{cc}>Work with me</a></li></ul>
  </div>
</header>
<main id="top">
""".format(hc=home_cls, logo=LOGO, items=items, cc=AC if active == "Contact" else "")

def footer():
    soc = "".join('<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>'.format(n=n, u=u) for n, u in LINKS.items())
    pages = "".join('<li><a href="{h}">{l}</a></li>'.format(h=h, l=l) for l, h in NAV)
    return """</main>
<footer class="footer dark">
  <div class="wrap">
    <div class="footer-top">
      <a href="contact.html" class="footer-big">Let's build<br><em>something.</em></a>
      <div class="footer-cols">
        <div><p class="label muted" style="margin-bottom:14px">Pages</p><ul>{pages}<li><a href="fono-projects.html">FONO projects</a></li><li><a href="contact.html">Work with me</a></li></ul></div>
        <div><p class="label muted" style="margin-bottom:14px">Elsewhere</p><ul>{soc}</ul></div>
        <div><p class="label muted" style="margin-bottom:14px">Stay close</p><ul><li><a href="{wl}" target="_blank" rel="noopener">Join the newsletter</a></li><li><a href="mailto:{em}">{em}</a></li></ul></div>
      </div>
    </div>
    <div class="footer-bottom"><span class="logo" style="color:var(--paper)">{logo}</span><span>© <span id="yr">2026</span> Favour Ogazi</span></div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
""".format(pages=pages, soc=soc, wl=WAITLIST_URL, em=EMAIL, logo=LOGO)

def photo(src, label, cls="", show_label=True):
    lab = e(label) if show_label else ""
    return '<figure class="photo {c}" data-label="{lab}"><img src="{s}" alt="{a}" loading="lazy"></figure>'.format(c=cls, lab=lab, s=src, a=e(label))

def page(name, title, desc, body, active):
    (OUT / name).write_text(head(title, desc) + nav(active) + body + footer(), encoding="utf-8")

def quote_cards(items):
    return "".join('<figure class="quote-card rv"><blockquote><p>“{q}”</p></blockquote><figcaption><b>{n}</b><cite>{r}</cite></figcaption></figure>'.format(q=e(q), n=e(n), r=e(r)) for q, n, r in items)

# ======================================================================= PAGES
def home():
    pr = "".join('<div{c}><h3>{t}</h3><p>{d}</p></div>'.format(c=NJ if i else "", t=e(t), d=e(d)) for i, (t, d) in enumerate(PRINCIPLES))
    body = """
<section class="hero dark" aria-label="Introduction">
  <div class="wrap">
    <div>
      <h1 class="rv">Favour<span>Ogazi</span></h1>
      <p class="tagline rv">Operations Leader · Founder · Writer</p>
    </div>
    <div class="hero-side">
      {portrait}
      <p class="lead rv">I bring clarity to complex problems, build systems that work, and turn strategy into measurable results.</p>
      <span class="scroll-cue">Scroll</span>
    </div>
  </div>
</section>

<section class="scrolly light" style="height:220vh" aria-label="What I do">
  <div class="stage"><div class="wrap">
    <p class="reveal-text" data-words>I take ideas, businesses, teams and messy situations, and make them <em>work&nbsp;better.</em></p>
  </div></div>
</section>

<section class="scrolly dark sides-wrap" style="height:440vh" aria-label="One operator, several sides">
  <div class="stage"><div class="wrap">
    <div class="sides">
      <ul class="side-list"><li>Operator</li><li>Advisor</li><li>Writer</li><li>Speaker</li></ul>
      <div class="side-panels">
        <div><h3 class="h-md">Operator</h3><p>I lead operations for a cross-border payments and treasury business: trade desk execution, client onboarding, and the operating rhythm that keeps teams accountable.</p><a class="link-arrow" href="work.html">See the work</a></div>
        <div class="no-js-hide"><h3 class="h-md">Advisor</h3><p>Through FONO, I help founders fix pricing, build operating systems, implement AI and plan for growth.</p><a class="link-arrow" href="fono.html">About FONO</a></div>
        <div class="no-js-hide"><h3 class="h-md">Writer</h3><p>I write uncommon ideas on psychology, relationships, productivity and faith: ideas that help people think differently and grow.</p><a class="link-arrow" href="writing.html">Read ideas from Favour</a></div>
        <div class="no-js-hide"><h3 class="h-md">Speaker &amp; teacher</h3><p>Talks, panels and classes on operations, leadership, careers, content and storytelling.</p><a class="link-arrow" href="speaking.html">Speaking &amp; teaching</a></div>
        <div class="no-js-hide"><h3 class="h-md">Not four people. One builder.</h3><p>Running operations, advising businesses, writing to make sense of it, and teaching what I learn.</p><a class="link-arrow" href="about.html">About me</a></div>
      </div>
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
""".format(portrait=photo("assets/img/portrait.jpg", "Favour Ogazi"), pr=pr)
    page("index.html", "Home", "Favour Ogazi is an operations leader, founder and writer who brings clarity to complex problems, builds systems that work, and turns strategy into measurable results.", body, "Home")

def work():
    idx = "".join('<li><a href="#p-{s}">{t}</a></li>'.format(s=c["slug"], t=e(c["short"])) for c in CASES)
    projects = "".join("""
      <article class="project rv" id="p-{slug}" data-c="{tags}">
        <a href="work-{slug}.html">{ph}</a>
        <div class="meta"><span class="label">{kind}</span><span class="label muted">{org}</span><span class="label muted">{year}</span></div>
        <h2><a href="work-{slug}.html">{title}</a></h2>
        <p>{summary}</p>
        <a class="link-arrow" href="work-{slug}.html">Read case study</a>
      </article>""".format(ph=photo(("https://img.youtube.com/vi/%s/maxresdefault.jpg" % c["video"]) if c["video"] else ("assets/img/work-%s.jpg" % c["slug"]), c["short"], "wide"), slug=c["slug"], tags=c["tags"], kind=e(c["kind"]), org=e(c["org"]), year=e(c["year"]), title=e(c["title"]), summary=e(c["summary"])) for c in CASES)
    body = """
<section class="page-hero light" id="selected-work">
  <div class="wrap">
    <p class="label muted rv">Portfolio · Case studies</p>
    <h1 class="rv">Selected <em>work</em></h1>
    <div class="row"><p class="lead rv">Systems built, teams led, launches delivered. Each case study shows the problem, what I did, the people involved, and what changed.</p>
    <div class="chips rv" data-filter-group="#projects" role="group" aria-label="Filter work"><button type="button" aria-pressed="true" data-f="all">All</button><button type="button" aria-pressed="false" data-f="ops">Operations</button><button type="button" aria-pressed="false" data-f="projects">Projects</button></div></div>
  </div>
</section>
<section class="light" style="padding-bottom:clamp(40px,6vw,80px)">
  <div class="wrap split">
    <div class="split-sticky"><p class="label muted">Index</p><ul class="index-list" data-spy>{idx}</ul></div>
    <div id="projects">{projects}</div>
  </div>
</section>
<section class="section dark" id="testimonials" aria-label="Testimonials">
  <div class="wrap" style="display:grid;gap:40px">
    <div style="display:grid;gap:14px"><p class="label muted">Testimonials</p><h2 class="h-xl">In their <em>words.</em></h2></div>
    <div class="testimonials">{tq}</div>
  </div>
</section>
""".format(idx=idx, projects=projects, tq=quote_cards(TESTIMONIALS))
    page("work.html", "Work", "Selected work and case studies by Favour Ogazi across operations and projects.", body, "Work")

def case_pages():
    for i, c in enumerate(CASES):
        nxt = CASES[(i + 1) % len(CASES)]
        built = "".join("<li>%s</li>" % e(b) for b in c["built"])
        metrics = "".join("<div><b>%s</b><span>%s</span></div>" % (e(v), e(l)) for v, l in c["metrics"])
        chapters = [("context", "Context", "<p>%s</p>" % e(c["context"])),
                    ("problem", "The challenge", "<p>%s</p>" % e(c["problem"])),
                    ("built", "What I did", '<ul class="prose" style="padding-left:20px">%s</ul>' % built),
                    ("outcome", "Outcome", '<div class="metrics">%s</div><p class="muted" style="font-size:14px">%s</p>' % (metrics, e(c["metrics_note"]))),
                    ("lessons", "What I learned", "<p>%s</p>" % e(c["lesson"]))]
        if c["quote"]:
            q, n, r = c["quote"]
            chapters.append(("words", "In their words", '<figure class="quote-card light-card"><blockquote><p>“%s”</p></blockquote><figcaption><b>%s</b><cite>%s</cite></figcaption></figure>' % (e(q), e(n), e(r))))
        cnav = "".join('<li><a href="#%s">%s</a></li>' % (k, t) for k, t, _ in chapters)
        csec = "".join('<section class="chapter rv" id="%s"><p class="label muted">%02d</p><h2>%s</h2><div class="prose">%s</div></section>' % (k, n, t, b) for n, (k, t, b) in enumerate(chapters, 1))
        if c["video"]:
            media = '<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0" title="%s video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>' % (c["video"], e(c["short"]))
        else:
            media = photo("assets/img/work-%s.jpg" % c["slug"], c["short"], "wide")
        body = """
<section class="page-hero dark">
  <div class="wrap">
    <a class="label muted rv" href="work.html">← All work</a>
    <p class="label rv" style="color:#CFCFCB">{kind}</p>
    <h1 class="rv" style="font-size:clamp(38px,6.2vw,92px)">{title}</h1>
    <p class="lead rv" style="color:#CFCFCB">{summary}</p>
    <div class="case-meta rv"><div><span class="label muted">Organisation</span><b>{org}</b></div><div><span class="label muted">Role</span><b>{role}</b></div><div><span class="label muted">Type</span><b>{kind}</b></div><div><span class="label muted">When</span><b>{year}</b></div></div>
  </div>
</section>
<section class="dark" style="padding-bottom:clamp(48px,7vw,96px)"><div class="wrap">{media}</div></section>
<section class="section light">
  <div class="wrap chapters">
    <ul class="chapter-nav" data-spy>{cnav}</ul>
    <div>{csec}</div>
  </div>
</section>
<section class="white"><div class="wrap next-case"><p class="label muted">Next case study</p><a href="work-{ns}.html">{nt} →</a></div></section>
""".format(kind=e(c["kind"]), title=e(c["title"]), summary=e(c["summary"]), org=e(c["org"]), role=e(c["role"]), year=e(c["year"]), media=media, cnav=cnav, csec=csec, ns=nxt["slug"], nt=e(nxt["short"]))
        page("work-%s.html" % c["slug"], c["short"], c["summary"], body, "Work")

def fono():
    svc = "".join('<li><div class="row-inner"><span class="k">%02d</span><h3>%s<span class="sub">%s</span></h3><span></span></div></li>' % (n, e(t), e(d)) for n, (t, d) in enumerate(SERVICES, 1))
    steps = [("Understand", "We learn your business, your goals and what's getting in the way."), ("Design", "We build tailored, data-grounded strategies and systems. No templates."), ("Execute", "We work alongside you to put them in place."), ("Evaluate", "We measure what changed and keep improving.")]
    st = "".join('<div class="rv"><span class="label muted">%02d</span><h3>%s</h3><p>%s</p></div>' % (n, e(t), e(d)) for n, (t, d) in enumerate(steps, 1))
    names = " · ".join(e(p["name"]) for p in FONO_PROJECTS[:8])
    body = """
<section class="page-hero dark">
  <div class="wrap">
    <p class="label muted rv">The firm · Since 2023</p>
    <h1 class="rv" style="font-size:clamp(80px,18vw,280px)">FONO</h1>
    <div class="row">
      <div class="prose rv" style="color:#CFCFCB;max-width:52ch">
        <p class="lead" style="color:var(--paper)">FONO Consulting is an advisory firm focused on helping business owners run their businesses with clarity, structure and purpose.</p>
        <p>We help founders fix their pricing, build operating systems that don't depend on them for everything, put AI to work in everyday operations, and plan growth they can execute. Practical help, from strategy to the work itself.</p>
      </div>
      <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn rv" href="contact.html">Work with FONO</a><a class="btn ghost rv" href="fono-projects.html">See FONO projects</a></div>
    </div>
  </div>
</section>
<section class="scrolly light" style="height:220vh" aria-label="Why FONO exists">
  <div class="stage"><div class="wrap">
    <p class="label muted" style="margin-bottom:28px">Why we exist</p>
    <p class="reveal-text" data-words>Too many founders are passionate, dedicated but overwhelmed. We take the overwhelm away and reinforce clarity.</p>
  </div></div>
</section>
<section class="section white">
  <div class="wrap grid-2">
    <div style="display:grid;gap:18px;align-content:start"><p class="label muted">How we think</p><h2 class="h-lg">Your trusted <span class="serif-i">copilots.</span></h2></div>
    <div class="prose rv">
      <p>Every business is different, so we don't do one-size-fits-all. We take the time to understand your vision, your goals and your challenges.</p>
      <p>Then we build tailored strategies, grounded in data, that take you from idea to execution and evaluation.</p>
    </div>
  </div>
</section>
<section class="section light" id="services">
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
    <p class="label muted">Selected FONO projects</p>
    <p class="h-lg" style="max-width:24ch">18 businesses and institutions, from fintech startups to state governments.</p>
    <p class="muted" style="max-width:70ch">{names} and more.</p>
    <a class="btn" href="fono-projects.html" style="justify-self:start">See FONO projects</a>
  </div>
</section>
""".format(svc=svc, st=st, names=names)
    page("fono.html", "FONO", "FONO Consulting helps founders with pricing, operating systems, AI implementation, growth strategy and leadership.", body, "FONO")

def slugify(s):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in s).strip("-").replace("--", "-")

def fono_projects():
    idx = "".join('<li><a href="#%s">%s</a></li>' % (slugify(p["name"]), e(p["name"])) for p in FONO_PROJECTS)
    rows = []
    for p in FONO_PROJECTS:
        dl = '<dt>Context</dt><dd>%s</dd><dt>What we did</dt><dd>%s</dd>' % (e(p["context"]), e(p["did"]))
        if p["results"]:
            dl += '<dt>Results</dt><dd>%s</dd>' % e(p["results"])
        ins = '<p class="serif-i" style="font-size:clamp(20px,2vw,26px);line-height:1.3;margin-top:8px">“%s”</p>' % e(p["insight"]) if p["insight"] else ""
        rows.append("""<article class="fono-project rv" id="{id}">
  <div class="kv"><p class="label muted">{year} · {sector}</p><h2 class="h-md" style="font-size:clamp(24px,2.6vw,36px)">{name}</h2><p class="label" style="margin-top:8px">{service}</p></div>
  <div style="display:grid;gap:14px"><dl>{dl}</dl>{ins}</div>
</article>""".format(id=slugify(p["name"]), year=e(p["year"]), sector=e(p["sector"]), name=e(p["name"]), service=e(p["service"]), dl=dl, ins=ins))
    body = """
<section class="page-hero light">
  <div class="wrap">
    <a class="label muted rv" href="fono.html">← FONO</a>
    <h1 class="rv">FONO <em>projects</em></h1>
    <p class="lead rv">The story behind each engagement: the context, what we did, and what changed.</p>
  </div>
</section>
<section class="light" style="padding-bottom:clamp(80px,11vw,160px)">
  <div class="wrap split">
    <div class="split-sticky"><p class="label muted">Projects</p><ul class="index-list small" data-spy>{idx}</ul></div>
    <div>{rows}</div>
  </div>
</section>
""".format(idx=idx, rows="".join(rows))
    page("fono-projects.html", "FONO projects", "Selected FONO Consulting projects, with context and results.", body, "FONO")

def writing():
    items = "".join('<li data-c="{c}"><a href="{u}" target="_blank" rel="noopener"><span class="k">{tag} · {src}</span><h3>{t}<span class="sub">{s}</span></h3><span class="d">{d}</span></a></li>'.format(c=c, u=u, tag=e(tag), src=e(src), t=e(t), s=e(s), d=e(d)) for t, d, src, c, tag, s, u in ESSAYS)
    tw = "".join('<a class="tweet-shot" href="{u}" target="_blank" rel="noopener"><img src="assets/img/{f}" alt="Post by @Favour_Ogazi: {t}" loading="lazy"></a>'.format(u=u, f=f, t=e(t)) for f, u, t in TWEETS)
    body = """
<section class="page-hero light">
  <div class="wrap">
    <h1 class="rv">Ideas, <em>over time</em></h1>
    <p class="lead rv">I'm a deep thinker and an avid reader. My ideas can be unconventional, but they come from hundreds of books and essays I've read and lived with. I write to help people think differently and grow.</p>
  </div>
</section>
<section class="light" style="padding-bottom:clamp(64px,9vw,120px)">
  <div class="wrap" style="display:grid;gap:32px">
    <div class="chips" data-filter-group="#essays" role="group" aria-label="Filter writing">
      <button type="button" aria-pressed="true" data-f="all">All</button><button type="button" aria-pressed="false" data-f="psychology">Psychology</button><button type="button" aria-pressed="false" data-f="relationships">Relationships</button><button type="button" aria-pressed="false" data-f="productivity">Productivity</button><button type="button" aria-pressed="false" data-f="faith">Faith</button><button type="button" aria-pressed="false" data-f="womanhood">Womanhood</button>
    </div>
    <ul class="rows" id="essays">{items}</ul>
  </div>
</section>
<section class="section white" id="scribbles">
  <div class="wrap" style="display:grid;gap:32px">
    <div class="section-head" style="margin:0"><div style="display:grid;gap:14px"><p class="label muted">Short form</p><h2 class="h-xl">Scribbles of <em>my thoughts.</em></h2></div><p class="muted" style="max-width:34ch">Sometimes I write short ideas to inspire. These are a few that hundreds of thousands of readers loved.</p></div>
    <div class="tweets">{tw}</div>
    <a class="link-arrow" href="{x}" target="_blank" rel="noopener">More on X</a>
  </div>
</section>
<section class="section dark">
  <div class="wrap grid-2" style="align-items:end">
    <div style="display:grid;gap:18px"><p class="label muted">The newsletter</p><h2 class="h-xl">Join 6,000+ <em>readers.</em></h2><p class="lead" style="color:#CFCFCB">New ideas on psychology, relationships, productivity and faith, straight to your inbox.</p></div>
    <div style="display:grid;gap:16px">
      <a class="btn" href="{sub}/subscribe" target="_blank" rel="noopener">Subscribe on Substack</a>
      <div style="display:flex;gap:24px;flex-wrap:wrap"><a class="link-arrow" href="{med}" target="_blank" rel="noopener">Medium</a><a class="link-arrow" href="{sub}" target="_blank" rel="noopener">Substack</a></div>
    </div>
  </div>
</section>
<section class="section white" id="anthology">
  <div class="wrap grid-2" style="align-items:center">
    <div class="big-type"><span class="label" style="color:var(--grey)">FO · Anthology</span><p>Something big is <em>coming.</em></p></div>
    <div style="display:grid;gap:18px"><p class="label muted">Coming soon</p><h2 class="h-xl">My first <em>anthology.</em></h2><a class="btn" href="{wl}" target="_blank" rel="noopener" style="justify-self:start">Be the first to know</a></div>
  </div>
</section>
""".format(items=items, tw=tw, x=LINKS["X"], sub=LINKS["Substack"], med=LINKS["Medium"], wl=WAITLIST_URL)
    page("writing.html", "Writing", "Ideas by Favour Ogazi on psychology, relationships, productivity, faith and womanhood.", body, "Writing")

def speaking():
    tl = "".join('<li><div class="row-inner"><span class="k">%02d</span><h3>%s<span class="sub">%s</span></h3><span></span></div></li>' % (n, e(t), e(d)) for n, (t, d) in enumerate(TOPICS, 1))
    blank = '<figure class="photo square" data-label=""></figure>'
    body = """
<section class="page-hero dark">
  <div class="wrap">
    <h1 class="rv">In the <em>room</em></h1>
    <div class="row"><p class="lead rv" style="color:#CFCFCB">Panels, workshops, interviews, podcasts and classes on operations, leadership, careers and storytelling.</p><a class="btn rv" href="contact.html">Invite me to speak</a></div>
  </div>
</section>
<section class="section white" id="teaching">
  <div class="wrap grid-2" style="align-items:center">
    <div style="display:grid;gap:18px"><p class="label muted">Teaching</p><h2 class="h-lg">Content creation &amp; digital marketing</h2><p class="lead">I teach remote cohorts at a London and Lagos tech academy: a two-month content creation course and a three-month digital marketing course.</p></div>
    {teach}
  </div>
</section>
<section class="section dark" id="on-stage">
  <div class="wrap" style="display:grid;gap:36px">
    <div style="display:grid;gap:14px"><p class="label muted">Moments</p><h2 class="h-xl">On <em>stage.</em></h2></div>
    <div class="grid-2" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px">{b}{b}{b}</div>
  </div>
</section>
<section class="section light" id="topics">
  <div class="wrap">
    <div class="section-head"><div style="display:grid;gap:14px"><p class="label muted">Book me for</p><h2 class="h-xl">Topics</h2></div><a class="link-arrow" href="contact.html">Invite me to speak</a></div>
    <ul class="rows">{tl}</ul>
  </div>
</section>
""".format(teach=photo("assets/img/teaching.jpg", "Favour Ogazi teaching", "wide"), b=blank, tl=tl)
    page("speaking.html", "Speaking", "Favour Ogazi speaks and teaches on business operations, leadership, fintech, AI, careers and storytelling.", body, "Speaking")

def about():
    pr = "".join('<div class="rv"><span class="label muted">%02d</span><h3>%s</h3><p>%s</p></div>' % (n, e(t), e(d)) for n, (t, d) in enumerate(PRINCIPLES, 1))
    exp = "".join('<li><div class="row-inner"><span class="k">%s</span><h3>%s<span class="sub">%s</span></h3><span></span></div></li>' % (e(w), e(r), e(o)) for w, r, o in EXPERIENCE)
    now = "".join('<li><div class="row-inner"><span class="k">%s</span><h3>%s</h3><span></span></div></li>' % (e(k), e(v)) for k, v in NOW)
    body = """
<section class="page-hero light">
  <div class="wrap">
    <p class="label muted rv">About</p>
    <h1 class="rv">One <em>builder</em></h1>
  </div>
</section>
<section class="light" style="padding-bottom:clamp(80px,11vw,160px)">
  <div class="wrap grid-2">
    {ph}
    <div class="prose rv" style="align-content:start">
      <p style="font-size:clamp(20px,2vw,26px);line-height:1.45;font-weight:500;letter-spacing:-.01em">I'm Favour, an operations leader who turns strategy into systems that work. I bring clarity to complex problems and help teams execute with ownership.</p>
      <p>Today I lead operations at Mighty, a B2B fintech in cross-border payments and treasury. Before that, I helped build DNI Pay from a young startup into a live payments platform. Through FONO, my advisory firm, I've worked with 18 businesses and institutions on pricing, operations, growth and AI.</p>
      <p>I'm also a writer and an avid reader. Writing is how I process what I see, think and feel, and thousands of readers follow my ideas on Substack, Medium and X. I believe documentation and clear communication are leadership skills, and I practise both.</p>
      <p>Outside work, I'm a woman of faith who cares deeply about her people. I serve in Children's Church, treasure my friendships, and love good stories, travel, movies and finding humour in ordinary things. I want a full life, with room for ambition, love, curiosity and quiet.</p>
      <div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:8px"><a class="link-arrow" href="{li}" target="_blank" rel="noopener">LinkedIn</a><a class="link-arrow" href="contact.html">Work with me</a></div>
    </div>
  </div>
</section>
<section class="section dark">
  <div class="wrap" style="display:grid;gap:48px">
    <div style="display:grid;gap:14px"><p class="label muted">How I work</p><h2 class="h-xl">Three <em>principles.</em></h2></div>
    <div class="grid-3">{pr}</div>
  </div>
</section>
<section class="section white" id="experience">
  <div class="wrap grid-2">
    <div style="display:grid;gap:18px;align-content:start"><p class="label muted">Path</p><h2 class="h-xl">Experience</h2><p class="muted">MSc Business and Management, Aston University · Operations Management, University of Pennsylvania · McKinsey Forward Program</p></div>
    <ul class="rows path">{exp}</ul>
  </div>
</section>
<section class="section light" id="now">
  <div class="wrap grid-2">
    <div style="display:grid;gap:18px;align-content:start"><p class="label muted">Updated every few months</p><h2 class="h-xl">Now</h2></div>
    <ul class="rows">{now}</ul>
  </div>
</section>
""".format(ph=photo("assets/img/about.jpg", "Favour Ogazi"), li=LINKS["LinkedIn"], pr=pr, exp=exp, now=now)
    page("about.html", "About", "About Favour Ogazi: operations leader, founder of FONO, writer and thinker.", body, "About")

def contact():
    ways = [("Leadership roles", "Operations Lead, Head of Operations, Strategy & Operations or Chief of Staff, especially at international fintech and technology companies."),
            ("Advisory & consulting", "Operating systems, process improvement, growth strategy or AI implementation, through FONO."),
            ("Speaking & teaching", "Panels, workshops, podcasts and classes."),
            ("Writing & bylines", "Essays and commentary on business, leadership and life."),
            ("Collaborations", "Partnerships and projects with peers and organisations."),
            ("Investment", "Later. Happy to start the conversation.")]
    w = "".join('<div class="rv"><h3>%s</h3><p>%s</p></div>' % (e(t), e(d)) for t, d in ways)
    soc = "".join('<a class="link-arrow" href="%s" target="_blank" rel="noopener">%s</a>' % (u, n) for n, u in LINKS.items())
    body = """
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
<section class="section white" id="message">
  <div class="wrap grid-2">
    <div style="display:grid;gap:22px;align-content:start">
      <p class="label muted">Email</p>
      <p class="h-md" style="word-break:break-word">{em}</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="mailto:{em}">Send an email</a><button class="btn ghost" type="button" data-copy="{em}">Copy address</button></div>
      <p class="label muted" style="margin-top:20px">Elsewhere</p>
      <div style="display:flex;gap:22px;flex-wrap:wrap">{soc}</div>
      <p class="label muted" style="margin-top:20px">Newsletter</p>
      <a class="link-arrow" href="{wl}" target="_blank" rel="noopener">Be the first to know</a>
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
""".format(w=w, em=EMAIL, soc=soc, wl=WAITLIST_URL)
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
    # Never delete public/ as a whole: photos in public/assets/img must survive rebuilds.
    (OUT / "assets" / "img").mkdir(parents=True, exist_ok=True)
    for f in ("site.css", "site.js"):
        shutil.copy(SRC / "assets" / f, OUT / "assets" / f)
    (OUT / "assets" / "img" / "README.txt").write_text(
        "Drop photos here with these names and they appear automatically:\n"
        "portrait.jpg (homepage), about.jpg, teaching.jpg,\n"
        "work-<slug>.jpg (cover) for each case study. Slugs: " + ", ".join(c["slug"] for c in CASES) + "\n", encoding="utf-8")
    favicon()
    home(); work(); case_pages(); fono(); fono_projects(); writing(); speaking(); about(); contact(); notfound()
    print("Built", sorted(p.name for p in OUT.glob("*.html")))
