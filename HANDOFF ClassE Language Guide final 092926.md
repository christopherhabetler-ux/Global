# HANDOFF: ClassE US Language Guide, working draft to send (092926)

## Status

v24 is the working draft. It's a language guide, not a pitch, and it's marked as a working draft at the top. All nine open decisions are settled or written as proposals. The PDF build is tested and comes out at 7 pages (repo file "PREVIEW ClassE US Language v24 092926.pdf").

Two things are left, and both need your Mac:
- merge the 092626 accuracy fixes, which exist only on disk
- port the v18 "If a buyer asks" items

## Your steps

1. Open a **fresh** Claude Code session in `~/Documents/CLAUDE/Projects/Sales Advisory/ClassE/LANGUAGE GUIDE/` and run `/model sonnet`.
2. Paste the prompt below.
3. Read page 1 and the seven-kinds table in the PDF it makes.
4. Send the email below with the PDF attached.

## Prompt for local Claude Code

```
Finalize the ClassE US language guide. The editorial work is done. This is a mechanical merge and build. Keep token use low: no subagents, no rubric or scorecard reruns, don't read whole files when diff or grep will do, don't render page images.

Working folder: ~/Documents/CLAUDE/Projects/Sales Advisory/ClassE/LANGUAGE GUIDE/

1. GET THE FILES. From GitHub repo christopherhabetler-ux/Global, branch claude/sweet-albattani-jnh10l, copy two files into _rebuild/:
   - "GUIDE ClassE US Language v24 DRAFT 092926.md"
   - "build guide pdf.py"
   Use: git clone --depth 1 -b claude/sweet-albattani-jnh10l https://github.com/christopherhabetler-ux/Global.git /tmp/cg (or gh repo clone). If both fail, stop and tell me.

2. MERGE THE 092626 FIXES. Run:
   diff "GUIDE ClassE US Language 092526.md" "GUIDE ClassE US Language 092626.md"
   For each change, grep a distinctive phrase from the OLD line in v24 and apply the NEW wording. A claim can appear in the seven-kinds table, the word list and Sources, so fix every copy. If the old line no longer exists in v24 (it's a shorter rewrite), apply citation fixes to Sources, and otherwise skip the change and log it. Keep v24's structure and wording everywhere else.

3. PORT FROM v18. Run:
   diff "GUIDE ClassE US Language 092626.md" "_rebuild/GUIDE ClassE US Language v18 DRAFT 092626.md"
   Take only the "If a buyer asks" items and add them as bullets under v24's "### If a buyer asks", after the i-Ready bullet. Skip anything else in the diff.
   Rules for ported text: keep it short, no definitions of teaching terms, and never call ClassE or a student "diagnostic," "an intervention," "mastered" or a tier.

4. SAVE AND BUILD. Save the result as "GUIDE ClassE US Language 092926.md" in the working folder, then run:
   python3 "_rebuild/build guide pdf.py" "GUIDE ClassE US Language 092926.md"
   If Chrome isn't found, open the HTML and Print, Save as PDF, with headers and footers off.

5. CHECK.
   - grep -ciE 'TODO|XX' "GUIDE ClassE US Language 092926.md" returns 0
   - mdls -name kMDItemNumberOfPages "GUIDE ClassE US Language 092926.pdf" shows 8 or fewer
   Fix anything that fails, rebuild once, and stop.

6. RECORD. Append one line to the Notion page "HANDOFF ClassE US Language Guide final 092926": "Built <MMDDYY>: <pdf path>. Merged N fixes from 092626, ported v18 items."

7. REPORT to me in under 15 lines: each change as "old -> new" in a few words, anything skipped and why, the page count, and the PDF path. Then open the PDF.
```

## Email to Matt and Joe

```
Subject: ClassE US language guide, working draft

Matt and Joe,

Attached is a working draft of the US language guide. It's meant to help all of us make word choices that describe ClassE accurately and show US educators we want what they want for teachers and students.

It isn't a script. Where it suggests wording, that's one option, and I expect we'll change some of it as we go.

A few places where it proposes moving away from words we've been using:
- "Diagnostic" and "intervention" as the first thing we say about ClassE. The guide describes what ClassE does instead, and treats intervention as a two-part answer: ClassE helps the teacher intervene, and Albert supports each student directly.
- "Mastery" off a single question, including on the report. "Progress toward mastery" works.
- Albert: before a call, we check the district's student-facing AI policy to decide how much to lead with him.

Most of the "sounds like" lines come from our own calls, including mine. They work in Israel. A US buyer hears them differently, so we keep the idea and change the word.

Take a look and tell me where you'd go a different way. Happy to walk through it together.

Christopher
```

## Resources, if the local session gets stuck

- Why the guide looks the way it does: Notion "REVIEW ClassE Language Guide usability 092826"
- Matt's original ask: Google Doc "ClassE U.S. Positioning & Messaging Workshop Takeaways," Next Steps 1
- Everything else: Notion "CONTEXT PACK — ClassE US Language Guide 092726"
