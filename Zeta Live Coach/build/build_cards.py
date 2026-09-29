import json,re
D={int(k):v for k,v in json.load(open("src/dan.json")).items()}
FIX=[(r"\bDean'slist\b","DeansList"),(r"\bDean's List\b","DeansList"),(r"\bKip\b","KIPP"),(r"\bkip\b","KIPP"),(r"Cloud Code","Claude Code"),(r"inhumanity","humanity"),(r"in the States","in the state")]
def clean(t):
    t=re.sub(r"\b[Kk]ind of,?\s*","",t)
    t=re.sub(r"\b[Ss]ort of\s*","",t)
    t=re.sub(r"\bUm[.,]*\s*","",t); t=re.sub(r"\bUh huh\.\s*","",t)
    for a,b in FIX: t=re.sub(a,b,t)
    t=re.sub(r"\s+"," ",t).strip()
    return t
def dan(a,b,start=None,end=None,skip=()):
    out=[];prev=None
    for n in range(a,b+1):
        if n in skip or n not in D: continue
        sp,tx=D[n]
        if not sp.startswith("Christopher"): continue
        if prev is not None and n-prev>1 and any((m in skip) for m in range(prev+1,n)): out.append("…")
        out.append(tx);prev=n
    t=" ".join(out)
    if start: i=t.index(start); t=("… " if i>0 else "")+t[i:]
    if end: i=t.index(end)+len(end); t=t[:i]+(" …" if i<len(t) else "")
    return clean(t)

exec(open("src_other.py").read())
def c(t): return clean(t)
DAN="Dan Rojas call, 09/25"; GIL="Zeta screen with Gillian, 09/11"; DRM="DREAM screen with Donna Choi Ellis, 08/17"; S2="School in the Square onsite, 09/08"
def P(src,asked,text): return {"src":src,"asked":asked,"text":text}
CARDS=[]
def card(**k): CARDS.append(k)

card(id="intro",grp="open",tier="Must",q="Tell me about yourself / walk me through your background",who="Either, first 2 minutes",
hook="DC → Excel 270th to #1 · referral practice, 100 schools · Carver → Lab → KIPP → tools",
why="The open sets the frame for the whole call. With Dan it ran almost 6 minutes; target 2.",
frame="I'll give you the quick arc, and I'll slow down on the principals.",fy=False,
parts=[P(DAN,"Do you want to tell me a little bit about yourself?",c(dan(30,31))+" [[slow]]"),
 P(GIL,"(Your background answer to Gillian. Used here for the consulting part, because the Dan version has the health reason in it.)",c(G_CONSULT)),
 P(DAN,"(continuing the answer to Dan)",dan(36,38,start="And I got to walk")),
 P(DAN,"(continuing)","[[trim]] "+dan(39,40,start="When I was there at Excel",end="which I later grew into Dean'slist.")),
 P(DAN,"(continuing)",dan(41,45)+" [[slow]]"),
 P(DAN,"(continuing)",dan(46,49)),
 P(DAN,"(continuing)",dan(50,51)),
 P(DAN,"(continuing)",dan(52,52,end="the specific solutions that they need")),
 P(DAN,"(continuing)","[[pause]] "+dan(54,55))],
say=["Replace \"We were able to be successful in that\" with the result: three years later the school had doubled, and he was Louisiana Principal of the Year. He runs the network now.","DeansList: zero to 275 schools.","The practice ran 14 years, not \"the better part of a decade.\"","Brooklyn Lab: both schools were reauthorized, and you were interim high school principal for half a year."],
land="And my read is that you all might be that kind of place. So that's why I'm here.",
avoid="The health reason for leaving Excel. \"That's been taking off\" about the tools. Anything past 2 minutes.",
bul=["DC → Excel turnaround, 270th → #1","Consulting: visitors wanted the model; KIPP, AF, Uncommon","100 schools; chaotic → stable → functional → rigorous","Collegiate: assess the principal, last-ditch → say the result","Brooklyn Lab: transition superintendent, renewals, new ownership","KIPP: 28 regions, hand it back","Custom tools for principals","Happiest in a midsize network with outsized ambition"])

