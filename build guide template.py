#!/usr/bin/env python3
"""Build the ClassE US language guide in the 092726 house template.

Takes the head (fonts, CSS), search bar and search script from the 092726 HTML,
fills the body from the guide Markdown, and prints the PDF with Chrome.
Usage: python3 "build guide template.py" <template.html> <guide.md> <output name>
"""
import html
import os
import re
import subprocess
import sys
from pathlib import Path

tpl_path, md_path, out_name = sys.argv[1], sys.argv[2], sys.argv[3]
tpl = Path(tpl_path).read_text(encoding="utf-8")
md = Path(md_path).read_text(encoding="utf-8")

HEAD = tpl[: tpl.find("<body")]
BODY_TAG = re.search(r"<body[^>]*>", tpl).group(0)
SEARCHBAR = tpl[tpl.find(BODY_TAG) + len(BODY_TAG): tpl.find('<header class="cover">')]
SCRIPT = tpl[tpl.rfind("<script"): tpl.rfind("</body>")]
BUBBLE = re.search(r'<svg class="bubble-ic".*?</svg>', tpl, re.S).group(0)
SAY_IC = ('<svg class="ic" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#0F52C1"/>'
          '<path d="M5.6 10.4l2.9 2.9 5.9-6.6" stroke="#fff" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
NOT_IC = ('<svg class="ic" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#A23B32"/>'
          '<path d="M6.6 6.6l6.8 6.8M13.4 6.6l-6.8 6.8" stroke="#fff" stroke-width="2.3" stroke-linecap="round"/></svg>')


def smart(t):
    t = re.sub(r'(^|[\s(\[\u2014-])"', "\\1\u201c", t)
    t = t.replace('"', "\u201d")
    t = re.sub(r"(\w)'", "\\1\u2019", t)
    t = re.sub(r"'", "\u2019", t)
    return t


def il(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return smart(t)


def section(title):
    m = re.search(r"^#{2,3} " + re.escape(title) + r"\n(.*?)(?=^#{2,3} |\Z)", md, re.S | re.M)
    return m.group(1).strip()


def bullets(text):
    return [re.sub(r"^(- |\d+\. )", "", l) for l in text.splitlines() if re.match(r"(- |\d+\. )", l)]


def paras(text):
    return [p.strip() for p in text.split("\n\n") if p.strip() and not p.strip().startswith(("-", "|", "1."))]


def rows(text):
    out = []
    for l in text.splitlines():
        if l.startswith("|") and not re.match(r"\|\s*-", l):
            out.append([c.strip() for c in l.strip().strip("|").split("|")])
    return out[1:]


def split_lead(t):
    m = re.match(r"\*\*(.+?)\*\*\s*(.*)", t)
    return (m.group(1), m.group(2)) if m else ("", t)


# ---------- content from the Markdown ----------
draft_note = re.search(r"^\*\*(This is the current working draft.*?)\*\*\s*(.*)$", md, re.M)
byline = re.search(r"^Prepared by.*$", md, re.M).group(0)
oq_sec = section("Open questions")
oq_intro = paras(oq_sec)[0]
oq = bullets(oq_sec)
why = section("Why this matters")
why_p = paras(why)
purpose = why_p[0].replace("Purpose: ", "", 1)
goal = next(p for p in why_p if p.startswith("Goal:")).replace("Goal: ", "", 1)
why_body = [p for p in why_p[1:] if not p.startswith(("Goal:", "Before a call"))]
use_line = next(p for p in why_p if p.startswith("Before a call"))
describe = section("What our words have to describe")
desc_p = paras(describe)
desc_b = bullets(describe)
beliefs = bullets(section("Our core beliefs"))
remember = bullets(section("Three things to remember"))
words = bullets(section("Words we use"))
words_intro = paras(section("Words we use"))
kinds_sec = section("Seven kinds of words that land wrong")
kinds = rows(kinds_sec)
kinds_rule = paras(kinds_sec)[0]
before = bullets(section("Before the call"))
recover = bullets(section("If a word goes wrong in the call"))
asks = bullets(section("If a buyer asks"))
tx = section("Texas and New York, side by side")
tx_lead = paras(tx)[0]
tx_rows = rows(tx)
wl = section("Word list, A to Z")
wl_key = paras(wl)[0]
wl_rows = rows(wl)
prod = section("For the product team")
terms_src = section("US terms and sources")
terms_p, sources_p = paras(terms_src)

# ---------- body ----------
B = []
B.append('<header class="cover"><div class="hero"><div class="cover-art" aria-hidden="true"><span class="c1"></span>'
         '<span class="c2"></span><span class="c3"></span></div><div class="hero-inner">'
         '<p class="draft-tag lbl">Working draft</p><h1>ClassE US language guide</h1>'
         f'<p class="byline">{il(byline)}</p></div></div><div class="intro">'
         '<section class="purpose" aria-label="Purpose">'
         f'<div class="pp-row"><p class="pp-k lbl">Purpose</p><p class="pp-v">{il("To guide us in making language choices that accurately reflect our product and our beliefs.")}</p></div>'
         f'<div class="pp-row"><p class="pp-k lbl">Goal</p><p class="pp-v">{il(goal)}</p></div>'
         f'<div class="pp-row"><p class="pp-k lbl">Status</p><p class="pp-v" style="font-size:11pt;font-weight:500">{il(draft_note.group(1) + " " + draft_note.group(2))}</p></div>'
         '</section>')
toc = [("questions", "01", "Open questions", []),
       ("why", "02", "Why this matters", []),
       ("onepage", "03", "The short version", [("believe", "Our core beliefs"), ("remember", "Three things to remember"),
                                                ("words", "Words we use"), ("kinds", "Seven kinds of words that land wrong"),
                                                ("before", "Before the call"), ("recover", "If a word goes wrong"), ("asks", "If a buyer asks")]),
       ("texas-ny", "04", "Texas and New York, side by side", []),
       ("reference", "05", "Word list, A to Z", []),
       ("appendix", "06", "Appendix", [("product", "For the product team"), ("terms", "US terms"), ("sources", "Sources")])]
B.append('<nav class="cover-toc" aria-label="Contents"><p class="toc-head lbl">Contents</p><ol class="toc-main">')
for aid, n, t, subs in toc:
    B.append(f'<li><a href="#{aid}"><span class="toc-n lbl">{n}</span><span>{il(t)}</span></a>')
    if subs:
        B.append('<ul class="toc-sub">' + "".join(f'<li><a href="#{s}">{il(st)}</a></li>' for s, st in subs) + "</ul>")
    B.append("</li>")
B.append("</ol></nav></div></header>")

B.append('<div class="shell"><nav class="side" aria-label="Contents"><p class="side-head lbl">Contents</p><ul>')
for aid, n, t, subs in toc:
    B.append(f'<li class="nav-top"><a href="#{aid}">{il(t)}</a></li>')
    B += [f'<li><a href="#{s}">{il(st)}</a></li>' for s, st in subs]
B.append("</ul></nav><main>")

# 01 Open questions
B.append(f'<section id="questions" class="band"><div class="wrap"><div class="oneline asks"><h3>Open questions</h3>'
         f'<p class="rem-note" style="margin:0 0 6pt">{il(oq_intro)}</p><ol>')
for i, a in enumerate(oq, 1):
    lead, rest = split_lead(a)
    B.append(f'<li><span class="rem-n lbl">{i}</span><p><strong>{il(lead)}</strong> {il(rest)}</p></li>')
B.append("</ol></div></div></section>")
# 02 Why
B.append('<section id="why" class="band why"><div class="wrap"><p class="eyebrow lbl">02</p><h2>Why this matters</h2>'
         f'<p class="w-lead">{il(purpose)}</p>')
B += [f'<p class="w-body">{il(p)}</p>' for p in why_body]
uses = [u.strip() + "." for u in use_line.rstrip(".").split(". ")]
B.append('<ul class="w-use">' + "".join(f"<li>{il(u)}</li>" for u in uses) + "</ul>")
B.append(f'<p class="w-body">{il(desc_p[0])}</p></div></section>')
B.append('<section id="describe" class="band"><div class="wrap"><div class="oneline"><h3>What our words have to describe</h3><ol>')
for i, b in enumerate(desc_b, 1):
    lead, rest = split_lead(b)
    B.append(f'<li><span class="rem-n lbl">{i}</span><p><strong>{il(lead)}</strong> {il(rest)}</p></li>')
last = desc_p[1]
first_sent, rest = last.split(". ", 1)
B.append(f'<li><span class="rem-n lbl">{len(desc_b) + 1}</span><p><strong>{il(first_sent)}.</strong> {il(rest)}</p></li>')
B.append("</ol></div></div></section>")

# 02 Short version
B.append('<section id="onepage" class="band believe"><div class="wrap"><p class="eyebrow lbl">03</p>'
         '<h2 class="display">The short version</h2><div id="believe" class="spread"><h3 class="spread-h">Our core beliefs</h3><ol class="beliefs">')
for i, b in enumerate(beliefs, 1):
    t, body = split_lead(b)
    B.append(f'<li><span class="bel-n lbl">{i}</span><div><p class="bel-t">{il(t)}</p><p class="bel-b">{il(body)}</p></div></li>')
B.append(f'</ol><p class="bel-foot">{il("Every part of this guide reflects one or more of these beliefs.")}</p></div></div></section>')

B.append('<section id="remember" class="band"><div class="wrap"><div class="remember"><h3>Three things to remember</h3><ol>')
for i, r in enumerate(remember, 1):
    m = re.match(r'(".*?")\s*(.*)', r)
    q, note = (m.group(1), m.group(2)) if m else (r, "")
    B.append(f'<li><span class="rem-n lbl">{i}</span><div><p>{il(q)}</p>' + (f'<p class="rem-note">{il(note)}</p>' if note else "") + "</div></li>")
B.append("</ol></div></div></section>")

B.append(f'<section id="words" class="band"><div class="wrap"><div class="oneline"><h3>Words we use</h3>'
         f'<p class="rem-note" style="margin:0 0 6pt">{il(words_intro[0])}</p><ol>')
for i, w in enumerate(words, 1):
    lead, rest = split_lead(w)
    B.append(f'<li><span class="rem-n lbl">{i}</span><p><strong>{il(lead)}</strong> {il(rest)}</p></li>')
B.append("</ol></div></div></section>")

B.append('<section id="kinds" class="band"><div class="wrap"><div class="rsec"><h3 class="rsec-h">Seven kinds of words that land wrong</h3>'
         '<div class="sub sub-direct"><table class="sn"><thead><tr><th scope="col" class="lbl h-cpt">Kind</th>'
         f'<th scope="col" class="lbl h-say">{SAY_IC}Try instead</th><th scope="col" class="lbl h-not">{NOT_IC}Sounds like</th></tr></thead><tbody>')
for kind, sounds, try_ in kinds:
    kl, kr = split_lead(kind)
    B.append(f'<tr><th scope="row" class="cpt">{il(kl)} <span style="font-weight:400">{il(kr)}</span></th>'
             f'<td class="say"><span class="mlab lbl">{SAY_IC}Try instead</span>{il(try_)}</td>'
             f'<td class="not"><span class="mlab lbl">{NOT_IC}Sounds like</span>{il(sounds)}</td></tr>')
B.append(f'</tbody></table></div><p class="note"><span class="note-tag lbl">Always</span> {il(kinds_rule)}</p></div></div></section>')

B.append('<section id="before" class="band"><div class="wrap"><div class="checklist"><h3>Before the call</h3><ul>')
B += [f'<li><span class="box" aria-hidden="true"></span><div><p>{il(b)}</p></div></li>' for b in before]
B.append("</ul></div></div></section>")
B.append(f'<section id="recover" class="band"><div class="wrap"><aside class="speech"><div class="speech-h">{BUBBLE}<h3>If a word goes wrong in the call</h3></div><ul>')
B += [f'<li class="bubble"><p>{il(r)}</p></li>' for r in recover]
B.append("</ul></aside></div></section>")
B.append('<section id="asks" class="band"><div class="wrap"><div class="oneline asks"><h3>If a buyer asks</h3><ol>')
for i, a in enumerate(asks, 1):
    lead, rest = split_lead(a)
    B.append(f'<li><span class="rem-n lbl">{i}</span><p><strong>{il(lead)}</strong> {il(rest)}</p></li>')
B.append("</ol></div></div></section>")

# 03 Texas and New York
B.append(f'<section id="texas-ny" class="band texas"><div class="wrap"><p class="eyebrow lbl">04</p><h2>Texas and New York, side by side</h2>'
         f'<p class="tx-lead">{il(tx_lead)}</p><table class="cmp"><thead><tr><th class="lbl corner"></th>'
         '<th scope="col" class="lbl"><span class="state-chip s1">Texas</span></th>'
         '<th scope="col" class="lbl"><span class="state-chip s2">New York and the Northeast</span></th></tr></thead><tbody>')
for label, t, n in tx_rows:
    B.append(f'<tr><th scope="row">{il(label)}</th><td><span class="mstate lbl"><span class="state-chip s1">Texas</span></span>{il(t)}</td>'
             f'<td><span class="mstate lbl"><span class="state-chip s2">New York and the Northeast</span></span>{il(n)}</td></tr>')
B.append("</tbody></table></div></section>")

# 04 Word list
B.append(f'<section id="reference" class="band reference"><div class="wrap"><p class="eyebrow lbl">05</p><h2 class="display">Word list, A to Z</h2>'
         f'<p class="ref-key">{il(wl_key)}</p><div class="rsec" id="word-list"><div class="sub sub-direct"><table class="sn"><thead><tr>'
         f'<th scope="col" class="lbl h-cpt">{NOT_IC}Word or phrase</th><th scope="col" class="lbl h-say">{SAY_IC}Try instead</th>'
         '<th scope="col" class="lbl h-nt">Why</th></tr></thead><tbody>')
for w, t, y in wl_rows:
    B.append(f'<tr><th scope="row" class="cpt">{il(w)}</th><td class="say"><span class="mlab lbl">{SAY_IC}Try instead</span>{il(t)}</td>'
             f'<td class="nt">{il(y)}</td></tr>')
B.append("</tbody></table></div></div></div></section>")

# 05 Appendix
B.append('<section id="appendix" class="band appendix"><div class="wrap"><div class="app-head"><p class="eyebrow lbl">06</p><h2 class="display">Appendix</h2></div>')
B.append(f'<div class="app-sec" id="product"><h3 class="rsec-h">For the product team</h3><p>{il(paras(prod)[0])}</p><ul>'
         + "".join(f"<li>{il(b)}</li>" for b in bullets(prod)) + "</ul></div>")
B.append('<div class="app-sec" id="terms"><h3 class="rsec-h">US terms</h3><dl class="glossary">')
for item in terms_p.replace("Terms: ", "", 1).split(". "):
    item = item.rstrip(".")
    if ", " not in item:
        continue
    k, v = item.split(", ", 1)
    B.append(f'<div class="acr"><dt>{il(k)}</dt><dd>{il(v[0].upper() + v[1:])}.</dd></div>')
B.append("</dl></div>")
src = sources_p.split(": ", 1)
B.append(f'<div class="app-sec" id="sources"><h3 class="rsec-h">Sources</h3><p>{il(src[0])}:</p><ul>'
         + "".join(f"<li>{il(s.strip().rstrip('.'))}.</li>" for s in re.split(r"\.\s+(?=[A-Z])", src[1]) if s.strip())
         + "</ul></div>")
B.append("</div></section></main></div>")

doc = HEAD + BODY_TAG + SEARCHBAR + "".join(B) + SCRIPT + "</body></html>"
out_dir = Path(md_path).resolve().parent
out_html = out_dir / (out_name + ".html")
out_pdf = out_dir / (out_name + ".pdf")
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
