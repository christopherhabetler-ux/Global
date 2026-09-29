import json,re,html
exec(open('build_cards.py').read().split('exec(open("src_other.py")')[0])   # dan(), clean()
exec(open('src_other.py').read())
def c(t): return clean(t)
B={int(k):v for k,v in json.load(open('bank.json')).items()}
def esc(s): return s.replace('`','\\`').replace('${','\\${')
def cue(kind,label): return f'<span class="dcue {kind}">{label}</span>'
def ins(text,phrase,kind,label,after=False):
    assert phrase in text,(phrase,text[:80])
    return text.replace(phrase,(phrase+' '+cue(kind,label)) if after else (cue(kind,label)+' '+phrase),1)
def em(text,phrase):
    assert phrase in text,(phrase,text[:80]); return text.replace(phrase,'<em>'+phrase+'</em>',1)
def P(*paras): return ''.join('<p>'+p+'</p>' for p in paras)
def SRC(s): return f'<p class="small">Your words: {s}</p>'
Q=[]
def q(**k): Q.append(k)

# ---------- A. THE OPENER ----------
b=B[1][:]
b[1]=em(ins(b[1],'we took the school','slow','slow, land the number'),'270th in the state to number one')
b[2]=ins(b[2],'I had the privilege','flat','plain')
b[3]=ins(b[3],'Then I found a client','beat','beat')
b[4]=cue('stop','SKIP this paragraph for Zeta (the kids)')+' '+b[4]
b[5]=ins(b[5],'We stabilized','flat','keep it moving, no weight on the renewal')
b[8]=ins(ins(b[8],'The happiest','beat','two-second beat'),"That's what my research says",'power','land this')+' '+cue('stop','STOP')
b[3]=b[3]+' '+cue('power','add the result')+' <em>'+B[4][0]+'</em>'
q(id='aboutyou',grp='A',t1=1,tier='LOCK',type='core',short='Background walk',
 trig='&ldquo;tell me about yourself&rdquo; &middot; &ldquo;walk me through your background&rdquo;',
 core="Systems in schools, change management, now tech. Turnaround, 100 schools, Collegiate, Brooklyn Lab, KIPP, the tools. The happiest I've been is a place like this.",
 why="Paola and Kruti haven't heard it. Dan got about 6 minutes; the bank version is about 2:35.",
 keys='background about yourself walk me through career history story arc resume',
 label='1 &middot; Walk me through your background.',
 hook="270th to number one / 100 schools, 14 years / Carver → CEO / happiest in a place like this",
 tests='Whether the arc reads as schools, and lands inside three minutes.',
 target='2:35. If short on time, Brooklyn Lab drops to its last sentence.',
 land="He hears a school person, and the last line points at Zeta.",
 avoid="The health reason for leaving Excel. \"Better part of a decade\" (it was 14 years). \"We were able to be successful in that.\"",
 answer=P(*b)+SRC('THE TWELVE ANSWERS, block 1 (your dictation, revised 092426). The Carver line in gold is from block 4.'),
 receipts=['(1) 270TH TO NUMBER ONE','(4) CARVER','(5) BROOKLYN LAB'],
 stop='Stop at "that\'s what brought me here." Then the role question, if they pause.')

w1=c(R_WHY1); w2=c(R_WHY2)
d54=dan(54,54,start='the happiest'); d225=dan(225,227,start="excellence with exploration",end="Let's attack people's ideas without attacking people.")
q(id='whyzeta',grp='A',t1=2,tier='LOCK',type='core',short='Why Zeta, why this side',
 trig='&ldquo;why Zeta&rdquo; &middot; &ldquo;why this role&rdquo; &middot; &ldquo;why schooling, not ops&rdquo;',
 core='Building things other people can run. A midsize network with outsized ambition. Excellence with exploration.',
 why='The ops seat is closed. This has to be a clear yes to the schooling side.',
 keys='why zeta why us why this role why now schooling side ops operations transformation felipe',
 label='2 &middot; Why Zeta? Why this side of the house?',
 hook='building things other people can run / excellence with exploration / best idea wins',
 tests='Whether he wants this seat, or the ops seat he applied for.',
 target='75 seconds',
 land='He wants this work, at this network, now.',
 avoid='Any sign you would rather have the Operations Transformation seat. Title, level or money.',
 answer=P(cue('flat','plain, easy')+' '+ins(w1,"building things that other people can run",'slow','slow'),
          w2,
          cue('beat','beat')+' '+d54,
          cue('warm','warm')+' '+d225+' '+cue('stop','STOP'))+
        SRC('DREAM screen 081726 (first two paragraphs); Dan Rojas call 092526, lines 54 and 225-227.'),
 receipts=[],
 stop='If they ask about ops: Felipe thought your strongest fit was the schooling side, and after the Dan call you see the logic.')

