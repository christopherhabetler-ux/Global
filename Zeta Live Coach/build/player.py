import json,re,html
def cards(path):
    t=open(path).read().strip(); blocks=re.split(r'\n(?=(?:Card \d+\.|Bench \d+\.|The close\.|The traps\.))',t)
    out=[]
    for b in blocks:
        title=b.split('\n')[0][:90] if re.match(r'(Card|Bench) \d+\.|The close|The traps',b) else 'Intro'
        out.append({'t':title,'x':b.strip()})
    return out
P1=cards('/home/user/Global/ZETA LISTEN 092926 part 1.md'); P2=cards('/home/user/Global/ZETA LISTEN 092926 part 2.md')
data=json.dumps({'p1':P1,'p2':P2},ensure_ascii=False)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Zeta Listen</title>
<style>
:root{--bg:#f7f6f2;--card:#fff;--line:#e3e0d8;--tx:#1d1d1b;--dim:#6b6960;--acc:#1f4e8c}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#f7f6f2;--card:#fff;--line:#e3e0d8;--tx:#1d1d1b;--dim:#6b6960;--acc:#1f4e8c}}
:root[data-theme="dark"]{--bg:#f7f6f2}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--tx);font:18px/1.55 Georgia,serif;padding:0 16px 140px;max-width:760px;margin:0 auto}
header{position:sticky;top:0;background:rgba(247,246,242,.97);padding:14px 0 10px;border-bottom:1px solid var(--line);z-index:5}
h1{font:700 15px/1.3 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;letter-spacing:1.2px;text-transform:uppercase}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:10px;font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif}
button,select{font:600 15px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;padding:10px 16px;border-radius:10px;border:1px solid var(--line);background:#fff;color:var(--tx);cursor:pointer}
button.main{background:var(--acc);color:#fff;border-color:var(--acc);min-width:110px}
.tab.on{background:var(--tx);color:#fff}
#now{font:600 14px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:var(--dim);margin-top:8px}
.c{background:#fff;border:1px solid var(--line);border-radius:12px;margin:12px 0;padding:14px 16px;cursor:pointer}
.c h2{font:700 16px/1.3 -apple-system,Segoe UI,Helvetica,Arial,sans-serif}
.c p{margin-top:8px;display:none;white-space:pre-wrap}
.c.on{border-color:var(--acc);box-shadow:0 0 0 3px rgba(31,78,140,.15)}
.c.on p{display:block}
.note{font:14px/1.45 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:var(--dim);margin-top:12px}
</style></head><body>
<header><h1>Zeta listen &middot; tap a card to play from there</h1>
<div class="row"><button class="tab on" data-p="p1">Part 1 &middot; the 18 cards</button><button class="tab" data-p="p2">Part 2 &middot; bench + traps</button></div>
<div class="row"><button class="main" id="play">Play</button><button id="back">&#9664; Card</button><button id="next">Card &#9654;</button>
<select id="rate"><option value="1">1x</option><option value="1.2">1.2x</option><option value="1.4" selected>1.4x</option><option value="1.6">1.6x</option></select></div>
<div id="now">Tap Play, or tap any card.</div></header>
<div id="list"></div>
<p class="note">Uses your phone's or computer's built-in voice. On iPhone, keep the screen on while it plays (it stops if the phone locks). Every answer is the same text as the companion cards.</p>
<script>
var D=__DATA__, part='p1', i=0, playing=false, voice=null;
function pickVoice(){var v=speechSynthesis.getVoices().filter(function(x){return /^en(-|_)US/i.test(x.lang)});
 voice=v.filter(function(x){return /Samantha|Aaron|Evan|Nathan|Zoe|Ava|Google US English|Natural|Premium|Enhanced/i.test(x.name)})[0]||v[0]||null}
speechSynthesis.onvoiceschanged=pickVoice; pickVoice();
function render(){var L=document.getElementById('list');L.innerHTML='';
 D[part].forEach(function(c,k){var d=document.createElement('div');d.className='c'+(k===i?' on':'');
  var h=document.createElement('h2');h.textContent=c.t;var p=document.createElement('p');p.textContent=c.x;
  d.appendChild(h);d.appendChild(p);d.onclick=function(){i=k;start()};L.appendChild(d)})}
function chunks(t){return t.replace(/\\.\\.\\./g,'. ').match(/[^.!?\\n]+[.!?]*["”]?|\\n/g).map(function(s){return s.trim()}).filter(Boolean)}
var q=[];
function speakNext(){if(!playing)return;if(!q.length){i++;if(i>=D[part].length){stop();return}render();scrollOn();q=chunks(D[part][i].x);}
 var u=new SpeechSynthesisUtterance(q.shift());if(voice)u.voice=voice;u.rate=+document.getElementById('rate').value;
 u.onend=function(){setTimeout(speakNext,120)};speechSynthesis.speak(u);document.getElementById('now').textContent='Playing: '+D[part][i].t}
function scrollOn(){var o=document.querySelector('.c.on');if(o)o.scrollIntoView({behavior:'smooth',block:'start'})}
function start(){speechSynthesis.cancel();playing=true;q=chunks(D[part][i].x);render();scrollOn();document.getElementById('play').textContent='Pause';setTimeout(speakNext,150)}
function stop(){playing=false;speechSynthesis.cancel();document.getElementById('play').textContent='Play';document.getElementById('now').textContent='Paused on: '+D[part][i].t}
document.getElementById('play').onclick=function(){playing?stop():start()};
document.getElementById('next').onclick=function(){i=Math.min(i+1,D[part].length-1);playing?start():render()};
document.getElementById('back').onclick=function(){i=Math.max(i-1,0);playing?start():render()};
document.getElementById('rate').onchange=function(){if(playing)start()};
document.querySelectorAll('.tab').forEach(function(b){b.onclick=function(){stop();part=b.dataset.p;i=0;
 document.querySelectorAll('.tab').forEach(function(x){x.classList.toggle('on',x===b)});render()}});
render();
</script></body></html>'''.replace('__DATA__',data)
open('/home/user/Global/Zeta Listen 092926.html','w').write(page)
print('ok',len(P1),len(P2))
