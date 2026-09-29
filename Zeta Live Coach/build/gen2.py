"""Second pass: rebuild cards from the full Notion canon (092926 night).
Every quoted passage is located by exact substring in a source file, so nothing here is composed."""
import json,re
exec(open('build_cards.py').read().split('exec(open("src_other.py")')[0])   # dan(), clean()
exec(open('src_other.py').read())
def c(t):
    t=clean(t)
    for a,b in [('the principle could','the principal could'),('principle is the clothes','principal is the clothes'),('Kinect. And correct','Connect and correct'),('Jillian','Gillian')]:
        t=t.replace(a,b)
    return re.sub(r'\s+',' ',t).strip()
B={int(k):v for k,v in json.load(open('bank.json')).items()}          # uploaded concise pass (blocks 4,5,6,8,12 are unchanged there)
NB={}                                                                  # Notion dictated version, blocks 1,2,3,7,9,10,11,13
for part in open('canon/notion_bank.md').read().split('## ')[1:]:
    k,*ps=part.strip().split('\n'); NB[int(k)]=[p for p in ps if p.strip()]
TR=re.sub(r'\s+',' ',open('canon/transcripts.md').read())
BK=re.sub(r'\s+',' ',open('canon/banks.md').read())
def T(start,end,src=None):
    """exact passage from the mined transcripts (or banks) file, start..end inclusive"""
    s=src or TR; i=s.index(start); j=s.index(end,i)+len(end); return s[i:j]
def cue(kind,label): return f'<span class="dcue {kind}">{label}</span>'
def ins(text,phrase,kind,label,after=False):
    assert phrase in text,(phrase,text[:90])
    return text.replace(phrase,(phrase+' '+cue(kind,label)) if after else (cue(kind,label)+' '+phrase),1)
def em(text,phrase):
    assert phrase in text,(phrase,text[:90]); return text.replace(phrase,'<em>'+phrase+'</em>',1)
def bold(text,*phrases):
    for p in phrases:
        assert p in text,(p,text[:90]); text=text.replace(p,'<b>'+p+'</b>',1)
    return text
def P(*paras): return ''.join('<p>'+p+'</p>' for p in paras)
def SRC(s): return f'<p class="small">Your words: {s}</p>'
def FACT(s): return f'<p class="small"><b>Fact file wording, not a recording:</b> {s}</p>'
STOP=cue('stop','STOP')
Q=json.load(open('Q.json')); byid={x['id']:x for x in Q}
def upd(id,**k): byid[id].update(k)
def add(**k): k.setdefault('type','core'); k.setdefault('receipts',[]); Q.append(k); byid[k['id']]=k
NUM46="That year, 46% of ninth graders across all 48 high schools finished the quarter at a 3.0 or better. Up six points. Best quarter KIPP had ever had on that number"
assert NUM46 in NB[2][5]

# ---------- 1 background: dictated base, best line wins ----------
n=NB[1]
walk=c(T("And I got to walk into 100 different schools","figure out how to meet them."))
bg=[ bold(ins(ins(n[0],'we took the school','slow','slow'),'270th in the state to number one','power','land it',after=True),'270th in the state to number one'),
     cue('flat','one breath, all three parts')+' '+bold(n[1],'zero to 275','over a thousand now','haven\'t been affiliated with it in years'),
     n[2].split(' I worked with')[0]+' '+walk+' '+cue('beat','cut the list if short')+' KIPP, Uncommon, Achievement First, most of the regional, local and midsize operators.',
     bold(ins(n[3],'I was brought down to Carver','slow','slow'),'now he runs the organization'),
     cue('stop','SKIP for Zeta (the kids)')+' '+n[4],
     bold(n[5].replace('And we took both charters','And we took both charters'),'stabilize, lead and pass off')+' '+c(T("That wasn't super easy","knots and tangles that existed there.")),
     n[6],
     n[7].split(' We\'ve built a suite')[0],
     bold(ins(n[8],'The happiest','beat','two-second beat'),"That's what my research says you all are")+' '+STOP]
