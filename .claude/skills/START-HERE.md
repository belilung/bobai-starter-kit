# Your skills go here

This folder is **empty on purpose**. The whole point of this kit is that *you*
build your own skills with Claude Code - that's the real lesson.

A skill is just a folder with a `SKILL.md` file inside it:

```
.claude/skills/
└── research/
    └── SKILL.md     <- a name + description + plain-language instructions
```

When a folder like that exists here, Claude Code turns it into a slash command
(`/research`) automatically.

## Build your own (do this first)

Ask Claude Code, for example:

> Create a skill called "research" in .claude/skills/ that searches the web for
> recent sources on a topic and writes a sourced summary to outputs/.

Then run it with `/research ...`. The 10 Use Cases in `docs/` walk you through it.

## Stuck? Unpack the ready-made ones

Three finished skills (**research**, **voice**, **content-agent**) are waiting in
[`../../unpack-if-you-want/`](../../unpack-if-you-want/). Unzip `skills.zip` into
this folder and they work instantly. Use them as a reference, or as a safety net.

> Note: this `START-HERE.md` file is not a skill (no `SKILL.md`), so Claude Code
> ignores it. You can delete it once you've added your own skills.
