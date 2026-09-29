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

1. **Matt's theory is now something to test, not a premise.** Prompt 1B is new, and it checks both halves: whether the three largest publishers already ship something like ClassE, and where Benchmark actually sits. Prompts 2 and 3 carry the theory as propositions that could fail.
2. **Benchmark is a publisher, so rights look different.** Ingestion rights are an OPEN QUESTION in the ClassE brief. When the partner owns the content, that question changes shape, but the claim doesn't get promoted. Prompt 3 now tests this directly.
3. **The seat is a second look, not a first.** The objections list is weighted toward what someone who has already seen a ClassE pitch would press on. The seat is described by role only, and no name goes to an outside model.

Carried forward from the 95 Percent Group build: an upload-receipt check in the framing line (the Grok file came back empty last time), an archive fallback in the quote chase (the job-posting quote was never confirmed), and a search perimeter on every "search results only" claim (the TouchMath closing had none).

## Run order (four runs, one sitting, plus your read)

| # | Model | Runs alongside | Uploads | Save the answer as |
|---|---|---|---|---|
| 1 | Perplexity, deep research | 1B and 2 | none | `01 Perplexity.md` |
| 1B | Perplexity, deep research, second tab | 1 and 2 | none | `01B Perplexity market.md` |
| 2 | Gemini Pro, deep research | 1 and 1B | none | `02 Gemini.md` |
| 3 | GPT-5 Pro, web on | after 1, 1B, 2 land | 01, 01B, 02, and both files in `_upload-these/` (five files) | `03 GPT-5 Pro.md` |
| 3T | Grok, only if Claude asks | never sees 03 | same five | `04 Grok.md` |

**Timing to hit Wed.** Start 1, 1B and 2 tonight (Mon 092826) before bed; they run unattended. Run 3 Tue morning, before Zeta prep. Your three-to-five-sentence read on Benchmark goes in the same Tue sitting (see "Your read" at the bottom). Claude handles the quote chase, claim register, draft and blind review Tue after the 3:30 Zeta call ends. You read the PDF Wed morning and send it to Matt Wed.

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
9. **New:** Nothing about the person in the meeting goes to an outside model or into the document. Describe the seat, never the individual.

---

## Prompt 1: Perplexity (deep research mode)

Use auto or deepest research mode, not a heavy thinking model. Save as `01 Perplexity.md`.

```
You are the source-discovery lead for a high-stakes competitive-intelligence brief on Benchmark Education Company. Build an auditable source universe about Benchmark only. Do not compare it to any other company and do not recommend a partnership.

RESEARCH QUESTIONS
1. What is the complete current product portfolio? Give exact product names, grade spans, subjects, languages, instructional purposes, print and digital components, and how the products relate. Names to check, not facts to assume: Benchmark Advance, Benchmark Adelante, Benchmark Workshop, Benchmark Universe, and any phonics, intervention, assessment, or English-learner products. Confirm each name is current and add any that are missing.
2. How does a grades 4 to 6 ELA classroom actually use the core program week to week: lesson sequence, texts, student practice, assessment, feedback after an error, reteaching, reporting, and teacher workflow? Report grades 4 to 6 separately from K to 3 wherever the sources allow.
3. What assessment does Benchmark provide, and what happens after an assessment flags a student who needs help? Name the product that supplies the follow-up material and say whether it is digital, print, or teacher-delivered.
4. What evidence supports each product? Identify the exact product and edition, population, study design, comparison group, sample, measures, findings, limitations, claimed ESSA tier, EdReports ratings by edition and grade band, state adoption records, and any funding or commissioning relationship.
5. What changed in the last 24 months? Search releases, support updates, leadership statements, acquisitions, partnerships, job postings, AI statements, state adoptions, and district procurement records.
6. Is there public evidence of generative AI, adaptive practice, automatically generated practice or assessment items, or student-facing conversational support in any Benchmark product? Absence from a marketing page is not evidence of absence.
7. What does the digital platform integrate with (rostering, LTI, QTI, assessment data export, gradebook), and does Benchmark license its content or data to third-party platforms or name technology partners?
8. Company facts: ownership (private, family, private-equity, or other), headquarters, current CEO and product leadership, and any published figures on size, number of states or districts served, or adoption footprint. Report only what a source states; do not estimate.

SOURCE PRIORITY
A. Product manuals, support documentation, implementation guides, release notes
B. Full efficacy reports and study appendices; EdReports reviews
C. Government, state adoption, district, and standards-body records
D. Executive interviews, press releases, job postings
E. Independent reviews and trade press
F. Marketing pages only when no better source exists

METHOD
- Search each research question separately. Do not stop after finding a company page.
- Trace every repeated claim to its earliest identifiable source.
- Mark company-funded, company-commissioned, and genuinely independent evidence separately.
- Record paywalls, login walls, removed pages, and inaccessible documents. For a blocked page, try the Internet Archive (web.archive.org) and record the archived URL and capture date if you use it.
- If a claim rests only on a search-result snippet or an aggregator, label it SEARCH RESULT ONLY and record the query that produced it.
- For a negative finding, list the exact manuals, support sections, release-note period, and search terms checked.
- If a citation does not directly support the claim, reject it.

OUTPUT
A source ledger grouped by Portfolio, Classroom Mechanics (grades 4 to 6), Assessment and Follow-up, Evidence, Strategy, AI and Digital Direction, Integrations and Partners, Company Facts, Independent Validation, and Blocked Sources. Each row: claim, direct URL, publication date, exact quote, page or section, origin family, contradictions. End with:
A. Ten highest-value primary sources
B. Ten claims most likely to be overstated
C. Ten unresolved questions for the next researcher

Do not draft a comparison. Do not cite Perplexity as a source. Do not treat a search-result snippet as evidence.
```

