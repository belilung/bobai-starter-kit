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

- **`/research`** - search the web and write a sourced summary to `outputs/`.
- **`/voice`** - write a post in your personal style. Fill in your own samples
  first (see `.claude/skills/voice/SKILL.md`).
- **`/content-agent`** - the full pipeline: research -> draft in your voice ->
  you review -> publish to LinkedIn.
- **`tools/post_to_linkedin.py`** - the only thing that talks to LinkedIn.
- **`outputs/`** - where research notes and drafts are saved.

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
