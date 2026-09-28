# chrishabetler.com: Reconciled Plan 092826

Written 092826 (Mon), Eastern. Inputs: the GPT action plan (092726 file), GPT's two red-team passes, both Gemini reports, and your Notion website record: HANDOFF 092026b, THE PLAN 092026 (five-seat audit), MASTER PLAN 092026 (Lindsay), PLAN website review response 092426, BUILD NOTE 092426, TFA SUMMIT SPRINT 092426, PRICING STRUCTURE 091726, infrastructure facts 092526, WHO LOOKED week of 092126.

Limits, stated once: this was a cloud session. Your Mac files were not reachable, and chrishabetler.com is blocked from this container, so I did not load the live site or watch the videos. Everything about the live pages comes from GPT's 092726 read and your Notion record. Every number below was read from one of those pages.

---

## 1. Bottom line

**The site is good enough to convert a referral. It is not generating demand, and more audits will not change that.**

- First WHO LOOKED week (092126): 0 hands raised, 0 scorecard submissions, last scorecard submission 081726. Search Console, three months to 092226: 12 clicks, all brand queries. Google sent 11 visits in the week of 091826.
- In ten days the site has had a five-seat audit (092026), Lindsay's review, a GPT and Gemini round (092426), a second GPT round (092726), and now this. They mostly agree. The work that is left is shipping, not diagnosing.
- Money in the next 30 days comes from three places, and the site only has to not lose them: the United Schools coverage deal, TFA Summit conversations (Oct 2 to 3, Las Vegas), and referrals. A TFA contact who Googles you on Friday night lands on the homepage. That's the deadline that matters.

**My recommendation:** one focused website session before Wednesday 093026 night (the P0 list below, about two hours), no website work during TFA, then the homepage restructure and the Coverage film the week of 100526. After that, cap website time at one session a week until United Schools produces a real receipt. Confidence about 80%. What would change it: if United Schools or a TFA lead says the site itself raised a doubt, the restructure moves up.

---

## 2. How I weighed the sources

| Source | Weight | Why |
|---|---|---|
| Your rulings and Lindsay (a real reader) | Highest | You already decided these. Ties go to Lindsay, per your 092026 ruling. verified-facts governs what a claim may say. |
| GPT action plan 092726 (the file) | High | It loaded the live pages, and its red team caught its own overclaiming. Its claim register and "label illustrative data" rules are correct. |
| GPT red-team passes | Medium | Sharp on cringe lines and on the videos. Too prescriptive about copy. Its sample lines are GPT voice, and your rule is that your words beat polished words. |
| Gemini v1 and v2 | Low, mostly rejected | Already rejected on 092426. It never loaded the site (it says MongoDB on DigitalOcean; the site moved to Netlify on 043026 and returns 200 to every AI crawler, tested 092426). It built you from people-search sites and got someone else. |

**Gemini claims that must never reach the site or LinkedIn:**
- "Age 38, Phoenix AZ" and the baseball league: a different Christopher Habetler.
- 91% ISS reduction, 54% OSS, staff satisfaction 63 to 93, family engagement 51 to 99: Russell Clay Consulting's numbers, not yours.
- "VP of School Support at KIPP": wrong. verified-facts says Senior Director.
- "Deputy Superintendent at Brooklyn LAB" as a standing title: only accurate for the August 2021 moment.
- "Runs the AI Automation Society on Skool": not in your records.

**What survives from Gemini (four things):**
1. The IT-director reader is real. A district CTO will look for how data moves. That's the per-tool data note in P1.
2. The booking button needs to show up at more than one depth on the page. Already in the plan: sticky bar visible from the first screen, plus one at the end.
3. The AI-search problem. Gemini proved it live by inventing your career. Fix: one plain identity block on About with exact titles and dates, and Person schema with sameAs links, so a model quotes you instead of guessing.
4. The competitive gap. The visible AI-in-education names sell keynotes and teacher training. Nobody visible sells working operations tools built by a former school operator. That's positioning for you, not copy for the page.

---

## 3. Where the sources disagree, and my call

