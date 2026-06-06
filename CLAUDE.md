# Agent Instructions

This is a Claude Code starter kit. It gives you three ready-made skills and one
tool so you can research a topic, write it up in your own voice, and publish to
LinkedIn - all from a conversation.

## The WAT idea (Workflows, Agents, Tools)

The system splits the work so that the AI does the thinking and plain code does
the doing. That separation is what keeps it reliable.

- **Workflows / Skills** - the instructions. Markdown files in `.claude/skills/`
  that tell Claude how to do one job well.
- **Agent** - that's Claude. It reads the skill, runs the steps in order, handles
  problems, and asks you when something is unclear.
- **Tools** - the execution. Python scripts in `tools/` that do exact, repeatable
  work like calling the LinkedIn API. Credentials live in `.env` and nowhere else.

Why it matters: if every step were left to the AI guessing, accuracy would drop
fast. Offloading the exact steps to scripts keeps things consistent.

## What's in here

**The kit ships with no active skills - that is intentional.** The goal is for the
student to *build their own* skills with you. Help them do that.

- **`.claude/skills/`** - empty, with a `START-HERE.md` guide. New skills the
  student writes (a folder + a `SKILL.md`) become slash commands here.
- **`unpack-if-you-want/skills.zip`** - three finished reference skills
  (**research**, **voice**, **content-agent**). Only unpack these into
  `.claude/skills/` if the student is stuck or wants a reference.
- **`tools/post_to_linkedin.py`** - the only thing that talks to LinkedIn.
- **`outputs/`** - where research notes and drafts are saved.

## How to help the student

1. **Default to coaching them to build their own skill**, not handing them the
   finished one. If they ask "how do I research a topic," help them author a
   `research` skill in `.claude/skills/` - don't just unpack mine.
2. **Only unpack `unpack-if-you-want/skills.zip` when they ask** (e.g. "I'm stuck,
   just give me the ready ones"). Then unzip it into `.claude/skills/`.

## Ground rules

1. **Never post to LinkedIn without explicit confirmation from the user.**
   "Looks good" is not enough - wait for a clear "post it."
2. **Never print, log, or echo the `LINKEDIN_TOKEN`.** If it's missing, tell the
   user to check `.env`. Don't read the file out loud.
3. **Always save the draft to `outputs/` first**, whether it gets posted or not.
4. **Look for an existing skill or tool before building something new.**

## Start here

Open `docs/BobAI-10-Use-Cases.pdf` (or `docs/10-use-cases.md`) - it has 10
ready-to-run prompts. Copy one into the chat and go.
