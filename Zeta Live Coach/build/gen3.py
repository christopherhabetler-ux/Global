"""Third pass (092826 night): the condensed 092526 answer bank is retired (CH ruling).
Every card that drew on it is rebuilt from the dictated Notion blocks, the transcripts, the
060925 written Carver account, and the onsite quotes. Also strikes the 'Lean on the team' line."""
import json,re
exec(open('gen2.py').read().split('# ---------- 1 background')[0])   # helpers, NB, TR, BK, T(), c(), cue() ... (loads Q.json)
Q=json.load(open('Q.json')); byid={x['id']:x for x in Q}
def upd(id,**k): byid[id].update(k)
STOP=cue('stop','STOP')
def fix(t):  # spelling only, in his 060925 written answer
    for a,b in [('Collegate','Collegiate'),('succcessful','successful'),('relaitvely','relatively'),('behavior an instruction','behavior and instruction'),
                ('reciving','receiving'),('instaed','instead'),('evidene','evidence'),('becuase','because'),('inconzisteny','inconsistency'),
                ('consistient','consistent'),('punative','punitive'),('interactoins','interactions'),('teaechers','teachers'),('stablize','stabilize'),
                ('reciueved','received'),('Louisana','Louisiana'),('ulimately','ultimately'),('direcness','directness'),('sysstems','systems'),('  ',' ')]:
        t=t.replace(a,b)
    return t
CV=fix(T('I first started working with Jerel Bryant as a consultant.','nothing short of transformational"',BK))
def cv(start,end): i=CV.index(start); return CV[i:CV.index(end,i)+len(end)]
JEREL=cv('Jerel received Louisiana',"CEO of Collegiate Academies")+'.'

# ---------- 3 g2g: end on his own Carver line ----------
g=byid['g2g']['answer']
g=re.sub(r"<em>The best example is Carver.*?</em>","<em>"+JEREL+"</em>",g)
assert JEREL in g
upd('g2g',answer=g.replace('The last line is block 4 of your answer bank.','The last line is your written Carver answer, 060925.'))

# ---------- 4 carver: the 060925 written account ----------
upd('carver',answer=P(
  cue('warm','steady')+' '+bold(cv('I first started working with Jerel Bryant','can he be successful?'),'do we keep this leader, can he be successful?'),
  cv('When I arrived I found teachers','opting out of learning.'),
  cue('slow','slow')+' '+bold(cv('Knowing we had a high potential leader in Jerel','built his confidence to help him stop second guessing himself.'),'shoulder to shoulder'),
  bold(cv('I clearly named','narratives of blame.'),'I clearly named that this frayed relationship needed to be reset'),
  cv('I helped Jerel be the leader of the campus','It worked.')+' '+cv('Students started to feel','safe, predictable and purposeful.'),
  cue('power','land this')+' <b>'+JEREL+'</b> '+STOP)
  +SRC('your written Carver answer, Brooklyn Prospect 060925 (spelling fixed, nothing added). Cut: "decrease suspension by 75% (truly)" (that number is Collegiate network-wide), and the five-year growth line. Written, so say it your way.')
  +'<p class="small prepOnly">If asked for a reference line, his words about you (060925): "The work with Chris Habetler deeply accelerated the trajectory of my school and ultimately the network at large... Chris\'s work was nothing short of transformational."</p>',
  core='"do we keep this leader, can he be successful?"',land='"'+JEREL+'"',
  hook='do we keep this leader? / negative controllers / shoulder to shoulder / reset the frayed relationship / now CEO',
  stop='Stop on "CEO of Collegiate Academies."',
  avoid='The 75% suspension drop at Carver (network-wide only). "Led" Carver: you coached. Naming blame.')

# ---------- 8 scale: his own Jackie ending from the Dan call ----------
s=byid['scale']['answer']
s=re.sub(r"<p><span class=.dcue slow.>slow</span> Earn that.*?</p>", lambda m: "<p>"+ins(ins(c(dan(97,101,end="now has my old job")).rstrip(' …')+'.','Earn that','slow','slow'),"You're going to be part of that evolution",'power','land this')+' '+STOP+"</p>",s,count=1,flags=re.S)
s=re.sub(r'<p class="small">Your words:.*?</p>','<p class="small">Your words: Dan Rojas call 092526, lines 92-101, starting after the KIPP comparison; the "I don\'t care really" sentence is cut.</p>',s)
assert 'Jackie' in s
upd('scale',answer=s,land='"the high school is in the top 3% of all public high schools across the country. And even better, Jackie... now has my old job"',stop='Stop on "now has my old job."')

# ---------- 14 lab: stewardship, the mess, the call ----------
mess=T('A charter renewal is not a project deadline.','do not exist next year.',BK)
two=T('Two simultaneous renewals. A renewal in itself is already a big undertaking.','Now do that twice at the same time.',BK)
need=T('a huge need… right around COVID…','team that really trusted each other.',BK)
dl=c(T("They needed a transition superintendent to help them through renewal as well as recovery.","knots and tangles that existed there."))
dl=dl.replace(' So long story short, I took that on, did that for about a year and a half,',' …')
upd('lab',answer=P(
  cue('flat','set the scene')+' '+dl,
  cue('slow','name the mess')+' '+need,
  cue('beat','the call, out loud only')+' Your note, 083026: "i was the princpal at bk lab for half a year bc i decided to remove the principal and take it over bc it needed to be done."',
  T('I did not spread myself evenly across three schools','fail everything on time.',BK),
  cue('power','why the renewal mattered')+' '+two+' '+mess+' Both were reauthorized. '+STOP)
  +SRC('Dan call 092526; onsite 090826 (1:07:46); your 083026 note; Story Bank 081226; ONE STORY 091326.'),
  core='Frame: stewardship through a mess; he removed the principal and ran the high school himself for half a year.',
  land='"Two simultaneous renewals... Now do that twice at the same time." Both were reauthorized.',
  hook='transition superintendent / knots and tangles / a team that didn\'t trust each other / ran the high school / twice at the same time',
  stop='Stop on "Both were reauthorized."')