| Question | GPT | Lindsay or your ruling | My call |
|---|---|---|---|
| "Do Less. Do More." in the hero | Move it out | Your line, your connectives | **Keep it as the H1.** Add one plain line under it that says who it's for and what you build. The slogan never has to explain the work alone. 75% |
| CTA label | "Find my 3 hours" | "Book a quick call" everywhere | **Book a quick call.** GPT's version turns the unreceipted number into the button. 90% |
| "Three hours back a week, every week" | Soften it | Keep it, attach a receipt | **Keep the number, change the verb** so it promises a diagnosis, not a result: "Give me 30 minutes and I'll show you where three hours a week are going." United Schools becomes the receipt later. 70% |
| Paper-gradebook-to-AI illustration | Delete the whole unit | Lindsay: best three-second asset, keep it | **Keep the picture, delete the two fear lines** ("so you and your kids don't fall behind" and "a little stressed that you're already behind"). The picture says "schools." The sentences say "webinar." 65%. If two of five cold readers call it an AI seminar, cut it. |
| Status labels on tools (prototype, live, deployed) | Add them | You ruled no apologetic status lines (091726, 092426) | **No labels.** Truth gets handled by never claiming a tool runs at a school, and by the "every name below is made up" line on each walkthrough. |
| Which three tools lead the homepage | Coverage, Academic Health Coach, Communications | 092426 plan: Coverage, Dismissal, data reports | **Coverage (flagship, full story), Dismissal Hub, Academic Health Coach.** These are the three you couldn't do with a ChatGPT prompt, and Academic Health has the only real before and after on the site (/academic-health). Everything else behind "See all the tools." 70% |
| HANDOFF 092026b's one recommendation: build out the Communications, Meeting and Handbook pages | n/a | Last session's recommendation | **Reverse it.** GPT is right that these are the least distinctive. They drop to a "smaller things" list. Take screenshots from the TFA demos if they're cheap, but don't write new pages for them. 75% |
| Guarantee: "you keep the tool either way... I fix it that day" | Narrow it | Lindsay: move it next to the button | **It conflicts with your own price card.** PRICING STRUCTURE 091726 says "Coverage, if they keep it: $3,000." The site says they keep it either way and owe nothing. Pick one before TFA. Mine: "The first two weeks are free. If it doesn't earn a place in your week, you don't pay." Drop "keep it either way" and "fix it that day." 75%. **This is the one question for you.** |
| Tool renames | Rename several | n/a | **Not before TFA.** The kit and card are printed. Revisit after the film. |
| Old blog | Urgent cleanup | 092426: blog.chrishabetler.com does not resolve | **P2, one check.** Netlify still showed 17 referrals from blog.chrishabetler.com (082526 to 092426), so something still serves or links it. Five-minute check, then a Search Console removal request for stale URLs. |
| Separate paths for schools and edtech | Yes | Open question in THE PLAN 092026 | **Yes, in the nav only:** "For edtech and investors" points to /advisory. Never in the homepage body. Keep "I've been on all three sides of this market." 80% |

---

## 4. The plan, by priority

Impact and effort are my judgments, not measured.

### P0: before TFA, one session, by Wed 093026 night

| # | Change | Impact | Effort |
|---|---|---|---|
| 1 | **Plain line under the H1**: who it's for and what you build. Eyebrow readable: "For principals, ops directors and network leaders." | Very high | 15 min |
| 2 | **Replace "Never student records"** with a line that is true for every tool (draft in section 5). Check each tool's data flow first. | High (trust) | 30 min |
| 3 | **Delete the two fear lines.** Keep the illustration. | Medium | 5 min |
| 4 | **Make the guarantee match the price card** (after your answer). Put it next to the booking button. | High | 15 min |
| 5 | **Change the three-hours sentence** to the diagnosis version. | Medium (exposure) | 5 min |
| 6 | **Check the Coverage page lunch count.** GPT found "four adults" in one place and "six adults" in another. Ops readers will catch it. | Medium | 10 min |
| 7 | **Grep for leftover claims**: "hand them off so they run without me", "Built, installed, and running in schools right now", "human in the loop". Remove or rewrite. | Medium | 15 min |
| 8 | **Booking clicks you can count, with no new account**: every booking button points to chrishabetler.com/book, a redirect in `_redirects` to the Superhuman link. Netlify analytics then counts /book visits. | Medium | 15 min |
| 9 | **Confirm on a real phone**: sticky bar visible from the first screen on the homepage, and a booking link in the body of /about. Both were flagged 092026; confirm whether they shipped. | High | 10 min |

