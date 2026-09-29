# Benchmark Crosswalk Research Prompts 092826

Benchmark Education × ClassE, for Matt Campbell. Rebuilt 092826 from the 092426 kit, because Matt's 092526 email changed the brief after the kit was written.

- **Delivery to Matt:** Wed 09/30/26. Christopher promised it in his 092426 email and Matt answered "that works."
- **Matt's meeting:** Mon 10/05/26 at 10:30.
- **Notion landing page:** https://app.notion.com/p/3e505467120c81708348f1cc48180884
- **Drop folder (on the Mac):** `~/Downloads/crosswalk-drops/Benchmark/`, with the two ClassE files already in `_upload-these/`.

## What changed since the 092426 kit

The 092426 page says Matt gave no hypothesis and nothing about who's in the room. His 092526 reply gave both:

> "I'm meeting with Amy Philippon. She was in the Sharktank, so this is a second look. I don't know a lot about Benchmark. Actually, very little. I just have a theory that the big publishers (MH, HMH, Savaas) already have somethign similar, but the medium and small publishers (of which there are many) may be interested in partnership to help them catch up."

Also from that thread: "Just keep the same format as the most recent draft. You nailed it." He reads the report beforehand "to inform myself about gaps and to guide the questions I might ask," not during the call. He wants the .md as well as the PDF.

That changes three things in the prompts:

1. **Matt's theory is now something to test, not a premise.** The research prompt checks both halves: whether the three largest publishers already ship something like ClassE, and where Benchmark actually sits. Prompt 3 tests it again against Benchmark's own plans.
2. **Benchmark is a publisher, so rights look different.** Ingestion rights are an OPEN QUESTION in the ClassE brief. When the partner owns the content, that question changes shape, but the claim doesn't get promoted. Prompt 3 now tests this directly.
3. **The seat is a second look, not a first.** The objections list is weighted toward what someone who has already seen a ClassE pitch would press on. The seat is described by role only, and no name goes to an outside model.

Carried forward from the 95 Percent Group build: an upload-receipt check in the framing line (the Grok file came back empty last time), an archive fallback in the quote chase (the job-posting quote was never confirmed), and a search perimeter on every "search results only" claim (the TouchMath closing had none).

## Two prompts, three runs, one sitting tonight

Revised 092826 at 9pm ET, cut from four prompts to two. The research prompt goes into Perplexity and Gemini unchanged, in separate chats, the same way the Zeta prompt went into ChatGPT and Gemini. Where the two answers disagree, that's the cross-check. Prompt 3 is the red team.

| Step | Where | Uploads | Save as |
|---|---|---|---|
| 1 | Research prompt in Perplexity (deep research) | none | `01 Perplexity.md` |
| 1 | Same prompt in Gemini (deep research), at the same time | none | `02 Gemini.md` |
| - | Your read, while those two run (questions at the bottom) | none | `00 My read.md` |
| 2 | Prompt 3 in GPT-5 Pro, web on, after both land | 01, 02, and both files in `_upload-these/` (four files) | `03 GPT-5 Pro.md` |
| - | Grok, only if Claude asks; never sees 03 | same four | `04 Grok.md` |

- Gemini shows a research plan first. Click Start research without editing it.
- If Prompt 3 starts after 11pm, let it run and save the answer in the morning.
- Tue after the 3:30 Zeta call, Claude does the quote chase, claim register, draft and blind review. Wed morning you read the PDF and send it to Matt.

**If Prompt 3 slips past Tue noon,** send Matt this line and take Thu 10/01. That still gives him four days before his meeting:

```
Matt, quick heads up: Benchmark will land Thursday 10/1 instead of Wednesday. I want one more verification pass on the digital-product claims before it reaches you. Still four days ahead of your 10/5 meeting.
```

## Standing rules (unchanged)

1. Perplexity and Gemini output are finding aids. Only a reopened primary source counts as evidence.
2. Never upload Matt's canonical ClassE knowledge base or any pre-092126 draft to an outside model. Upload only the two files in `_upload-these/`.
3. Never show one adversarial seat the other seat's output.
4. Keep Matt's status labels: CONFIRMED/STRONG, WORKING POSITION, HYPOTHESIS, OPEN QUESTION, DO NOT CLAIM.
5. ClassE has no published efficacy study and no ESSA tier. Don't imply otherwise.
6. Don't claim whole-curriculum ingestion, equal-difficulty Twin Questions, settled category language, or broad causal outcomes.
7. A finding of no material fit is useful. Don't manufacture a gap.
8. A URL alone is not evidence. A claim needs a working source plus an exact quote or page reference.
9. Nothing about the person in the meeting goes to an outside model or into the document. Describe the seat, never the individual.

