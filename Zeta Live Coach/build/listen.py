import json,re,html
Q=json.load(open('Q.json')); by={x['id']:x for x in Q}
def say(h):
    h=re.sub(r'<p class="small[^"]*">.*?</p>','',h,flags=re.S)
    h=re.sub(r'<span class="dcue[^>]*>.*?</span>','',h)
    h=h.replace('</p>','\n')
    t=html.unescape(re.sub(r'<[^>]+>','',h)).replace(' … ','... ').replace('…','...')
    return '\n\n'.join(re.sub(r'\s+',' ',l).strip() for l in t.split('\n') if l.strip())
def pl(s): return html.unescape(re.sub(r'<[^>]+>','',s or '')).replace('&middot;',',').strip()
def q(label): return re.sub(r'^(MUST-ASK \d|\d+) · ','',pl(label))
def card(n,id,intro):
    x=by[id]; out=[f'Card {n}. {q(x["label"])}',intro,'Here it is, in your words.',say(x['answer'])]
    land=pl(x.get('land','')); 
    if land and not land.startswith('Frame'): out.append('Land on this. '+land.replace('"',''))
    out.append('Then stop. '+pl(x.get('stop','')).replace('Stop on','Your last words are').replace('Stop.','').strip())
    return '\n\n'.join(o for o in out if o.strip())
P1=[]
P1.append("""Zeta. Paola Zalkind and Kruti Mehta. The listen file, part one.
For Tuesday, September twenty-ninth, three o'clock Eastern. Thirty minutes on Zoom, two people.

Here's how this tape works. The coach parts are framing, nothing more. Every answer you hear is your own words, cut from your dictated answers, your interview recordings, and your own writing. Nothing in the answers was written for you. Where a line was cut, you'll hear a pause. Play it on a walk. Don't take notes. The job is just to hear your own career in your own voice until it's automatic.

Where you are. The operations seat is closed. Felipe passed you to the schooling side, and Dan's first real question was about managing principals. So the seat in play is almost certainly the principal manager seat. Don't name it first. Let them say it.

Who's in the room. Paola Zalkind is Chief Schooling Officer. She manages Zeta's school leaders. Teach For America, then Success Academy, from kindergarten teacher to founding principal of Union Square to Managing Director of Schools, then Director of Leader Development at KIPP New Jersey, then Zeta. She built principals for a living. She's the principal-manager decision, and she'll push for proof.

Kruti Mehta is Managing Director of Scaling School Excellence. Accenture, then B C G, then Zeta in its second year, then a Booth M B A. She's the consultant's lens: codify what works, launch new schools with fidelity. She probably needs someone with school-leader credibility beside her. Don't pitch your practice to her.

Four rules, from the Dan debrief.
One. The first sentence is the claim. The last sentence is a person or a number.
Two. Every principal answer ends on proof. Carver. Brooklyn Lab. The forty-six percent. With Dan, one of five answers did.
Three. Ask your first question by minute ten. With Dan you asked nothing until time was up.
Four. Two minutes, then stop. Two of them, thirty minutes.

Alright. The cards, in order. Sixteen answers, then your two asks.""")
intro={
'aboutyou':"This one opens almost every call. Two and a half to three minutes. Skip the paragraph about the kids for Zeta. Keep Brooklyn Lab moving. It ends on why Zeta.",
'whyzeta':"The ops seat is closed, so this has to be a clear yes to the schooling side. The third paragraph is your own answer from tonight about the seat.",
'g2g':"Paola's core question. Dan asked it, and your answer had four good principles and no proof. This time it ends on Carver.",
'carver':"Your best proof for a job managing principals, and with Dan it came out as one word, successful. This is your written account of it.",
'managed':"If she asks whether you've managed principals, or been one. Plain, no hedge. Interim goes out loud only.",
'hs':"Dan's biggest problem is the high school, and it rolls up to Paola. Open with the claim, not with what you don't know. The seating chart paragraph is the one to cut if time is short.",
'ownership':"Dan's follow-up. For Paola, it shows culture as academic identity. Keep it under two minutes.",
'scale':"Kruti's lane. Earn it, in plain words, means a new principal runs the proven play until the school is stable and functional, and that earns the room to change it. Pair it with how you invest in people.",
'netsys':"For Kruti, if it's about central office and schools. These are your lines from the School in the Square onsite, as the debrief quoted them.",
'adopt':"Adoption without authority. Zeta is growing fast and Kruti needs schools to want the playbook. Don't put the forty-six percent in the same breath as the twenty-eight and forty-eight.",
'initiative':"An initiative from design to scale. This is your answer from the DREAM screen, and it ends on the number.",
'launch':"Zeta has Flushing, Tremont Park and the high school all in year one. This is how you launched a school.",
'instruction':"The likeliest doubt about you for a schooling seat. Yes and no, then everything upstream, then the proof. The CREDO line now belongs to Carver.",
'lab':"The renewal only means something in context. Stewardship, not a turnaround, but name the mess. The decision itself stays out loud only.",
'leftkipp':"Short, clean, no apology. If they press on the exit, the other true line is that the position was eliminated after you delivered and met goals.",
'assocdean':"Zeta says love your people. This shows you own a management miss, and it has a happy ending. If they ask why you left Excel, you knew you'd be leaving at the end of the year. Never the health reason.",
'ask1':"Your must-ask, by minute ten. You learn the seat without naming it.",
'ask2':"Around minute twenty. One for each of them, then the next step. The last two lines for Kruti and Paola are proposed, not yet yours, so say them your way.",
}
for i,id in enumerate(['aboutyou','whyzeta','g2g','carver','managed','hs','ownership','scale','netsys','adopt','initiative','launch','instruction','lab','leftkipp','assocdean','ask1','ask2'],1):
    P1.append(card(i,id,intro[id]))
