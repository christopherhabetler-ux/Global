#!/usr/bin/env python3
"""Build the ClassE US language guide in the 092726 house template.

Takes the head (CSS), search bar and search script from the 092726 HTML, embeds the
Wix Madefor fonts so the PDF matches on any machine, fills the body from the guide
Markdown, and prints the PDF with Chrome.
Usage: python3 "build guide template.py" <template.html> <guide.md> <output name>
"""
import base64
import html
import os
import re
import subprocess
import sys
from pathlib import Path

tpl_path, md_path, out_name = sys.argv[1], sys.argv[2], sys.argv[3]
tpl = Path(tpl_path).read_text(encoding="utf-8")
md = Path(md_path).read_text(encoding="utf-8")
here = Path(md_path).resolve().parent

HEAD = tpl[: tpl.find("<body")]
BODY_TAG = re.search(r"<body[^>]*>", tpl).group(0)
SEARCHBAR = tpl[tpl.find(BODY_TAG) + len(BODY_TAG): tpl.find('<header class="cover">')]
SCRIPT = tpl[tpl.rfind("<script"): tpl.rfind("</body>")]
SAY_IC = ('<svg class="ic" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#0F52C1"/>'
          '<path d="M5.6 10.4l2.9 2.9 5.9-6.6" stroke="#fff" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
NOT_IC = ('<svg class="ic" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#A23B32"/>'
          '<path d="M6.6 6.6l6.8 6.8M13.4 6.6l-6.8 6.8" stroke="#fff" stroke-width="2.3" stroke-linecap="round"/></svg>')

# ---------- fonts: embed so headless Chrome never falls back ----------
def embedded_fonts():
    cache = here / "_fonts.css"
    if cache.exists():
        return cache.read_text()
    href = re.search(r'href="(https://fonts\.googleapis\.com/css2[^"]+)"', HEAD).group(1).replace("&amp;", "&")
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
    css = subprocess.run(["curl", "-sSL", "-A", ua, href], capture_output=True, text=True, check=True).stdout
    blocks = re.findall(r"/\*\s*latin\s*\*/\s*(@font-face\s*{[^}]*})", css)
    out = []
    for b in blocks:
        url = re.search(r"url\((https://[^)]+)\)", b).group(1)
        data = subprocess.run(["curl", "-sSL", url], capture_output=True, check=True).stdout
        out.append(b.replace(url, "data:font/woff2;base64," + base64.b64encode(data).decode()))
    text = "\n".join(out)
    cache.write_text(text)
    return text


try:
    FONTS = "<style>" + embedded_fonts() + "</style>"
    HEAD = re.sub(r'<link[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>', "", HEAD)
except Exception as e:  # offline: keep the Google Fonts links
    print("fonts not embedded:", e)
    FONTS = ""

OVERRIDES = """<style>
.beliefs li, .remember li, .oneline li { grid-template-columns: minmax(0, 1fr); }
.why .w-body, .w-use, .why .w-lead { max-width: none; }
.plain-list { margin: 4pt 0 10pt; padding: 8pt 12pt 8pt 26pt; background: var(--wash); border-left: 3px solid var(--blue); }
.plain-list li { margin: 0 0 3pt; }
.sec-intro { margin: 0 0 8pt; color: var(--gray); }
.remember .sec-intro { color: rgba(255,255,255,0.82); }
.faq { margin: 0; }
.faq div { padding: 7pt 0; border-top: 1px solid var(--line); break-inside: avoid; }
.faq div:first-child { border-top: 0; }
.faq dt { font-weight: 700; color: var(--navy); }
.faq dd { margin: 2pt 0 0; }
.qbox { padding: 12pt 18pt; border: 2px solid var(--navy); border-radius: 18px; }
.qbox ul { margin: 0; padding-left: 16pt; }
.qbox li { margin: 0 0 6pt; }
table.sn.said .h-not { width: 34%; } table.sn.said .h-say { width: 36%; } table.sn.said .h-nt { width: 30%; }
h3.sec-h { margin: 14pt 0 6pt; color: var(--navy); }
@page { size: 11in 8.5in; }
@page cover { size: 11in 8.5in; }
.pagestart { break-before: page; }
.band { padding-top: 0 !important; }
.beliefs.four { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }
table.sn.cat { margin: 14pt 0 10pt; }
table.sn.cat .h-cat { width: 17%; } table.sn.cat .h-not { width: 27%; } table.sn.cat .h-say { width: 29%; } table.sn.cat .h-nt { width: 27%; }
table.sn.cat th.cat-l { vertical-align: top; text-align: left; padding: 6pt 10pt 0 0; border-top: 3px solid var(--navy); background: transparent; }
.cat-l h3 { margin: 0 0 4pt; font-size: 11.5pt; line-height: 1.2; color: var(--navy); }
.cat-l p { margin: 0; font-size: 8.4pt; line-height: 1.4; font-weight: 400; color: var(--gray); text-transform: none; letter-spacing: 0; }
.cover { height: 8.5in !important; }
table.cmp { font-size: 8.8pt; } table.cmp td, table.cmp th { padding-top: 5pt !important; padding-bottom: 5pt !important; }
table.terms { width: 100%; border-collapse: collapse; font-size: 8.2pt; line-height: 1.3; }
table.terms th { width: 2.3in; text-align: left; vertical-align: top; padding: 2.2pt 10pt 2.2pt 0; color: var(--navy); }
table.terms td { vertical-align: top; padding: 2.2pt 0; border-bottom: 1px solid var(--line); }
table.terms tr { break-inside: avoid; }
.sources { margin-top: 8pt; font-size: 8pt; color: var(--gray); }
.ai-note { margin-top: 6pt; padding: 6pt 10pt; background: var(--wash); font-size: 8.8pt; font-style: italic; }
</style>"""


def smart(t):
    t = re.sub(r'(^|[\s(\[-])"', "\\1\u201c", t)
    t = t.replace('"', "\u201d")
    t = re.sub(r"'", "\u2019", t)
    return t


def il(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return smart(t)


def section(title, level=2):
    h = "#" * level
    m = re.search(r"^" + h + " " + re.escape(title) + r"\n(.*?)(?=^#{2," + str(level) + r"} |\Z)", md, re.S | re.M)
    return m.group(1).strip()


def bullets(text):
    return [l[2:] for l in text.splitlines() if l.startswith("- ")]


def paras(text):
    return [p.strip() for p in text.split("\n\n") if p.strip() and not p.strip().startswith(("-", "|", "#"))]


def rows(text):
    out = [[c.strip() for c in l.strip().strip("|").split("|")] for l in text.splitlines()
           if l.startswith("|") and not re.match(r"\|\s*-", l)]
    return out[1:]


def lead(t):
    m = re.match(r"\*\*(.+?)\*\*\s*(.*)", t)
    return (m.group(1), m.group(2)) if m else ("", t)


# ---------- content ----------
byline = re.search(r"^Prepared by.*$", md, re.M).group(0)
status = re.search(r"^\*\*(Current working draft.*?)\*\*\s*(.*)$", md, re.M)
why_p = paras(section("Why this matters").split("\n### ")[0])
purpose = why_p[0].replace("Purpose: ", "", 1)
goal = why_p[1].replace("Goal: ", "", 1)
why_body = why_p[2:]
beliefs_sec = section("Shared beliefs", 3)
lang = section("Language to get right")
lang_intro = paras(lang)[0]
cats = re.findall(r"^### (.+?)\n(.*?)(?=^### |\Z)", lang, re.S | re.M)
check = section("Check locally")
txny = section("Texas and New York, side by side", 3)
oq = bullets(section("Open questions"))
terms_sec = section("US terms and sources")
terms = rows(terms_sec)
tail = paras(terms_sec)
sources_p = next(p for p in tail if p.startswith("Sources"))
ai_note = next(p for p in tail if p.startswith("In an effort"))

toc = [("why", "01", "Why this matters", [("beliefs", "Shared beliefs")]),
       ("language", "02", "Language to get right", [(re.sub(r"\W+", "-", c[0].lower()).strip("-"), c[0]) for c in cats]),
       ("local", "03", "Check locally", [("texas-ny", "Texas and New York, side by side")]),
       ("questions", "04", "Open questions", []),
       ("appendix", "05", "US terms and sources", [])]

B = []
B.append('<header class="cover"><div class="hero"><div class="cover-art" aria-hidden="true"><span class="c1"></span>'
         '<span class="c2"></span><span class="c3"></span></div><div class="hero-inner">'
         '<p class="draft-tag lbl">Working draft</p><h1>ClassE US language guide</h1>'
         f'<p class="byline">{il(byline)}</p></div></div><div class="intro"><section class="purpose" aria-label="Purpose">'
         f'<div class="pp-row"><p class="pp-k lbl">Purpose</p><p class="pp-v">{il(purpose)}</p></div>'
         f'<div class="pp-row"><p class="pp-k lbl">Status</p><p class="pp-v" style="font-size:11pt;font-weight:500">{il(status.group(1) + " " + status.group(2))}</p></div>'
         '</section><nav class="cover-toc" aria-label="Contents"><p class="toc-head lbl">Contents</p><ol class="toc-main">')
for aid, n, t, subs in toc:
    B.append(f'<li><a href="#{aid}"><span class="toc-n lbl">{n}</span><span>{il(t)}</span></a>')
    if subs:
        B.append('<ul class="toc-sub">' + "".join(f'<li><a href="#{s_}">{il(st)}</a></li>' for s_, st in subs) + "</ul>")
    B.append("</li>")
B.append("</ol></nav></div></header>")
B.append('<div class="shell"><nav class="side" aria-label="Contents"><p class="side-head lbl">Contents</p><ul>')
for aid, n, t, subs in toc:
    B.append(f'<li class="nav-top"><a href="#{aid}">{il(t)}</a></li>')
    B += [f'<li><a href="#{s_}">{il(st)}</a></li>' for s_, st in subs]
B.append("</ul></nav><main>")

# 01 Why this matters + shared beliefs
B.append(f'<section id="why" class="band why"><div class="wrap"><p class="eyebrow lbl">01</p><h2>Why this matters</h2>'
         f'<p class="w-lead">{il(goal)}</p>')
B += [f'<p class="w-body">{il(p)}</p>' for p in why_body]
B.append(f'<div id="beliefs" class="spread"><h3 class="spread-h">Shared beliefs</h3><p class="sec-intro">{il(paras(beliefs_sec)[0])}</p><ol class="beliefs four">')
for b in bullets(beliefs_sec):
    t, body = lead(b)
    B.append(f'<li><div><p class="bel-t">{il(t)}</p><p class="bel-b">{il(body)}</p></div></li>')
B.append("</ol></div></div></section>")

# 02 Language to get right, by category
B.append(f'<section id="language" class="band pagestart"><div class="wrap"><p class="eyebrow lbl">02</p><h2>Language to get right</h2>'
         f'<p class="sec-intro">{il(lang_intro)}</p>')
for name, body in cats:
    cid = re.sub(r"\W+", "-", name.lower()).strip("-")
    note = paras(body)[0]
    rr = rows(body)
    B.append(f'<table class="sn said cat" id="{cid}"><thead><tr><th scope="col" class="lbl h-cat"></th>'
             f'<th scope="col" class="lbl h-not">{NOT_IC}Instead of</th><th scope="col" class="lbl h-say">{SAY_IC}Try</th>'
             '<th scope="col" class="lbl h-nt">What went wrong</th></tr></thead><tbody>')
    for k, (said, try_, why) in enumerate(rr):
        catcell = (f'<th scope="rowgroup" rowspan="{len(rr)}" class="cat-l"><h3>{il(name)}</h3><p>{il(note)}</p></th>' if k == 0 else "")
        B.append(f'<tr>{catcell}<td class="not"><span class="mlab lbl">{NOT_IC}Instead of</span>{il(said)}</td>'
                 f'<td class="say"><span class="mlab lbl">{SAY_IC}Try</span>{il(try_)}</td><td class="nt">{il(why)}</td></tr>')
    B.append("</tbody></table>")
B.append("</div></section>")

# 03 Check locally
B.append(f'<section id="local" class="band pagestart"><div class="wrap"><p class="eyebrow lbl">03</p><h2>Check locally</h2>'
         f'<p class="w-body">{il(paras(check)[0])}</p><ul class="plain-list">' + "".join(f"<li>{il(c)}</li>" for c in bullets(check)) + "</ul>")
B.append(f'<h3 id="texas-ny" class="sec-h">Texas and New York, side by side</h3><p class="tx-lead">{il(paras(txny)[0])}</p>'
         '<table class="cmp"><thead><tr><th class="lbl corner"></th><th scope="col" class="lbl"><span class="state-chip s1">Texas</span></th>'
         '<th scope="col" class="lbl"><span class="state-chip s2">New York and the Northeast</span></th></tr></thead><tbody>')
for label, t, n in rows(txny):
    B.append(f'<tr><th scope="row">{il(label)}</th><td><span class="mstate lbl"><span class="state-chip s1">Texas</span></span>{il(t)}</td>'
             f'<td><span class="mstate lbl"><span class="state-chip s2">New York and the Northeast</span></span>{il(n)}</td></tr>')
B.append("</tbody></table></div></section>")

# 04 Open questions
B.append('<section id="questions" class="band pagestart"><div class="wrap"><p class="eyebrow lbl">04</p><h2>Open questions</h2><div class="qbox"><ul>')
for q in oq:
    t, rest = lead(q)
    B.append(f"<li><strong>{il(t)}</strong> {il(rest)}</li>")
B.append("</ul></div></div></section>")

# 05 US terms and sources, AI note
B.append('<section id="appendix" class="band pagestart"><div class="wrap"><p class="eyebrow lbl">05</p><h2>US terms and sources</h2>'
         '<table class="terms"><tbody>')
for term, what in terms:
    B.append(f"<tr><th scope=\"row\">{il(term)}</th><td>{il(what)}</td></tr>")
B.append("</tbody></table>")
head_s, body_s = sources_p.split(": ", 1)
B.append(f'<p class="sources"><strong>{il(head_s)}:</strong> {il(body_s)}</p>'
         f'<p class="ai-note">{il(ai_note)}</p></div></section></main></div>')

doc = HEAD.replace("</head>", FONTS + OVERRIDES + "</head>") + BODY_TAG + SEARCHBAR + "".join(B) + SCRIPT + "</body></html>"
out_html = here / (out_name + ".html")
out_pdf = here / (out_name + ".pdf")
out_html.write_text(doc, encoding="utf-8")
print("HTML:", out_html)
chrome = os.environ.get("CHROME") or next((c for c in [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/opt/pw-browsers/chromium"] if Path(c).exists()), None)
if chrome:
    args = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
            f"--print-to-pdf={out_pdf}", out_html.as_uri()]
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        args.insert(1, "--no-sandbox")
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF:", out_pdf)
