# BobAI Starter Kit

A ready-to-run Claude Code project. It comes with three skills - **research**,
**voice**, and **content-agent** - so you can go from "I have a topic" to a
published LinkedIn post, all by talking to Claude.

Start with **`docs/BobAI-10-Use-Cases.pdf`** - 10 prompts you can copy straight
into the chat.

> **"I don't see the skills in Finder!"** That's normal. The skills live in a
> folder called `.claude` that starts with a dot, and macOS Finder hides
> dot-folders. They are still there, and **Claude Code reads them automatically**.
> To see the folder in Finder, press **Cmd + Shift + .** (period). You don't have
> to - just open this folder in Claude Code and the skills work.

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

That first one (research) works immediately - no setup. Voice and publishing need
the two short steps below.

## 3. Set up your voice (2 minutes)

Open `.claude/skills/voice/SKILL.md`. It ships empty on purpose. Paste 3-5 of your
own posts into the `## Voice samples` section, replacing the placeholders. That's
how Claude learns to write like you. Save the file.

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

| Command | What it does | Example |
|---|---|---|
| `/research` | Web research with sources, saved to `outputs/` | `/research the latest AI tools for solo founders` |
| `/voice` | Write something in your style | `/voice a short LinkedIn post about shipping my first project` |
| `/content-agent` | Research -> draft -> you review -> publish | `/content-agent write a post about AI lead-gen for founders` |

## 6. Safety notes

- `.env` is gitignored - your token stays on your machine and is never committed.
- Claude **never posts without your explicit confirmation** - it shows you the
  draft and waits for a clear "post it."
- Every draft is saved to `outputs/` so you always keep a copy.

## Folder map

```
.claude/skills/   the three skills (research, voice, content-agent)  [hidden in Finder]
tools/            post_to_linkedin.py (the only thing that posts)
outputs/          research notes and drafts land here
docs/             the 10 Use Cases (PDF + markdown)
CLAUDE.md         how Claude should behave in this project
.env.example      copy to .env and add your token                    [hidden in Finder]
```

Folders that start with a dot (`.claude`, `.env.example`, `.gitignore`) are hidden
by macOS Finder. Reveal them with **Cmd + Shift + .** - Claude Code reads them
regardless.