# ---------- B. PRINCIPALS (Paola) ----------
g=dan(60,71)
g=ins(g,"we have to separate someone's performance",'slow','slow')
g=em(g,"the clothes that you wear, not the skin that you're in")
g=ins(g,'99% of the time','power','land this')
g=ins(g,'Mandate authority is almost worthless','beat','beat')
q(id='g2g',grp='B',t1=3,tier='LOCK',type='core',short='Good principal → great',
 trig='&ldquo;how do you manage principals&rdquo; &middot; &ldquo;good to great&rdquo; &middot; &ldquo;feedback to a principal&rdquo;',
 core="Clothes, not skin. Support hat 99%. My side of the street clean. Shoulder to shoulder. Then Carver.",
 why="Paola manages Zeta's principals. Dan asked this exact question and the answer ended with no proof.",
 keys='principal manage feedback good to great coaching develop protective support evaluation',
 label="3 &middot; The good principal who needs to get to great. What's your common feedback?",
 hook='clothes, not skin / support hat 99% / end on Carver',
 tests='Whether he can manage strong, protective principals without mandating.',
 target='2 minutes',
 land='A named principal and a result: Carver, Louisiana Principal of the Year, now CEO.',
 avoid='Ending on "completely let go of any hierarchical sense of mandate authority." Four principles and no proof (what happened with Dan).',
 answer=P(g+' '+cue('power','then the proof')+' <em>The best example is Carver, and the principal I was brought in to assess is now the CEO.</em> '+cue('stop','STOP'))+SRC('Dan Rojas call 092526, lines 60-72. The last line is block 4 of your answer bank.'),
 receipts=['(4) CARVER'],stop='Carver in one line, then stop.')

c4=B[4][:]
c4[0]=ins(c4[0],'The best example','warm','steady')
c4[2]=ins(c4[2],"Jerel is one of the best",'slow','slow')
c4[4]=ins(c4[4],'connect and correct','power','land this')
c4[6]=em(ins(c4[6],'Two hundred students','slow','slow'),'Jerel is the CEO')+' '+cue('stop','STOP')
q(id='carver',grp='B',t1=4,tier='LOCK',type='core',short='Carver, the whole story',
 trig='&ldquo;a principal who was struggling&rdquo; &middot; &ldquo;hard feedback&rdquo; &middot; &ldquo;developing a leader&rdquo;',
 core='The problem is not the man. We were managing him against his strengths. Jerel is the CEO.',
 why='Your best proof for a principal-manager seat. With Dan it came out as "we were able to be successful in that."',
 keys='carver struggling principal underwater hard feedback develop leader coach jerel ben marcovitz collegiate',
 label='4 &middot; Tell me about a principal who was struggling. What did you do?',
 hook='brought in to assess / Mom and Dad get right / connect and correct / Jerel is the CEO',
 tests='Whether he can diagnose, tell a hard truth, and grow a leader instead of replacing him.',
 target='90 seconds',
 land='Two hundred students to eight or nine hundred. Jerel is the CEO.',
 avoid='The 75% suspension drop (network-wide, never Carver alone). Naming blame.',
 answer=P(*c4)+SRC('THE TWELVE ANSWERS, block 4 (your dictation).'),
 receipts=['(4) CARVER'],stop='Stop on "Jerel is the CEO."')