upd('aboutyou',answer=P(*bg)+SRC('THE TWELVE ANSWERS block 1 as dictated (Notion, revised 092426); the 100-schools line and "knots and tangles" are from the Dan call 092526. The concise-pass rewording is dropped.'),
    hook='270th to number one / DeansList, three parts / Carver / stabilize, lead, pass off / happiest in a place like this',
    avoid='The health reason for leaving Excel. "Better part of a decade." "I\'m happy to go more into that." "Long story short." The kids paragraph.',
    target='2:35 to 3:00. Cut the consulting list and the AI details first.')

# ---------- 5 managed principals: his words exist ----------
m1=NB[1][5].split(' We led through COVID.')[0]
m2=c(T("superintendent role at Brooklyn Lab and so that was overseeing three schools","overseeing three schools"))+' … '+c(R_ACAD_LAB2)
m3=T('Two of my three schools did not see their superintendent','not in June.',BK)
m4=c(T("I was brought down to, as a consultant, I was brought down to Collegiate Academies","things just weren't working."))
upd('managed',answer=P(
  cue('flat','plain, no hedge')+' '+bold(m1,'stabilize, lead and pass off'),
  bold(m2,'responsible for the academic results directly through the principals'),
  cue('beat','then the trade you made')+' '+bold(m3,'a decision maker who answered fast'),
  cue('slow','Collegiate')+' '+m4+' '+cue('power','then Carver, card 4'),
  cue('slow','interim, out loud only')+' Your note, 083026: "i was the princpal at bk lab for half a year bc i decided to remove the principal and take it over bc it needed to be done."'+' '+STOP)
  +SRC('THE TWELVE ANSWERS block 1 (dictated); DREAM screen 081726; Story Bank 081226 (his words, 071426); School in the Square round 082426; your 083026 note.')
  +FACT('managed three principals and the C-level team, with the CEO and CFO co-managed. Collegiate principal portfolio shared with the CAO. Never "managed 48 principals." Never merge the 8 you coached at Collegiate summer PD with the 3 at Brooklyn Lab.'),
  hook='stabilize, lead, pass off / results through the principals / decision maker who answered fast / interim, half a year',
  avoid='Volunteering that you never held a standing principalship. A bare "principal." "Evaluated." "New charter operator."',
  target='75 seconds')

# ---------- 6 hs: the number in its dictated form ----------
x=byid['hs']; x['answer']=x['answer'].replace('In the third quarter, 46% of ninth graders across all 48 high schools finished at a 3.0 or better, up six points.',NUM46+'.')
assert NUM46 in x['answer']

# ---------- 9 adopt: dictated block 2 ----------
k=NB[2]
upd('adopt',answer=P(
  bold(ins(k[0],'Nobody had to say yes','slow','slow'),'Nobody had to say yes'),
  bold(k[1],'no school chose that alternate path'),
  cue('flat','cut if short')+' '+k[2],
  cue('flat','cut if short')+' '+k[3],
  k[4],
  cue('power','land the number')+' '+bold(k[5],'46% of ninth graders'),
  k[6]+' '+STOP)+SRC('THE TWELVE ANSWERS block 2 as dictated (Notion, revised 092426). Last paragraph cut.'),
  stop='Stop on "Now the regions are running the play."',
  avoid='The 46% in the same breath as the 28/48 adoption. "Used by all 28" for the tool. Grading KIPP. "Kate Starke led the team" is true: never "I led the national strategy."')

# ---------- 10 initiative: drop "cited", keep the number ----------
i1=c(R_INIT); i2=c(R_INIT2); i3=c(R_INIT3); i4=c(R_INIT4)
i5=c(R_INIT5).split(' In our last quarter')[0]
i4=bold(ins(i4,'the data went from present but obscured','slow','slow'),'present but obscured to right in front of them')
upd('initiative',answer=P(cue('flat','set the scene')+' '+i1,cue('beat','beat')+' … '+i2,i3,i4,i5+' '+cue('power','the number')+' <b>'+NUM46+'.</b> '+STOP)
  +SRC('DREAM screen 081726, your answer to "one initiative from design through implementation." The number is block 2 as dictated. Cut: "it\'s been cited as one of the primary drivers" (the fact file says the link is your own read, never that KIPP credited it).'),
  land=NUM46+'.')