card(id="why",grp="open",tier="Must",q="Why Zeta? Why this side of the house?",who="Paola",
hook="Building things other people can run · midsize, outsized ambition · excellence with exploration",
why="The ops seat is closed. This answer has to be a clear yes to the schooling side.",
frame="If there was one thing to sum up what I've been doing my whole career, it's building things that other people can run.",fy=True,
parts=[P(DRM,"Why did you decide to apply for this role?",c(R_WHY1)+" [[pause]] "+c(R_WHY2)),
 P(DAN,"(the end of your answer to \"tell me about yourself\")",dan(54,54,start="the happiest")),
 P(DAN,"(your closing argument at the end of the call)",dan(225,227,end="Let's attack people's ideas without attacking people."))],
say=["If they ask about the ops role: Felipe thought your strongest fit was the schooling side, and after talking with Dan you see the logic. (Your words to Dan: \"I see the logic. And yeah, it makes sense.\")"],
land="Let's debate the heck out of things. Let's attack people's ideas without attacking people.",
avoid="Any sign you'd rather have the ops role.",
bul=["Building things other people can run","Buy-in on merit, not obligation","Happiest in a midsize, growing network","Excellence with exploration","High school experience across operations, culture and academics","Best idea wins"])

card(id="best",grp="open",tier="Likely",q="What do you do best? What are you looking for next?",who="Either",
hook="Find the pain point fast · build with a team · a document is worthless until it's in a classroom",
why="Gillian asked this; her notes went to the COOs and Emily Kim, so this is on record with them.",
frame="I like strategy. I like being part of a team that's willing to work incredibly hard and have fun while doing it.",fy=True,
parts=[P(GIL,"What do you feel like you're really looking to get out of your next role?",c(G_LOVE))],
say=[],land="Help them do it incredibly well.",avoid="Leading with AI.",
bul=["Understand pain points fast, through relationships","A clear bar for excellence","Build with practitioners and support teams together","Student outcomes are the only measure","A document is worthless until it's driving results in a classroom"])

card(id="g2g",grp="prin",tier="Must",q="How do you manage principals? The good principal who needs to get to great?",who="Paola",
hook="Clothes, not skin · support hat 99% · side of the street clean · shoulder to shoulder → Carver",
why="Paola's job. Dan asked exactly this, and the answer had no proof.",
frame="The playbook I've developed over time, by doing it wrong and then eventually doing it better, comes down to four things.",fy=False,
parts=[P(DAN,"What's the common piece of feedback you give the principal who is pretty good but needs to go to great?",dan(60,72))],
say=["End on Carver instead of \"completely let go of any hierarchical sense of mandate authority\": I was brought in to assess whether the principal of their largest high school could do the job. Three years later the school had doubled, and he was Louisiana Principal of the Year. He runs the network now."],
land="Say the Carver result, then stop.",avoid="Ending on the principle. Going past 2 minutes.",
bul=["1. Performance is not identity: clothes, not skin","2. Support vs. evaluation: support hat 99%, nothing is a surprise","3. My side of the street clean, above reproach","4. Shoulder to shoulder; their perspective is valid","Mandate authority is almost worthless","End on Carver"])

card(id="carver",grp="prin",tier="Must",q="A principal who was struggling. What did you do?",who="Paola",
hook="Assess, last-ditch · \"hiding our best person\" · doubled, Louisiana Principal of the Year",
why="Your best proof for a principal-manager seat. With Dan it came out as one sentence.",
frame="The one I'd point to is Carver, in New Orleans.",fy=False,
parts=[P(DAN,"(from your background answer)",dan(43,44))],
phrases={"src":"Your Carver dictation, 09/20","asked":"(dictated for your answer bank)","list":["we're hiding our best person","running the whole thing"]},
say=["The stakes: close to a last look at whether the school stayed open.","You were brought in to assess, not to coach. The coaching came after, over three years.","Three years later the school had doubled in size, and student satisfaction was up 50%.","He was named Louisiana Principal of the Year, and he runs the organization now."],
land="He runs the organization now.",avoid="The 75% suspension drop (that's Collegiate network-wide, never Carver alone). \"We were able to be successful.\"",
bul=["Brought in to assess, last-ditch","\"We're hiding our best person\"","Three years of coaching","Doubled · satisfaction +50%","Louisiana Principal of the Year → now CEO"])