q(id='managed',grp='B',t1=5,tier='LIKELY',type='core',short='Have you managed principals?',
 trig='&ldquo;have you managed principals&rdquo; &middot; &ldquo;you\'ve never been a principal&rdquo;',
 core='Two seats managing principals, and I held a building myself for six months.',
 why='The seat is likely Principal Manager. Your fact file has a ruling on exactly how to say this.',
 keys='managed principals portfolio principal experience interim never been a principal evaluated',
 label='5 &middot; Have you managed principals? Have you been a principal?',
 hook='Collegiate portfolio / three at Brooklyn Lab / interim, half a year, my call',
 tests='Whether he has done the seat, not just coached near it.',
 target='45 seconds',
 land='Managing principals is the seat itself, twice.',
 avoid='Volunteering that you have not held a standing principal seat. A bare "principal" without "interim."',
 answer=P(cue('flat','plain, no hedge')+' No recorded answer in your words yet. Say these facts your way:',
  '<em>Collegiate:</em> a portfolio of principals as Chief Culture Officer, shared with the CAO. About a hundred site visits a year on structured observation and debrief.',
  '<em>Brooklyn Lab:</em> managed and evaluated three principals and the C-level team as superintendent.',
  cue('slow','slow')+' <em>Brooklyn Lab, interim:</em> your words, 083026: "i was the princpal at bk lab for half a year bc i decided to remove the principal and take it over bc it needed to be done." (Say it out loud if it fits; never in writing.)')+SRC('verified-facts rulings L1254, L230, L484 and L1242-1250, via PRINCIPAL MANAGER TRACK 092026.'),
 receipts=['(5) BROOKLYN LAB'],stop='Stop after the interim line.')

# ---------- C. THE HIGH SCHOOL ----------
h=dan(118,126,start='high school can')
h=ins(h,"high school can't be like middle school",'power','lead with this')
h=ins(h,"we had a spine",'slow','slow')
h2=dan(127,135); h3=dan(136,139)
h3=ins(h3,'what are the 50','beat','beat')
q(id='hs',grp='C',t1=6,tier='LOCK',type='core',short='What high school should be',
 trig='&ldquo;the high school&rdquo; &middot; &ldquo;what would you rethink&rdquo; &middot; &ldquo;college admissions&rdquo;',
 core="Not middle school with a couple of dials turned. Same spine, dressed entirely different. 50/25/25.",
 why="Dan's biggest problem, and it rolls up to Paola. Dan said \"I love that idea.\"",
 keys='high school rethink ninth grade college admissions gradual release seating chart 50 25 identity',
 label='6 &middot; What should high school be? What needs a structural rethink?',
 hook='not middle school with the dials turned / same spine, dressed different / 50-25-25',
 tests='Whether he has a real point of view on the high school they just opened.',
 target='2 minutes. The seating-chart paragraph is the one to cut.',
 land='Lives of unlimited opportunity, and what a ninth grader needs to do to get there. Then the 46%.',
 avoid='Opening with "I wish I had the answer" (what happened with Dan).',
 answer=P(h,cue('flat','cut if short')+' '+h2,h3+' '+cue('power','then the number')+' <em>In the third quarter, 46% of ninth graders across all 48 high schools finished at a 3.0 or better, up six points.</em> '+cue('stop','STOP'))+SRC('Dan Rojas call 092526, lines 118-139. The number is from block 10 of your answer bank.'),
 receipts=['(3) ACADEMIC HEALTH, 46%'],stop='The 46%, then stop.')

cu=dan(143,159)
cu=ins(cu,"It's not fun because it's fun",'slow','slow')
cu=ins(cu,'we always talk about student ownership','beat','beat')
cu=ins(cu,'as adults, be saying a whole lot less','power','land this')
q(id='ownership',grp='C',t1=7,tier='LIKELY',type='core',short='Culture and student ownership',
 trig='&ldquo;beyond systems&rdquo; &middot; &ldquo;culture&rdquo; &middot; &ldquo;student voice&rdquo;',
 core="Cool to be smart. Ownership that isn't thin and surfacey. It's my school.",
 why="Dan's follow-up. For Paola it shows culture as academic identity.",
 keys='culture student ownership honor council orientation leaders identity belonging events',
 label='7 &middot; Beyond systems, what would you change about high school?',
 hook="cool to be smart / not thin and surfacey / it's my school",
 tests='Whether culture means more than discipline to him.',
 target='90 seconds',
 land='As adults, we would be saying a whole lot less and helping our students say a whole lot more.',
 avoid='Running past two minutes.',
 answer=P(cu+' '+cue('stop','STOP'))+SRC('Dan Rojas call 092526, lines 143-159.'),
 receipts=[],stop='Stop on "say a whole lot more."')