---

## Prompt 1: research (paste into Perplexity and Gemini, separate chats)

```
You are the lead researcher for a high-stakes competitive-intelligence brief on Benchmark Education Company, the K-8 literacy curriculum publisher. Build an auditable, sourced picture of the company. Accuracy matters more than volume, and "not found" is an acceptable answer. Do not recommend a partnership, and do not compare Benchmark to other companies except in Part 3.

PART 1, BENCHMARK
1. Portfolio. Every current product and named component: exact name, current edition, grade span, subject and language, buyer, user, print or digital, and how the products relate. Names to check, not facts to assume: Benchmark Advance, Benchmark Adelante, Benchmark Workshop, Benchmark Universe, and any phonics, intervention, assessment, or English-learner products. Confirm each name is current and add any that are missing.
2. The grades 4 to 6 classroom, week to week: lesson sequence, texts, student practice, feedback after an error, assessment, reteaching, reporting, and teacher workflow. Report grades 4 to 6 separately from K to 3 wherever the sources allow.
3. After an assessment flags a student: what happens next, which product supplies the follow-up material, and whether that step is digital, print, or teacher-delivered.
4. The digital platform: what students actually do in it, whether it responds on its own after a wrong answer (hint, feedback, follow-up item) or leaves that to the teacher, and any public evidence of generative AI, adaptive practice, or automatically generated items. Absence from a marketing page is not evidence of absence.
5. Integrations and partners: rostering, LTI, QTI, data export, gradebook, and whether Benchmark licenses its content or data to third-party platforms or names technology partners.
6. Evidence: for every efficacy study, the exact product and edition, author and funder, design, comparison group, sample, measures, findings, limitations, and the claimed ESSA tier versus what the design appears to meet. Include EdReports ratings by edition and grade band, and state adoption records.
7. The last 24 months: releases, leadership, acquisitions, partnerships, job postings, AI statements, and state adoptions.
8. Company facts: ownership, headquarters, CEO and product leadership, and any published figures on size or adoption footprint. Report only what a source states; do not estimate.

PART 2, TEST THESE PROPOSITIONS
For each, say SUPPORTED, CONTRADICTED, or UNVERIFIED, with the quote that decides it:
1. Benchmark is primarily a core ELA curriculum publisher.
2. Its digital platform delivers student practice with automatic feedback, not just digital versions of print materials.
3. Its assessments drive reteaching inside the program, and the program supplies the reteaching materials.
4. Its evidence base is independent of the company.
5. A current product uses generative AI, adaptive practice, or automatically generated items.
6. Benchmark licenses content to, or integrates with, third-party practice or assessment platforms.
7. Benchmark has announced, or is visibly building (roadmap, job postings, acquisitions), AI-generated or adaptive student practice of its own.

PART 3, TEST A MARKET HYPOTHESIS
Hypothesis: "The largest K-8 ELA publishers (McGraw Hill, HMH, Savvas) already offer something similar to AI-generated, curriculum-connected student practice with feedback. Medium and smaller publishers generally do not, and may look for a technology partner to catch up." Test it; don't prove it.
- "Something similar" means a capability live today (not a pilot or an announcement) that does at least two of these on the publisher's own grades 3 to 8 ELA content: generates or adapts practice items; responds to a wrong answer with feedback and a follow-up item on the same skill; reports item-level skill gaps to the teacher. Math-only or writing-feedback-only features don't count.
- For each of the three: the named capability, live, pilot, or announced, and whether it was built, bought, or partnered.
- Where Benchmark sits relative to them, using published indicators only.
- Any publisher and AI-partner pairings announced in the last 24 months.
- A verdict in 150 words or fewer: which half of the hypothesis holds, which fails, and what public research can't settle.

METHOD
- Source priority: product manuals, support documentation and release notes first; then efficacy reports and EdReports; then state and district records; then press releases, interviews and job postings; then trade press; marketing pages only when nothing better exists.
- "Benchmark" is a common word. Keep only sources about Benchmark Education Company. Exclude generic "benchmark assessment" results and other companies with Benchmark in the name, and flag any source where it's unclear which company is meant.
- Trace repeated claims to their earliest source, and treat copies of one claim as one origin, not corroboration.
- Mark company-funded, company-commissioned, and independent evidence separately. Don't infer today's functionality from a study of an older edition.
- If a page is blocked or gone, try the Internet Archive and record the archived URL and capture date. Otherwise record it as blocked.
- If a claim rests only on a search snippet or an aggregator, label it SEARCH RESULT ONLY and record the query.
- Every negative finding lists exactly what was checked: which documents, which release-note period, which search terms.

OUTPUT
1. Source ledger, one row per claim: claim | URL | publication date | exact quote | page or section | origin family | independent or company
2. Portfolio table
3. Evidence register, one row per study
4. The Part 2 proposition results
5. The Part 3 market table and verdict
6. Claims safe to use, claims needing a hedge, claims to exclude
7. Blocked sources, and the ten questions public research could not settle

Do not draft a comparison with any other product. Do not cite yourself or another AI as a source.
```

