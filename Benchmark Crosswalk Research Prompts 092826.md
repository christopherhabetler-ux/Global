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

1. **Matt's theory is now something to test, not a premise.** Prompt 2 checks both halves: whether the three largest publishers already ship something like ClassE, and where Benchmark actually sits. Prompt 1 checks whether Benchmark is building its own, and Prompt 3 weighs all of it.
2. **Benchmark is a publisher, so rights look different.** Ingestion rights are an OPEN QUESTION in the ClassE brief. When the partner owns the content, that question changes shape, but the claim doesn't get promoted. Prompt 3 now tests this directly.
3. **The seat is a second look, not a first.** The objections list is weighted toward what someone who has already seen a ClassE pitch would press on. The seat is described by role only, and no name goes to an outside model.

Carried forward from the 95 Percent Group build: an upload-receipt check in the framing line (the Grok file came back empty last time), an archive fallback in the quote chase (the job-posting quote was never confirmed), and a search perimeter on every "search results only" claim (the TouchMath closing had none).

## The plan (final, red-teamed 092826 9:30pm ET)

**Round 1, now, all at once (about 30 minutes):**
1. Prompt 1 into Perplexity, deep research. Save as `01 Perplexity.md`.
2. The same Prompt 1 into Gemini, deep research. Gemini shows a plan first; click Start research without editing it. Save as `02 Gemini.md`.
3. Prompt 2 into a second Perplexity tab, deep research. Save as `03 Market.md`.
4. Your read, the three questions at the bottom. Save as `00 My read.md`.

Claude is running Prompt 2 on its own at the same time, as a second engine on Matt's theory.

**Round 2, when round 1 lands, both at once:** in GPT-5 Pro and in Grok, separate conversations, upload the same five files (01, 02, 03, and both files in `_upload-these/`), then paste the framing line and Prompt 3. Save as `04 GPT-5 Pro.md` and `05 Grok.md`. If it's late, let them run overnight.

**The handoff:** attach all six files to this Claude conversation the moment you have them. Tonight is fine; the Tuesday morning coffee is fine too. **Do not put them in the ClassE Crosswalks Drive folder.** It's shared with Matt, so anything placed there reaches him.

**Tuesday:** Claude starts the moment the files arrive, not after your 3:30 Zeta call. That covers seat reconciliation, the quote chase, the claim register, the draft, the blind review, and the PDF, HTML and .md. The PDF is ready for you Tuesday evening.

**Wednesday:** you read the PDF, and it goes to Matt.

## Red team of this plan

I attacked my own plan the way Prompt 3 attacks a gap. Here's what failed and what changed.