# ---------- D. SCALING (Kruti) ----------
s=dan(92,96,start='Now, in contrast that with Excel',end='lives of unlimited opportunities.')
s2=dan(97,100,end='starting from a solid foundation of what we know that works.')+' '+B[3][4].split('nationally, ')[0].split('. ')[-1]+'nationally, '+B[3][4].split('nationally, ')[1]
s2=ins(s2,'Earn that','slow','slow')
s2=ins(s2,"You're going to be part of that evolution",'power','land this')
q(id='scale',grp='D',t1=8,tier='LOCK',type='core',short='Earn it: when to scale, playbook vs autonomy',
 trig='&ldquo;playbook or autonomy&rdquo; &middot; &ldquo;why do networks plateau&rdquo; &middot; &ldquo;when is it ready to scale&rdquo;',
 core='We were clear on who we were. A new principal runs the proven play until the school is stable and functional; then they have earned room to change it.',
 why="Kruti's job is scaling what works. \"Earn it\" means: autonomy is earned by first getting the school stable and functional on the proven playbook.",
 keys='scale scaling playbook autonomy fidelity new principal earn it plateau network kipp excel replicate',
 label='8 &middot; When is a practice ready to scale? Playbook or principal autonomy?',
 hook='clear on who we were / earn it: stable, functional, then innovate / you are part of the evolution',
 tests='Fidelity versus autonomy, and whether he respects principals.',
 target='90 seconds',
 land='The high school is in the top 3% of all public high schools across the country. Jackie now has my old job.',
 avoid='"I don\'t care really if you as a first-year principal..." (it came right before "earn that" with Dan). The KIPP half of the comparison.',
 answer=P(s,s2+' '+cue('stop','STOP'))+SRC('Dan Rojas call 092526, lines 92-100, starting after the KIPP comparison; the "I don\'t care really" sentence is cut. The last sentence is block 3 of your answer bank (sixth grade, per your 091426 ruling), in place of the "fifth, sixth, and seventh" version you gave Dan.'),
 receipts=['(1) 270TH TO NUMBER ONE'],stop='Stop on "now has my job." Then, if there is room, pair it with how you invest in people: Carver.')

k2=B[2][:]
k2[1]=ins(k2[1],'Nobody had to say yes','slow','slow')
k2[6]=em(ins(k2[6],'46% of ninth graders','power','land the number'),'46% of ninth graders across all 48 high schools finished at a 3.0 or better')
k2[7]=k2[7]+' '+cue('stop','STOP')
q(id='adopt',grp='D',t1=9,tier='LOCK',type='core',short='Adoption without authority (KIPP)',
 trig='&ldquo;adoption&rdquo; &middot; &ldquo;influence without authority&rdquo; &middot; &ldquo;across autonomous schools&rdquo;',
 core='Nobody had to say yes, so we had to get them to want to say yes. Aligned on the problem, made the pilot a success, stayed in the implementation.',
 why='Zeta is growing fast; Kruti needs adoption without force.',
 keys='adoption influence authority mandate kipp regions pilot champions buy in 28 48 alternate path',
 label='9 &middot; How do you get schools to adopt something they don\'t have to?',
 hook='no mandate / problem, pilot, implementation / 46% up six / no school took the alternate path',
 tests='Whether he can scale without positional power.',
 target='2 minutes',
 land='All 28 regions and all 48 high schools adopted the strategy. No school chose the alternate path.',
 avoid='"Used by all 28" for the tool (it was piloted and handed off). Criticizing KIPP.',
 answer=P(*k2)+SRC('THE TWELVE ANSWERS, block 2 (your dictation, rebuilt 092526).'),
 receipts=['(2) 28 REGIONS, 48 HIGH SCHOOLS, NO MANDATE','(3) ACADEMIC HEALTH, 46%'],stop='Stop on "That\'s the exact type of work I love doing."')

