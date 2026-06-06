# BobAI Starter Kit

A Claude Code project for learning to build your own **skills** - small folders of
plain-language instructions that turn into slash commands like `/research`.

**This kit ships with no active skills, on purpose.** The goal is for *you* to
build them. Three finished reference skills (**research**, **voice**,
**content-agent**) are zipped up in `unpack-if-you-want/` - a safety net you only
open if you get stuck.

Start with **`docs/BobAI-10-Use-Cases.pdf`** - 10 prompts that walk you through it.

---

## How it works

1. **Build your own skill.** Ask Claude Code to create one (the 10 Use Cases show
   you how). A skill is just `.claude/skills/<name>/SKILL.md`. See
   `.claude/skills/START-HERE.md`.
2. **Stuck? Unpack the ready-made ones.** Unzip `unpack-if-you-want/skills.zip`
   into `.claude/skills/` and `/research`, `/voice`, `/content-agent` work
   instantly. Read them to see how a good skill is written, then make them yours.

> **"I don't see anything in Finder!"** The skills folder is `.claude`, which
> starts with a dot - macOS Finder hides dot-folders. Press **Cmd + Shift + .**
> (period) to reveal it. Claude Code reads it either way.

---

## 1. Prerequisites

- **Claude Code** installed - https://claude.com/claude-code
- **Python 3** - check with `python3 --version` (any 3.10+ is fine)
- A terminal and this folder open in Claude Code

No `pip install` needed. The LinkedIn tool uses only the Python standard library.

## 2. Quick start

1. Unzip this folder somewhere you'll find it.
2. Open the folder in Claude Code (`cd` into it, run `claude`).
3. Open `docs/BobAI-10-Use-Cases.pdf` and copy **Use Case #1** into the chat.

Use Case #1 has you build your first skill from scratch. Prefer the shortcut?
Unzip `unpack-if-you-want/skills.zip` into `.claude/skills/` and the finished
skills are live.

## 3. Set up your voice (2 minutes)

The voice skill ships empty on purpose - it needs *your* writing. Whether you
built your own or unpacked the ready one, open `.claude/skills/voice/SKILL.md`,
paste 3-5 of your own posts into the `## Voice samples` section, and save. That's
how Claude learns to write like you.

## 4. Set up LinkedIn publishing (required to post)

Publishing goes through `tools/post_to_linkedin.py`, which reads a token from
`.env`. Drafting and research work without this - you only need it to actually
post.

**Get a token that can post:**

1. Copy the template: `cp .env.example .env`
2. Go to https://www.linkedin.com/developers/apps and **create an app** (link it
   to a Company Page you control - LinkedIn requires one).
3. On the app's **Products** tab, request the **"Share on LinkedIn"** product and
   wait for it to be granted.
4. Generate an access token that includes the **`w_member_social`** scope (and
   `openid profile` so the tool can find your user id).
5. Paste it into `.env`:
   ```
   LINKEDIN_TOKEN=your_token_here
   ```

> **Important:** a token from "Sign In with LinkedIn" (OIDC) will NOT work for
> posting - it only has `openid/profile/email`. You need the **Share on LinkedIn**
> product and the **`w_member_social`** scope, or every post returns a 403.

Test it (this prints a usage error and posts nothing):
```bash
python3 tools/post_to_linkedin.py
```

## 5. Using the skills

Once a skill exists in `.claude/skills/` (built by you, or unpacked), it's a slash
command:

| Command | What it does | Example |
|---|---|---|
| `/research` | Web research with sources, saved to `outputs/` | `/research the latest AI tools for solo founders` |
| `/voice` | Write something in your style | `/voice a short LinkedIn post about shipping my first project` |
| `/content-agent` | Research -> draft -> you review -> publish | `/content-agent write a post about AI lead-gen for founders` |

Don't see them? You haven't built or unpacked any skills yet - see "How it works"
at the top.

## 6. Safety notes

- `.env` is gitignored - your token stays on your machine and is never committed.
- Claude **never posts without your explicit confirmation** - it shows you the
  draft and waits for a clear "post it."
- Every draft is saved to `outputs/` so you always keep a copy.

## Folder map

```
.claude/skills/        where YOUR skills live (starts empty + START-HERE.md)  [hidden in Finder]
unpack-if-you-want/     skills.zip - the 3 finished skills, as a fallback
tools/                  post_to_linkedin.py (the only thing that posts)
outputs/                research notes and drafts land here
docs/                   the 10 Use Cases (PDF + markdown)
CLAUDE.md               how Claude should behave in this project
.env.example            copy to .env and add your token                       [hidden in Finder]
```

Folders that start with a dot (`.claude`, `.env.example`, `.gitignore`) are hidden
by macOS Finder. Reveal them with **Cmd + Shift + .** - Claude Code reads them
regardless.