card(id="account",grp="prin",tier="Likely",q="How do you hold principals accountable and still develop them?",who="Paola",
hook="Clarity → investment → training → accountability · curiosity, not accusation",
why="Zeta: \"the requirement of the manager is a lot higher.\" School in the Square asked the same thing.",
frame="The order matters to me: clarity, investment, training, and only then accountability.",fy=False,parts=[],
phrases={"src":S2,"asked":"How do you balance holding leaders accountable for results while also coaching and developing them?","list":["my success would be their success","support hat / evaluation hat","nothing's a surprise","clarity, investment, training, accountability","not just in August","I stopped thinking I knew everything and really listened","I realized there was a clarity issue that was my fault","unfair on a human level","we talked about the calendar going out last week. I didn't get it. What can you tell me about that?","curiosity, not accusation","my side of the street needs to be entirely clean","I can't not answer my email for two weeks and then hold you accountable","the first line of defense","the real rock stars, the teachers and students, can go shine","the easy nice guy way","there's nothing nice and friendly about me thinking one thing behind your back and not saying it to you"]},
none="Only fragments of this answer were kept word for word, so there's no full script. Build it from the phrases below.",
say=["Close on Carver, not on the nice-guy failure."],land="Say the Carver result, then stop.",avoid="Ending on the failure story.",
bul=["My success is their success","Clarity → investment → training → accountability","The calendar example: curiosity, not accusation","My side of the street first","End on Carver"])

card(id="lead",grp="prin",tier="Likely",q="What's your philosophy on leading and managing people?",who="Paola",
hook="Build the relationship by having the hard conversation · support hat 98/2 · my success comes from yours",
why="A likely Paola question; she ran leader development at KIPP New Jersey.",
frame="I've been incredibly lucky to have some really special people take an interest in me, and support me along the way, and so I try and honor them by stealing the best of them.",fy=True,parts=[],
phrases={"src":S2,"asked":"What is your core philosophy around how you lead and manage people?","list":["everyone from the person I taught across the hall from to my dad","we build the relationship by having the hard conversation","because I don't want people wondering where they stand","feeling critiqued for something that's ultimately a clarity issue on my part","my side of the street has to be entirely clean","98% of the time I'm wearing a support hat. 2% of the time I put on my evaluation hat","I say this in a management memo, and as well as my first meeting of the year","my success can only come from your success","there can be multiple right ways to do things","them coming to me is not an admission of weakness or a fault. It's an admission of something they need","I used to hesitate a lot around accountability because I was feeling like perhaps I hadn't done my part"]},
none="Only fragments were kept word for word. Build it from the phrases below.",
say=["Proof: at Collegiate, eight principals delivered the summer PD themselves.","Pick one support-hat number. Dan heard 99%; here it was 98%."],
land="My success can only come from your success.",avoid="Calling your own framework silly.",
bul=["Honor my mentors by stealing the best of them","Build the relationship by having the hard conversation","Nobody wondering where they stand","Support hat / evaluation hat, said out loud and in writing","Coming to me isn't weakness","Proof: eight principals delivering summer PD"])

card(id="hs",grp="hs",tier="Must",q="What should high school be? What would you rethink?",who="Paola",
hook="Not middle school with the dials turned · same spine, dressed different · 50/25/25",
why="Dan's biggest open problem, and he said \"I love that idea.\" Last time you opened with \"I wish I had the answer.\"",
frame="High school can't be like middle school just with a couple of dials turned.",fy=True,
parts=[P(DAN,"Where are high schools getting it right, and where does there need to be a complete structural rethinking?","… "+dan(119,126)),P(DAN,"(continuing)","[[trim]] "+dan(127,135)),P(DAN,"(continuing)","[[slow]] "+dan(136,139))],
say=["Bridge to Dan's worry about the C in ninth grade: at KIPP, across 48 high schools, 46% of ninth graders finished the quarter at a 3.0 or better, up six points, the best quarter KIPP had on that number.","Excel's high school is in the top 3% of public high schools in the country."],
land="Say the 46%, then stop.",avoid="Opening with \"I wish I had the answer.\"",
bul=["Claim first: not middle school with the dials turned","Don't over- or under-correct systems","Same spine of values, dressed entirely different","Seating-chart release (can trim)","50 / 25 / 25 audit","Lives of unlimited opportunity → ninth-grade grades → 46%"])