i1=c(R_INIT); i2=c(R_INIT2); i3=c(R_INIT3); i4=c(R_INIT4); i5=c(R_INIT5)
i4=em(ins(i4,'the data went from present but obscured','slow','slow'),'present but obscured to right in front of them')
q(id='initiative',grp='D',t1=10,tier='LIKELY',type='core',short='An initiative, design to scale',
 trig='&ldquo;an initiative you led across schools&rdquo; &middot; &ldquo;pilot to scale&rdquo;',
 core='The data was there and nobody could use it. One button, a report per teacher. Present but obscured, to right in front of them.',
 why="Kruti's job is taking what works to scale. This is your pilot-to-network story.",
 keys='initiative pilot design implementation data academic health reports teacher student gpa weekly',
 label='10 &middot; An initiative you led from design through implementation across schools.',
 hook='data nobody could use / one button, a report per teacher / present but obscured',
 tests='Whether he can take a pilot to scale.',
 target='2 minutes',
 land='Cited as one of the primary drivers that got the right folks focused on the right conversation and the right actions.',
 avoid='Leading with the tool. Forgetting the book mid-story (last time).',
 answer=P(cue('flat','set the scene')+' '+i1,cue('beat','beat')+' … '+i2,i3,i4,i5+' '+cue('power','the number')+' <em>In the third quarter, 46% of ninth graders across all 48 high schools finished at a 3.0 or better, up six points.</em> '+cue('stop','STOP'))+SRC('DREAM screen 081726, your answer to "one initiative from design through implementation." The number is from block 2.'),
 receipts=['(3) ACADEMIC HEALTH, 46%'],stop='The number, then stop.')

x3=B[3][:]
x3[1]=ins(x3[1],'I spent six days','slow','slow')
x3[1]=ins(x3[1],'It became one of the most important things we did.','power','land this')
x3[4]=x3[4]+' '+cue('stop','STOP')
q(id='launch',grp='D',t1=11,tier='LIKELY',type='core',short='Launching a school: three phases',
 trig='&ldquo;launching a new school&rdquo; &middot; &ldquo;first-year principal&rdquo; &middot; &ldquo;turnaround&rdquo;',
 core='Stability, then the adults, then student ownership. Six days writing the playbook.',
 why='Zeta has Flushing, Tremont Park and the high school all in year one.',
 keys='launch new school first year principal turnaround excel phases playbook six days stability',
 label='11 &middot; How do you launch a new school or onboard a first-year principal?',
 hook='stability / the adults / student ownership / six days on the playbook',
 tests='Whether he knows what a first year needs.',
 target='2 minutes',
 land='Excel is now in the top 3% of all public high schools nationally.',
 avoid='Running all three phases at full length if time is short.',
 answer=P(*x3)+SRC('THE TWELVE ANSWERS, block 3 (your dictation, revised 092526).'),
 receipts=['(1) 270TH TO NUMBER ONE'],stop='Stop on the top 3%.')

# ---------- E. THE HARD ONES ----------
a10=B[10][:]
a10[0]=ins(a10[0],"Yes and no.",'flat','plain, no apology')
a10[5]=em(ins(a10[5],'46% of ninth graders','power','land the number'),'Best quarter KIPP had ever had on that number')+' '+cue('stop','STOP')
q(id='instruction',grp='E',t1=12,tier='LOCK',type='curve',short='Systems and culture, not academics?',
 trig='&ldquo;you\'re a systems and culture person&rdquo; &middot; &ldquo;instructional leadership&rdquo;',
 core="Yes and no. I've spent my career on the part that decides whether instruction works.",
 why='DREAM asked this twice. It is the likeliest doubt about you for a schooling seat.',
 keys='instruction academic curriculum rigor systems culture never led instruction learning curve',
 label="12 &middot; You're known for systems and culture. Why trust you with academics?",
 hook='yes and no / culture is a means to an end / the four I spike in / 46%',
 tests='Whether a culture guy can manage instructional leaders.',
 target='2 minutes',
 land='Best quarter KIPP had ever had on that number.',
 avoid='Ending on the gap.',
 answer=P(*a10)+SRC('THE TWELVE ANSWERS, block 10 (your dictation, revised 092526). Your DREAM version of the same answer is in Story (9).'),
 receipts=['(3) ACADEMIC HEALTH, 46%','(9) THE DREAM VERSION'],stop='Stop on the 46%.')

