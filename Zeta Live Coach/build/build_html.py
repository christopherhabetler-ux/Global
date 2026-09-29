import json,re
exec(open('build_cards.py').read().split('exec(open("src_other.py")')[0])   # dan(), clean()
exec(open('src_other.py').read())
def c(t): return clean(t)
B={int(k):v for k,v in json.load(open('bank.json')).items()}
Q=json.load(open('Q.json'))
B={}   # the condensed 092526 bank is retired (CH 092926); NB = dictated Notion blocks
NB={}
for part in open('canon/notion_bank.md').read().split('## ')[1:]:
    k,*ps=part.strip().split('\n'); NB[int(k)]=[p for p in ps if p.strip()]
TR=re.sub(r'\s+',' ',open('canon/transcripts.md').read()); BK=re.sub(r'\s+',' ',open('canon/banks.md').read())
def T(a,b,src=None):
    x=src or TR; i=x.index(a); return x[i:x.index(b,i)+len(b)]
_cv=json.load(open('cv.json')); CV=_cv['CV']; JEREL=_cv['JEREL']
def cv(a,b): i=CV.index(a); return CV[i:CV.index(b,i)+len(b)]
CC=c(T("The most, the one that's kind of the stickiest was","It has to be a connection.")).replace('Kinect. And correct','Connect and correct')

def cue(kind,label): return f'<span class="dcue {kind}">{label}</span>'
def sent(text,starts,ends=None):
    """exact substring of text from `starts` through `ends` (inclusive)"""
    i=text.index(starts)
    j=text.index(ends,i)+len(ends) if ends else len(text)
    return text[i:j]
def js(v): return json.dumps(v,ensure_ascii=False)

TPL='/root/.claude/uploads/082d523f-53ee-5a6a-90ab-6722c5806cce/9526ee6a-ZETA_ROJAS_CALL_COMPANION_092526.html'
t=open(TPL).read()

# ---------------- STORIES (every "full" is your words; source in brackets) ----------------
S=[]
def story(sid,name,proves,full,src): S.append({'sid':sid,'name':name,'proves':proves,'full':full+f' <span class="small">[{src}]</span>'})
story('(1)','270TH TO NUMBER ONE','He led a turnaround as Dean of Students, and he wrote the playbook first.',
  NB[3][0]+' … '+sent(NB[3][1],'I spent six days')+' … '+NB[3][6],'bank block 3 as dictated')
story('(2)','28 REGIONS, 48 HIGH SCHOOLS, NO MANDATE','Adoption without authority. The job a principal manager does every week.',
  '… '+sent(NB[2][0],'the KIPP Foundation is the national arm','want to say yes.')+' … '+sent(NB[2][1],'All 28 regions'),'bank block 2 as dictated')
story('(3)','ACADEMIC HEALTH, 46%','Ninth grade is where networks lose kids, and he moved the number.',
  '… '+sent(NB[2][4],'we built a push-button')+' '+NB[2][5],'bank block 2 as dictated')
story('(4)','CARVER','He coached a struggling principal into the CEO seat.',
  cv('I first started working with Jerel Bryant','can he be successful?')+' … '+cv('I helped Jerel be the leader','It worked.')+' … '+JEREL,'written Carver answer 060925')
story('(5)','BROOKLYN LAB, IN CONTEXT','Stewardship through a mess: a team that did not trust each other, COVID, an ownership transfer, two renewals at once. And he ran a high school himself.',
  T('Two simultaneous renewals. A renewal in itself','twice at the same time.',BK)+' '+T('A charter renewal is not a project deadline.','do not exist next year.',BK)+' Both were reauthorized.','ONE STORY 091326; Story Bank 081226')
story('(6)','DEANSLIST','A school operations product he built. Only if asked.',
  c(dan(40,40,end="grew into Dean'slist."))+' <span class="small">Facts, not your words: zero to 275 while you were there, in over a thousand now, not affiliated in years. All three together or none.</span>','Dan call line 40')
story('(7)','THE COVERAGE SCHEDULE MAKER','He is building school tools now, with an honest ceiling.',
  'Your words 090326: "returning somewhere between two and four hours a week."','ONE STORY 091326')
story('(8)','THE ASSOCIATE DEAN','The failure is real, and it has a happy ending.',
  'I learned I had to leave, and all of a sudden I\'ve got six months before he is now the Dean of Students. And I realized I failed him … within a month, he was clearly meeting well-established targets … he\'s now co-Dean of Students with one of my former students','onsite 090826, debrief-quoted')
