# HANDOFF: ClassE US Language Guide, final and send (092926)

## Status

v19 is written and a PDF preview has been built (14 pages). The layout and build script are tested. Two things are left that need your Mac:
- merge the 092626 accuracy fixes, which exist only on disk
- port the v18 "If a buyer asks" box

After that, build the PDF and send.

## Your steps

1. Open a **fresh** Claude Code session in `~/Documents/CLAUDE/Projects/Sales Advisory/ClassE/LANGUAGE GUIDE/` and run `/model sonnet`. The thinking is done, so this part is mechanical.
2. Paste the prompt below.
3. Read page 2 (the nine decisions) and the short version in the PDF it makes. That's your relationship on the line, so it's the one read you shouldn't skip.
4. Send the email below with the PDF attached.

## Prompt for local Claude Code

```
Finalize the ClassE US language guide. The editorial work is done. This is a mechanical merge and build. Keep token use low: no subagents, no rubric or scorecard reruns, don't read whole files when diff or grep will do, don't render page images.

Working folder: ~/Documents/CLAUDE/Projects/Sales Advisory/ClassE/LANGUAGE GUIDE/

1. GET THE FILES. From GitHub repo christopherhabetler-ux/Global, branch claude/sweet-albattani-jnh10l, copy two files into _rebuild/:
   - "GUIDE ClassE US Language v19 DRAFT 092926.md"
   - "build guide pdf.py"
   Use: git clone --depth 1 -b claude/sweet-albattani-jnh10l https://github.com/christopherhabetler-ux/Global.git /tmp/cg (or gh repo clone). If both fail, stop and tell me. Don't rebuild from Notion.

2. MERGE THE 092626 FIXES. Run:
   diff "GUIDE ClassE US Language 092526.md" "GUIDE ClassE US Language 092626.md"
   For each change, grep a distinctive phrase from the OLD line in the v19 file and apply the NEW wording. The same claim can appear up to three times in v19: a section example, the A-to-Z word list, and Sources. Fix every copy. If the old line no longer exists in v19 (v19 cut explanations of teaching terms and moved legal citations to Sources), apply the fix to Sources if it's a citation, and otherwise skip it and log it. Keep v19's structure and wording everywhere else.

3. PORT THE v18 BOX. Run:
   diff "GUIDE ClassE US Language 092626.md" "_rebuild/GUIDE ClassE US Language v18 DRAFT 092626.md"
   Take only (a) the "If a buyer asks" box and (b) the "Usage is not a result" line. Skip the IEP line; v19 already has it.
   - Put (a) in v19 as "### If a buyer asks", directly after the "### If a word goes wrong in the call" list, as a short bulleted list.
   - Add (b) to the "Claims we have not measured, and sales talk" bullet in "Seven kinds of words that land wrong."
   - v19 rules for ported text: no definitions of teaching terms. Never use diagnose, intervention, progress monitoring, mastery, proficient, exercise or tier as a name for ClassE or a student.

4. SAVE AND BUILD. Save the result as "GUIDE ClassE US Language 092926.md" in the working folder (no DRAFT in the name). Then run:
   python3 "_rebuild/build guide pdf.py" "GUIDE ClassE US Language 092926.md"
   That writes the .html and .pdf next to it. If Chrome isn't found, open the HTML and Print, Save as PDF, with headers and footers off.

5. CHECK. Each of these must be true:
   - grep -n '^- Say' "GUIDE ClassE US Language 092926.md" | grep -iE 'diagnos|mastery|proficien|progress monitoring|intervention|exercise' returns nothing
   - grep -ciE 'draft|TODO|XX' "GUIDE ClassE US Language 092926.md" returns 0
   - mdls -name kMDItemNumberOfPages "GUIDE ClassE US Language 092926.pdf" shows 16 or fewer
   Fix anything that fails, rebuild once, and stop.

6. RECORD. Append one line to the Notion page "GUIDE ClassE US Language v19 DRAFT 092926": "Final built <MMDDYY>: <path to pdf>. Merged N fixes from 092626, ported v18 box."

7. REPORT to me in under 15 lines: each change as "old -> new" in a few words, anything skipped and why, the page count, and the PDF path. Then open the PDF.
```

## Email to Matt and Joe

```
Subject: ClassE US language guide, for your review

Matt and Joe,

Attached is the US language guide. It flags the words a US educator can hear as outdated, controversial or unintentionally offensive, and gives the word to use instead.

One thing I need from you before it goes to the team. The page right after the introduction lists nine words we have used ourselves, in the workshop takeaways and in the product, where the guide recommends something different. Each row says how a US buyer may hear it. A few are clearly your call, like the category name and "exercise," and "mastery" on the report is a product decision. Once you decide, I'll take that page out and update the word list to match.

How the team uses it:
- Before a call or demo: the short version.
- Before a deck or email goes out: the A-to-Z word list at the back.
- In a call: the four lines under "If a word goes wrong."

Most of the Not lines come from our own calls, including mine. They work in Israel. A US buyer hears them differently, so we keep the idea and change the word.

Happy to walk through it together.

Christopher
```

## Resources, if the local session gets stuck

- v19 text: Notion "GUIDE ClassE US Language v19 DRAFT 092926", or the repo file above
- Why v19 looks the way it does: Notion "REVIEW ClassE Language Guide usability 092826"
- Matt's original ask: Google Doc "ClassE U.S. Positioning & Messaging Workshop Takeaways," Next Steps 1
- Everything else: Notion "CONTEXT PACK — ClassE US Language Guide 092726"