l5=B[5][:]
l5[1]=ins(l5[1],'the original high school principal left','flat','plain')
l5[3]=em(ins(l5[3],'I made the call','slow','slow'),'both were reauthorized')+' '+cue('stop','STOP')
q(id='lab',grp='E',t1=13,tier='LIKELY',type='core',short='Brooklyn Lab: the hard call',
 trig='&ldquo;hardest decision&rdquo; &middot; &ldquo;crisis&rdquo; &middot; &ldquo;Brooklyn Lab&rdquo;',
 core='I moved a leader I had asked to step in, and ran the high school myself, in the middle of COVID and the renewals.',
 why='The renewal is only a feat in context: two authorizers running separate processes, no credible institutional records, numbers you could not trust, low achievement and culture, COVID, a turnaround, and an acquisition in motion. You cannot say most of that. Your words that carry it: untangling knots and doing forensic analysis on the data.',
 keys='brooklyn lab hardest decision interim principal renewal reauthorized covid crisis superintendent',
 label='13 &middot; The hardest call you have made. Brooklyn Lab.',
 hook='moved the leader / ran the high school myself / knots, forensics / both reauthorized',
 tests='Whether he makes hard calls and owns them.',
 target='75 seconds',
 land='We took both charters through renewal at the same time, and both were reauthorized.',
 avoid='Saying the numbers you were shown were false or unknown. Blaming the founder. Leading with the renewal: any decent school gets reauthorized, so it only means something after the knots and the forensics.',
 answer=P(*l5)+SRC('THE TWELVE ANSWERS, block 5 (your dictation).'),
 receipts=['(5) BROOKLYN LAB'],stop='Stop on "both were reauthorized."')

k9=B[9][:]
k9[4]=em(k9[4],"They're running it now.")+' '+cue('stop','STOP')
q(id='leftkipp',grp='E',t1=14,tier='LIKELY',type='core',short='Leaving KIPP',
 trig='&ldquo;why did you leave KIPP&rdquo; &middot; &ldquo;what have you been doing since May&rdquo;',
 core='A two-year design role. It ends when the cycle runs without me.',
 why='Short, clean, no apology.',
 keys='left kipp leave why did you leave since may gap design role one kipp',
 label='14 &middot; Why did you leave KIPP? What since?',
 hook='design and hand-back / runs without me / arm\'s reach',
 tests='Whether there is a problem behind the exit.',
 target='45 seconds',
 land='Twenty-eight regions, forty-eight high schools. They\'re running it now.',
 avoid='Anything critical about KIPP. The Verizon line if it lands wrong with ex-Success people.',
 answer=P(*k9)+SRC('THE TWELVE ANSWERS, block 9 (your dictation, revised 092526).'),
 receipts=['(2) 28 REGIONS, 48 HIGH SCHOOLS, NO MANDATE'],stop='Stop.')

a6=B[6][:]
a6[2]=ins(a6[2],'I realized',"slow",'slow')
a6[4]=a6[4]+' '+cue('stop','STOP')
q(id='assocdean',grp='E',t1=15,tier='LIKELY',type='core',short='A failure: the associate dean',
 trig='&ldquo;a failure&rdquo; &middot; &ldquo;a time you were wrong&rdquo; &middot; &ldquo;growth area&rdquo;',
 core='I had a fixed mindset about someone I managed. I fixed it, late.',
 why='Zeta is "love your people." This shows you own a management miss.',
 keys='failure mistake wrong fixed mindset associate dean develop growth area manager',
 label='15 &middot; Tell me about a failure.',
 hook='fixed mindset / six months / clarity, investment, training, accountability / co-dean now',
 tests='Self-awareness and how he develops people.',
 target='90 seconds',
 land='He\'s co-dean there now, and still one of the best I\'ve seen do this job.',
 avoid='Why you had to leave Excel.',
 answer=P(*a6)+SRC('THE TWELVE ANSWERS, block 6 (your dictation).'),
 receipts=['(8) THE ASSOCIATE DEAN'],stop='Stop on the last line.')

# ---------- F. YOUR ASKS ----------
q(id='ask1',grp='F',t1=16,tier='LOCK',type='exit',short='MUST-ASK 1: which role',
 trig='by minute 10',core='Which role, and what success looks like at twelve months.',
 why='You left the Dan call without knowing the seat or the next step.',
 keys='ask role which seat success twelve months principal manager',
 label='MUST-ASK 1 &middot; Which role? By minute 10.',hook='which role / success at 12 months / listen',
 tests='',target='one sentence',land='They describe the seat.',avoid='Waiting until the end.',
 answer=P(cue('flat','PROPOSED wording, not yet yours: say it your way')+' Which role they are considering you for, and what success would look like at twelve months. '+cue('stop','STOP'))+SRC('Proposed wording. The form that worked with Dan (line 211): "What, if anything, should I read into the fact that you and I are having a conversation on the school excellence side of things as opposed to operations?"'),
 receipts=[],stop='Ask and listen.')