card(id="culture",grp="hs",tier="Likely",q="Beyond systems: culture and student ownership",who="Paola",
hook="Cool to be smart · ownership that isn't surfacey · \"it's my school\"",
why="Dan's follow-up question. It shows the culture side is academic identity, not pizza parties.",
frame="Two corners made all the difference at Excel.",fy=False,
parts=[P(DAN,"Beyond seating charts, what other specific things would you change about high school?",dan(143,159))],
phrases={"src":S2,"asked":"(the Excel orientation story, from a question about keeping students enrolled)","list":["incentives are great, and challenges are great, and events are great","bribing them or tricking them","manufactured, but genuine","I never want you to tell a student anything that's not entirely true","are you sure?","I hated this place. I thought they were too strict. I thought they were too mean.","Mr. Habetler's not making me say this","there's something about this place that's worth giving it a try"]},
say=["Excel student attrition over those years was 3%.","Jackie, your former sixth grader, has your old job at Excel."],
land="We would, as adults, be saying a whole lot less and helping our students say a whole lot more.",avoid="Running past 2 minutes; this one is long.",
bul=["Academic identity: cool to be smart, fun because it's challenging","Ownership is usually thin and surfacey","Groups that run the school day: honor council, events committee","A third of a 150-student grade in a group","\"It's my school\"","Orientation story (optional)"])

card(id="scale",grp="scale",tier="Must",q="When is a practice ready to scale? Playbooks or autonomy?",who="Kruti",
hook="Clear on who we were · earn it: stable → functional → innovate · Jackie has my old job",
why="Kruti's job. \"Earn it\" means: a new principal runs the proven playbook first; once the school is stable and functional, they've earned the room to change it.",
frame="Fundamentally, we were clear on who we were.",fy=True,
parts=[P(DAN,"Compare Excel to KIPP. What makes scale so hard for so many charters?",dan(92,96,start="Now, in contrast that with Excel",end="lives of unlimited opportunities.")),P(DAN,"(continuing)","[[slow]] "+dan(97,101))],
say=["Right after \"earn that,\" say how you help them get there. On the Dan call, \"earn that\" came right after \"I don't care really if you as a first-year principal have all these thoughts,\" and that line is the one to lose.","The 95%: say it only if you're sure of it."],
land="Jackie now has my old job.",avoid="\"I don't care really if you...\" Grading KIPP or AF. The KIPP half of the comparison.",
bul=["Playbooks for everything; replicated, not cloned","Innovation keeps talent and is the lab","Grow from a proven start, at a pace talent allows","Earn it: stable → functional → then innovate","Run the play; it evolves; you're part of it","Excel HS top 3%; Jackie has my old job"])

card(id="initiative",grp="scale",tier="Must",q="An initiative you led from design through implementation across schools",who="Kruti",
hook="Data was there, nobody could use it · one button, a report per teacher · present but obscured → right in front of them",
why="Your strongest scaling story. DREAM's recruiter called it \"absolutely incredible.\"",
frame="The academic health data transparency work.",fy=True,
parts=[P(DRM,"Can you share one specific initiative or pilot you've led from design through implementation across multiple schools?",c(R_INIT)+" [[pause]] I went all in on "+c(R_INIT2)),P(DRM,"(continuing)",c(R_INIT3)+" [[slow]] "+c(R_INIT4)),P(DRM,"(continuing)",c(R_INIT5))],
say=["The number: 46% of ninth graders at a 3.0 or better, up six points, across 48 high schools.","It replaced a 40-minute manual workflow with one click, and it kept running after you handed it off."],
land="It's been cited as one of the primary drivers that really got the right folks focused on the right conversation and the right actions.",avoid="Forgetting the book mid-story (last time). Leading with the tool instead of the problem.",
bul=["Data existed; nobody could use it","One button: a report per teacher and per student","Designed for one school, then national","Weekly, not end of quarter","Present but obscured → right in front of them","Biggest GPA jump; not all the credit"])