Gates, from your website project rules: write-like-us WRITE then SHIP on every new sentence, website-qa at phone and desktop width, zero em dashes, none of the barred words (hold, hero, leverage and their forms). Deploy command is yours to run.

### P1: week of 100526, the homepage becomes seven beats

1. **Hero**: H1, plain line, proof line (50+ schools and networks, every one a referral, 91% came back), six logos, face, Book a quick call.
2. **Coverage, in full.** The morning, the school's rules, the two calls that come back to a person, nothing goes out until approval, each adult sees only their change. Plus the film when it's done.
3. **Two more tiles**: Dismissal Hub, Academic Health Coach. Then "See all the tools."
4. **How it works, shown not labeled**: "The tool handles what your rules already decide. Everything else comes back to you. Nothing goes out until you approve it." Replaces "human in the loop" everywhere.
5. **Two testimonials** with role and organization. Your pick from those already live.
6. **The offer box**, from the price card: two weeks free, then the three ways to say yes, without annual totals (your rule).
7. **Book a quick call.** One filled button. Scorecard and email demoted to text links.

Also in P1:
- **"What this touches" note on each tool page**: does it use AI, what data, where it lives, who sees names. This is the page the IT director reads.
- **Scorecard result**: lead with estimated school days as a range, labeled "time spent on work that could be streamlined," with the arithmetic visible. Keep no email gate.
- **Advisory in the nav** as "For edtech and investors."
- **Five-reader cold test.** TFA gives you the readers: three ops people and two principals you meet there. Ask: who is this for, what does he build, what would you do next. Record answers before asking if they liked it.

### P2: week of 101226

- **Coverage film** (section 6): edit, caption, test with the same five readers.
- **About**: open with the professional thesis, then the identity block (exact titles and dates from verified-facts), then the story. Trim the first-day-of-school passage by about a third. Keep Dad Slate and one daughter project. Cut "That's where the magic happens."
- **Person schema** with sameAs links (LinkedIn and your other real profiles).
- **LinkedIn headline and About**, drafted for you to paste. Your LinkedIn still leads with KIPP and culture work.
- **Old blog check** and Search Console removal requests.
- Image weight: the logos are the whole performance cost. The 092026 audit estimated 700 to 900KB recoverable.

### P3: only after evidence

- **United Schools as the first real case.** The two free weeks are the measuring instrument. Log minutes per morning from day one, so the case exists the day you say it can be public. When it does, it replaces the three-hours hedge with a receipt.
- **Second film** (Dismissal or Academic Health) only if the Coverage film beats the page without it in the reader test.
- Tool renames, a master film, a security page beyond the per-tool notes: later, or never.

### What not to do

- No new audits until the five-reader test is back.
- No Gemini material, ever.
- No AI avatars, synthetic school footage, stock B-roll or music beds in the videos.
- No second thread working in the site files at the same time (your 092026 rule).

---

## 5. Draft copy for P0

Drafts only. Each goes through write-like-us before it ships. Your wording beats mine.

**Line under the H1 (pick one, or say it your way):**
> I spent twenty years inside schools. Now I build the tools I always wished we had: coverage, dismissal, data meetings, the weekly work that keeps landing on your best people.

> Twenty years running schools taught me where the time goes. I build the tools that get it back: coverage before the first bell, dismissal changes, the data meeting nobody has time to prep.

**Replacement for "Never student records":**
> Student information stays in your school's own accounts. When a tool uses AI, names are swapped for codes before the AI sees anything, and nothing goes out until a person approves it.