q(id='ask2',grp='F',t1=17,tier='LOCK',type='exit',short='MUST-ASK 2 + next step',
 trig='minute 20',core='One question each, then the next step.',
 why='Grounded in what Zeta is doing this fall.',
 keys='ask question kruti paola campuses ninth graders next step who else',
 label='MUST-ASK 2 &middot; One for each of them, then the next step.',hook='Kruti: consistency / Paola: the 119 / next step',
 tests='',target='as needed',land='You know the next step and who decides.',avoid='Answering your own question.',
 answer=P(cue('flat','PROPOSED wording, not yet yours: say it your way'),'<em>Kruti:</em> with Flushing, Tremont Park and the high school all opening this fall, what has been hardest to keep consistent campus to campus.','<em>Paola:</em> for the 119 ninth graders in that first class, what a great first year looks like by June.',cue('slow','slow')+' The next step, and who else you would talk to. '+cue('stop','STOP'))+SRC('Proposed wording.'),
 receipts=[],stop='Ask and listen.')

# ---------- BENCH ----------
def bench(**k): k.setdefault('type','core'); k.setdefault('receipts',[]); q(**k)
b8=B[8][:]; b8[5]=ins(b8[5],'My estimate','flat','plain')
bench(id='now',grp='P',short='What you do now (AI)',label='What are you doing right now? The AI work.',hook='time / two fears / safe, human-in-the-loop / not for its own sake',
 keys='ai tools now current coverage schedule what are you doing technology',core='Principals point me at a problem; I build the thing that saves them time.',why='Only if asked. Do not pitch.',
 tests='',target='60 seconds',land='Some need a place to start, all of them need time, and I can help with both.',avoid='"Taking off." Any claim a tool is running at a school.',
 answer=P(*b8)+SRC('THE TWELVE ANSWERS, block 8 (your dictation).'),stop='Stop.')
b12=B[12][:]
bench(id='whynow',grp='P',short='Why take this after being a chief',label='Why take this seat after being a superintendent and a chief?',hook='bass player / tomorrow in front of kids / a builder',
 keys='why now step down lateral ego superintendent chief level title',core='The right title in the wrong organization is a losing proposition.',why='If level comes up.',
 tests='',target='75 seconds',land="It's been a long time since I was directly responsible for the thing that had to happen in front of kids the next day, and I want that back.",avoid='Title, level, money.',
 answer=P(b12[1],b12[2])+SRC('THE TWELVE ANSWERS, block 12 (paragraphs 2-3).'),stop='Stop.')
b13=B[13][:]
bench(id='change',grp='P',short='How you lead change',label='How do you lead change?',hook='one thing / clarity, investment, training, accountability / paper is worthless',
 keys='lead change approach leadership style rollout',core='The one thing, then the systems. Paper is worthless until the people are behind it.',why='If the question is about approach, not a story.',
 tests='',target='75 seconds',land='Paper is worthless until the people are behind it.',avoid='Reciting a framework.',
 answer=P(*b13[:5])+SRC('THE TWELVE ANSWERS, block 13.'),stop='Stop.')
b11=B[11][:]
bench(id='growth',grp='P',short='Growth area',label='Your biggest area for growth?',hook='narrowing focus / build slow to go fast / first downs',
 keys='growth area weakness criticism',core='Narrowing focus.',why='One growth area, owned, with the fix.',
 tests='',target='45 seconds',land='The strategy is first downs.',avoid='A second weakness.',
 answer=P(*b11)+SRC('THE TWELVE ANSWERS, block 11.'),stop='Stop.')
b7=B[7][:]
bench(id='consult',grp='P',short='Consultant to operator',label='Why go back inside a network after consulting?',hook='stay credible / kept a distance before / a promise to principals',
 keys='consultant operator consulting why operate distance',core='There is no substitute for the full experience.',why='The unspoken "will he stay?"',
 tests='',target='75 seconds',land="I can't break a promise to principals.",avoid='The hotels line if it sounds flip.',
 answer=P(b7[0],b7[2],b7[3],b7[6])+SRC('THE TWELVE ANSWERS, block 7 (paragraphs 1, 3, 4, 7).'),stop='Stop.')