P1.append("""The close. Last two minutes. Warm, at the camera. Thank them. Echo one thing each of them said, in their words. Then your own lines.

From the Gillian screen: I wanna find the right group of people doing the right work more than anything.

From the Dan call: I love being in environments where it's like best idea wins, strong opinions, loosely held. Let's debate the heck out of things. Let's attack people's ideas without attacking people.

Then the next step, and who else you'd talk to. Not, you know the story.

That's part one. The first sentence is the claim. Every principal answer ends on Carver, Brooklyn Lab, or the forty-six percent. Ask by minute ten. Two minutes, then stop. And let the silences be theirs.""")
P2=["""Zeta. The listen file, part two. The bench, and the traps.
Same rule as part one. The coach parts are framing. The answers are your words."""]
intro2={
'whynow':"Why this seat, and would you take it. The first line is yours from tonight. The guards behind it: it's not a one-year role, so it's never a stepping stone. The commute is a slog you've accepted, and you don't raise it. Your AI work, you don't raise on this call.",
'sped':"Special education is a strength lane. Lead with it, no hedge. Collegiate built it at true deep levels. Excel, you managed it. Brooklyn Lab, you oversaw it.",
'yearone':"If they ask what you'd own in year one. Your ninety-day note, then the onsite lines. The last line is a proposed frame, not yours.",
'accountable':"Holding a leader accountable and keeping the relationship. Zeta says love your people. This is how you hold the bar and love the person.",
'inherit':"A system you inherited that wasn't working. This is the Collegiate story from the School in the Square round, and it's really a principal-development story.",
'ambiguity':"A big goal, total ambiguity, full autonomy. The four-day COVID playbook. Leave out the student and staff counts.",
'pay':"Never raise it first. If they ask, this is your DREAM answer, with the cash-in line cut. Top of the band. Set your number before three.",
'commute':"In person every day in the Bronx. Never raise it first. The part about your kids is cut.",
'start':"Start date. Flexible.",
'now':"What you're doing now. One sentence per tool, then stop. Never pitch the practice to Kruti.",
'change':"How you lead change, if the question is about approach and not a story.",
'growth':"Your growth area. One, owned, with the fix.",
'consult':"Why go back inside a network after consulting. The unspoken question is, will he stay.",
'pushback':"A time your approach with a principal didn't work. The principal stays unnamed.",
}
for i,id in enumerate(intro2,1):
    x=by[id]; P2.append('\n\n'.join([f'Bench {i}. {q(x["label"])}',intro2[id],'In your words.',say(x['answer'])]))
P2.append("""The traps. These are literal strings. If you hear one starting, the sentence after it doesn't get said.

Never the health reason for leaving Excel. Never a grade for KIPP or Achievement First. Never the rest of the mess, or any Success comparison, because Paola spent years at Success. Never, I don't care really, if you as a first-year principal. Never a bare principal. It was interim, half a year, while superintendent. Never that the numbers at Brooklyn Lab were false. Never managed forty-eight principals. Never that the tool was used by all twenty-eight. It was piloted and handed off. Never suspensions down seventy-five percent at Carver. That's network-wide. Never five-year renewals, never SUNY, never new charter operator. Never the principal manager title unless they say it first. Never the kids, the commute, or pay, first.

And the self-disqualifying strings. I'm not trying to. I don't mean to. There's a lot I'd have to learn. I need to catch up. That's not where I'm at. I'm probably more of a. I'm not an expert in. I don't want to overstate. This is not a question I prepared for. Happy to go deeper. Long story short. I'll get to your exact question, but first. I'll just pause right there. And never a little bit, or kind of, on a credential. If you hear yourself say a vague word about your own results, the next word out of your mouth is a number.

That's the tape. You've already done the hard part. Dan brought you into his hardest problem and said, I love that idea. Go be the person who did the work.""")
open('/home/user/Global/ZETA LISTEN 092926 part 1.md','w').write('\n\n'.join(P1)+'\n')
open('/home/user/Global/ZETA LISTEN 092926 part 2.md','w').write('\n\n'.join(P2)+'\n')
for f in ['part 1','part 2']:
    t=open(f'/home/user/Global/ZETA LISTEN 092926 {f}.md').read(); w=len(t.split()); print(f,w,'words, about',round(w/160),'min at normal speed')
