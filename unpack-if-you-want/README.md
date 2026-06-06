# Unpack if you want

Inside `skills.zip` are three **finished** skills:

- **research** - web research with sources, saved to `outputs/`
- **voice** - writes in your personal style
- **content-agent** - research -> draft in your voice -> review -> post to LinkedIn

## Try building your own first

The point of this course is to build these yourself. Open the project in Claude
Code and ask it to create a skill (see `docs/BobAI-10-Use-Cases.pdf`). You'll
learn far more by writing your own `SKILL.md` than by copying mine.

## ...but if you get stuck, unpack these

Drop the ready-made skills into the live skills folder and they work instantly.

**In Finder:** double-click `skills.zip`, then drag the `research`, `voice`, and
`content-agent` folders into `.claude/skills/`.

**In the terminal** (from the project root):

```bash
unzip "unpack-if-you-want/skills.zip" -d .claude/skills/
```

**Or just ask Claude Code:**

> Unzip unpack-if-you-want/skills.zip into .claude/skills/ so the ready-made
> skills are active.

After that, restart Claude Code (or reopen the project) and `/research`, `/voice`,
and `/content-agent` will be available. Open one of them in `.claude/skills/` to
see how it's written - then make it your own.
