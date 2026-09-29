# Benchmark Market Check: K-8 ELA AI Practice Hypothesis

Prepared 2026-09-29 (task date 2026-09-28). Public web sources only.

## Read this first: the evidence standard was not met

The brief says to open every cited source, quote it exactly, and not rely on search snippets. In this session I could not do that for any publisher, trade-press, state or archive website. The network policy blocked every WebFetch and curl request with `EGRESS_BLOCKED` / `CONNECT tunnel failed, response 403`. Blocked hosts I tested: savvas.com, hmhco.com, support.hmhco.com, mheducation.com, investors.mheducation.com, mhereseller.zendesk.com, benchmarkeducation.com, prnewswire.com, businesswire.com, finance.yahoo.com, sec.gov, web.archive.org, en.wikipedia.org, doe.mass.edu, edsurge.com, marketbrief.edweek.org, the74million.org, districtadministration.com, thejournal.com, edtechdigest.com. The only public host that loaded was github.com, which is not relevant here. **Every web page below is therefore marked BLOCKED.** Wayback Machine copies were tried and were blocked too, so there are no capture dates.

**What I did open.** Benchmark Education Company's Indeed company profile and three of its live Indeed job postings, through the Indeed job-data connector. Quotes from those are exact. Everything else here is a **lead**: what the search engine reported a page says. It is not a verified quote, and nothing in this file rests on it as fact.

Codes used below:
- **Status:** `BLOCKED-LEAD` means the page could not be opened and the claim comes from a search-engine summary. `OPENED` means I read the source myself and quote it exactly.
- **Label:** SUPPORTS / UNDERCUTS / MIXED, then **[H1]** (big three already have the capability) or **[H2]** (mid-size and smaller publishers lack it and may partner). Labels on BLOCKED-LEADs are provisional. They only hold if the page, once opened, says what the summary claims.

---

## 1. Capability table (leads unless marked OPENED)

"Quote" means search-summary wording, **not verified**, wherever the Status is BLOCKED-LEAD.