card(id="adopt",grp="scale",tier="Likely",q="Getting schools to adopt something when they don't have to say yes",who="Kruti",
hook="Being the boss isn't how it works · a we, not us-versus-them · 28 said yes, again in year two",
why="Zeta is opening schools fast; Kruti needs someone who gets adoption without forcing it.",
frame="Being someone's boss, I guess technically means you should be able to get them to do something, but we all know that that's not how things work.",fy=True,
parts=[P(DRM,"What feels most aligned with your strengths, working without mandated authority?",c(R_AUTH2)+" [[pause]] "+c(R_AUTH3)),P(DRM,"(earlier in that call, about KIPP)",c(R_ADOPT1)+" … "+c(R_ADOPT2)),P(DAN,"(from your principal-management answer)",dan(70,72,start="Mandate authority is almost worthless"))],
say=["Your consulting practice ran 14 years (you said 10 on this call)."],
land="People felt very much a part of the process.",avoid="\"Fiefdom,\" \"franchise model,\" \"opt in or opt out\" about KIPP.",
bul=["Listen, bring people along, let the idea win on merit","A we, not us-versus-them","Tell people 10 things are wrong and they still want to do it","28 regions said yes, and again in year two with the bar raised","It worked, and people were part of the process"])

card(id="netsys",grp="scale",tier="Likely",q="How do network systems actually work at the school level?",who="Kruti",
hook="They aren't designed at the network level · follow the bright spot · cut the group out, get resentment",
why="Pairs with \"earn it\": the playbook itself came from what worked at a school.",
frame="Well, it's simple. They aren't designed at the network level.",fy=True,parts=[],
phrases={"src":S2,"asked":"How do you ensure that operational systems designed at the network level actually work for the people implementing them at the school level?","list":["Well, it's simple. They aren't designed at the network level.","I'm not saying that to be glib","they don't come from this room","what's working at one school","what are the attributes of that that make it work","let's limit the scope, let's follow the bright spot","there's no way that a single system is going to come out of a room of seven smart people that's going to be perfect for everyone","oh my God, I told them that","network mandates that oftentimes are 90% or 95% what the group would make, but we cut the group out, and it leads to a ton of resentment"]},
none="Only fragments were kept word for word. Build it from the phrases below.",
say=["KIPP proof: 28 autonomous regions, no mandate authority, an alternate path that no region took, and in year two they came back with the bar raised."],
land="Say the KIPP result, then stop.",avoid="Quizzing them on a management book (last time).",
bul=["Systems come from what's working at one school","Name what makes it work","Limit what has to be identical","The people doing it are in the room where it's written","Mandates that cut the group out breed resentment"])

card(id="covid",grp="scale",tier="Likely",q="A crisis, or a goal with no roadmap. What did you do?",who="Kruti or Paola",
hook="Over 1,000 students, ~200 staff, COVID · four days: gather, paper, leadership, staff · paper alone is worthless",
why="Zeta just opened several schools at once; this shows you can move fast without steamrolling people.",
frame="Leading an organization of over a thousand students and nearly 200 staff through COVID.",fy=True,
parts=[P(DRM,"Tell me about a significant piece of work where you were given a goal and a high degree of autonomy.",c(R_COVID1)+" … "+c(R_COVID2)),P(DRM,"(continuing)",c(R_COVID3)+" … "+c(R_COVID4)),P(DRM,"(how you summed it up)","[[slow]] "+c(R_COVID5))],
phrases={"src":S2,"asked":"(the same weekend, told as an inherited-operation story)","list":["the winter break of, I think, 2020, where COVID came back","keep students safe, families clear, and keep our teachers productive and safe","this was the weekend for it","entrance… student movement… PPE… testing and verification","what should happen at 7:45, what should happen at 7:50","90 minutes every single morning, only doing testing","we'd reinvented how we do school in one weekend"]},
say=[],land="Nothing that gets to the people is going to matter if the fundamental premise is: this is being done to us.",avoid="\"This is not a question I prepared for\" (last time).",
bul=["1,000+ students, ~200 staff","Day 1: gather information, including what people needed emotionally","Day 2: answers on paper","Day 3: leadership team alignment","Day 4: a full day with staff","Paper alone is worthless if it feels done to people"])