| # | Weak point | Severity | Fix |
|---|---|---|---|
| 1 | "Claude does everything after that," but this Claude runs in the cloud and can't read `~/Downloads` on your Mac. The handoff didn't exist. | Fatal | You attach the files to this conversation. There's also an explicit warning against the ClassE Crosswalks Drive folder, which reaches Matt. |
| 2 | The question the whole document turns on (what Benchmark's digital platform does after a wrong answer in grades 4 to 6) mostly sits behind a login. Public marketing won't answer it, and the models would have returned "not found." | High | Prompt 1 now sends the research to places that describe the platform publicly: state review reports, EdReports usability sections, district adoption packets, and Benchmark's own training videos, cited with timestamps. |
| 3 | Claude sat idle until 3:30 Tuesday, which burned about 14 hours of a 40-hour window. | High | Claude starts the moment the files land. The Tue-noon trip-wire now has real slack. |
| 4 | Matt's theory ran on one engine, and it's the part he'll carry into the room. | Medium | Claude runs the same Prompt 2 independently tonight, so the theory gets two engines at no extra paste. The two red-team seats also re-open its sources. |
| 5 | "One row per claim" invites a 300-row ledger that crowds out analysis and gets cut off mid-answer. | Medium | The ledger is capped at the 60 most load-bearing claims. |
| 6 | I overstated a receipt. The Canvas split was between two drafts (Gemini graded the Twin Question gap High, Claude graded it Low-medium), not between two red-team seats. | Low | Stated accurately here. The case for two seats stands without it: independent judgment on the step that decides what reaches Matt, for one extra paste. |
| 7 | Both red-team seats read the same research files, so they aren't independent on facts. | Accepted | Intended. They're independent on judgment, and facts are settled by the quote chase against the source, never by the seats. |

What would still make this document weak: if Benchmark's platform behavior isn't described anywhere public, even after fix 2. In that case the document says so plainly, and it becomes the first question Matt can ask in the room. That's useful to him, not a failure.

**Trip-wire: if the round 2 answers aren't in by Tue noon,** send Matt this line and take Thu 10/01. That still gives him four days before his meeting:

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

## Prompt 1: Benchmark research (paste into Perplexity AND Gemini, separate chats)

```
You are the lead researcher for a high-stakes competitive-intelligence brief on Benchmark Education Company, the K-8 literacy curriculum publisher. Build an auditable, sourced picture of the company. Accuracy matters more than volume, and "not found" is an acceptable answer. Do not recommend a partnership, and do not compare Benchmark to any other company.

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

METHOD
- Source priority: product manuals, support documentation, help-center articles and release notes first; then efficacy reports and EdReports; then state and district records; then press releases, interviews and job postings; then trade press; marketing pages only when nothing better exists.
- The digital platform is mostly behind a login, so go where its behavior is described in public: state instructional-materials review reports and publisher correlations (for example Texas, Florida, California, Louisiana, Oklahoma, Indiana), the EdReports usability and technology sections, district adoption committee packets and board presentations, and Benchmark's own training and demo videos (YouTube, webinars). Cite the timestamp for a video.
- "Benchmark" is a common word. Keep only sources about Benchmark Education Company. Exclude generic "benchmark assessment" results and other companies with Benchmark in the name, and flag any source where it's unclear which company is meant.
- Trace repeated claims to their earliest source, and treat copies of one claim as one origin, not corroboration.
- Mark company-funded, company-commissioned, and independent evidence separately. Don't infer today's functionality from a study of an older edition.
- If a page is blocked or gone, try the Internet Archive and record the archived URL and capture date. Otherwise record it as blocked.
- If a claim rests only on a search snippet or an aggregator, label it SEARCH RESULT ONLY and record the query.
- Every negative finding lists exactly what was checked: which documents, which release-note period, which search terms.

OUTPUT
1. Source ledger, one row per claim, capped at the 60 most load-bearing claims: claim | URL | publication date | exact quote | page or section | origin family | independent or company
2. Portfolio table
3. Evidence register, one row per study
4. The Part 2 proposition results
5. Claims safe to use, claims needing a hedge, claims to exclude
6. Blocked sources, and the ten questions public research could not settle

Do not draft a comparison with any other product. Do not cite yourself or another AI as a source.
```

## Prompt 2: market check (Perplexity, second tab, alongside Prompt 1)

```
You are a market researcher testing a working hypothesis about the US K-8 English language arts curriculum market. Test it; do not prove it. Either answer is useful.

THE HYPOTHESIS TO TEST
"The largest K-8 ELA curriculum publishers (McGraw Hill, HMH, Savvas) already offer something similar to AI-generated, curriculum-connected student practice with feedback. Medium and smaller publishers generally do not, and may look for a technology partner to catch up."

WHAT "SOMETHING SIMILAR" MEANS HERE
A capability live today for students or teachers (not a pilot, beta, or announcement) that does at least two of these on the publisher's own grades 3 to 8 ELA content: generates or adapts practice or assessment items; responds to a wrong answer with feedback or a hint and then a follow-up item on the same skill; reports item-level skill gaps to the teacher. Math-only or writing-feedback-only features don't count. Record pilots and announcements separately.

RESEARCH QUESTIONS
1. For each of McGraw Hill, HMH, and Savvas: which named products or features, if any, meet the definition for grades 3 to 8 ELA? Give the name, what it does, live, pilot, or announced, the date, and whether it uses generative AI.
2. For each of the three: was the capability built in-house, acquired, or delivered through a named technology partner?
3. Where does Benchmark Education Company (the K-8 literacy curriculum publisher) sit relative to those three? Report only published indicators: state adoptions, districts or students served, revenue or employee figures from a stated source, and how trade press or analysts categorize it. Do not estimate, and do not rank without a source.
4. Among other K-8 ELA core-curriculum publishers of Benchmark's size or smaller, which have publicly announced AI-generated or adaptive practice, and was it built, bought, or partnered? Enumerate with dates.
5. Which publisher and AI-company partnerships were announced in the last 24 months (press releases, conference sessions, trade press)? Name the pairs.

METHOD
- Primary sources first: product pages, support and release notes, press releases, investor or annual reports, state adoption lists, EdReports. Then trade press (EdWeek Market Brief, EdSurge, The 74, District Administration).
- "Benchmark" is a common word. Keep only sources about Benchmark Education Company, and flag any source where it's unclear which company is meant.
- For each publisher, list what you checked, so a "not found" has a search perimeter.
- Label each finding SUPPORTS, UNDERCUTS, or MIXED, and say which half of the hypothesis it bears on: the large-publisher half or the smaller-publisher half.
- If a page is blocked or gone, try the Internet Archive and record the archived URL and capture date.
- If a claim rests only on a search snippet or an aggregator, label it SEARCH RESULT ONLY and record the query.

OUTPUT
1. Table: publisher | named capability | meets the definition? (yes / partly / no) | live, pilot, or announced | built, bought, or partnered | URL | date | exact quote
2. Benchmark's position, every figure sourced
3. Smaller-publisher findings, enumerated
4. Publisher and AI-partner pairings
5. Verdict, 200 words or fewer: which half of the hypothesis the evidence supports, which it undercuts, and what public research can't settle

Do not recommend a partnership or name any AI vendor as a candidate. Do not cite yourself or another AI as a source.
```

## Prompt 3: red team (GPT-5 Pro AND Grok, separate conversations, after round 1 lands)

New conversation, web research on. **Upload five files:** `01 Perplexity.md`, `02 Gemini.md`, `03 Market.md`, and the two files in `_upload-these/`. Paste the framing line, then the prompt. Do the same in Grok. Save as `04 GPT-5 Pro.md` and `05 Grok.md`. Neither seat ever sees the other's answer.

Framing line, paste first:

```
Before anything else, list each uploaded file by name with its first heading and roughly how long it is. If any file is empty, unreadable, or missing, stop and tell me which one; do not continue. Then read all five files before answering. The Perplexity and Gemini files answer the same research prompt; treat their disagreements as findings to settle against the source. Both are finding aids, not evidence. The ClassE research brief controls every ClassE claim. Reopen disputed sources on the web.
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
Using the market file (03 Market) and your own reopened sources, test this working hypothesis: "The largest K-8 ELA publishers (McGraw Hill, HMH, Savvas) already offer something similar; medium and smaller publishers generally do not, and may look for a partner to catch up." Answer separately:
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

## Your read (tonight, in round 1)

Three to five sentences, or a voice memo. Save it as `00 My read.md` in the drop folder. Last time your Intersection line was the best sentence in the 95 Percent Group document, and it arrived last. This time it comes first. Answer these three:

1. What's your gut read on Benchmark: what does it do best, and where do you think it stops?
2. Given Matt's theory about big and smaller publishers, where do you think Benchmark falls, and why?
3. What's the one question you'd want Matt to be able to answer after reading this?