| Publisher | Capability | Meets definition? | Live / pilot / announced | Built / bought / partnered | URL | Date | Reported wording (unverified unless OPENED) | Status / label |
|---|---|---|---|---|---|---|---|---|
| HMH | **Waggle** adaptive practice, ELA + math, K-8, aligned to Into Reading | **Likely yes** (adapts practice; hints/feedback; skill data), if verified | Live (reported) | **Bought**: Waggle acquired 2019 | hmhco.com/programs/waggle ; hmhco.com/platform-product-updates/accelerate-student-learning-with-waggles-new-skill-based-ai-engine ; edsurge.com/news/2019-01-15-houghton-mifflin-harcourt-acquires-waggle-an-ai-driven-solution-for-k-12 | Acquired Jan 2019; "new skill-based AI engine" update reported Dec 2024 | "aligns with HMH Into Reading's scope and sequence"; "embedded hints and feedback"; "12 distinct data points" | BLOCKED-LEAD. SUPPORTS [H1] |
| HMH | **Amira Learning**: AI reading tutor + oral fluency assessment, PreK-8, linked to Into Reading content | **Partly** (tutoring and assessment tied to Into Reading resources; unclear whether it adapts HMH's own items) | Live (reported) | **Partnered**: Amira is a separate company; HMH is described as a "leading partner" | hmhco.com/platform-product-updates/amira-ai-comprehension-model-and-deeper-connected-discovery ; gettingsmart.com/2024/06/11/... ; marketbrief.edweek.org/.../amira-learning-merges-with-istation.../2024/06 | Amira-Istation merger June 2024 | "connects oral reading fluency assessment results with relevant HMH Into Reading content"; Amira "will still be accessible through leading partners like Houghton Mifflin Harcourt" | BLOCKED-LEAD. MIXED [H1] |
| HMH | **Writable**: AI writing feedback, grades 3-12 | **No** (writing-feedback only; excluded) | Live (reported) | **Bought**: Writable acquired; OpenAI-powered integrations reported Aug 2023 | hmhco.com/about-us/press-releases/hmh-acquires-award-winning-software-company-writable-... ; hmhco.com/about-us/press-releases/hmh-introduces-generative-ai-teacher-supports-... | Aug 21, 2023 (reported) | "new OpenAI-powered integrations within Writable" | BLOCKED-LEAD. Excluded |
| HMH | **Embedded generative AI suite on HMH Ed**: lesson-plan generators, text translators, vocabulary scaffolding, for Into Reading / Into Literature | **Unclear / probably no** (teacher-facing; no reported student hint → follow-up loop) | Announced June 30, 2025 for back-to-school 2025 | Built/partner not stated in summary | hmhco.com/about-us/press-releases/hmh-unveils-new-ai-tools-vision-for-instruction-aligned-ai-in-classrooms ; hmhco.com/programs/ai-tools | June 30, 2025 | "lesson plan generators, text translators, vocabulary scaffolding and more" | BLOCKED-LEAD. MIXED [H1] |
| Savvas | **Whooo's Reading AI scoring engine** in myView Literacy (K-5) and myPerspectives (6-12): feedback on open-ended comprehension responses, skill data to teachers | **Partly** (feedback + teacher skill insight on reading-comprehension responses, which goes beyond writing-only; no reported follow-up item) | Live for back-to-school 2024 (reported) | **Bought**: Whooo's Reading acquired March 2023 | savvas.com/.../2023/savvas-learning-company-acquires-whooos-reading-and-its-ai-technology ; savvas.com/.../2024/savvas-announces-new-ai-enabled-scoring-engine-for-back-to-school | Acquired Mar 2023; engine announced Aug 2024 (reported) | "in-the-moment feedback on their written responses to open-ended critical thinking questions"; "which skills their students need extra support with" | BLOCKED-LEAD. MIXED [H1] |
| Savvas | **SuccessMaker**: continuously adaptive reading, paired with Momentum screeners/diagnostics and myView | **Partly / possibly yes** (adaptive Savvas-owned reading content, K-8; not myView items; generative status unknown) | Live (reported) | Built (legacy Savvas/Pearson product) | savvas.com/solutions/literacy/core-programs/myview-literacy | Not established | "a proven-effective, continuously adaptive personalized reading program" | BLOCKED-LEAD. MIXED [H1] |
| Savvas | **SavvyWriter**: AI sentence-level writing feedback, myPerspectives 6-12 | **No** (writing-feedback only) | Announced Sept 2025 for back-to-school | Built on Whooo's-derived AI (reported) | savvas.com/.../2025/new-ai-powered-tools-for-back-to-school ; morningstar.com/news/pr-newswire/20250903ne63841/... | Sept 3, 2025 | "AI-powered, sentence-level feedback" | BLOCKED-LEAD. Excluded |
| Savvas | **Savvas Studio**: teacher AI tools that "generate customized practice" | **Unclear** (teacher-side generation; literacy scope reported as "phonics practice, reading selections, and background builders"; K-2-leaning) | Reported as math-first (enVision+, Oct 2025) | Not stated | savvas.com/resource-request/math/savvas-studio ; savvas.com/solutions/more-solutions/topics/ai | 2025 | "generate customized practice" | BLOCKED-LEAD. MIXED [H1] |
| McGraw Hill | **Wonders Adaptive Learning**: foundational-skills adaptive practice, K-5 | **Partly** (adaptive, but described as foundational skills; grades 3-5 ELA coverage unclear) | Live (reported) | Not stated | mheducation.com/prek-12/program/microsites/MKTSP-BGA10M0/browse/wonders.html ; doe.mass.edu/instruction/curate/ela-2023-wonders.pdf | Not established | "personalized digital instruction and practice in foundational skills" | BLOCKED-LEAD. MIXED [H1] |
| McGraw Hill | **Achieve3000 Literacy**: adaptive leveled nonfiction, grades 2-12, "Bayesian algorithms" | **Partly / possibly yes** (adapts texts and activities; McGraw Hill-owned content; supplemental, not Wonders/StudySync) | Live (reported) | **Bought**: Achieve3000 acquired (year not verified here) | mheducation.com/prek-12/program/microsites/achieve-3000-literacy.html ; mhereseller.zendesk.com/hc/en-us/articles/38490021660435-... | Not established | "Bayesian algorithms and text pairing based on Lexile levels" | BLOCKED-LEAD. MIXED [H1] |
| McGraw Hill | **Writing Assistant** (GenAI), grades 6-12, in Actively Learn / Achieve3000 | **No** (writing-feedback only) | Launched (reported); wider rollout Nov 17, 2025 | Not stated | mheducation.com/.../mcgraw-hill-announces-two-new-generative-ai-tools-... ; mheducation.com/.../new-genai-assistants-add-personalized-experiences-... | Nov 17, 2025 (wider availability) | "the company's first GenAI tools to be introduced in its products" | BLOCKED-LEAD. Excluded |
| McGraw Hill | **Teacher Assistant** (GenAI chatbot) | **No** (teacher planning; math first) | Live in California Reveal Math; literacy integration **announced** for "next year" (2026) | Not stated | mheducation.com/.../new-genai-assistants-add-personalized-experiences-and-support-to-mcgraw-hill-k-12-programs.html | Nov 17, 2025 | "broader national rollout and integration into additional K-12 math and literacy products scheduled for next year" | BLOCKED-LEAD. Announcement only |
| McGraw Hill | **Teachally acquisition**: AI curriculum authoring, localization, translation | **No** (content-development tooling) | Announced Sept 2, 2026 | **Bought** | mheducation.com/.../mcgraw-hill-acquires-teachally-... | Sept 2, 2026 | "create, localize and translate standards-aligned instructional materials" | BLOCKED-LEAD. Out of scope for the definition |

**Pilots and announcements, kept separate:**
- McGraw Hill Teacher Assistant for literacy: announced, not live.
- McGraw Hill "Agentic AI tool": reported as "piloting" (SEC 8-K / ARS FY2026, BLOCKED).
- Imagine Learning: four "Curriculum-Informed AI" tools, reported as "currently in pilot and expanding for the 2025–2026 school year".

**Answers to Q1–Q2 (provisional).**
- **HMH** has the strongest lead: Waggle, bought in 2019, reported with hints, feedback, adaptive practice and alignment to Into Reading.
- **Savvas** has AI response feedback (bought: Whooo's Reading) plus legacy adaptive SuccessMaker.
- **McGraw Hill's** strongest ELA leads are adaptive, but either supplemental (Achieve3000, bought) or K-5 foundational skills (Wonders Adaptive Learning). Its generative tools are writing-only or teacher-only.
- None of the three shows a *named external AI-company partner* delivering the student practice loop. The one reported external model supplier is OpenAI inside Writable, which is writing-only.

---

## 2. Benchmark Education Company's position (sourced figures only)

| Indicator | Figure | Source | Status |
|---|---|---|---|
| Employees | "201 to 500" | Indeed company profile, https://www.indeed.com/cmp/Benchmark-Education-Company (field `employeesLocalizedLabel`) | OPENED (via Indeed connector) |
| Revenue | "$5M to $25M (USD)" | Same Indeed profile (field `revenueLocalizedLabel`). The basis for this label is not stated, so treat it as low-confidence. I am reporting it, not endorsing it. | OPENED |
| Founded / ownership | Founded 1998; "Family owned and operated for more than 25 years"; CEO "Tom Reycraft", President "Sera Reycraft" | Indeed profile; Indeed job posting JOBSEARCH_100005 | OPENED |
| Reach | "This role directly contributes to delivering high-quality digital learning experiences to millions of users" | Indeed posting "Digital Production and Packaging", posted July 6, 2026, https://to.indeed.com/aal7zvq8cfrh | OPENED |
| Self-description | "a leading publisher of core, supplemental, and intervention literacy and language resources in English and Spanish, with valid and reliable digital assessments that inform instruction" | Indeed postings (boilerplate) | OPENED |
| District adoption | Fairfax County Public Schools adopted Benchmark Advance K-6, "seven-year partnership", implementation from 2024-25 | benchmarkeducation.com press release; PR Newswire 302104756; S3 PDF "PR_Fairfax VA_Benchmark Advance Adoption_4.1.24.pdf" | BLOCKED-LEAD |
| State adoption, FL | "Florida Benchmark Advance (c)2026" appears on Florida's adopted-materials site | flimadoption.org/bids/adoptedmaterial/1272 | BLOCKED-LEAD |
| State adoption, TX | Texas editions of Benchmark Phonics / Benchmark Fonética reported as IMRA-approved in the 2025 cycle | benchmarkeducation.com/newsroom | BLOCKED-LEAD |
| State review, MD / DE | Maryland review reported as "Exceeds Expectations"; Delaware DOE hosts a Benchmark Advance page | education.delaware.gov/cipd-ela-program/benchmark-advance/ | BLOCKED-LEAD |
| Trade-press categorization | Not established. EdWeek Market Brief was blocked. | n/a | Not found / BLOCKED |

**Relative to the big three.** The only comparative figure the searches surfaced is HMH's own claim: "more than 50 million students and 4 million educators" (June 30, 2025 release, BLOCKED-LEAD). I found no student count for Benchmark. On the Indeed labels alone, Benchmark is a mid-size private publisher; I did not open any source that ranks it. **Label: SUPPORTS [H2] framing (Benchmark is not a big-three peer), low confidence.**

---

## 3. Benchmark's own AI plans

| Finding | Source | Status | Label |
|---|---|---|---|
| Benchmark Universe reportedly offers "AI-powered feedback" and Benchmark Advance reportedly offers "AI grading tools" | benchmarkeducation.com/benchmarkuniverse ; benchmarkeducation.com/benchmark-advance-adelante | BLOCKED-LEAD | MIXED [H2]. If real, Benchmark already has *some* AI, but grading/feedback alone meets at most one criterion. |
| **"Benchmark Advance + Amira Learning Partnership – connecting powerful AI assessment with high-quality instruction"** | benchmarkeducation.com/benchmark-advance-adelante ; benchmarkadvance.com | BLOCKED-LEAD | **UNDERCUTS [H2] "may look for a partner"**. If verified, Benchmark has *already* partnered for AI reading assessment, with the same vendor HMH distributes. Date not established. |
| Job postings (3 opened): Lead Digital Production Engineer (July 6, 2026); VP Corporate & Channel Marketing (Sept 25, 2026); Producer Multimedia Content (July 8, 2026). None uses the words AI, machine learning, adaptive or generative. The engineering role centers on "QTI-compliant assessments and test items" and "Rapidly prototype new content formats". | Indeed connector, job IDs JOBSEARCH_100005 / 100001 / 100003 | OPENED | Weak SUPPORTS [H2]. There is no public in-house AI hiring signal in the sample. Absence in 3 postings is not evidence of no plan. |
| Other postings listed but not opened: Marketing Copy Editor, Meeting & Event Planner, Chef | Indeed search "Benchmark Education Company", New Rochelle, NY | Titles only | n/a |
| Indeed search "Benchmark Education AI" (remote) returned no results | Indeed connector | OPENED | Weak SUPPORTS [H2] |
| No Benchmark press release announcing AI-generated or adaptive student practice surfaced in searches | Search perimeter below | Not found | Neutral. The newsroom itself was BLOCKED. |

---

## 4. Other K-8 ELA core publishers (Benchmark's size or smaller)

Size comparisons were **not** established. No source I opened gives revenue or headcount for these companies, so "Benchmark's size or smaller" is unverified for all of them.

| Publisher | Reported AI / adaptive item | Built / bought / partnered | Date | Status | Label |
|---|---|---|---|---|---|
| Imagine Learning (EL Education K-8) | Four "Curriculum-Informed AI" teacher tools (Lesson Plan Creator, Curriculum Coach, Communication Drafter…), "currently in pilot" | Not stated | 2025-26 | BLOCKED-LEAD (imaginelearning.com/press/imagine-learning-introduces-a-smarter-way-to-bring-ai-into-the-classroom/) | MIXED [H2]. Mid-size publisher moving on AI, but teacher-facing pilot, not student practice. |
| Amplify (CKLA) | Boost Reading, "adaptive K–5 personalized learning program"; in-house Amplify ASR speech recognition for 2025-26, "replace Soapbox's ASR" | **Built** (ASR in-house, replacing a partner's) | Study Jan 2025; ASR for 2025-26 | BLOCKED-LEAD (amplify.com/news/...) | UNDERCUTS [H2]. A non-big-three publisher has live adaptive practice and brought AI in-house. Amplify's size relative to Benchmark is not established and is likely larger. |
| Great Minds (Wit & Wisdom) | 2025-26 digital updates cover reports and PDFs; no AI item surfaced. "Affirm" digital assessment/practice tool dates from Feb 2020. | Built | 2020; 2025-26 | BLOCKED-LEAD (digitalsupport.greatminds.org/wit-wisdom-2025-2026-digital-updates) | SUPPORTS [H2] (no AI practice found) |
| Carnegie Learning (ELA), CommonLit 360, Zaner-Bloser | No AI-practice announcement surfaced in one combined search | n/a | n/a | Not found (thin perimeter) | Inconclusive |

---

## 5. Publisher and AI-company pairings (last 24 months: Sept 28, 2024 – Sept 28, 2026)

Every row is a BLOCKED-LEAD.

| Publisher | Partner / deal | Type | Date | Source (blocked) |
|---|---|---|---|---|
| Benchmark Education | Amira Learning | Partnership (AI assessment + Benchmark Advance) | Date not established | benchmarkeducation.com/benchmark-advance-adelante |
| HMH | Amira Learning (continues post-merger) | Distribution partnership | Reaffirmed June 2024 (just outside the window) | gettingsmart.com; marketbrief.edweek.org 2024/06 |
| McGraw Hill | Teachally | Acquisition | Sept 2, 2026 | mheducation.com press release |
| McGraw Hill | TeachFX | Acquisition (AI teacher coaching) | Date not established | mheducation.com press release |
| Amplify | Soapbox Labs ASR replaced by in-house ASR | Partner → built | For 2025-26 | amplify.com/news |
| Savvas | Whooo's Reading | Acquisition | Mar 2023 (outside the window) | savvas.com 2023 release |
| HMH | OpenAI (models inside Writable) | Model supplier | Aug 2023 (outside the window) | hmhco.com 2023 release |
| Ecosystem (not publisher-specific) | CZI Learning Commons open AI platform, "more than 70 partners" incl. model labs | Infrastructure | Sept 22, 2026 (reported) | edsurge.com; learningcommons.org |

I found **no** announced pairing between any of McGraw Hill, HMH or Savvas and a frontier-model company for K-8 ELA student practice within the window.

---

## 6. Verdict (≤200 words)

**Neither half can be confirmed to the standard requested.** Every publisher and trade-press page was network-blocked. The only first-hand material is Benchmark's Indeed profile and job postings.

**H1 (big three already have it):** the leads lean *partly holds*. HMH's Waggle is the only lead that plausibly meets two or more criteria on grades 3-8 ELA: adaptive practice, hints/feedback and skill data aligned to Into Reading. It is acquired and not generative. Savvas and McGraw Hill show adjacent capabilities: AI feedback on responses, supplemental adaptivity (SuccessMaker, Achieve3000), and teacher-only or writing-only generative AI. None of the three shows a live *generative* student practice loop.

**H2 (smaller publishers lack it; may seek a partner):** the leads lean toward it *failing as framed*. Benchmark reportedly already has an Amira Learning partnership and "AI grading" and "AI-powered feedback" claims. Amplify reportedly built adaptive practice and ASR in-house. Benchmark's sampled job postings show no AI hiring. That is consistent with partnering, but it is not evidence of intent.

**What public research can't settle:** whether these features run on each publisher's core grades 3-8 items rather than supplemental content, actual usage, contract terms, and any partner's intent.

---

## 7. Search perimeter

**WebSearch queries run (engine summaries only; results not opened):**
1. McGraw Hill Wonders AI adaptive practice ELA 2025
2. HMH Into Reading AI adaptive practice Waggle Amira grades 3-8
3. Savvas myView Literacy AI adaptive practice feedback 2025
4. Savvas Whooo's Reading acquisition AI Savvas Realize literacy
5. HMH Writable acquisition Waggle ELA AI "HMH" 2024 2025 Coach AI teacher assistant
6. McGraw Hill Achieve3000 Literacy AI "Wonders" "StudySync" generative AI feature 2025 2026
7. Benchmark Education Company AI Benchmark Universe adaptive practice
8. "Benchmark Education" "Benchmark Advance" state adoption 2025 students served
9. "Benchmark Education Company" artificial intelligence job posting OR press release 2026
10. Benchmark Universe "AI" feedback Benchmark Advance 2026 edition new features
11. HMH generative AI teacher supports connected literacy Into Reading press release date
12. "Accelerate student learning with Waggle's new skill-based AI engine" HMH
13. "Benchmark Education" "Amira Learning" partnership Benchmark Advance
14. HMH Unveils New AI Tools Vision for Instruction-Aligned AI Into Reading Into Literature June 2025 details
15. Savvas unveils new AI-powered tool back to school 2025 literacy myView myPerspectives
16. Savvas 2026 AI announcement literacy students practice hints "Savvas" generative AI tutor reading
17. McGraw Hill 2026 AI K-12 literacy announcement Wonders StudySync "Teaching Assistant" OR "AI"
18. HMH 2026 AI announcement Into Reading student practice adaptive "HMH"
19. "New GenAI Assistants Add Personalized Experiences and Support to McGraw Hill's K-12 Programs"
20. McGraw Hill Teachally acquisition September 2026 K-12 curriculum AI
21. McGraw Hill Google Cloud Gemini partnership education 2025 (no publisher pairing found)
22. K-12 curriculum publisher partners with OpenAI OR Anthropic OR Google OR Microsoft ELA 2025 2026 announcement
23. Amplify CKLA AI adaptive practice Boost Reading generative AI 2025 2026
24. Great Minds Wit & Wisdom AI tool launch 2025 2026
25. Imagine Learning EL Education K-8 language arts AI "Imagine Learning" generative AI 2025 2026
26. Zaner-Bloser OR "Carnegie Learning" OR CommonLit ELA AI practice feedback launch 2025 2026 partnership
27. EdWeek Market Brief AI curriculum publishers ELA smaller publishers partner AI vendors 2026
28. Savvas Studio AI teacher tools generate customized practice literacy launch date
29. HMH Amira Learning relationship partner exclusive distribution Istation merger 2024
30. Benchmark Education Texas IMRA approved Benchmark Advance Florida adoption Indiana adoption list 2025 2026

**Pages I tried to open; all BLOCKED (EGRESS_BLOCKED):**
- savvas.com: 2025 new-AI-tools release; 2024 scoring-engine release
- hmhco.com/programs/waggle, plus its web.archive.org copy
- support.hmhco.com/s/article/Waggle-on-Ed-Resources
- mheducation.com: ALEKS Adventure release; investors.mheducation.com Connect release; mhereseller.zendesk.com Achieve3000 AI article
- benchmarkeducation.com home
- prnewswire.com: Savvas 302242132; businesswire.com: McGraw Hill 20260407438831
- finance.yahoo.com: McGraw Hill GenAI release
- sec.gov: McGraw Hill 8-K ex99 (June 30, 2026)
- thejournal.com: Whooo's Reading article; edtechdigest.com: HMH Waggle
- doe.mass.edu: Wonders PDF; en.wikipedia.org: McGraw Hill Education
- Home pages of edsurge.com, marketbrief.edweek.org, the74million.org, districtadministration.com
- curl test to savvas.com and en.wikipedia.org: 403 at the proxy

**Opened successfully (Indeed connector):**
- Indeed company profile, Benchmark Education Company
- Indeed search "Benchmark Education Company", New Rochelle, NY: 6 postings listed
- Indeed search "Benchmark Education AI", remote: 0 results
- Indeed search "Benchmark Education software engineer product manager", New Rochelle: 0 results
- Job details JOBSEARCH_100005, 100001, 100003
- ZipRecruiter search "Benchmark Education Company", New Rochelle: no Benchmark Education results (irrelevant employers returned)

**Not checked at all:** Benchmark's LinkedIn page, state adoption lists opened directly (CA, TX, FL, IN, OK, NC), the big three's product release notes, 10-K/ARS filings (McGraw Hill ARS FY2026 was found but blocked), District Administration and The 74 article-level searches.

**To finish this check:** re-run with the environment's network access set to allow these publisher and trade-press domains, then open each BLOCKED-LEAD URL above and replace the reported wording with exact quotes.
