# Crosswalk System Improvements 092826

What changes in the crosswalk process, the `company-crosswalk` skill, and the run-kit generator, based on what broke during the 95 Percent Group build and what I found while prepping Benchmark. Each fix names the evidence that prompted it.

I wrote this from a cloud session. I couldn't open `~/Documents/CLAUDE/Skills/company-crosswalk/SKILL.md`, `make_kit.py`, or the 092426 RETRO file, so the skill and generator changes are written as a spec for a session on the Mac to apply (see the paste block at the bottom). I didn't guess at what those files currently say.

## The fixes

### 1. Gate 0: re-read Matt's latest email before building prompts, and again before drafting

- **Evidence.** During 95 Percent Group, the Lori lines went into the document before anyone read Matt's email ruling them out (Session Log 092426, "Mistakes Made"). This week it happened again in a new way. The Benchmark page, written 092426, says Matt has no hypothesis and that "nothing about who is in the room" is known. But his 092526 reply named the contact, called the meeting a second look, and gave a theory. The page and prompts were never updated.
- **Change.** Before Step 1, and again before Step 4, pull the latest Matt thread and rewrite `MEETING_CONTEXT.md` from it. The kit's run sheet gets a line: "Matt thread last read: [date]." Nobody pastes a prompt while that date is older than his latest email.

### 2. When Matt has a hypothesis, turn it into a test

- **Evidence.** On Canvas, Matt's hypothesis about the Mastery flag and reassessment was the spine the findings were tested against, and he called the result "absolutely nails it" (Session Log 092326). On 95 Percent Group, the hypothesis was "start cold." For Benchmark he has one again.
- **Change.** A hypothesis becomes three things: a proposition in Prompt 2 Task C that can fail, a named step in Prompt 3 (Step 2C in the Benchmark kit), and, when it's about other companies, a separate comparator run (Prompt 1B). That keeps Prompt 1 clean ("Benchmark only") and still tests the theory. The generator gets a `--hypothesis` flag.

### 3. Framing line opens with an upload receipt

- **Evidence.** The 95 Percent Group Grok seat came back empty because the upload was empty, and nobody caught it until the output was read (95 Percent Group landing page, 092326).
- **Change.** The framing line now tells the model to list each uploaded file with its first heading and length, and to stop if anything is empty. That catches it in seconds instead of after a 20-minute run. `file_outputs.py` already refuses empty outputs; this catches empty inputs.

### 4. Archive fallback in every research prompt and the quote chase

- **Evidence.** The 95 Percent Group document had to carry a callout saying the VP of Software Engineering posting was blocked and its quoted text "never confirmed."
- **Change.** Prompts 1, 1B and 2 and the quote chase try the Internet Archive for any blocked page, and record the archived URL and capture date. The quote chase gains a sixth field, LIVE or ARCHIVED.

### 5. Every "search results only" claim carries its query

- **Evidence.** The 95 Percent Group document says of TouchMath's closing, "we did not record the search behind that, so whether it closed is unknown." It also has three rows marked "from search results only."
- **Change.** Prompt 1 labels these SEARCH RESULT ONLY and records the query. Prompt 3 flags any that are load-bearing.

### 6. Describe the seat for outside models, and match the objections to the kind of meeting

- **Evidence.** Matt, 092326: "I don't necessarily need its take on how we should approach Lori." For 95 Percent Group the seat was a former product leader at a first look. For Benchmark it's a current leader at a second look.
- **Change.** No name goes to an outside model. The seat is written as a role plus the meeting type: first look, second look, or buyer. The generator gets a `--seat` string and a `--look first|second` flag, and the objections list is weighted by meeting type. A second look presses on what has changed since the first pitch.

### 7. A publisher-target axis preset with a rights test