story('(9)','THE DREAM VERSION (academics)','Your other recorded answer to "you are a systems and culture person." Reference, not a script.',
  c(R_ACAD1)+' … '+c(R_ACAD_LAB)+'. '+c(R_ACAD_LAB2)+' … '+c(R_ACAD_KIPP),'DREAM screen 081726')
story('(10)','THE FOUR-DAY COVID PLAYBOOK','He runs a crisis as a plan on paper that actually reaches people. Good for launch or ambiguity questions.',
  c(R_COVID2)+' '+c(R_COVID3)+' … '+c(R_COVID4)+' … '+c(R_COVID5)+' <span class="small">The passage does not name the school. No student or staff count with it; the one you gave DREAM does not match the Brooklyn Lab file.</span>','DREAM screen 081726')

# ---------------- ENGINES (one / full / bend lines are your words) ----------------
cl=dan(60,60,start='your identity as a principal',end="not the skin that you're in.").strip('… ')
E=[
{'sid':'ENGINE 1','name':'NO MANDATE, NO SCHOOL TOOK THE ALTERNATE PATH',
 'one':sent(NB[2][0],'Nobody had to say yes','want to say yes.'),
 'proves':'Adoption without authority: how a network office gets principals to use what works. Kruti\'s whole job.',
 'full':sent(NB[2][0],'the KIPP Foundation is the national arm','want to say yes.')+' '+cue('slow','slow')+' '+sent(NB[2][1],'First thing we did','watching them nod.')+' '+cue('power','land this')+' '+sent(NB[2][1],'All 28 regions'),
 'guards':'Strategy adoption is 28 and 48. The push-button tool was PILOTED and handed off, never "used by all 28." You SUPPORTED 48 high schools; never "managed 48 principals." Never grade KIPP.',
 'bends':[
  ["What's hard about the high school",'Lead with ninth-grade academic health.',sent(NB[2][5],'That year','Up six points.')],
  ['How do you lead change','Lead with the one thing.',sent(NB[13][1],'The first part is the most important part','on track.')],
  ["A principal won't use the system",'Lead with merit over obligation.',"Building systems and structures and practices that people buy into on merit, not out of obligation."],
  ['A strong principal pushes back','Lead with your side of the street.',c(dan(65,65,end='above reproach.')).strip('… ')]]},
{'sid':'ENGINE 2','name':'EARN IT: RUN THE PLAY, THEN INNOVATE',
 'one':"Earn that, right? Get to the place of stable, get to the place of functional, then let's have a conversation about innovation.",
 'proves':'In plain words: a new principal runs the proven playbook until the school is stable and functional, and that earns the room to change it. It is about sequence, not control. Pair it with how you invest in people (Dan\'s "love people" speech came about 15 minutes later).',
 'full':c(dan(97,100,end='starting from a solid foundation of what we know that works.')).rstrip(' …')+' '+cue('power','then the proof')+' '+c(dan(100,101,end='now has my old job')).strip(' …')+'.',
 'guards':'Never "I don\'t care really if you as a first-year principal..." Never grade KIPP or AF. Jackie is sixth grade. Always pair with investment: Carver, the associate dean.',
 'bends':[
  ['First ninety days, a new principal','Lead with writing it down.',sent(NB[3][1],'I spent six days','crazy use of time.')],
  ['A principal wants to do their own thing','Lead with the evolution line.',"The play is not perfect. The play is going to evolve. You're going to be part of that evolution."],
  ['Why do networks plateau','Lead with identity, not the KIPP grade.',"So fundamentally, we were clear on who we were."],
  ['How does that square with loving your people','Lead with Carver.',CC]]},
{'sid':'ENGINE 3','name':'CARVER',
 'one':'do we keep this leader, can he be successful?',
 'proves':'He can tell a hard truth about a struggling principal and grow him into the top seat. Paola\'s whole job.',
 'full':cv('I first started working with Jerel Bryant','can he be successful?')+' '+cue('slow','slow')+' '+cv('I did this by primarily working shoulder to shoulder','built his confidence')+' '+cue('beat','beat')+' '+cv('I clearly named','narratives of blame.')+' '+cue('power','land this')+' '+JEREL,
 'guards':'It started as an assessment. Coached, never led. Louisiana Principal of the Year (your wording, kept 092926). The 75% suspension drop is Collegiate network-wide, never Carver alone. CREDO: "One of our schools, Carver, had the largest CREDO effect size in the country."',
 'bends':[
  ['The good principal who needs to get to great','Lead with clothes, not skin. Then Carver.',cl[0].upper()+cl[1:]],
  ['Hard feedback','Lead with naming the frayed relationship.',cv('I clearly named','narratives of blame.')],
  ['A principal is underwater','Lead with strengths, not deficits.',cv('Knowing we had a high potential leader','built his confidence')],
  ['Culture','Lead with connect and correct.',CC]]}]

