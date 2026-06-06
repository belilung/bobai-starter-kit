---
name: content-agent
description: Research a topic, write a LinkedIn post in my voice, review with me, and publish to LinkedIn. Use when the user says "content agent", "write me a LinkedIn post about X", or invokes /content-agent.
---

# Content Agent Skill

End-to-end pipeline: research a topic, draft a post in the user's voice, iterate with the user, then publish to LinkedIn.

## Steps

1. **Topic** — if the user did not give a topic in the invocation, ask one short question to get it.

2. **Research** — invoke the existing `research` skill on the topic. Do not duplicate its logic. It will save `outputs/research-{topic-slug}.md`. Note the slug; reuse it in step 6.

3. **Draft** — invoke the existing `voice` skill, using the research summary as source material. Ask the user **once** for the target length (short / medium / long, or an explicit line count) and pass that to the voice skill so it does not need to ask again at the end.

4. **Show the draft inline** — print the full post text in the chat exactly as it would appear on LinkedIn.

5. **Review loop** — use the `AskUserQuestion` tool with these three options:
   - **Post as-is** → go to step 6
   - **Revise** → the user describes what to change in plain language; rewrite the draft (still respecting all `voice` skill rules, especially the banned-word list and the no-em-dash rule), then show the new draft and ask again
   - **Cancel** → save the current draft to `outputs/linkedin-post-{topic-slug}.md` and stop

   Loop until the user picks Post or Cancel. Never auto-post.

6. **Publish** — only after explicit Post confirmation:
   - Save the final text to `outputs/linkedin-post-{topic-slug}.md` (overwrite if it exists)
   - Run `python3 tools/post_to_linkedin.py "<final text>"` from the project root
   - If the tool exits 0, share the URN and public URL it printed
   - If the tool exits non-zero, surface the full stderr message to the user — do not retry automatically

## Rules

- **Never post without an explicit Post confirmation from step 5.** A user typing "looks good" is not enough — only the `AskUserQuestion` "Post as-is" choice counts.
- **Never call the LinkedIn API directly from this skill.** Always go through `tools/post_to_linkedin.py`.
- **Never print or log the `LINKEDIN_TOKEN` value.** If the tool reports the token is missing, tell the user to check `.env` — do not try to read or echo the file.
- **Always save the final draft to `outputs/linkedin-post-{slug}.md`**, whether the user posted, cancelled, or the publish step failed. The user should always have a copy on disk.
- Respect every rule from the `voice` skill (banned words, no em-dash, voice samples) during the revise loop — do not relax them just because the user asked for a change.
