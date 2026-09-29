"""ZETA LIVE 092926: one clean page. 16 collapsible questions; open = reminders, key points left, first line + script right, landing last. Asks on their own tab."""
import json,re,html,glob,os
Q=json.load(open('Q.json')); by={x['id']:x for x in Q}
ns={}; g=open('gen5.py').read()
exec(g.split("for id,items in BL.items():")[0].replace("Q=json.load(open('Q.json')); by={x['id']:x for x in Q}",""),ns); BL=ns['BL']
REV={}
for f in sorted(glob.glob('rev_out_*.json')):
    try: REV.update(json.load(open(f)))
    except Exception as e: print('bad',f,e)
ORDER=['aboutyou','whyzeta','g2g','carver','managed','hs','ownership','scale','netsys','adopt','initiative','launch','instruction','lab','leftkipp','assocdean']
def qtext(x): return re.sub(r'^\d+ &middot; ','',x['label'])
def tokens(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    t=t.replace('[slow]','<span class="cue">slow</span>').replace('[beat]','<span class="cue">pause</span>').replace('[land]','<span class="cue land">land it</span>').replace('[STOP]','<span class="cue stop">stop</span>')
    return ''.join('<p>'+p.strip()+'</p>' for p in t.split('\n\n') if p.strip())
def from_card(h):
    h=re.sub(r'<div class="bullets">.*?</div>','',h,flags=re.S); h=re.sub(r'<div class="prepOnly">.*','',h,flags=re.S)
    h=re.sub(r'<div class="coreline">.*?</div>','',h,flags=re.S); h=re.sub(r'<p class="small[^"]*">.*?</p>','',h,flags=re.S)
    h=re.sub(r'<p class="lab"[^>]*>.*?</p>','',h,flags=re.S)
    h=re.sub(r'<span class="dcue ([a-z]+)">(.*?)</span>',lambda m:'<span class="cue'+(' stop' if m.group(1)=='stop' else ' land' if m.group(1)=='power' else '')+'">'+m.group(2).lower()+'</span>',h)
    return h
def first_sentence(h):
    t=html.unescape(re.sub(r'<span class="cue[^>]*>.*?</span>','',h)); t=re.sub(r'<[^>]+>','',t).strip()
    m=re.match(r'(.+?[.?!])(\s|$)',t); return m.group(1) if m else t[:140]
def plain(s): return html.unescape(re.sub(r'<[^>]+>','',s or '')).strip().strip('"')
rows=[]; src={}
for n,id in enumerate(ORDER,1):
    x=by[id]; r=REV.get(id)
    if r and r.get('script'):
        first=r.get('first_line') or ''; body=r['script'].strip()
        if first and body.startswith(first): body=body[len(first):].lstrip()
        script=tokens(body); land=r.get('landing') or plain(x.get('land')); src[id]='revised'
    elif r and r.get('note'):
        script='<p class="give">Give me bullets. There isn\'t a good script for this one yet; talk from the points on the left.</p>'; first=''; land=plain(x.get('land')); src[id]='bullets only'
    else:
        script=from_card(x['answer']); first=first_sentence(script); land=plain(x.get('land')); src[id]='card'
    pts=''.join('<li>'+b+'</li>' for b in BL.get(id,[]))
    rows.append(f'''<details class="q" id="q-{id}"><summary><span class="n">{n}</span><span class="qt">{qtext(x)}</span></summary>
<div class="body"><div class="remind">Breathe. Slow down. You've got this.</div>
<div class="grid"><div class="left"><div class="h">Key points</div><ul>{pts}</ul></div>
<div class="right">{('<div class="first"><div class="h">First line</div>'+html.escape(first,quote=False)+'</div>') if first else ''}
<div class="h">Script</div><div class="script">{script}</div>
{('<div class="landing"><div class="h">Land on</div>'+html.escape(land,quote=False)+'</div>') if land and not land.startswith('Frame') else ''}</div></div></div></details>''')
def askblock(id,title):
    x=by[id]; pts=''.join('<li>'+b+'</li>' for b in BL.get(id,[]))
    return f'<section class="card"><h2>{title}</h2><ul class="asks">{pts}</ul><div class="script">{from_card(x["answer"])}</div></section>'
ASKS=(askblock('ask1','By minute 10: the seat')+askblock('ask2','Around minute 20: one each, then the next step')+
 '<section class="card"><h2>The close</h2><div class="script"><p>Thank them. Echo one thing each of them said, in their words.</p>'
 '<p>&ldquo;I wanna find the right group of people doing the right work more than anything.&rdquo;</p>'
 '<p>&ldquo;I love being in environments where it\'s like best idea wins, strong opinions, loosely held. Let\'s attack people\'s ideas without attacking people.&rdquo;</p>'
 '<p>Then: the next step, and who else you\'d talk to.</p></div></section>')
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Zeta Live</title>
<style>
:root{{--bg:#f7f6f2;--card:#fff;--line:#e2ded3;--tx:#1b1b19;--dim:#6a675e;--acc:#1f4e8c;--gold:#9a6700}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#f7f6f2;--card:#fff;--line:#e2ded3;--tx:#1b1b19;--dim:#6a675e}}}}
:root[data-theme="dark"]{{--bg:#f7f6f2}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--tx);font:18px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;padding:0 16px 80px;max-width:1280px;margin:0 auto}}
header{{position:sticky;top:0;z-index:5;background:rgba(247,246,242,.97);border-bottom:1px solid var(--line);padding:12px 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
.brand{{font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:13px;color:var(--dim);margin-right:6px}}
.tab{{font:600 15px inherit;padding:9px 16px;border-radius:999px;border:1px solid var(--line);background:#fff;color:var(--tx);cursor:pointer}}
.tab.on{{background:var(--tx);color:#fff;border-color:var(--tx)}}
#f{{flex:1;min-width:180px;font:16px inherit;padding:9px 12px;border-radius:10px;border:1px solid var(--line);background:#fff}}
.page{{display:none}}.page.on{{display:block}}
details.q{{scroll-margin-top:74px;background:#fff;border:1px solid var(--line);border-radius:14px;margin:10px 0;overflow:hidden}}
details.q[open]{{box-shadow:0 8px 28px rgba(0,0,0,.08);border-color:#cfc9ba}}
summary{{list-style:none;cursor:pointer;display:flex;gap:14px;align-items:baseline;padding:16px 18px}}
summary::-webkit-details-marker{{display:none}}
.n{{font-weight:800;color:var(--acc);min-width:24px;font-size:17px}}
.qt{{font-weight:700;font-size:20px;line-height:1.3}}
.body{{padding:0 18px 20px}}
.remind{{font-size:14px;font-weight:700;color:var(--gold);letter-spacing:.3px;padding:8px 0 12px;border-top:1px solid var(--line)}}
.grid{{display:grid;grid-template-columns:minmax(260px,34%) 1fr;gap:26px}}
@media(max-width:820px){{.grid{{grid-template-columns:1fr}}}}
.h{{font-size:11px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--dim);margin-bottom:6px}}
.left ul{{padding-left:18px}}.left li{{margin:6px 0;font-size:17px;line-height:1.4}}
.first{{background:#fff8e1;border-left:5px solid var(--gold);border-radius:0 10px 10px 0;padding:10px 14px;margin-bottom:14px;font-size:21px;font-weight:700;line-height:1.35;font-family:Georgia,serif}}
.first .h{{color:var(--gold)}}
.script{{font-family:Georgia,"Iowan Old Style",serif;font-size:20px;line-height:1.6}}
.script p{{margin-bottom:12px}}
.script b,.script em{{font-style:normal;font-weight:700;background:linear-gradient(transparent 60%,#ffe58a 60%)}}
.cue{{display:inline-block;font:700 11px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;text-transform:uppercase;letter-spacing:.8px;color:#7a5200;background:#fff1c9;border-radius:5px;padding:1px 6px;margin:0 4px;vertical-align:middle}}
.cue.stop{{color:#b3261e;background:#fdecea}}.cue.land{{color:#1f4e8c;background:#e7effa}}
.landing{{margin-top:14px;background:#eef6f0;border-left:5px solid #1f7a3f;border-radius:0 10px 10px 0;padding:10px 14px;font-weight:700;font-size:18px}}
.landing .h{{color:#1f7a3f}}
.give{{font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;font-weight:700;color:#b3261e}}
.card{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;margin:12px 0}}
.card h2{{font-size:20px;margin-bottom:10px}}
.asks{{padding-left:18px;margin-bottom:12px}}
.small{{display:none}}
</style></head><body>
<header><span class="brand">Zeta &middot; 3:00</span><button class="tab on" data-p="p16">The 16</button><button class="tab" data-p="pask">Your asks &amp; close</button><input id="f" placeholder="filter: principal, high school, KIPP, Brooklyn Lab..."></header>
<div class="page on" id="p16">{''.join(rows)}</div>
<div class="page" id="pask">{ASKS}</div>
<script>
document.querySelectorAll('.tab').forEach(function(b){{b.onclick=function(){{document.querySelectorAll('.tab').forEach(function(x){{x.classList.toggle('on',x===b)}});
 document.querySelectorAll('.page').forEach(function(p){{p.classList.toggle('on',p.id===b.dataset.p)}});window.scrollTo(0,0)}}}});
var f=document.getElementById('f');f.oninput=function(){{var t=f.value.toLowerCase().trim();
 document.querySelectorAll('details.q').forEach(function(d){{d.style.display=(!t||d.textContent.toLowerCase().indexOf(t)>-1)?'':'none'}})}};
document.querySelectorAll('details.q').forEach(function(d){{d.addEventListener('toggle',function(){{if(d.open)setTimeout(function(){{d.scrollIntoView({{behavior:'smooth',block:'start'}})}},30)}})}});
</script></body></html>'''
open('/home/user/Global/Zeta Live 092926.html','w').write(page)
print(json.dumps(src))