TICK=[
 'Answer in the FIRST sentence. The claim, not "I wish I had the answer."',
 'Every principal answer ends on a person or a number. Carver. The 46%. Interim, half a year.',
 'MUST-ASK 1 by minute 10: which role, and what success looks like.',
 'Two people. Two minutes an answer, then STOP. You ran 3 to 6 minutes with Dan.',
 'Pace 150, not 175. Slow down on the proof.',
 '"Earn it" always comes with how you invest in people.',
 'Brooklyn Lab: knots and forensics first. The renewal last, lightly.',
 'Never grade KIPP or AF. Never "the rest of the mess." Never why you left Excel.',
 'Never volunteer the kids, the commute, or pay.',
 'Look at whoever asked. Then the other one on the last sentence.',
]
PANIC={'say':'<span class="dcue flat">your words, Gillian 091126</span> '+"Sorry, short answer, yes.",
 'then':'No recorded line for buying time. Frame: take a breath, restate the question in five words, then go to the strongest thing you own. Carver: Jerel is the CEO. KIPP: 46% of ninth graders at a 3.0 or better, up six points. Excel: 270th in the state to number one.'}
PANIC['say']='No recorded stall line in your words. Frame: pause, one breath, restate their question in five words, then answer the first sentence only.'
MUST=[
 'Carver: "'+JEREL+'"',
 '46% of ninth graders at a 3.0 or better, up six points. Best quarter KIPP had ever had.',
 '28 regions, 48 high schools, no mandate. No school chose the alternate path.',
 'Interim high school principal at Brooklyn Lab, half a year, while superintendent.',
 '270th in the state to number one. Top 3% nationally now.',
 'Clothes: "the clothes that you wear, not the skin that you\'re in."',
 'ASK by minute 10: which role, and success at twelve months.',
 'ASK: the next step, and who else.'
]
DELIVERY=[
 'One breath before every answer. The silence is shorter than it feels.',
 'Pace 150. With Dan you ran 175, 17% faster than on 091126.',
 'Two minutes, then stop. Hit the STOP button and count three.',
 'The first sentence is the claim. The proof is the last sentence.',
 'Two interviewers: eyes on the one who asked, swing to the other for the last line.',
 'When you concede something, concede it once and flat. Never twice.',
 'Camera, not the screen, on every sentence that matters.',
 'Heard yourself say "kind of" twice in a row? Stop, breathe, restart the sentence.'
]