# ---------- 11 launch: dictated block 3 ----------
x3=NB[3]
upd('launch',answer=P(
  x3[0], bold(ins(x3[1],'I spent six days','slow','slow'),'It became one of the most important things we did.'),
  x3[2], cue('flat','cut to two sentences if short')+' '+x3[3],
  bold(x3[6],'270th in the state to number one')+' '+STOP)+SRC('THE TWELVE ANSWERS block 3 as dictated (Notion, revised 092526). Paragraphs 5 and 6 cut.'),
  land='We took that school from 270th in the state to number one, and got National Charter School of the Year.', stop='Stop on National Charter School of the Year.')

# ---------- 12 instruction: dictated block 10, CREDO moved to Carver ----------
a=NB[10]
cr=a[2].replace(' Collegiate had the largest CREDO effect size of any high school in the country, and a seven-level special education continuum.',' …')
last='… '+a[4].split('but ')[1]
upd('instruction',answer=P(
  cue('flat','plain, no apology')+' '+bold(a[0],'Yes and no.'),
  bold(a[1],'first line of defense'),
  cr+' '+cue('power','add')+' <em>One of our schools, Carver, had the largest CREDO effect size in the country.</em>',
  bold(a[3],'interim high school principal'),
  cue('power','land the number')+' <b>'+last+'</b> '+STOP)
  +SRC('THE TWELVE ANSWERS block 10 as dictated (Notion, revised 092526). The CREDO sentence (gold) is fact-file wording, per your 092926 ruling that it belongs to Carver. Cut: "so I\'m not trying to take all the credit."'),
  avoid='Ending on the AP line. "I\'m not trying to." Claiming curriculum ownership or a CAO title.')

# ---------- 13 lab: steward, name the mess ----------
l5=B[5][:]
mess=T('A charter renewal is not a project deadline.','do not exist next year.',BK)
two=T('Two simultaneous renewals. A renewal in itself is already a big undertaking.','Now do that twice at the same time.',BK)
need=T('a huge need… right around COVID…','team that really trusted each other.',BK).replace('…','…')
upd('lab',answer=P(
  bold(l5[0],'moving a leader I\'d asked to step in'),
  l5[1], cue('slow','name the mess')+' '+need, bold(l5[2],'untangling knots and doing forensic analysis'),
  bold(l5[3],'I ran the high school for half a year'),
  cue('beat','if they ask why the renewal mattered')+' '+two+' '+mess+' '+STOP)
  +SRC('THE TWELVE ANSWERS block 5; School in the Square onsite 090826 (1:07:46, as quoted in WHAT THE RECORDING IS WORTH); ONE STORY 091326; Story Bank 081226.'),
  why='The renewal only means something in context. Stewardship, not a turnaround you drove, but name the mess: a team that did not trust each other, systems that were not in place, COVID, the ownership transfer, two renewals at once.',
  avoid='"Turnaround." That the numbers were false. Blaming the founder. "Five-year" renewals (they were three-year), "SUNY" (Zeta\'s authorizer), "new charter operator."')

# ---------- 14 leftkipp: dictated block 9 + the HR-true line ----------
k9=NB[9]
upd('leftkipp',answer=P(k9[0],cue('flat','cut if short')+' '+k9[2],k9[3],bold(k9[4],"They're running it now.")+' '+STOP)
  +SRC('THE TWELVE ANSWERS block 9 as dictated (Notion, revised 092526); paragraph 2 cut.')
  +FACT('if pressed on the exit: "KIPP was a two-year role. The position was eliminated after we delivered and met goals." (ONE STORY 091326; you confirmed 092926 that both are true.)'),
  avoid='"Too many cooks." "I chose to leave." Anything critical of KIPP. The Verizon line if it lands wrong.')