bench(id='sped',grp='Q',short='Special education (strength)',label='Special education. How have you led it?',hook='Collegiate: best SPED operation I know / managed at Excel / oversaw at Lab',
 keys='special education sped students with disabilities ell english learners inclusion',core='A strength lane. Lead with it, never hedge.',why="Zeta's authorizer has flagged SPED and ELL enrollment. This is your strongest unplayed card.",
 tests='',target='60 seconds',land='No recorded answer in your words. Say the facts your way.',avoid='Saying you managed SPED teachers at Collegiate (you coached principals and held standards there).',
 answer=P('No recorded answer in your words yet. The facts:','<em>Collegiate:</em> a seven-level service continuum, including low-incidence programs and a post-secondary program. Your ruling: the best special education operation of any charter network you know in the country. You coached principals and held standards there.','<em>Excel:</em> you managed special education. <em>Brooklyn Lab:</em> you oversaw it.')+SRC('verified-facts L250, ruling 57, via PRINCIPAL MANAGER TRACK 092026.'),stop='Stop.')
bench(id='pushback',grp='Q',short='A coaching miss at Collegiate',label='A time your approach with a principal did not work.',hook='wasted a year / systems before buy-in / cleaned it up',
 keys='coaching miss failure principal buy in collegiate pushback',core='I built the documents before I had the leader.',why='A second failure story if they want one about principals specifically.',
 tests='',target='60 seconds',land='Yes, I cleaned it up, but it was a failure.',avoid='Naming the principal or the school.',
 answer=P('Your words, 082626: "focused on building the systems and the structure of the documents and did not insist on the leader\'s buy-in, or even their time and their sign-off." "that school fell as a result of it." "a real, genuine failure that had real, measurable impact. Yes, I cleaned it up, but it was a failure."')+SRC('verified-facts L1202, via PRINCIPAL MANAGER TRACK 092026. The principal stays unnamed.'),stop='Stop.')
pay=c(R_PAY)
bench(id='pay',grp='R',short='Compensation',label='Compensation expectations? (never raise first)',hook='right team over cashing in / top of the band',
 keys='compensation salary pay range band money',core='Title and pay match the scope.',why='Debrief: Principal Manager band $125K to $175K; your salary of record $175K; your rule is to ask for the top of the band.',
 tests='',target='20 seconds',land='Top of the band, and the number grows if the scope does.',avoid='Naming a number first.',
 answer=P(pay)+SRC('DREAM screen 081726, when the band was $145K to $165K. At Zeta, set your own number before the call.'),stop='Stop.')
cm=c(G_COMMUTE_A)+' … '+c(G_COMMUTE_B)
bench(id='commute',grp='R',short='In person, the Bronx',label='In person every day in the Bronx. Does that work? (never raise first)',hook='considered it / right people, right work / eyes wide open',
 keys='commute in person bronx westchester every day hybrid travel',core='Short answer is no concern, if that is still true.',why='Gillian asked about Inwood on 09/11. The Principal Manager seat is 425 Westchester Ave, daily.',
 tests='',target='20 seconds',land='I want to find the right group of people doing the right work more than anything.',avoid='The kids. "I know that can be a red flag."',
 answer=P(cm)+SRC('Zeta screen 091126, your commute answer; the "…" skips the part about your kids.'),stop='Stop.')
bench(id='start',grp='R',short='Start date',label='When could you start?',hook='flexible / hand off thoughtfully',keys='start date when available october',core='Flexible.',why='Gillian floated October 13.',tests='',target='15 seconds',land='It\'s a good time for me.',avoid='Committing before checking United Schools.',
 answer=P(c(G_START))+SRC('Zeta screen 091126.'),stop='Stop.')
bench(id='yearone',grp='R',short='Year one',label='What would you want to own in year one?',hook='principals / ninth-grade academic health for the high school',keys='year one own first year 90 days priorities',core='Principals, and especially the high school side.',why='No recorded answer. The position is yours.',tests='',target='30 seconds',land='That is where my record is strongest.',avoid='',
 answer=P('No recorded answer in your words. Proposed bullets: managing a set of principals, the way Dan described; owning ninth-grade academic health for the new high school; why: Carver and the 46%.'),stop='Stop.')

json.dump(Q,open('Q.json','w'))
print(len(Q),'questions;',sum(1 for x in Q if x.get('t1')),'in THE 15+asks')