# ---------------- HTML sections ----------------
H={}
H['now']='''<div class="card"><div class="lab">Tuesday 092926 &middot; 3:00-3:30 PM ET &middot; thirty minutes, two people</div>
<div class="ans"><p><b>Paola Zalkind</b>, Chief Schooling Officer, and <b>Kruti Mehta</b>, Managing Director, Scaling School Excellence. Zoom: <b>us06web.zoom.us/my/krutiatzeta</b>.</p>
<p>The ops seat is closed. Felipe passed you to the schooling side, and Dan's first question was about managing principals. The live seat is almost certainly <b>Principal Manager</b>.</p>
<p>Dress: business casual, collar. It applies on Zoom.</p></div></div>
<div class="card"><div class="lab">The four things that decide this call</div><div class="ans">
<p><b>1.</b> First sentence is the claim. Last sentence is a person or a number.</p>
<p><b>2.</b> Every principal answer ends on proof: Carver, Brooklyn Lab interim, the 46%. With Dan, 1 of 5 answers did.</p>
<p><b>3.</b> MUST-ASK 1 by minute 10. With Dan you asked nothing until time was up.</p>
<p><b>4.</b> Two minutes, then stop. Two of them, thirty minutes.</p></div></div>
<div class="card prepOnly"><div class="lab">What the Dan call cost (debrief 092526)</div><div class="ans">
<p>Execution B-, outcome B+/A-. Background ran about 5&frac34; minutes against 2:35. Carver came out as "we were able to be successful in that." You graded KIPP and AF "B minus to C minus" out loud. You gave the health reason for leaving Excel. "The rest of the mess" to a ten-year Success principal. The close sounded offhand: "blah, blah, blah."</p></div></div>'''
H['open']='''<div class="card"><div class="lab">The running order</div><div class="ans">
<p><b>0-1</b> &middot; Warm open. Thank them for the time. If Paola is warm, TFA is an easy line at the end, not now.</p>
<p><b>1-4</b> &middot; Background walk, card 1. 2:35. Skip the kids paragraph.</p>
<p><b>By minute 10</b> &middot; <b>MUST-ASK 1</b>, card 17: has this role existed, and what made that person successful.</p>
<p><b>Paola's turn</b> &middot; cards 3-5. Every one ends on Carver or Brooklyn Lab.</p>
<p><b>Kruti's turn</b> &middot; cards 8-12. Earn it, paired with investing in people. Card 9 if it's about network systems.</p>
<p><b>Minute 20</b> &middot; card 18. One question each, then the next step.</p></div></div>'''
H['hs']='''<div class="card"><div class="lab">Their high school, say-able</div><div class="ans">
<p><b>Opened August 2026</b> in an interim Washington Heights site, <b>119 ninth graders</b> from Zeta's own first class. <span class="small">Sources: Zeta research 092826; CALL PREP Dan Rojas</span></p>
<p>Design shown to Community Board 12, March 2026: <b>Z pods</b> of about 12 students who stay together, four <b>Z houses</b>, portfolios, AP required to graduate, SAT prep in school, a ZLab. <span class="small">Source: Zeta research 092826 (search excerpts)</span></p>
<p>From Dan: about <b>91%</b> of high school students stay year to year. His worry is college admissions: a strong student with one C in ninth grade got into no Ivy. The redemption-arc essay has stopped working. ZLab is "our fifth core." There is a taekwondo team. <span class="small">Source: Rojas debrief 092526 &sect;6</span></p>
<p><span class="dcue stop">never</span> A Zeta attrition or proficiency number. The NYPD episode. The 181st St opposition.</p></div></div>
<div class="card"><div class="lab">The link nobody else will make (frame, not words)</div><div class="ans">
<p>Dan's fear is the ninth-grade C that follows a kid forever. Your KIPP work was ninth-grade grades, weekly, across 48 high schools: 46% at a 3.0 or better, up six points. Z pods are the structure; a weekly ninth-grade academic health routine is what protects it. Your words for that are on card 10 ("present but obscured, to right in front of them").</p></div></div>
<div class="card"><div class="lab">Your high school record, said plainly</div><div class="ans">
<p><b>Collegiate Academies:</b> high school network, five years as Chief Culture Officer. One of our schools, Carver, had the largest CREDO effect size in the country.</p>
<p><b>Brooklyn Lab:</b> interim high school principal for half a year, while superintendent.</p>
<p><b>KIPP:</b> national high school strategy, 48 high schools. 46% of ninth graders at 3.0+, up six.</p>
<p><b>Carver:</b> 200 students when you walked in, eight or nine hundred now. Jerel is the CEO.</p>
<p><b>Excel:</b> its high school is in the top 3% of public high schools nationally.</p></div></div>'''
H['repairs']='''<div class="card"><div class="lab">Repair 1 &middot; Carver, reduced to "successful"</div><div class="ans">
<p>Say the whole thing, live. Your line (060925): <em>"'''+JEREL+'''"</em> Card 4.</p></div></div>
<div class="card"><div class="lab">Repair 2 &middot; Principles with no proof</div><div class="ans">
<p>Card 3 now ends on Carver. Any principal answer that ends on a principle is not over.</p></div></div>
<div class="card"><div class="lab">Repair 3 &middot; "Earn it" heard alone</div><div class="ans">
<p>"Earn that" landed with Dan, and about 15 minutes later he gave a speech on "you have to love people." In plain words, earn it means: a new principal runs the proven play until the school is stable and functional, then gets room to change it. Say it, then Carver or the associate dean, so they hear the investment too.</p></div></div>
<div class="card"><div class="lab">Repair 4 &middot; Grading KIPP and AF</div><div class="ans">
<p>Describe how KIPP works, never its results. The Excel contrast makes the point alone. Your line: <em>"So fundamentally, we were clear on who we were."</em></p></div></div>
<div class="card"><div class="lab">Repair 5 &middot; Leaving Excel</div><div class="ans">
<p>Never the health reason. The approved form: you knew you would be leaving at the end of the year. Your onsite line: <em>"I learned I had to leave."</em></p></div></div>
<div class="card"><div class="lab">Repair 6 &middot; The questions</div><div class="ans">
<p>Ask by minute 10. Then ask, and be silent. Do not answer your own question.</p></div></div>'''
H['numbers']='''<div class="card"><div class="lab">Every number, with its source. Never say one that is not on this card.</div><div class="ans">
<p><b>Excel:</b> 270th to #1 in Massachusetts &middot; National Charter School of the Year &middot; Dean of Students &middot; 40% of staff reported to you &middot; six days on the playbook &middot; HS top 3% nationally. <span class="small">Sources: bank blocks 1, 3</span></p>
<p><b>Consulting:</b> over 100 schools &middot; fourteen years. <span class="small">Source: bank block 1</span></p>
<p><b>Collegiate:</b> 5 years CCO &middot; Carver: largest CREDO effect size in the country &middot; seven-level special education continuum &middot; suspension drop is <b>network-wide</b> only. <span class="small">Sources: bank block 1; ONE STORY 091326; your ruling 092926</span></p>
<p><b>Carver:</b> 200 to eight or nine hundred students &middot; Jerel is the CEO. <span class="small">Source: bank block 4</span></p>
<p><b>Brooklyn Lab:</b> superintendent for a transitional period &middot; 3 principals and the C-level team (CEO and CFO co-managed) &middot; interim HS principal, half a year &middot; two simultaneous renewals, three-year terms, both reauthorized, Board of Regents. <span class="small">Sources: bank blocks 1, 5; ONE STORY 091326; fact check 092926</span></p>
<p><b>KIPP:</b> 28 regions &middot; 48 high schools &middot; all adopted the HS strategy, no school took the alternate path &middot; 46% of 9th graders at 3.0+, up 6, best quarter KIPP had had &middot; 20 schools hit the goal &middot; the tool was piloted and handed off. <span class="small">Source: bank block 2 as dictated; your rulings 092926</span></p>
<p><b>Coverage schedule maker:</b> two schools' master schedules &middot; installed at one &middot; your estimate two to three hours a week. <span class="small">Source: bank block 8</span></p>
<p><b>Zeta:</b> high school 119 ninth graders &middot; 91% HS retention (Dan). <span class="small">Sources: research 092826; Rojas debrief</span></p>
<p><b>Principal Manager band:</b> $125K-$175K &middot; 425 Westchester Ave, daily. Never raise. <span class="small">Source: Rojas debrief &sect;0</span></p></div></div>'''
H['room']='''<div class="card"><div class="lab">Paola Zalkind &middot; Chief Schooling Officer</div><div class="ans">
<p>Her Zeta bio: she "manages Zeta's school leaders." TFA corps (5th grade). Success Academy from about 2006: teacher, AP, founding principal of SA Union Square (2013), then Managing Director of Schools. Then Director of Leader Development at <b>KIPP New Jersey</b>. At Zeta, Managing Director of Academics, now CSO. M.A., Teachers College.</p>
<p><b>What she is screening for:</b> has he actually managed principals, can he grow one, and does he show proof. She built principals for a living. She is the Principal Manager decision.</p>
<p class="small">Jessica Sie (CAO) owns curriculum, so Paola's lane is principals and school execution. LIKELY.</p></div></div>
<div class="card"><div class="lab">Kruti Mehta &middot; Managing Director, Scaling School Excellence</div><div class="ans">
<p>UT Austin BBA, Accenture, then BCG. Joined Zeta in its second year: "a complete leap of faith in myself when I left my consulting job." Network Operational Excellence, then Policy and Advancement, then Chicago Booth MBA (2024), now scaling. No school-leader history found.</p>
<p><b>What she is screening for:</b> can he codify what works and get schools to adopt it with fidelity. She likely needs someone with school-leader credibility beside her. LIKELY.</p>
<p class="small">She is the host (her Zoom room). Use whatever title she uses.</p></div></div>
<div class="card prepOnly"><div class="lab">Who's who</div><div class="ans">
<p>Emily Kim, Founder/CEO &middot; Paola Zalkind, CSO &middot; Jessica Sie, CAO &middot; Felipe Bustamante, COO Schools (passed you to this side) &middot; Dan Rojas, MD Schooling Excellence &middot; Gillian Clouser, talent, your advocate.</p></div></div>'''
H['asks']='''<div class="card"><div class="lab">MUST-ASK 1 by minute 10 &middot; your words</div><div class="ans">
<p><b>Zeta screen 091126:</b> "Is this a role that's existed in the past? And if so, what can you tell me about it and what made that person successful or what would you believe is necessary to make this person successful?"</p>
<p class="small">Don't name the Principal Manager title unless they do. Card 17.</p></div></div>
<div class="card"><div class="lab">Around minute 20 &middot; your words</div><div class="ans">
<p><b>FranklinCovey 081826, the one that got the rubric:</b> "What separates a [their seat] who make it in year one from ones that don't, and being as specific as possible as you can."</p>
<p><b>Onsite 090826 (debrief-quoted):</b> "What's your biggest concern about hiring someone with my profile?"</p>
<p><span class="dcue flat">proposed</span> Kruti: hardest thing to keep consistent campus to campus this fall. Paola: a great first year by June for the 119.</p></div></div>
<div class="card"><div class="lab">The next step</div><div class="ans">
<p><b>FranklinCovey 081426:</b> "How quickly are we looking to move on all this, do you know?" &middot; and who else you'd talk to.</p></div></div>'''
close_line=c(G_COMMUTE_A).split('. ')[-2]+'.' if False else "I wanna find the right group of people doing the right work more than anything."
H['close']=f'''<div class="card"><div class="lab">The last two minutes</div><div class="ans">
<p>{cue('warm','warm, at the camera')} Thank them. {cue('beat','beat')} Echo ONE thing each of them said, in their words. {cue('beat','beat')}</p>
<p>Your words: <em>"{close_line}"</em> <span class="small">[Zeta screen 091126]</span></p>
<p>Your words: <em>"I love being in environments where it's like best idea wins, strong opinions, loosely held. Let's debate the heck out of things. Let's attack people's ideas without attacking people."</em> <span class="small">[Dan call line 227]</span></p>
<p>{cue('slow','slow')} The next step, and who else. {cue('stop','STOP')}</p>
<p class="small">Not "blah, blah, blah. You know the story."</p></div></div>
<div class="card"><div class="lab">After the call, same day</div><div class="ans">
<p>Thank-yous within two hours, separate threads, one specific thing each said. first.last@zetaschools.org is likely; check the invite.</p></div></div>'''
H['traps']='''<div class="card"><div class="lab">Banned strings. These are literal, not concepts.</div><div class="ans">
<p><span class="dcue stop">never</span> The health reason for leaving Excel</p>
<p><span class="dcue stop">never</span> A grade for KIPP or AF ("B minus to C minus")</p>
<p><span class="dcue stop">never</span> "The rest of the mess," or any Success comparison. Paola spent years at Success</p>
<p><span class="dcue stop">never</span> "I don't care really if you as a first-year principal..."</p>
<p><span class="dcue stop">never</span> A bare "principal." It was <b>interim</b>, half a year, while superintendent</p>
<p><span class="dcue stop">never</span> The Brooklyn Lab removal decision in writing. Out loud only</p>
<p><span class="dcue stop">never</span> That the numbers you were shown at Brooklyn Lab were false</p>
<p><span class="dcue stop">never</span> "Managed 48 principals." You supported 48 high schools. Never merge the 8 you coached at Collegiate PD with the 3 at Brooklyn Lab</p>
<p><span class="dcue stop">never</span> "The tool is used by all 28." It was piloted and handed off</p>
<p><span class="dcue stop">never</span> Suspensions down 75% at Carver. It was network-wide</p>
<p><span class="dcue stop">never</span> "Better part of a decade" for consulting. It was fourteen years</p>
<p><span class="dcue stop">never</span> The kids, the commute, or pay, first</p>
<p><span class="dcue stop">never</span> A Zeta proficiency or attrition number, the NYPD episode, the 181st St fight</p>
<p><span class="dcue stop">never</span> "Five-year" renewals (they were three-year), "SUNY" (Zeta's authorizer), "new charter operator"</p>
<p><span class="dcue stop">never</span> "I led the national strategy." Kate Starke led the team. The tool was piloted and handed off</p>
<p><span class="dcue stop">never</span> "KIPP credited my system" or "cited as the driver." The link is your own read</p>
<p><span class="dcue stop">never</span> Carver as "led." You coached</p>
<p><span class="dcue stop">never</span> The coverage tool as "piloting" or "in pilot," and never pitch the practice to Kruti</p>
<p><span class="dcue stop">never</span> Excel's home-language share as 70% or 75%. "About half," or no number</p>
<p><span class="dcue stop">never</span> The Principal Manager title, unless they say it first</p></div></div>
<div class="card"><div class="lab">The self-disqualifying strings (banned as strings, DREAM 081726 and FC 081426)</div><div class="ans">
<p><span class="dcue stop">never</span> "I'm not trying to" &middot; "I don't mean to" &middot; "there's a lot I'd have to learn" &middot; "I need to catch up" &middot; "that's not where I'm at" &middot; "I'm probably more of a" &middot; "I'm not an expert in" &middot; "I don't want to overstate"</p>
<p><span class="dcue stop">never</span> "This is not a question I prepared for" &middot; "happy to go deeper" &middot; "long story short" &middot; "I'll get to your exact question, but first" &middot; "I'll just pause right there"</p>
<p><span class="dcue stop">never</span> "a little bit" or "kind of" on a credential. A vague word about your results means the next word is a digit</p>
<p class="small">Sources: IP DEBRIEF EXTRACT 090526; HOW I SHOW UP 090326. If you hear yourself building a disclaimer, the sentence after it does not get said.</p></div></div>'''
H['rp']='''<div class="card"><div class="lab">How to use these</div><div class="ans">
<p>Three likely sequences. The follow-ups are frames; your answers point to cards with your words. <b>Say each out loud once.</b></p></div></div>
<div class="card"><div class="lab">ROLE PLAY 1 &middot; Paola, then the push for proof</div><div class="ans">
<p><span class="rpq">PAOLA</span> How do you develop a principal who's good but not great?</p>
<p><span class="rpa">YOU</span> Card 3, ending on Carver. <span class="dcue stop">stop</span></p>
<p><span class="rpq">PAOLA</span> What did you actually do with him week to week?</p>
<p><span class="rpa">YOU</span> Card 4, the middle: shoulder to shoulder, real-time feedback, resetting the frayed relationship. <span class="dcue stop">stop on "CEO of Collegiate Academies"</span></p></div></div>
<div class="card"><div class="lab">ROLE PLAY 2 &middot; Kruti, fidelity vs. autonomy</div><div class="ans">
<p><span class="rpq">KRUTI</span> How do you decide what's non-negotiable when a principal wants to do it differently?</p>
<p><span class="rpa">YOU</span> Card 8, earn it. <span class="dcue power">then</span> Engine 2, last bend: connect and correct.</p>
<p><span class="rpq">KRUTI</span> And when a school just isn't adopting it?</p>
<p><span class="rpa">YOU</span> Card 9, KIPP. End on "no school chose it."</p></div></div>
<div class="card"><div class="lab">ROLE PLAY 3 &middot; The doubt</div><div class="ans">
<p><span class="rpq">PAOLA</span> You've never been a standing principal. Why should principals trust you?</p>
<p><span class="rpa">YOU</span> Card 5: two seats managing principals, and interim at Brooklyn Lab for half a year. <span class="dcue flat">flat, no apology</span> Then card 12's first line: "Yes and no." <span class="dcue stop">stop</span></p></div></div>'''
H['intel']='''<div class="card"><div class="lab">From the Dan call 092526 (debrief &sect;6)</div><div class="ans">
<p>The ops seat is closed; Felipe made the call. Zeta moves people between teams rather than letting them go. "You have to love people": kids, parents ("most especially the ones that are most challenging"), and staff. "The requirement of the manager is a lot higher." Dan oversees many principals and designed the high school. He said "I love that idea" about the 50/25/25 audit. "We will be in touch very soon."</p></div></div>
<div class="card"><div class="lab">What Zeta is doing now</div><div class="ans">
<p>Tremont Park opened Sept 17, 2026. Queens Flushing opened August 2026. The high school opened August 2026. Z Combinator, a federal grant for charter founders. <span class="small">Source: research 092826, LIKELY on counts</span></p></div></div>
<div class="card prepOnly"><div class="lab">Connection points, light touch</div><div class="ans">
<p>Paola was at KIPP New Jersey; you were at the KIPP Foundation. Don't name anyone you haven't checked. Paola is a TFA alum and the TFA 35th Summit is this Friday and Saturday: an easy line at the end. Kruti left consulting for Zeta; you went consulting to operator (bench card).</p></div></div>
<div class="card prepOnly"><div class="lab">Know it, don't raise it</div><div class="ans">
<p>The NYPD episode. The 181st St community board fight. The Sept 2025 rally. Reported 2026 ELA dip. Listen if any of it surfaces. Never introduce it.</p></div></div>'''