## Prompt 3: GPT-5 Pro (after both research answers land)

New conversation, web research on. **Upload four files:** `01 Perplexity.md`, `02 Gemini.md`, and the two files in `_upload-these/`. Paste the framing line, then the prompt. Save as `03 GPT-5 Pro.md`.

Framing line, paste first:

```
Before anything else, list each uploaded file by name with its first heading and roughly how long it is. If any file is empty, unreadable, or missing, stop and tell me which one; do not continue. Then read all four files before answering. The Perplexity and Gemini files answer the same research prompt; treat their disagreements as findings to settle against the source. Both are finding aids, not evidence. The ClassE research brief controls every ClassE claim. Reopen disputed sources on the web.
```

Prompt 3:

```
You are the red-team intelligence analyst. Your job is to prevent a false or inflated Benchmark × ClassE crosswalk from reaching Matt Campbell. Assume the apparent gaps may be wrong. Try to disprove them.

INPUT AUTHORITY
1. The ClassE research brief (uploaded) controls every ClassE claim
2. Verified primary sources
3. Independent corroboration
4. Perplexity and Gemini outputs only as finding aids, never as evidence

STEP 1, BUILD THE AXIS
Build the comparison axis from Benchmark's actual operating model as the uploaded files establish it. If Benchmark is primarily a core curriculum publisher, the axis runs: adopted core curriculum and texts; lesson sequence; assessment; what happens after an assessment flags a student; reteaching and practice materials; feedback after an error; progress monitoring; reporting; digital platform and integrations; content licensing and partners; evidence and EdReports ratings; professional learning. Do not import an intervention-company axis. Concentrate on grades 4 to 6 ELA, which is ClassE's live US scope, and say where Benchmark's grades 4 to 6 materials differ from its K to 3 materials.

STEP 2, ATTACK EVERY GAP
For each proposed gap, test whether:
A. the capability already exists in another Benchmark product or edition
B. a partner, service, or teacher workflow fills it
C. the absence is deliberate and pedagogically important
D. the proposed ClassE addition would conflict with the program's design or scope and sequence
E. the addition would require new efficacy validation, or could put an EdReports rating or state adoption at risk
F. ClassE's own capability is unverified, limited, or marked DO NOT CLAIM in the brief
G. the gap is too narrow or immaterial to matter
H. the finding depends on silence in public marketing
I. the gap is BUILD-SHAPED rather than PARTNER-SHAPED: Benchmark intends to own that step itself. Check roadmap statements, job postings, acquisitions, and executive interviews.
J. the apparent opening is a capability ClassE merely also has, rather than a missing step in Benchmark's existing workflow
K. PUBLISHER RIGHTS. Benchmark owns its content. The brief lists the copyright and publisher authorization model for ingestion as an OPEN QUESTION. State what changes about that question when the partner is the rights holder, and what does not: quality control of generated items on Benchmark's texts, editorial and brand review, alignment to Benchmark's scope and sequence, and data ownership. Do not promote any ClassE ingestion claim above its status in the brief.

STEP 2B, THE WORKFLOW-STOP TEST
Answer in order before judging any gap:
1. What job does Benchmark already do exceptionally well?
2. Where does its current workflow stop?
3. What manual work does a teacher or district do after Benchmark's product produces its output?
4. Does ClassE naturally begin where Benchmark stops?
5. Would ClassE strengthen Benchmark's core product, or add another overlapping feature?
6. Is there a roadmap initiative that closes the gap?
7. Can ClassE technically access the trigger data and return useful data?
8. What proof would Benchmark require before exposing ClassE to its customers?
9. What is the smallest realistic partnership step that creates evidence for a deeper one?

STEP 2C, THE MARKET HYPOTHESIS
Using Part 3 of both research files and your own reopened sources, test this working hypothesis: "The largest K-8 ELA publishers (McGraw Hill, HMH, Savvas) already offer something similar; medium and smaller publishers generally do not, and may look for a partner to catch up." Answer separately:
1. Does the evidence show the three largest publishers have a live capability similar to ClassE's loop in grades 3 to 8 ELA? Name it, or say what was checked.
2. Does the evidence place Benchmark among the medium or smaller publishers the hypothesis describes? Cite the indicator.
3. Does Benchmark already have, or publicly plan, its own version? If so, the partner half of the hypothesis fails for Benchmark specifically, whatever holds for the market.
4. Which half of the hypothesis survives, which fails, and which public research cannot settle.

STEP 3, CHECK EVIDENCE FAILURE
Flag circular sourcing, duplicated origin families, inaccessible citations, edition mismatch, product-family confusion, commissioned research described as independent, claimed ESSA tier treated as proven, negative findings without a search perimeter, SEARCH RESULT ONLY claims used as load-bearing, and confidence unsupported by source quality.

STEP 4, FORCE THE OPPOSITE CASE
Write the strongest evidence-based case that ClassE adds little or nothing to Benchmark. Then the strongest evidence-based case for a narrow addition. Compare which needs fewer unsupported assumptions.

OUTPUT
1. Red-team verdict, 300 words or fewer
2. Claim-by-claim contradiction matrix
3. Provisional capability table on Benchmark's own terms
4. Gaps that survived
5. Gaps rejected, with the exact reason
6. The market-hypothesis result from Step 2C, 200 words or fewer
7. ClassE claims downgraded under the brief's status labels
8. Questions public research cannot settle
9. Source and search-perimeter defects to repair
10. Recommendation: proceed to synthesis, another research pass, or stop
11. THE SEAT'S OBJECTIONS. The meeting is a second look. A senior Benchmark leader saw an early ClassE pitch once before, at a panel where several publisher executives heard edtech companies pitch, and has agreed to look again. Write the twelve hardest questions that seat would ask, ranked by how much damage an unprepared answer does. Weight toward what a second look presses on: what has changed since the first pitch, evidence of results, whether ClassE understands how a core ELA program is taught, quality control of AI-generated items on a publisher's own texts, content and data rights, and how ClassE fits or collides with Benchmark's own digital platform. For each, give the strongest honest answer the evidence supports, and a plain "no good answer yet" where there is none. Not a talk track, and no advice on how to run the meeting.

Do not write sales advice. Do not reward novelty. A conclusion of no material fit is acceptable. Give source, URL, date, and exact quote for every substantive claim.
```

