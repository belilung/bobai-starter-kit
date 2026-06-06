# BobAI Starter Kit — 10 Use Cases

Ten ready-to-run prompts. Copy any prompt into Claude Code and go. They build on
each other, so working top to bottom is the fastest way to learn the kit.

## Before you start: the skills are empty on purpose

This kit ships with **no active skills**. The point is to build them yourself - the
prompts below help you do exactly that. Two ways to use this:

- **Build your own** (recommended): the prompts coach you to write each skill from
  scratch in `.claude/skills/`. That's where the real learning is.
- **Unpack the ready ones** (shortcut): unzip `unpack-if-you-want/skills.zip` into
  `.claude/skills/`, and `/research`, `/voice`, `/content-agent` work instantly.
  Use them, then read them to see how they're built.

For the voice prompts, fill in your own samples in `.claude/skills/voice/SKILL.md`.
For publishing, set your `LINKEDIN_TOKEN` in `.env` (see README section 4).

---

## 01 — Run your first research
**Goal:** get a clean, sourced summary on any topic.

> /research the latest AI tools for solo founders in 2026

**What to expect:** Claude searches recent sources, reads them, and writes a
TL;DR + key findings + sources to `outputs/research-<topic>.md`.
**Tip:** if the topic is broad, Claude asks one clarifying question - answer it
and it continues.

---

## 02 — Sharpen a research request
**Goal:** control the angle and the time window.

> /research AI lead-generation for B2B founders. Focus on tactics people actually
> shipped in the last 60 days, not predictions. Give me 5 sources.

**What to expect:** tighter findings, recent-only sources, a "what this means for
founders" takeaway.
**Tip:** name the audience and the timeframe - you get sharper results.

---

## 03 — Set up your voice
**Goal:** teach Claude to write like you (one-time setup).

> Open .claude/skills/voice/SKILL.md and help me add my voice samples. I'll paste
> three of my posts and you put them in the right place.

**What to expect:** Claude drops your posts into the samples section without
breaking the file's rules.
**Tip:** pick posts that sound the most like *you* - casual, real, your emojis.

---

## 04 — Write a post in your voice
**Goal:** turn an idea into a post that sounds like you.

> /voice a short LinkedIn post about why I started learning to build with AI

**What to expect:** a draft in your style, with the banned corporate words and
em-dashes avoided. Claude asks how long you want it.
**Tip:** give it one concrete detail (a number, a moment) and the post gets real.

---

## 05 — Adjust tone and length
**Goal:** refine a draft without losing your voice.

> Make that post 30% shorter, open with a question, and keep it warm not salesy.

**What to expect:** a rewrite that still respects every voice rule.
**Tip:** describe the change in plain language - "punchier", "less braggy",
"end on a question."

---

## 06 — One research note, two post lengths
**Goal:** get more mileage out of a single research run.

> Using my latest research in outputs/, write me two versions: a 3-line hook post
> and a longer story post. Both in my voice.

**What to expect:** two drafts from the same source material, saved so you can
compare.
**Tip:** post the short one first; keep the long one for later in the week.

---

## 07 — The full pipeline
**Goal:** research, draft, and review in one flow.

> /content-agent write a LinkedIn post about AI tools that save solo founders time

**What to expect:** Claude researches, drafts in your voice, then shows you the
post and asks: post as-is, revise, or cancel. It never posts on its own.
**Tip:** this chains the research and voice skills for you - one command does it all.

---

## 08 — Revise inside the pipeline
**Goal:** iterate on the draft before anything goes live.

> Revise: cut the intro, lead with the strongest tip, and add a line about my own
> experience.

**What to expect:** the draft updates, voice rules still hold, and you're asked
again - revise or post.
**Tip:** you can loop revise as many times as you want. Nothing publishes until
you choose to.

---

## 09 — Publish to LinkedIn
**Goal:** post the approved draft for real.

> Looks great. Post it to LinkedIn.

**What to expect:** with your `LINKEDIN_TOKEN` set, Claude runs the tool and shares
the live URL. The draft is saved to `outputs/` either way.
**Tip:** no token yet? See README section 4. A "Sign In with LinkedIn" token won't
work - you need the Share on LinkedIn product and the `w_member_social` scope.

---

## 10 — Extend the kit
**Goal:** make Claude Code build you a new skill.

> Create a new skill called "newsletter" in .claude/skills/ that turns one of my
> research notes into a short email newsletter in my voice. Follow the same format
> as the existing skills.

**What to expect:** a new `SKILL.md` you can run as `/newsletter` next time.
**Tip:** this is the real superpower - the kit grows as you ask for more.