# ---------------- assemble ----------------
a=t.index('var STORIES = [')
b=t.index('/* ============================== ENGINE - do not edit')
data=('var STORIES = '+js(S)+';\n\nvar Q = '+js(Q)+';\n\nvar TICK = '+js(TICK)+';\n\nvar PANIC = '+js(PANIC)+
      ';\n\nvar MUST = '+js(MUST)+';\n\nvar DELIVERY = '+js(DELIVERY)+';\n\nvar HTML = '+js(H)+';\n\nvar ENGINES='+js(E)+';\n\n\n')
t=t[:a]+data+t[b:]
R=[
('<title>Zeta Call Companion &middot; Dan Rojas &middot; 092526</title>','<title>Zeta Call Companion &middot; Zalkind &amp; Mehta &middot; 092926</title>'),
('placeholder="high school &middot; ninth grade &middot; KIPP &middot; principal &middot; growth &middot; left KIPP &middot; instruction &middot; commute"','placeholder="principal &middot; Carver &middot; scale &middot; earn it &middot; high school &middot; KIPP &middot; instruction &middot; Brooklyn Lab"'),
("'zeta0925_'","'zeta0929_'"),
("{g:'B', c:'c2', name:'His High School', she:true}","{g:'B', c:'c2', name:'Principals &middot; Paola', she:false}"),
("{g:'C', c:'c3', name:'Adoption Without Authority', she:false}","{g:'C', c:'c3', name:'The High School', she:false}"),
("{g:'D', c:'c4', name:'Leaders Who Are Struggling', she:false}","{g:'D', c:'c4', name:'Scaling &middot; Kruti', she:false}"),
("{g:'Q', c:'c2', name:'More Scenarios'}","{g:'Q', c:'c2', name:'More Principal Answers'}"),
("{g:'S', c:'c8', name:'Openers &amp; Backup Asks'}","{g:'S', c:'c8', name:'Backup Asks'}"),
('<div id="cMustN">8</div>','<div id="cMustN">'+str(len(MUST))+'</div>'),
("""var COACH=[
 {t:0,   s:'Answer in the first sentence. Background: three and a half minutes, then stop.'},
 {t:300, s:'MUST-ASK 1 before your third answer: what did the alignment conversation sound like?'},
 {t:600, s:'He is describing the high school. Listen. One sharp follow-up beats a long answer.'},
 {t:900, s:'Said it yet? 28 regions, 48 high schools, no school took the alternate path. 46%, up six.'},
 {t:1200,s:'Ten minutes left. MUST-ASK 2: the high school, first month, Mott Haven.'},
 {t:1560,s:'Close: the right group of people doing the right work. Next step and timeline.'}
]""","""var COACH=[
 {t:0,   s:'First sentence is the claim. Background: 2:35, skip the kids paragraph, then stop.'},
 {t:300, s:'MUST-ASK 1 by minute 10: which role, and what success looks like at twelve months.'},
 {t:600, s:'Every principal answer ends on proof: Carver, interim at Brooklyn Lab, the 46%.'},
 {t:900, s:'Said it yet? "The principal I was brought in to assess is now the CEO." 46%, up six.'},
 {t:1200,s:'Ten minutes left. One question each: Kruti consistency, Paola the 119.'},
 {t:1560,s:'Close: the right group of people doing the right work. Next step, and who else.'}
]"""),
]
for x,y in R:
    assert x in t,x[:60]; t=t.replace(x,y)