card(id="build",grp="scale",tier="Bench",q="How would you build something new when you're not the expert?",who="Kruti",
hook="Outcome first · where did we almost go wrong? · done when it runs without me",
why="Useful for launching new schools or taking on the high school.",
frame="I get super clear on exactly what the outcome needs to be.",fy=True,parts=[],
phrases={"src":S2,"asked":"If you aren't the content expert, how would you go about building that out for people?","list":["I get super clear on exactly what the outcome needs to be. Not what the step, the action is, but rather the outcome","I'm not wasting people's time with silly questions","it's not asking for their opinion for the sake of just asking for their opinion","I frankly need that expertise","where did we go wrong last year? Where do we almost go wrong last year?","finding the bright spots","I've got a deep network of folks who have run operations","we map out the arc of what needs to happen, milestones, the exact next steps, the owners, the owners with a date a month before the actual due date","we establish a cadence of communication, there's a tracker","the project doesn't end when we run the first successful full cycle","I'm happy to manage it, and I will be managing it for as long as it takes","building the capacity of others such that we're handing off systems rather than dragging people through processes"]},
none="Only fragments were kept word for word. Build it from the phrases below.",
say=[],land="Handing off systems rather than dragging people through processes.",avoid="Reciting it as a numbered seven-step list (last time).",
bul=["Outcome, not the action","I need their expertise","Where did we almost go wrong?","Bright spots","Owners, dates a month early, a tracker","Done = runs without me"])

card(id="lab",grp="hard",tier="Likely",q="Brooklyn Lab: what was that job, and what was hard about it?",who="Either",
hook="Transition superintendent · no trust, no systems, under-enrolled, up for renewal · hard, early, unapologetic",
why="A renewal alone isn't impressive. The context is what makes it one.",
frame="Renewal by itself isn't the accomplishment. It was everything that was happening at the same time.",fy=False,
parts=[P(DAN,"(from your background answer)",dan(47,49))],
phrases={"src":S2,"asked":"(on enrollment and on compliance under pressure)","list":["we had a huge need","we didn't have strong systems in place","we frankly didn't have a team that really trusted each other","under enrolled and up for reauthorization","we did it hard, we did it early, we did it unapologetically, but we wouldn't do it without strong communication"]},
say=["What made it hard, in one line: two authorizers running separate processes, no reliable institutional records, a turnaround, COVID, and working to get acquired, all at once.","Then the result: both schools were reauthorized, and the transfer to new ownership went through.","You were interim high school principal for half a year while superintendent."],
land="Both schools were reauthorized.",avoid="Saying the numbers you were shown couldn't be trusted. Blaming the founder.",
bul=["Transition superintendent: renewal + new ownership","No trust, no systems, under-enrolled, up for renewal","Two authorizers, separate processes","Turnaround + COVID + acquisition at once","Both reauthorized","Interim HS principal, half a year"])

card(id="academic",grp="hard",tier="Must",q="You're known for systems and culture. Why trust you with academics?",who="Paola",
hook="Last 5–6 years leaned academic · Lab: results through principals · KIPP: meaningful grades → 46%",
why="DREAM asked this twice. It's the likeliest doubt about you for a schooling seat.",
frame="My career in the last five to six years has really leaned into that side of the work.",fy=True,
parts=[P(DRM,"Highlight your work connected to academics and teaching and learning. What have you owned or led, and at what scale?",c(R_ACAD1)+" [[pause]] At Brooklyn Lab, the "+c(R_ACAD_LAB)+". "+c(R_ACAD_LAB2)),P(DRM,"(continuing)",c(R_ACAD_KIPP)),P(DRM,"(where you might have a learning curve)","[[slow]] "+c(R_ACAD_REP)+" … "+c(R_ACAD_AP))],
say=["End on the result, not the gap: across 48 high schools, 46% of ninth graders finished the quarter at a 3.0 or better, up six points.","You were interim high school principal at Brooklyn Lab while superintendent."],
land="Say the 46%, then stop.",avoid="Ending on \"not the AP government standards person.\"",
bul=["Last 5–6 years leaned into academics","Lab: 3 schools, academic results through principals, all onboarding and L&D","KIPP: meaningful, normed grades; curriculum and grading practices","Own the reputation","Led PD, coached teachers, led departments","End on 46%"])

card(id="kipp",grp="hard",tier="Likely",q="Why did you leave KIPP? What have you been doing since?",who="Either",
hook="Design and hand-back role · running without me · custom tools for principals",
why="Short and clean. No apology.",
frame="It was a two-year design and hand-back role.",fy=True,
parts=[P(DRM,"(why you were leaving KIPP)",c(R_KIPP)+" … "+c(R_KIPP2)),P(DAN,"(from your background answer)",dan(51,51))],
say=["Since: custom tools for school leaders, school leader consulting, and sales advisory."],
land="It's running without me.",avoid="\"Too many cooks in the kitchen\" and any criticism of KIPP.",
bul=["Brought on to get One KIPP off the ground","Handed back to the regions","Running without me","Since: tools, consulting, advisory"])

