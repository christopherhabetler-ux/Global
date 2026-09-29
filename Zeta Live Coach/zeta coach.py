#!/usr/bin/env python3
"""Zeta live interrupt coach, 092926. No dependencies.

Watches a transcript file that grows while you talk and flashes one short
alert when a trigger phrase appears, plus clock alerts. Same design as the
081426 LIVE CALL COACH: no model in the loop, so alerts are instant.

  python3 "zeta coach.py" --transcript ~/transcripts/live.txt     # live
  python3 "zeta coach.py" --transcript old.txt --replay            # test on an old transcript
  python3 "zeta coach.py" --demo                                   # see the display, no audio
"""
import argparse, os, re, sys, time

CALL_MINUTES = 30
COOLDOWN = 90  # seconds before the same alert can fire again

# (level, phrases, alert). Phrases are matched case-insensitively on what was just said.
TRIGGERS = [
    ("STOP",    ["wish i had the answer", "don't have the answer", "i'm not sure i have"], "Claim first. \"High school can't be middle school with the dials turned.\""),
    ("SAY",     ["able to be successful", "we were successful", "it went well"], "Say the number. Doubled. Louisiana Principal of the Year. Runs the network now."),
    ("SAY",     ["mandate authority"], "Now land it on Carver. A person, a result."),
    ("CAREFUL", ["b minus", "c minus", "kipp didn't", "kipp doesn't", "franchise model", "fiefdom"], "Don't grade KIPP or AF. Describe how it works."),
    ("STOP",    ["rest of the mess"], "Drop it. Both of them are ex-Success."),
    ("STOP",    ["heart", "health reason", "surgery"], "Stop. \"I knew I'd be leaving at the end of the year.\""),
    ("CAREFUL", ["operations transformation", "the ops role", "ops seat"], "All in on the schooling side."),
    ("CAREFUL", ["better part of a decade"], "Fourteen years."),
    ("CAREFUL", ["reauthoriz", "renewal"], "Context: two authorizers, no reliable records, COVID, an acquisition. All at once."),
    ("CAREFUL", ["i was a principal", "been a principal", "as principal"], "Interim. Say interim."),
    ("SAY",     ["earn that", "earn it"], "Now the investment: how you support them to get there."),
    ("CAREFUL", ["fifth, sixth", "fifth sixth"], "Jackie: sixth grade, or drop the grade."),
    ("CAREFUL", ["taking off"], "Don't claim usage. Built, not running."),
    ("SAY",     ["compensation", "salary", "what range", "pay range", "what are you looking for"], "Don't name a number first. Title and pay match the scope. Top of the band."),
    ("SAY",     ["commute", "in person every day", "in the building every day", "westchester ave"], "Short answer. Only what's true."),
    ("STOP",    ["blah"], "End on the ask: next step, and who else?"),
    ("STOP",    ["i hope that answers", "does that answer", "i could go on"], "Stop. Ask them a question."),
]
TIMERS = [
    (1,  "SAY",  "Frame first. A number in the first 20 seconds."),
    (8,  "SAY",  "ASK: which role are you considering me for? Success at 12 months?"),
    (11, "CAREFUL", "Did you ask the role question? If not, now."),
    (20, "SAY",  "Your two questions. Kruti: consistency across new campuses. Paola: the 119 ninth graders."),
    (26, "SAY",  "Next step, and who else would I talk to?"),
    (29, "STOP", "Close: thank you, I'm excited. Stop talking."),
]

COL = {"STOP": "\033[1;97;41m", "SAY": "\033[1;30;43m", "CAREFUL": "\033[1;97;44m"}
RST = "\033[0m"

def norm(s):
    return re.sub(r"\s+", " ", s.lower().replace("’", "'"))

class Coach:
    def __init__(self, clock=time.time):
        self.clock = clock
        self.start = clock()
        self.last = {}
        self.fired_timers = set()
        self.heard = ""
        self.current = None

    def elapsed(self):
        return self.clock() - self.start

    def feed(self, text):
        t = norm(text)
        self.heard = (self.heard + " " + t)[-160:]
        out = []
        for level, phrases, alert in TRIGGERS:
            for p in phrases:
                if p in t:
                    now = self.clock()
                    if now - self.last.get(alert, -1e9) >= COOLDOWN:
                        self.last[alert] = now
                        out.append((level, alert, p))
                    break
        return out

    def timers(self):
        m = self.elapsed() / 60
        out = []
        for minute, level, alert in TIMERS:
            if m >= minute and minute not in self.fired_timers:
                self.fired_timers.add(minute)
                out.append((level, alert, f"minute {minute}"))
        return out

def draw(coach, alert=None):
    e = int(coach.elapsed())
    mm, ss = divmod(e, 60)
    left = max(0, CALL_MINUTES * 60 - e)
    sys.stdout.write("\033[2J\033[H")
    print(f"\033[1m ZETA · {mm:02d}:{ss:02d} elapsed · {left//60:02d}:{left%60:02d} left\033[0m\n")
    if alert:
        level, text, why = alert
        print(f" {COL[level]}  {level}  {RST}\n")
        print(f"\033[1m {text}\033[0m\n")
        print(f"\033[2m ({why})\033[0m")
        sys.stdout.write("\a")
    else:
        print(" \033[2m(listening)\033[0m")
    print(f"\n\033[2m heard: ...{coach.heard[-90:]}\033[0m")
    sys.stdout.flush()

def live(path):
    coach = Coach()
    while not os.path.exists(path):
        draw(coach); print(f"\n waiting for {path}"); time.sleep(1)
    with open(path, "r", errors="ignore") as f:
        f.seek(0, 2)
        shown, shown_at = None, 0
        while True:
            chunk = f.read()
            hits = coach.feed(chunk) if chunk else []
            hits += coach.timers()
            if hits:
                shown, shown_at = hits[0], time.time()
            if shown and time.time() - shown_at > 12:
                shown = None
            draw(coach, shown)
            time.sleep(0.7)

def replay(path):
    t = [0.0]
    coach = Coach(clock=lambda: t[0])
    n = 0
    for line in open(path, errors="ignore"):
        line = line.strip()
        if not line:
            continue
        t[0] += 12  # assume about 12 seconds per transcript line
        for level, alert, why in coach.feed(line) + coach.timers():
            n += 1
            print(f"{level:8} {alert}\n         ...\"{line[:110]}\"  [{why}]\n")
    print(f"{n} alerts.")

def demo():
    t0 = time.time()
    coach = Coach()
    samples = ["I wish I had the answer, but", "we were able to be successful in that", "the rest of the mess", "blah, blah, blah"]
    for s in samples:
        hit = coach.feed(s)
        draw(coach, hit[0] if hit else None)
        time.sleep(3)
    print("\n demo done")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcript")
    ap.add_argument("--replay", action="store_true")
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()
    if a.demo:
        demo()
    elif a.replay and a.transcript:
        replay(a.transcript)
    elif a.transcript:
        live(os.path.expanduser(a.transcript))
    else:
        ap.print_help()