# live coach feed from this Claude session (artifact db doc coach/alert) -> the bottom coach bar
t=t.replace("""function coachPaint(){
  var m=COACH[0];""","""var CO=null;
function coachPaint(){
  if(CO&&Date.now()<CO.until){var nx=document.getElementById('cNowTx');if(nx.textContent!==CO.text)nx.textContent=CO.text;
    document.getElementById('cNow').classList.add('hot');return}
  var m=COACH[0];""")
t=t.replace("showSec('quest'); paint();","""showSec('quest'); paint();
/* live coach: the Claude session writes coach/alert; it takes over RIGHT NOW for 20 seconds */
(function(){var lab=document.querySelector('#cNow .clab'),last=0;
if(!(window.claude&&window.claude.use))return;
window.claude.use('db').then(function(db){if(!db)return;lab.textContent='Right now \\u00b7 coach on';
db.doc('coach/alert').onSnapshot(function(s){if(!s.exists)return;var d=s.data()||{};var at=+d.at||0;
  if(!d.text||(at&&at<=last)||(at&&Date.now()-at>90000))return;last=at;
  CO={text:(d.level?d.level.toUpperCase()+': ':'')+d.text,until:Date.now()+20000};coachPaint()},
 function(){lab.textContent='Right now \\u00b7 coach lost'})}).catch(function(){})})();""")
out='/home/user/Global/Zeta Call Companion 092926.html'
open(out,'w').write(t)
print('wrote',len(t),'bytes;',len(Q),'Q;',len(S),'stories')