## Prompt 1B: Perplexity, second tab (market position check)

New in this kit. Run it in a separate Perplexity tab alongside Prompt 1. Save as `01B Perplexity market.md`.

```
You are a market researcher testing a working hypothesis about the US K-8 English language arts curriculum market. Test it; do not prove it. Either answer is useful.

THE HYPOTHESIS TO TEST
"The largest K-8 ELA curriculum publishers (McGraw Hill, HMH, Savvas) already offer something similar to AI-generated, curriculum-connected student practice with immediate feedback. Medium and smaller publishers generally do not, and may look for a technology partner to catch up."

WHAT "SOMETHING SIMILAR" MEANS HERE
A digital capability, live for students or teachers today, that does at least two of the following on the publisher's own ELA content in grades 3 to 8: generates or adapts practice or assessment items; gives the student feedback or a hint after an error and then a follow-up item on the same skill; reports item-level skill gaps to the teacher. A roadmap announcement, pilot, or beta is not "live." Record it separately.

RESEARCH QUESTIONS
1. For each of McGraw Hill, HMH, and Savvas: which named products or features, if any, meet the definition above for grades 3 to 8 ELA? Give the product name, what it does, whether it is generally available, pilot, or announced, the date, and whether it uses generative AI. If a feature applies to math only, or to writing feedback only, say so and do not count it as ELA practice.
2. For each of the three, is the capability built in-house, acquired, or delivered through a named technology partner?
3. Where does Benchmark Education Company sit relative to those three? Report only published indicators: number of state adoptions, districts or students served, revenue or employee figures from a stated source, and how trade press or analysts categorize it. Do not estimate, and do not rank without a source.
4. Among other K-8 ELA core-curriculum publishers of Benchmark's size or smaller, which have publicly announced AI-generated or adaptive practice, and was it built, bought, or partnered? Enumerate what you find, with dates.
5. Is there public evidence of publishers partnering with third-party AI practice or tutoring companies in the last 24 months (announcements, conference sessions, trade press)? Name the pairs.

METHOD
- Use primary sources first: product pages, support and release notes, press releases, investor or annual reports, state adoption lists, EdReports, and trade press (EdWeek Market Brief, EdSurge, The 74, District Administration).
- For each publisher, enumerate what you checked, so a "not found" has a search perimeter.
- Label each finding SUPPORTS, UNDERCUTS, or MIXED with respect to the hypothesis, and say which half of the hypothesis it bears on (the large-publisher half or the smaller-publisher half).
- Record blocked sources and try the Internet Archive for them.

OUTPUT
1. A table: publisher | named capability | meets the definition? (yes / partly / no) | live, pilot, or announced | built, bought, or partnered | source URL | date | exact quote
2. Benchmark's position, with every figure sourced
3. Smaller-publisher findings, enumerated
4. Publisher and AI-partner pairings found
5. A verdict of 200 words or fewer: which half of the hypothesis the evidence supports, which it undercuts, and what public research cannot settle

Do not recommend a partnership. Do not mention any specific AI vendor as a candidate. Do not cite Perplexity as a source.
```