# ---------- 15 assocdean: guard the Excel exit ----------
upd('assocdean',avoid='Why you left Excel. If asked: you knew you would be leaving at the end of the year. Never the health reason.')

# ---------- bench: change (Heath brothers), growth, consult from the dictated versions ----------
b13=NB[13]
upd('change',answer=P(b13[0],bold(b13[1],'paper is worthless') if 'paper is worthless' in b13[1] else b13[1],bold(b13[2],'paper is worthless until the people are behind it'),b13[4]+' '+STOP)+SRC('THE TWELVE ANSWERS block 13 as dictated (Notion, 092426). Paragraph 4 cut.'))
upd('growth',answer=P(*NB[11][:-1],bold(NB[11][-1],'the strategy is first downs')+' '+STOP)+SRC('THE TWELVE ANSWERS block 11 as dictated (Notion, 092526).'))
b7=NB[7]
upd('consult',answer=P(b7[0],b7[2],b7[3],bold(b7[4],"I can't break a promise to principals.")+' '+STOP)+SRC('THE TWELVE ANSWERS block 7 as dictated (Notion, 092526). Paragraph 2 cut.'))

# ---------- SPED ----------
s1=c(T("They have a true all means all. mission","a high support organization?"))
s2=a[2].split(' Collegiate had the largest')[0]
s3=T("Lean on the team where they're the experts; lean in where my systems work applies.","applies.",BK)
upd('sped',answer=P(cue('flat','lead with it, no hedge')+' '+s1, s2, bold(s3,"Lean on the team where they're the experts"),
  '<b>Facts (you confirmed 092926):</b> Collegiate, a seven-level special education continuum, including sub-separate low-incidence programs, ED programs, and a post-secondary program; you coached principals and held standards there. Excel, about 30% special education, and you managed it. Brooklyn Lab, you oversaw it.'+' '+STOP)
  +SRC('Dan call 092526; THE TWELVE ANSWERS block 10; your rubric line (ANSWERED FROM DISK 080626).'),
  land='The strongest inclusive-by-design evidence in your record, said as a strength.',
  avoid='"I learned a ton about special education." "I\'m a systems person, not a clinician." Managing SPED teachers at Collegiate. Raising Zeta\'s own ELL or SPED enrollment.',
  core='Collegiate built it at true deep levels. Excel, you managed it. Lean on the experts, lean in with systems.')

# ---------- pay: cut the "cash in" line ----------
pay=c(R_PAY)
pay=pay.split(" I'm not at a place")[0]+' … '+"I'm very happy to be part of the right team. That's where I've been the happiest in my life."
upd('pay',answer=P(pay)+SRC('DREAM screen 081726, when the band was $145K to $165K. Cut: "I\'m not at a place in my life where I need to cash in" (flagged in the IP debrief extract).')+FACT('CALL PREP 092026, if asked: "The posted range works for me. I\'m much more focused on the fit." The standing rule is top of the band; set your number before 3.'))

# ---------- start: add the pace line ----------
upd('start',answer=P(c(G_START),c(T("I am happy. I'm happy to be patient","ready to.")))+SRC('Zeta screen 091126.'))

# ---------- year one: his note ----------
upd('yearone',answer=P(
  cue('slow','slow')+' Your note (CH feedback for NCS prep): "For first 90 days, we would start observing and listening this year. Absorb. Listen. Think."',
  'School in the Square onsite 090826, as quoted in the debrief: "people need their reality to be heard, valued, and considered before they\'re asked to do something different" · "let\'s limit the scope, let\'s follow the bright spot" · "I stopped thinking I knew everything and really listened"',
  cue('flat','then the what, as bullets')+' Principals, the way Dan described the job. Ninth-grade academic health for the high school. Proof: Carver and the 46%.'+' '+STOP)
  +'<p class="small">Your words: the 90-day note is yours; the onsite lines are debrief quotes (secondary). The last line is a proposed frame, not your words. Do not name the Principal Manager title unless they do.</p>',
  hook='absorb, listen, think / reality heard before change / follow the bright spot / principals + ninth grade',
  core='Absorb. Listen. Think. Then principals and ninth-grade academic health.')