- **Evidence.** The generator's default axis is the intervention sequence built for 95 Percent Group (run-kit page, 092326). The Benchmark page had to hand-edit the axis to fit a core-curriculum publisher. By the kit's own rule ("change it in `make_kit.py`, not in the run folder"), that edit is owed back to the generator. Benchmark is also the first target that owns its content, which changes the ingestion-rights OPEN QUESTION in the ClassE brief.
- **Change.** Add `--axis-type publisher`. It swaps in the core-curriculum axis, adds "content licensing and partners," adds test K (publisher rights: what changes, what doesn't, no status promotion), and adds test E's EdReports and state-adoption risk. BrainPOP will likely need its own preset (supplemental content and video), which gets decided when its kit is built.

### 8. Christopher's read moves to the start

- **Evidence.** Crosswalk ops facts 092426: "his Intersection line was the best sentence in the 95PG document and arrived last."
- **Change.** The run sheet asks for the three-question read (gut read, where the target sits, the one question Matt should be able to answer) in the same sitting as Prompt 3, not after the claim register.

### 9. A slip trigger with a pre-written fallback

- **Evidence.** The Benchmark schedule had the research sitting on Sat 9/26 and drafting on Mon 9/28. As of Monday evening the parent task still reads "Not started," with delivery Wed 9/30.
- **Change.** Each kit's run sheet carries a trip-wire: if the Step 3 answer isn't in by T-1 at noon, send the fallback line to Matt (it's written into the Benchmark prompt file) and take one extra day, as long as that still leaves four days before his meeting.

### 10. Hub status stops drifting

- **Evidence.** As of 092826 the Crosswalk Mini Hub still said "95 Percent Group, owed today, Wednesday 9/23" and "Benchmark Education, then BrainPOP. Both parked until Matt gives dates." Both dates landed 092526.
- **Change.** I updated the hub today. Going forward, each step's close-out includes a one-line hub status edit, and the skill's "done" checklist names that edit.

## Applied today (092826)

- Benchmark prompts rebuilt as `Benchmark Crosswalk Research Prompts 092826.md` in this repo, and pasted into the Benchmark Notion landing page.
- Benchmark landing page: meeting section rewritten from Matt's 092526 email, and schedule reset.
- Crosswalk Mini Hub: status set to Benchmark active (due Wed 9/30), BrainPOP next (meeting Mon 10/12, deliver Wed 10/7).
- This file, with a Notion copy on the run-kit page.

## Still to apply on the Mac

Paste this into a Claude Code or Cowork session that has `~/Documents` mounted:

```
Apply the crosswalk improvements from "Crosswalk System Improvements 092826.md" (GitHub christopherhabetler-ux/global, branch claude/sharp-dijkstra-rnbepa; the same text is on the Notion run-kit page). Read ~/Documents/CLAUDE/Skills/company-crosswalk/SKILL.md, the crosswalk-kit make_kit.py, and ClassE/CROSSWALKS/RETRO — crosswalk process after 95 Percent Group 092426.md first. Then:

1. SKILL.md: add Gate 0 (re-read Matt's latest thread before Step 1 and before Step 4; record "Matt thread last read" in the run sheet), the hypothesis-to-test rule, the seat rule (role plus first/second look, never a name to an outside model), the three-question read moved to the Prompt 3 sitting, the slip trip-wire, and the hub status line in the done checklist. Keep every existing gate and failure mode; add these as new items with their evidence lines.
2. make_kit.py: add --hypothesis, --seat, --look first|second, and --axis-type intervention|publisher. The publisher preset uses the axis, tests E and K, Step 2C, and objections item 11 from "Benchmark Crosswalk Research Prompts 092826.md". Put the upload-receipt sentence at the start of the shared framing line, the archive fallback in the shared method block, the SEARCH RESULT ONLY rule in Prompt 1, and the LIVE/ARCHIVED field in the quote chase. When --hypothesis names other companies, emit Prompt 1B too.
3. Regenerate the sample kit, diff it against the Benchmark prompt file, and report any wording that differs.
4. Log a Session Log entry and update the Notion run-kit page with the new generator ZIP.
Don't change any file in a delivered crosswalk folder.
```