## Prompt 2: Gemini Pro (deep research, alongside Prompts 1 and 1B)

Gemini does its own retrieval and doesn't need Perplexity's answer. Save as `02 Gemini.md`.

```
You are the document-analysis lead for a high-stakes intelligence brief on Benchmark Education Company. Build the definitive product and evidence map from primary documents: product guides, support documentation, implementation guides, efficacy reports, EdReports reviews, and state adoption records. Focus on extraction and reconciliation, not recommendations. Do not compare Benchmark to any other company.

TASK A, PRODUCT ARCHITECTURE
One row for every current product and named component: exact name, current edition, grade span, subject and language, buyer, user, teacher role, student workflow, lesson sequence, texts used, practice mechanism, feedback after an error, assessment and reteaching, reporting, professional learning, digital or print status, integrations, and source support. Where the sources allow, describe grades 4 to 6 separately.

TASK B, EVIDENCE REGISTER
For every efficacy or validation study: exact product and edition studied; author and affiliation; funder or commissioning relationship; publication status; dates, setting, grades, population; sample size and attrition; design and comparison condition; baseline equivalence; outcome measures; effect sizes and significance if reported; stated limitations; claimed ESSA tier and whether the design appears to meet it; whether findings transfer to the edition sold today. Include EdReports ratings by edition and grade band.

TASK C, CONTRADICTION TESTS
Reconcile conflicting grade spans, product names, editions, efficacy claims, and descriptions of digital functionality. Test these propositions, and for each say SUPPORTED, CONTRADICTED, or UNVERIFIED with the quote that decides it:
1. Benchmark is primarily a core ELA curriculum publisher.
2. Its digital platform delivers student practice with automatic feedback, rather than digital versions of print materials.
3. Its assessments drive reteaching inside the program, and the program supplies the reteaching materials.
4. Its evidence base is independent.
5. A current product uses generative AI, adaptive practice, or automatically generated items.
6. Benchmark licenses its content to, or integrates with, third-party digital practice or assessment platforms.
7. After a student misses a grades 4 to 6 practice item in the digital platform, the platform itself responds (hint, feedback, or a follow-up item), rather than leaving the response to the teacher.

RULES
- Use exact quotations and page numbers.
- Do not infer current functionality from a study of an older edition.
- Distinguish a company claim of an ESSA tier from your own assessment of the study design.
- Mark every unsupported proposition UNVERIFIED.
- Identify duplicated sources that share one origin.
- If a page is blocked, try the Internet Archive and record the archived URL and capture date.

OUTPUT
1. Complete portfolio table
2. Study-by-study evidence register
3. Contradiction matrix for the seven propositions
4. Claims safe to use
5. Claims requiring hedging
6. Claims to exclude
7. Missing documents and follow-up questions

Do not draft a comparison.
```

## Prompt 3: GPT-5 Pro (after 1, 1B and 2 land)

New conversation, web research on. **Upload five files:** `01 Perplexity.md`, `01B Perplexity market.md`, `02 Gemini.md`, and the two files in `_upload-these/`. Paste the framing line, then the prompt. Save as `03 GPT-5 Pro.md`.

Framing line, paste first:

```
Before anything else, list each uploaded file by name with its first heading and roughly how long it is. If any file is empty, unreadable, or missing, stop and tell me which one; do not continue. Then read all five files before answering. Perplexity and Gemini are finding aids, not evidence. The ClassE research brief controls every ClassE claim. Reopen disputed sources on the web.
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
Using 01B and your own reopened sources, test this working hypothesis: "The largest K-8 ELA publishers (McGraw Hill, HMH, Savvas) already offer something similar; medium and smaller publishers generally do not, and may look for a partner to catch up." Answer separately:
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

Separate conversation. Same five uploads, same framing line, same Prompt 3. It must never see `03 GPT-5 Pro.md`. Save as `04 Grok.md`. Claude asks for this only when the GPT-5 Pro verdict is close or thin.

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

## Your read (Tue, same sitting as Prompt 3)

Three to five sentences, or a voice memo. Last time your Intersection line was the best sentence in the 95 Percent Group document, and it arrived last. This time it comes first. Answer these three:

1. What's your gut read on Benchmark: what does it do best, and where do you think it stops?
2. Given Matt's theory about big and smaller publishers, where do you think Benchmark falls, and why?
3. What's the one question you'd want Matt to be able to answer after reading this?