Only if true for all seven tools. If Dismissal Hub or any other tool sends names to an AI service, the line has to say so for that tool instead.

**Three-hours line:**
> Give me 30 minutes and I'll show you where three hours a week are going.

**Offer box, if you drop "keep it either way":**
> The first two weeks are free. If it doesn't earn a place in your week, you don't pay.

---

## 6. The Coverage film

**Goal:** a cold ops director can say what went in, which rules it followed, which two calls came back to a person, and what each teacher received, after one viewing. Runtime follows from that, probably 75 to 110 seconds.

**Why a new film:** the current coverage video (092426) is a machine-recorded screencast with captions and no sound. It shows the tool. It doesn't give the viewer the problem or the judgment. Your voice is the missing piece.

**Source footage:** record from the **Maple Grove demo** on habetler-demos, not the Dana v2 playground. Maple Grove is a made-up school end to end. The current coverage screens carry a real school's bell schedule and homeroom names, and that school is a client in an open negotiation.

**Beats:**

| Beat | On screen | You say (your words, recorded) |
|---|---|---|
| The morning | Phone, early, "I'm out today" texts arriving. Caption: "Maple Grove Elementary is made up." | "If you run operations, you know this morning." |
| What you're juggling | Master schedule, absences, the rules | Two adults in co-taught rooms, intervention protected, lunch covered, pulls spread fairly |
| Input | Typing or dictating the messy sentence, then the read-back | "It shows me what it understood before it does anything." |
| The plan | Generated plan with reasons | "Now it runs the school's rules." |
| The judgment | The two cards that come back to a person. Resolve one. | "It doesn't pretend every decision should be automated." |
| The send | Approve, then one teacher's phone showing only their change | "Nobody gets a spreadsheet. Each person gets their change." |
| Close | Plain end card | "What eats thirty minutes of your morning?" |

**Rules:** captions on, a silent-friendly cut, a transcript on the page. No time-saved figure on screen unless it's labeled as your estimate. Use the demo's real behavior only. If the tool can't do a beat, rewrite the beat.

**Stack:**
1. Screen Studio (Mac) for capture: slow cursor, one zoom at most per beat.
2. Your voice, in a quiet room with a decent USB mic. Audio quality matters more than video quality here.
3. Descript to edit: cut the words first, then fit the footage to them. Captions and transcript come out of it.
4. ElevenLabs voice clone: optional, only for fixing a word or two later, never the whole narration.

**Time, my estimate:** about 90 minutes to record, about 3 hours to edit the first time.

---

## 7. What I need from you

1. **Your call on the guarantee** (section 3). It blocks P0 item 4 and the offer box.
2. **Paste the handoff block below into your Mac Claude session** that works in `~/Documents/CLAUDE/Projects/Website/`. It has the files, the gates and the deploy command. I don't.
3. **After TFA:** one raw screen recording of the Maple Grove coverage demo, no narration, for the film.

---

## 8. Handoff block for the Mac session

```
Website session 092826. Read the plan first: "Website Plan 092826" in Notion (or in the Global repo on GitHub, branch claude/fervent-wozniak-spc2w9). It supersedes the recommendation in HANDOFF 092026b section 3.

Before editing: find the _build folder that matches the live deploy (6ab7bf2ab5c5162836324be6, published 092626). Compare it against a cache-busted curl of live. Never edit the root index.html. Stage in a new folder, _build/stage-092826/.

Do the P0 list only (plan section 4, items 1 to 9). Use the draft lines in plan section 5 as starting points, run every new sentence through write-like-us WRITE then SHIP, and keep my words where the drafts differ from how I talk. Item 2: check each tool's actual data flow before using the replacement line; if any tool sends names to an AI service, tell me which one and stop on that item. Item 4 waits for my guarantee answer, which is: [PASTE MY ANSWER HERE].

Gates: website-qa at 390 and 1440 widths plus qa-safari, zero em dashes, none of the barred words. Show me the phone render before giving me the deploy command. Write a SHIP RECORD (MMDDYY) to Notion when it's live.
```
