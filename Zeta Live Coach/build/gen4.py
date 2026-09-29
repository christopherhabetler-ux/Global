"""Fourth pass (092926 ~1pm): card 3 becomes his dictated philosophy answer (trust, clarity, support, accountability)."""
import json,re
exec(open('gen2.py').read().split('# ---------- 1 background')[0])
Q=json.load(open('Q.json')); byid={x['id']:x for x in Q}
D=re.sub(r'\s+',' ',open('canon/dictation_092926.md').read())
def d(a,b): i=D.index(a); return D[i:D.index(b,i)+len(b)]
JEREL=json.load(open('cv.json'))['JEREL']
STOP=cue('stop','STOP')
p1=d("I'm going to talk about trust, clarity, support, and accountability.","feed into each other, right?")
p2=d("trust is everything because you get trust from clarity.","understanding, and validation.")
p3=d("a great meeting doesn't end with a list of principal next steps.","doing the work.")
p4a=d("Let's go to the problem, real-time coach.","real-time coach.")
p4b=d("Let me show up to the meeting so prepared that","as your best lessons.")
p5=d("Because if I want a principal to have a tough feedback conversation, they need to see an example of it. I can't just wing that,","I can't just wing that,").rstrip(',')+'.'
p6=d("We can't show up and expect to talk our way into improved understanding","we have.").replace(', because nobody',' … nobody') if False else d("We can't show up and expect to talk our way into improved understanding","that's incredibly intentional development.")
p7=d("nobody's time is more valuable in the school than the principal's.","every minute they're learning,").rstrip(',')+'.'
p8=d("the accountability, which is that no one's guessing where they stand.","no one's guessing where they stand.")
p9=d("Are they doing the right work? * Are they doing it incredibly well?","incredibly well?").replace('* ','')
p10=d("95% of my time, I'm in my support role.","letting a thing slide.")
p11=d("If I'm going to keep someone's trust, they have to know that I'm telling the truth.","telling the truth.")
p12=d("90% of the time, when they make a mistake, they know it's a mistake.","get better as a human being.")
p13=d("the accountability feeds the trust.","feeds the trust.")
p14=d("knowing that I'm your biggest cheerleader, but I'm also part of being your coach:","show you the better version.")
ans=P(
 cue('flat','first sentence, the map')+' '+bold(p1[0].upper()+p1[1:],'trust, clarity, support, and accountability','also not linear'),
 cue('slow','trust')+' '+bold(p2[0].upper()+p2[1:],'Trust is everything'),
 cue('slow','support')+' '+bold(p3[0].upper()+p3[1:],"They're on the floor doing the work."),
 'The best development meetings I\'ve ever had have either been: '+p4a+' … Or: '+p4b,
 bold(p5,'they need to see an example of it')+' '+bold(p6,'We have to teach our way into it'),
 p7[0].upper()+p7[1:]+' '+cue('beat','beat'),
 cue('slow','accountability')+' '+bold(p8[0].upper()+p8[1:],"no one's guessing where they stand")+' Adam Meinig\'s two questions: <b>'+p9+'</b>',
 bold(p10,"I'm never rounding up")+' '+p11,
 cue('flat','cut if short')+' '+p12,
 cue('power','land this')+' '+p13[0].upper()+p13[1:]+' … '+bold(p14[0].upper()+p14[1:],"I'm your biggest cheerleader"),
 cue('power','then the proof')+' <em>'+JEREL+'</em> '+STOP)
ans+=('<p class="small">Your words: your dictation 092926, about 1 PM (cut, nothing added; the bullets joined as "either... or"). '
      '"Adam Mining" in the dictation is Adam Meinig (Collegiate, your co-tenure notes). The last line is your written Carver answer, 060925.</p>'
      '<p class="small prepOnly"><b>Short version, about 75 seconds:</b> paragraph 1, the first sentence of trust, the floor line, "We have to teach our way into it," "no one\'s guessing where they stand," Adam\'s two questions, "I\'m never rounding up," the cheerleader line, then Carver.</p>')
x=byid['g2g']
x.update(answer=ans,
 label="3 &middot; What's your philosophy on managing people, or leaders? (Also: the good principal who needs to get to great.)",
 short='Your philosophy: trust, clarity, support, accountability',
 trig='&ldquo;philosophy on managing people&rdquo; &middot; &ldquo;how do you manage principals&rdquo; &middot; &ldquo;good to great&rdquo; &middot; &ldquo;feedback to a principal&rdquo;',
 core='"trust, clarity, support, and accountability... we kind of work in that order, but it\'s also not linear."',
 hook='trust / clarity / support on the floor / accountability: no one guessing / feeds the trust / Carver',
 why="The onsite at School in the Square asked exactly this (\"your core philosophy around how you lead and manage people\"), and Paola manages principals. Dan's good-to-great question is the same answer; end on Carver either way.",
 tests='Whether he has a coherent model of developing leaders, and proof it works.',
 target='2 minutes; the short version is in the prep note.',
 land='"the accountability feeds the trust." Then Carver.',
 avoid='Four principles and no proof (what happened with Dan). Reading it as a list. "Terrorizing or berating."',
 keys=x['keys']+' philosophy managing people leaders manage leadership style trust clarity support accountability development meetings',
 stop='Stop on "now CEO of Collegiate Academies."')
json.dump(Q,open('Q.json','w'))
print('gen4 ok')