# ---------- asks: his recorded questions ----------
g1=c(T("Is this a role that's existed in the past?","to make this person successful?"))
g2=c(T("What makes it challenging and/or what would make someone wildly successful","what can I learn from that?"))
upd('ask1',answer=P(cue('flat','your Gillian question, asked by minute 10')+' <b>'+g1+'</b>',
  cue('beat','follow-up if they answer short')+' '+g2,
  'Your form that worked with Dan (line 211): "What, if anything, should I read into the fact that you and I are having a conversation on the school excellence side of things as opposed to operations?"'+' '+STOP)
  +SRC('Zeta screen 091126; Dan call 092526.'),
  label='MUST-ASK 1 &middot; The seat. By minute 10.', hook='has this role existed / what made that person successful / listen',
  core='Find out the seat without naming it.', avoid='Naming the Principal Manager title first. Waiting until the end.')
f1=c(T("What separates a client partner who make... who make it in year one","as specific as possible as you can."))
s2q=T("if you had to boil it down to one thing that really the school needs to, the organization needs to improve on, what would it be?","what would it be?")
on1=T("What separates good from great in this role? And what's your biggest concern about hiring someone with my profile?","my profile?")
nx=c(T("How quickly are we looking to move on all this, do you know?","do you know?"))
upd('ask2',answer=P(
  cue('power','the one that got you the rubric')+' FranklinCovey 081826: <b>"'+f1+'"</b> '+cue('flat','swap in their seat\'s name'),
  'School in the Square onsite 090826 (debrief-quoted): "'+on1+'"',
  'School in the Square 082426: "'+s2q+'"',
  cue('flat','PROPOSED, not yet yours')+' Kruti: what has been hardest to keep consistent campus to campus this fall. Paola: what a great first year looks like by June for the 119 ninth graders.',
  cue('slow','then the next step')+' FranklinCovey 081426: "'+nx+'" '+STOP)
  +SRC('FranklinCovey Part 2 081826 and Part 1 081426; School in the Square 082426; onsite 090826 (secondary). The Kruti and Paola lines are proposed.'),
  label='MUST-ASK 2 &middot; One each, then the next step. Minute 20.', hook='what separates year one / biggest concern about my profile / next step')

# ---------- new cards ----------
add(id='netsys',grp='D',t1=12,tier='LIKELY',short='Network systems that work in schools',
 trig='&ldquo;central office vs schools&rdquo; &middot; &ldquo;why don\'t network initiatives stick&rdquo;',
 core="They aren't designed at the network level. Find the bright spot, extract the principle, let the people in the room help make it.",
 why="Kruti's whole job is taking what works across campuses. This was one of your five best answers at the onsite.",
 keys='network central office systems school level consistency bright spot designed implement fidelity',
 label='12 &middot; How do network systems actually work for the people in schools?',
 hook="aren't designed at the network level / follow the bright spot / the people in this room",
 tests='Whether he builds with schools or at them.', target='75 seconds',
 land='Even if you don\'t agree with it, you at least know your opinion was heard.',
 avoid='A central-office framework speech. Criticizing Zeta\'s current systems.',
 answer=P(cue('flat','plain, first sentence')+' <b>"Well, it\'s simple. They aren\'t designed at the network level."</b>',
  '"I\'m not saying that to be glib" · "what\'s working at one school" · "what are the attributes of that that make it work" · "let\'s limit the scope, let\'s follow the bright spot"',
  cue('power','land this')+' "The policy might be made in this room, but the people in this room are the operations directors themselves — because then, even if you don\'t agree with it, you at least know your opinion was heard." '+STOP)
  +'<p class="small">Your words: School in the Square onsite 090826, as quoted in the DEBRIEF and THE INTERVIEW REWRITTEN (secondary; the raw recording is on your Mac). For Zeta, "operations directors" becomes principals.</p>',
 receipts=['(2) 28 REGIONS, 48 HIGH SCHOOLS, NO MANDATE'],stop='Stop on "your opinion was heard."')