## Grok tiebreak (only if Claude asks)

Separate conversation. Same four uploads, same framing line, same Prompt 3. It must never see `03 GPT-5 Pro.md`. Save as `04 Grok.md`. Claude asks for this only when the GPT-5 Pro verdict is close or thin.

## Prompt 3B: quote chase (Claude runs this with web tools; paste only if Claude hands it to you)

Run after Step 3, only on the claims that survived.

```
For each claim ID below, open the cited source and return ONLY these six fields, one line per claim:

CLAIM ID | the exact verbatim sentence from the page that supports the claim | the section heading or page number where that sentence appears | the URL you actually opened | the date you accessed it | LIVE or ARCHIVED (with capture date)

RULES
- Do not paraphrase and do not summarize. I need the sentence as written.
- If the source does not contain a sentence supporting the claim as worded, write NO SUPPORTING SENTENCE and then quote the closest thing you did find.
- If the page is gone, paywalled, redirected or materially changed, try the Internet Archive. If an archived copy supports it, mark ARCHIVED with the capture date. If not, write BLOCKED, say which, and stop on that row.
- Never substitute a sentence from a different page to fill a gap. A near miss I can see is worth more to me than a confident replacement I cannot check.
- If the supporting sentence is marketing copy rather than documentation, say so on the line.
- Do not re-argue whether the claim is true. Only report what the page says.

CLAIM IDS AND THEIR CITED SOURCES:
[paste the surviving claim IDs with the source each one points to]
```

## Your read (tonight, while the research runs)

Three to five sentences, or a voice memo. Save it as `00 My read.md` in the drop folder. Last time your Intersection line was the best sentence in the 95 Percent Group document, and it arrived last. This time it comes first. Answer these three:

1. What's your gut read on Benchmark: what does it do best, and where do you think it stops?
2. Given Matt's theory about big and smaller publishers, where do you think Benchmark falls, and why?
3. What's the one question you'd want Matt to be able to answer after reading this?
