---
name: research
description: Research a topic on the web with sources. Use when the user says "research" or "look up" or "find information about" or invokes /research.
---

# Research Skill

When the user asks to research a topic:

## Steps

1. If the topic is unclear, ask one short clarifying question.
2. Use WebSearch to find 4-6 recent sources from the last 90 days.
3. Use WebFetch to read each source carefully.
4. Identify the 3 most important findings.
5. Write a structured summary in this format:

   ## TL;DR
   2 sentences max.

   ## Key Findings
   - Finding 1 (Source: [Publication], [Date])
   - Finding 2 (Source: ...)
   - Finding 3 (Source: ...)

   ## What this means for founders
   1 short paragraph with practical implication.

   ## Sources
   List all URLs with publication and date.

6. Save the file to outputs/research-{topic-slug}.md
7. Tell me where the file is saved.

## Rules

- Never invent statistics, dates, or quotes
- Only use sources from the last 90 days unless the topic is evergreen
- If you find fewer than 3 good sources, tell me and stop
- Prefer primary sources over aggregators