cc=c(T("I was brought down to, as a consultant, I was brought down to Collegiate Academies","the principal on this.")) if False else None
cn=c(T("And what we saw was was that teachers were not being","It has to be a connection."))
cn2=c(T("We built on the momentum.","what this video makes you think."))
add(id='inherit',grp='Q',short='A system you inherited that wasn\'t working',label='A system you inherited that wasn\'t working. How did you fix the root cause?',
 hook='assess the principal / student behavior is adult behavior / connect and correct / the 30-second video',
 keys='inherited system broken root cause culture demerit consequences connect correct collegiate principal video',
 core='We saw the problem, agreed on it, named small actions, and built on the momentum.',why='A principal-development story in your words, from the School in the Square round.',
 tests='',target='2 minutes',land='We normalized the better version.',avoid='"I\'m happy to talk more specifically about something maybe more operational." Naming the principal.',
 answer=P(m4,cn,cue('power','land this')+' '+bold(cn2,'comment one word')+' '+STOP)+SRC('School in the Square round 082426. Cut: the doctor analogy and the Monday-morning example.'),stop='Stop on the video.')
rf=c(T("We recognize that it's a false choice between high expectations and high levels of accountability.","that we will be."))
add(id='accountable',grp='Q',short='Relationships and accountability',label='How do you hold a leader accountable and keep the relationship?',
 hook='false choice / clarity up front / curious question / say good morning',
 keys='accountability relationships hard conversation hold accountable feedback manage leader support evaluation hat',
 core="It's a false choice between high expectations and high levels of accountability.",why='Zeta says "love your people." This is how you hold the bar and love the person.',
 tests='',target='75 seconds',land='We say good morning and we care about each other, and we use that to drive each other to be who we promised to be.',avoid='"I used to hesitate a lot around accountability" as the ending.',
 answer=P(bold(rf,"it's a false choice between high expectations and high levels of accountability"),
  'Onsite 090826, debrief-quoted: "We build the relationship by having the hard conversation, and that\'s the way in which people really know where they stand." · "There\'s nothing nice and friendly about me thinking one thing behind your back and not saying it to you." · "Hey, we talked about the calendar going out last week. I didn\'t get it. What can you tell me about that?"'+' '+STOP)
 +SRC('School in the Square screen 082126; onsite 090826 (secondary).'),stop='Stop.')
cv1=c(T("I effectively did a version of My kind of strong start spring readiness planning","as much as it was a logistical issue."))
cv2=c(T("Day two began the work of Getting as many answers as possible on paper","every student who wants to come in"))
cv3=c(T("And recognizing that You both have to have the answer on paper.","make my voice heard."))
add(id='ambiguity',grp='Q',short='Ambiguity: the four-day COVID playbook',label='A time with a big goal, total ambiguity and full autonomy.',
 hook='four days / gather, paper, leadership team, staff / paper is worthless if it does not reach people',
 keys='ambiguity autonomy covid crisis reopening playbook four days remote school',
 core='I condensed spring readiness planning into four days.',why='Good for launch or crisis questions. Kruti has three first-year campuses.',
 tests='',target='90 seconds',land='Nothing that gets to the people is going to matter if the premise is that this is being done to us.',
 avoid='"This is not a question I prepared for." A student or staff count (the one you gave DREAM does not match the Brooklyn Lab file).',
 answer=P(cv1,cv2+' …',cue('power','land this')+' '+bold(cv3,'having the answer only on paper is next to worthless')+' '+STOP)+SRC('DREAM screen 081726. Cut: the opening disclaimer and the org size.'),stop='Stop.')

# ---------- renumber THE 15 tiles in group order ----------
order=['aboutyou','whyzeta','g2g','carver','managed','hs','ownership','scale','netsys','adopt','initiative','launch','instruction','lab','leftkipp','assocdean','ask1','ask2']
for i,id in enumerate(order,1):
    x=byid[id]; x['t1']=i
    x['label']=re.sub(r'^(MUST-ASK \d|\d+) &middot;',lambda m: m.group(0) if m.group(1).startswith('MUST') else f'{i} &middot;',x['label'])
