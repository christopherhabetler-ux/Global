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