card(id="consult",grp="hard",tier="Bench",q="Consultant to operator: why come back inside a network?",who="Either",
hook="Did it the wrong way before · happiest in a small growing network · people person",
why="Answers the unspoken \"will he stay?\"",
frame="I know, because I've done it the wrong way, that you can't approach working at a network the way you do working as a consultant.",fy=True,parts=[],
phrases={"src":S2,"asked":"How do you feel about the transition from consulting back to one network?","list":["I know because I've done it the wrong way that you can't approach working at a network the way you do working as a consultant","it wasn't intentional, but looking back on it, it's something I do very differently","I'm legitimately excited","the happiest I've ever been professionally was when I was in a small growing network with great people","my sense from what I've gathered, which is limited, and I'd love to get your read on this","I'd rather not do it from a hotel in Indianapolis","as much as I thought consulting and national work would sound cool, it's really not that fun","I'm a people person"]},
none="Only fragments were kept word for word. Build it from the phrases below.",
say=["Name the specific thing you do differently now (you never said it last time)."],land="I'm a people person.",avoid="Saying you do it differently without saying what.",
bul=["Did it the wrong way before","Kept a distance at Collegiate and Lab","Name what's different now","Happiest in a small growing network","People person"])

card(id="mistake",grp="hard",tier="Bench",q="A mistake, a growth area, or changing someone's mindset",who="Either",
hook="The mindset was my own · kept my associate dean in one lane · now co-dean with my former student",
why="Fits Zeta's \"love your people\" culture: you own a management failure and fixed it.",
frame="The mindset I had to overcome was my own.",fy=False,parts=[],
phrases={"src":S2,"asked":"An example of trying to overcome a mindset with somebody, and the outcome?","list":["an Associate Dean of Students who was a wonderful human being, a true friend of mine, but I managed him","he was the guy that everybody loves, the parents just couldn't get upset with him, or if they did, he figured out a way to make it work","that's what he does really well. I'm kind of on the system side of things","that worked at first, especially when we were stabilizing the school","what I didn't do is I didn't update my thinking","in years three and four, I wasn't developing him to become a Dean of Students","letting him stay and thrive in his sphere","I learned I had to leave, and all of a sudden I've got six months before he is now the Dean of Students. And I realized I failed him","there's a little bit of bumpiness along the way, but within a month, he was clearly meeting well-established targets","if I would have started two or three years earlier, he would have been much further down the road, and the school would have been better off, and he would have been better off","he was the Dean of Students for many years after. In fact, he's now co-Dean of Students with one of my former students"]},
none="Only fragments were kept word for word. Build it from the phrases below.",
say=["Close with the lesson: you don't get to hold a fixed mindset about a person.","Don't give the reason you had to leave."],land="He's now co-Dean of Students with one of my former students.",avoid="Why you left Excel.",
bul=["Associate dean everyone loved; I kept him in one lane","Didn't update my thinking","Six months to get him ready; I failed him","Within a month, meeting targets","Now co-dean with my former student"])

card(id="ask1",grp="ask",tier="Must",q="ASK BY MINUTE 10: which role?",who="Both",
hook="Which role · success at 12 months · then listen",
why="You left the Dan call not knowing the seat or the next step.",
frame="Which role are you considering me for, and what would success look like at twelve months?",fy=False,
parts=[P(DAN,"(how you asked Dan about the routing; the form that worked)",dan(211,211))],
say=[],land="Then stop and listen.",avoid="Waiting until the end of the call.",bul=["Ask by minute 10","Let them describe it","If they turn it back: see \"Year one\""])

card(id="ask2",grp="ask",tier="Must",q="Your questions, and the close",who="Both",
hook="Kruti: consistency across new campuses · Paola: the 119 ninth graders · next step and who else",
why="One question for each of them, then the next step.",
frame="I have one for each of you.",fy=False,
parts=[P(DAN,"(how you closed with Dan; stop before \"blah, blah, blah\")",dan(228,229,end="Two, I'm excited."))],
say=["Kruti: With Flushing, Tremont Park and the high school all opening this fall, what's been hardest to keep consistent from campus to campus?","Paola: For the 119 ninth graders in that first class, what does a great first year look like by June?","Close: What's the next step, and who else would I talk to?"],
land="What's the next step?",avoid="\"Blah, blah, blah. You know the story.\"",bul=["One question each","Next step, and who else","Thank them; stop"])

