#!/usr/bin/env python3
"""Build the ClassE US language guide: Markdown -> print HTML -> PDF.

No dependencies beyond python3 and Chrome/Chromium.
Usage: python3 "build guide pdf.py" "GUIDE ClassE US Language v19 DRAFT 092926.md" ["Output name"]
Writes "<Output name>.html" and "<Output name>.pdf" next to the input file.
"""
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

CSS = """
@page { size: Letter; margin: 0.6in 0.75in; }
* { box-sizing: border-box; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 10.5pt;
       line-height: 1.45; color: #1f2328; margin: 0; }
h1 { font-size: 22pt; margin: 0 0 4pt; color: #0b3d5c; }
h1 + p { color: #555; margin-top: 0; }
h2 { font-size: 15pt; color: #0b3d5c; border-bottom: 1.5px solid #0b3d5c;
     padding-bottom: 3pt; margin: 18pt 0 8pt; break-after: avoid; }
h3 { font-size: 12pt; color: #0b3d5c; margin: 14pt 0 5pt; break-after: avoid; }
p { margin: 0 0 7pt; }
ul, ol { margin: 0 0 8pt; padding-left: 18pt; }
li { margin-bottom: 3pt; }
hr { border: 0; break-after: page; margin: 0; height: 0; }
table { width: 100%; border-collapse: collapse; margin: 4pt 0 10pt; font-size: 9pt; }
thead { display: table-header-group; }
th { background: #0b3d5c; color: #fff; text-align: left; padding: 4pt 5pt; font-weight: 600; }
td { border-bottom: 0.75px solid #d0d7de; padding: 4pt 5pt; vertical-align: top; }
tr { break-inside: avoid; }
.pair { border: 0.75px solid #d0d7de; border-radius: 4pt; margin: 0 0 7pt;
        padding: 5pt 8pt; break-inside: avoid; }
.pair div { margin: 1.5pt 0; display: flex; }
.pair .k { flex: 0 0 30pt; font-weight: 700; }
.pair .q { color: #57606a; }
.say .k { color: #1a7f37; }
.not .k { color: #cf222e; }
.not { color: #57606a; }
.why { color: #424a53; font-size: 9.5pt; }
.why .k { color: #57606a; }
"""


def inline(text):
    text = html.escape(text, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)


def table(lines):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
    rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c or "--") for c in r)]
    head, body = rows[0], rows[1:]
    out = ["<table><thead><tr>"] + [f"<th>{inline(c)}</th>" for c in head] + ["</tr></thead><tbody>"]
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    return "".join(out) + "</tbody></table>"


def pair(first, rest):
    parts = [("say", first[len("Say"):])] + [
        (l.split(":", 1)[0].strip().lower(), l.split(":", 1)[1]) for l in rest
    ]
    out = ['<div class="pair">']
    for kind, txt in parts:
        label, qual = kind.capitalize(), ""
        if txt.startswith(","):  # "Say, in Texas: ..." -> qualifier before the line
            qual, txt = txt[1:].split(":", 1)
            qual = f'<em class="q">{inline(qual.strip())}:</em> '
        txt = txt.lstrip(":").strip()
        out.append(f'<div class="{kind}"><span class="k">{label}</span><span>{qual}{inline(txt)}</span></div>')
    return "".join(out) + "</div>"


def convert(md):
    lines = md.splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.strip() == "---":
            out.append("<hr>")
            i += 1
        elif m := re.match(r"(#{1,3}) (.*)", line):
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            i += 1
        elif line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i])
                i += 1
            out.append(table(block))
        elif line.startswith("- Say"):
            while i < len(lines) and lines[i].startswith("- Say"):
                first, i = lines[i][2:], i + 1
                rest = []
                while i < len(lines) and lines[i].startswith("\t"):
                    rest.append(lines[i].strip())
                    i += 1
                out.append(pair(first, rest))
        elif re.match(r"(- |\d+\. )", line):
            tag = "ol" if line[0].isdigit() else "ul"
            items = []
            while i < len(lines) and re.match(r"(- |\d+\. )", lines[i]) and not lines[i].startswith("- Say"):
                item = re.sub(r"^(- |\d+\. )", "", lines[i])
                items.append("<li>" + inline(item) + "</li>")
                i += 1
            out.append(f"<{tag}>{''.join(items)}</{tag}>")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"(#|\||- |\d+\. |---)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


def find_chrome():
    candidates = [
        os.environ.get("CHROME"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser"),
        "/opt/pw-browsers/chromium",
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    return None


def main():
    src = Path(sys.argv[1]).resolve()
    name = sys.argv[2] if len(sys.argv) > 2 else src.stem
    md = src.read_text(encoding="utf-8")
    title = re.search(r"^# (.*)", md, re.M).group(1)
    body = convert(md)
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
           f"<style>{CSS}</style></head><body>{body}</body></html>")
    out_html = src.with_name(name + ".html")
    out_pdf = src.with_name(name + ".pdf")
    out_html.write_text(doc, encoding="utf-8")
    print("HTML:", out_html)
    chrome = find_chrome()
    if not chrome:
        print("No Chrome found. Open the HTML in a browser and Print > Save as PDF (no headers/footers).")
        return
    args = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
            "--print-to-pdf-no-header", f"--print-to-pdf={out_pdf}", out_html.as_uri()]
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        args.insert(1, "--no-sandbox")
    subprocess.run(args,
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF:", out_pdf)


if __name__ == "__main__":
    main()