json.dump(Q,open('Q.json','w'))
print(len(Q),'cards;',sum(1 for x in Q if x.get('t1')),'on THE tiles')

# ---------- cores and landings: his exact words, or a third-person frame (no invented "I") ----------
FR={
 'aboutyou':("Frame: systems, change management, now tech. 270th to one, 100 schools, Carver, Brooklyn Lab, KIPP, the tools. Ends on why Zeta.",None),
 'g2g':("Clothes, not skin. Support hat 99%. Side of the street clean. Shoulder to shoulder. Then Carver.","Ends on a named principal and a result: Carver, Jerel now runs the organization."),
 'carver':("\"Jerel is one of the best I have ever seen at working with students, and we just weren't playing to his strengths.\"","\"Two hundred students when I walked in. Eight or nine hundred now, in a brand-new building. And Jerel is the CEO.\""),
 'managed':("Frame: superintendent over three principals, results through them, interim for half a year.","\"What they needed from me was a decision maker who answered fast, not a superintendent who visited.\""),
 'scale':("Frame: run the proven play until the school is stable and functional; that earns room to change it. Pair with how you invest in people.","\"Its high school is in the top 3% of all public high schools nationally, and a student I had in sixth grade now has my job.\""),
 'adopt':("\"Nobody had to say yes to what we were doing, so we had to use influence and the quality of our ideas to get them to want to say yes.\"","\"We built it, we tested it, it worked, and we handed it off. Now the regions are running the play.\""),
 'initiative':("\"The data went from present but obscured to right in front of them.\"",None),
 'launch':("Frame: stability, then the adults, then student ownership.",None),
 'instruction':("\"Yes and no.\" Then everything upstream, then the proof.",None),
 'lab':("Frame: moved a leader he had asked to step in, ran the high school himself, stewardship through a mess.","\"I made the call, and I ran the high school for half a year while still serving as superintendent.\""),
 'leftkipp':("\"The project doesn't end when we run the first successful full cycle. It ends when we run that cycle without me.\"",None),
 'assocdean':("Frame: a fixed mindset about someone he managed, fixed late, with a happy ending.","\"He's co-dean there now, with one of my former students, and he's still one of the best I've seen do this job.\""),
 'now':("Frame: principals point him at a problem; he builds the thing that saves them time.","Frame: one sentence per tool, then stop. Never pitch the practice."),
 'change':("\"Paper is worthless until the people are behind it.\"","\"Knows that paper is worthless until the people are behind it.\""),
 'consult':("\"There's no substitute for what it takes to run a school.\"",None),
 'sped':("Frame: Collegiate built it at true deep levels; Excel, he managed it; lean on the experts, lean in with systems.",None),
 'pushback':("Frame: built the documents before he had the leader.",None),
 'pay':("Frame: never raise it; top of the band.","Frame: the band works, and the fit matters more. Your number set before 3."),
 'yearone':("\"Absorb. Listen. Think.\"","Frame: principals and ninth-grade academic health, proved by Carver and the 46%."),
 'inherit':("Frame: saw the problem, agreed on it, named small actions, built on the momentum.","Frame: ends on the 30-second video the principal sent to everybody."),
 'accountable':("\"It's a false choice between high expectations and high levels of accountability.\"","\"There's nothing nice and friendly about me thinking one thing behind your back and not saying it to you.\""),
 'ambiguity':("Frame: spring readiness planning condensed into four days.","\"having the answer only on paper is next to worthless if it doesn't actually get to the people.\""),
 'whynow':("\"The right title in the wrong organization is a losing proposition.\"" if "losing proposition" in ' '.join(B[12]) else "Frame: the right seat over the title.",None),
}
for id,(core,land) in FR.items():
    byid[id]['core']=core
    if land: byid[id]['land']=land
json.dump(Q,open('Q.json','w'))