card(id="year1",grp="bench",tier="Bench",q="What would you want to own in year one?",who="Either",
hook="Principals · ninth-grade academic health for the high school",
why="No recorded answer. The position is yours.",
frame="Principals, and especially the high school side.",fy=False,parts=[],none="No recorded answer. Frame and bullets are proposals.",
say=[],land="",avoid="",bul=["Managing a set of principals, the way Dan described","Owning ninth-grade academic health for the new high school","Why: Carver and the 46% are your strongest proof"])

card(id="feedback",grp="bench",tier="Bench",q="How do you like to receive feedback? How should I manage you?",who="Paola",
hook="I want to know where I stand · plainly · \"this has already been decided\"",
why="A likely manager-fit question.",
frame="I want to know where I stand.",fy=True,parts=[],
phrases={"src":S2,"asked":"How do you prepare to receive feedback, and how do you like to work feedback with your manager?","list":["I want to know where I stand","I know everyone says this, and most people don't mean it","I would love to be able to assume that I'm in whatever standing I was in the last time we had the conversation unless I hear otherwise from you","proactively bring that up","especially if it's coming from someone I trust and respect","saying it as plainly as possible","I've done this for a while, long enough to know it's not really about me","take a problem back to first principles and examine the problem from its root","hey Chris, this has already been decided"]},
none="Only fragments were kept word for word.",say=[],land="",avoid="Running long past the landing (last time).",bul=["Where I stand","Proactively, plainly","It's not about me","First principles; tell me when it's decided"])

card(id="start",grp="bench",tier="Bench",q="When could you start?",who="Either",hook="Flexible · hand off current projects thoughtfully",
why="Gillian floated October 13 on 09/11.",frame="The work I'm doing now is flexible enough in scope.",fy=True,
parts=[P(GIL,"We're thinking about an October 13th start date. Any concerns?",c(G_START))],say=["Check this against your United Schools commitment first."],land="",avoid="",bul=["Flexible","Hand off projects thoughtfully"])

card(id="pay",grp="bench",tier="Bench",q="Compensation expectations",who="Either · never raise it first",hook="Title and pay match the scope · right team over cashing in",
why="Your standing rule: ask for the top of the published band. The debrief put the Principal Manager band at $125K to $175K.",
frame="I'd want the title and pay to match the scope.",fy=False,
parts=[P(DRM,"The range is $145,000 to $165,000 and we can't go outside the band. Is that aligned?",c(R_PAY))],
say=["At Zeta the number is yours to set. Your file: target $200K, comfortable $150K, salary of record $175K."],land="",avoid="Naming a number first.",bul=["Don't name a number first","Top of the band","If the scope grows, the number grows"])

card(id="inperson",grp="bench",tier="Bench",q="In person every day in the Bronx. Does that work?",who="Either · never raise it first",hook="Considered it · right people, right work · eyes wide open",
why="Gillian asked about the Inwood commute; the Principal Manager seat is at 425 Westchester Ave, daily.",
frame="I've considered it. Short answer is no.",fy=True,
parts=[P(GIL,"Our network office is at the top of Manhattan in Inwood. Any concern about the commute?",c(G_COMMUTE_A)+" … "+c(G_COMMUTE_B))],
say=["The \"…\" skips the part about your kids. Leave it out this time."],land="",avoid="Volunteering family logistics.",bul=["Considered it; no","Right people, right work","Eyes wide open"])

card(id="ai",grp="bench",tier="Bench",q="Tell us about the AI tools you're building",who="Kruti · only if asked",hook="Principals point me at a problem · in service of the role · not for its own sake",
why="Only if asked. Don't pitch the practice.",
frame="Principals point me at a problem, and I build the thing that saves them the time.",fy=False,
parts=[P(DAN,"(from your background answer)",dan(52,52,end="the specific solutions that they need")),P(GIL,"Are you looking for a role that still has this AI and technology component?",c(G_AI))],
say=[],land="Not for the sake of doing it.",avoid="\"That's been taking off.\"",bul=["Principals point me at a problem","Custom tools, workflows, apps","In service of the role, not for its own sake"])

json.dump(CARDS,open("cards.json","w"),ensure_ascii=False,indent=0)
print(len(CARDS),"cards")