# ---------- 092926 ~1:15pm: CH asked for a REVISION, not a cut: essence + 30-45s answer + short Jerel ----------
x=byid['g2g']
long_version=x['answer'].split('<p class="small">')[0]
ESS=('<div class="coreline"><b>What you\'re saying, in one breath</b>Trust is the foundation, and you earn it three ways. '
     'Clarity: nobody guesses what\'s expected. Support: you teach on the floor instead of handing out next steps. '
     'Accountability: you never round up, because telling the truth is what keeps the trust. It\'s not a sequence. Each one feeds the others.</div>')
A45=P(cue('flat','first sentence, the map')+' For me it\'s four things: <b>trust, clarity, support and accountability.</b> They run roughly in that order, but they\'re not linear. They feed each other.',
 cue('slow','slow')+' <b>Trust is everything</b>, and you earn it through the other three. <b>Clarity</b>: people know what\'s expected of them and what to expect from me. '
 '<b>Support</b>: my best development meetings don\'t end with a list of next steps. They happen on the floor, doing the work, because we can\'t talk our way into a better school. <b>We have to teach our way into it.</b> '
 'And <b>accountability</b>: no one\'s guessing where they stand. Ninety-five percent of the time I\'m in my support role, but <b>I never round up</b>. That\'s what keeps the trust.',
 cue('beat','beat, then the proof')+' The best example is Jerel.')
JER=P(cue('warm','steady')+' I was brought in to Carver as a consultant with one question: <b>do we keep this leader?</b> Jerel was the founding principal, a really compelling leader, and his school was struggling. Teachers were frustrated, and kids were opting out.',
 'What I saw was a high-potential leader getting a lot of feedback that things weren\'t good enough, and very little help. So I worked <b>shoulder to shoulder</b> with him, on the floor, with high doses of real-time feedback, mostly affirming. I named the relationship that needed to be reset. And we put what he was great at on stage.',
 cue('power','land this')+' It worked. <b>Jerel went on to be Louisiana Principal of the Year, and today he\'s CEO of Collegiate Academies.</b> '+cue('stop','STOP'))
x['answer']=(ESS+'<p class="lab" style="margin-top:12px">The answer &middot; 30 to 45 seconds</p>'+A45+
 '<p class="lab" style="margin-top:12px">The proof &middot; Jerel, about 45 seconds</p>'+JER+
 '<p class="small"><b>Revised at your request (092926, 1:15 PM)</b>, not cut: built from your dictation today and your written Carver answer (060925), in your phrasing where it exists. Say it your way.</p>'
 '<div class="prepOnly"><p class="lab" style="margin-top:14px">Long version &middot; your dictation, cut only</p>'+long_version+'</div>')
x['core']='Trust is everything, and you earn it through clarity, support and accountability. They feed each other.'
x['hook']='four things, not linear / trust is everything / teach our way into it / never round up / Jerel'
x['land']='"Jerel went on to be Louisiana Principal of the Year, and today he\'s CEO of Collegiate Academies."'
x['target']='45 seconds, then Jerel in 45. Under two minutes total.'
x['stop']='Stop on "CEO of Collegiate Academies."'
json.dump(Q,open('Q.json','w'))
print('card 3 revised')

# ---------- 092926 ~1:25pm: second revision, from his new outline (clarity incl. transparency; support = the model; accountability before relationship) ----------
ESS2=('<div class="coreline"><b>What you\'re saying, in one breath</b>Trust is everything, and it\'s earned, not assumed. '
      'Clarity and transparency so nobody guesses. Support that teaches, because you\'re modeling every second. '
      'Accountability as the thing that builds the relationship, not the thing the relationship permits.</div>')
A2=P(cue('flat','first sentence, the claim')+' <b>Trust is everything</b>, and you earn it through three things: <b>clarity, support and accountability.</b>',
 cue('slow','clarity')+' Clarity first. We\'re aligned on what we\'re going for and what your role is in it, and you know what to expect from me. I\'m <b>transparent</b> about where we\'re headed and why, so <b>nobody\'s guessing</b>.',
 cue('slow','support')+' Support. My job is to be <b>the model</b>. Coaching meetings are <b>teaching time, not talking time</b>, and I have to be incredibly intentional about that, because I\'m teaching every second whether I like it or not, <b>with every action and every inaction</b>.',
 cue('slow','accountability')+' And accountability. People usually say you need a relationship before you can have accountability. <b>I think it\'s the other way around: you can\'t have a relationship without accountability</b>, at least not for very long. '
 'People are watching to see whether you care enough to hold them to a high standard, whether you know what you\'re talking about, and whether you\'re willing to say what needs to be said. '
 'The best teachers and coaches any of us had were the most honest with us. <b>We knew where we stood.</b> Done well, that\'s what makes the relationship closer.',
 cue('beat','beat, then the proof')+' The best example is Jerel.')
x=byid['g2g']
x['answer']=(ESS2+'<p class="lab" style="margin-top:12px">The answer &middot; about 75 seconds</p>'+A2+
 '<p class="lab" style="margin-top:12px">The proof &middot; Jerel, about 45 seconds</p>'+JER+
 '<p class="small"><b>Revised at your request (092926, about 1:25 PM)</b> from your outline and your dictation today; the Jerel paragraph from your written Carver answer (060925). Say it your way.</p>'
 '<div class="prepOnly"><p class="lab" style="margin-top:14px">Long version &middot; your dictation, cut only</p>'+long_version+'</div>')
x['core']="Trust is everything, and you earn it through clarity, support and accountability. You can't have a relationship without accountability."
x['hook']="trust is everything / clarity + transparency / teaching time, not talking time / no relationship without accountability / Jerel"
x['target']='About 75 seconds, then Jerel in 45.'
json.dump(Q,open('Q.json','w'))
print('card 3 revision 2')