# ---------- 16 assocdean: the onsite telling ----------
fr=[x.strip() for x in T('"an Associate Dean of Students who was a wonderful human being','"adopt a fixed mindset about a person."',TR).split(' / ')]
fr=[f.strip('"') for f in fr]
want=['an Associate Dean of Students','he was the guy that everybody loves',"that's what he does really well",'that worked at first','what I didn\'t do is','in years three and four','I learned I had to leave','there\'s a little bit of bumpiness','if I would have started','he was the Dean of Students for many years']
pick=[next(f for f in fr if f.startswith(w)) for w in want]
upd('assocdean',answer=P(
  pick[0]+' … '+pick[1]+' … '+pick[2]+'.',
  pick[3]+' … '+cue('slow','slow')+' <b>'+pick[4]+'</b> … '+pick[5]+'.',
  cue('beat','beat')+' '+pick[6]+'.',
  'Debrief-quoted: "I realized I needed to be crystal clear about what he was good at and what I feel like he needed to develop in." … '+pick[7]+'.',
  pick[8]+'.',
  cue('warm','smile')+' '+pick[9]+'. '+STOP)
  +'<p class="small">Your words: School in the Square onsite 090826, as quoted in THE INTERVIEW REWRITTEN and the DEBRIEF ("kept verbatim" fragments; the raw recording is on your Mac). Joined with "…", nothing added.</p>',
  core='Frame: a fixed mindset about someone he managed, fixed late, with a happy ending.',
  land='"he\'s now co-Dean of Students with one of my former students"',stop='Stop on the co-dean line.')

# ---------- bench: now (AI), whynow, sped ----------
d16=c(T("Right now what I'm doing, which is something I think is really cool","It's flexible."))
upd('now',answer=P(d16, NB[1][7].split('. ',2)[2] if NB[1][7].count('. ')>=2 else NB[1][7], NB[13][3], c(G_AI).split(' Therefore')[0]+' '+STOP)
  +SRC('Dan call 092526; THE TWELVE ANSWERS blocks 1 and 13 as dictated; Zeta screen 091126.'),
  land='Frame: one sentence per tool, then stop. Never pitch the practice to Kruti.')
upd('whynow',answer=P(NB[9][2],c(G_ROLE)+' '+STOP)+SRC('THE TWELVE ANSWERS block 9 as dictated; Zeta screen 091126.'),
  core='Frame: a small team solving problems within arm\'s reach, over the title.',land='"That\'s the happiest I\'ve ever been professionally."')
sp=byid['sped']['answer']
sp=re.sub(r"<p><b>Lean on the team.*?</p>","",sp); sp=sp.replace("; your rubric line (ANSWERED FROM DISK 080626)","")
assert 'Lean on' not in sp
upd('sped',answer=sp,core='Frame: Collegiate built it at true deep levels; Excel, he managed it; Brooklyn Lab, he oversaw it.')

json.dump(Q,open('Q.json','w'))
json.dump({'JEREL':JEREL,'CV':CV},open('cv.json','w'))
print('gen3 ok')

# ---------- his typed answer 092826 ~11pm: would you take this seat ----------
GUT="I want to be part of a great organization, and this is a high impact role that would get me close to schools and close to network decision makers, so it's a great way to get to know the org and the schools and the people."
w=byid['whynow']
w['label']='Why this seat? Would you take it?'
w['short']='Why this seat (your 092826 answer)'
w['keys']=w['keys']+' why this seat would you take level role title step down stepping stone'
w['answer']=P(cue('flat','plain, first sentence')+' <b>'+GUT+'</b>',cue('beat','if they probe the level')+' '+NB[9][2],c(G_ROLE)+' '+STOP)+SRC('your typed answer 092826 (typos fixed, nothing added); THE TWELVE ANSWERS block 9 as dictated; Zeta screen 091126.')+'<p class="small prepOnly"><b>Your guard, 092826:</b> this is not a one-year role, so "get to know" never sounds like a stepping stone. The commute is a slog you have accepted; never raise it. You will want to keep doing your AI work; never raise it on this call. If AI comes up, your line is on the AI card: "short answer, yes to AI... in the service of the roles and responsibilities, not for the sake of doing it."</p>'
w['core']='"'+GUT+'"'
w['land']='"close to schools and close to network decision makers"'
w['avoid']='Anything that sounds like a stepping stone. The commute. Keeping your AI practice going.'
w['hook']='great organization / close to schools, close to decision makers / not a stepping stone'
json.dump(Q,open('Q.json','w'))
z=byid['whyzeta']
parts=z['answer'].split('</p>',2)
z['answer']=parts[0]+'</p>'+parts[1]+'</p><p>'+cue('power','the seat, in your words 092826')+' <b>'+GUT+'</b></p>'+parts[2]
z['answer']=z['answer'].replace("Your words: DREAM screen 081726 (first two paragraphs);","Your words: DREAM screen 081726 (first two paragraphs); your typed answer 092826 (third);")
assert GUT in z['answer']
json.dump(Q,open('Q.json','w'))
