---
title: "Sens-AI Framework - From Habits to Tools"
type: reference
source: "https://www.oreilly.com/radar/from-habits-to-tools/"
author: "[[Andrew Stellman]]"
published: 2025-10-15
date_saved: 2025-10-15
description: "The Future of AI-Assisted Development"
tags: [ai-development, developer-productivity, best-practices, sens-ai-framework, clippings]
key_concepts: [context, research, framing, refining, critical-thinking, ai-assisted-coding]
topic: AI Development Best Practices
related_to: ["[[Research Summary - GitHub Copilot Enterprise Implementation]]"]
---
*This article is part of a series on the Sens-AI Framework—practical habits for learning and coding with AI.*

AI-assisted coding is here to stay. I’ve seen many companies now require all developers to install Copilot extensions in their IDEs, and teams are increasingly being measured on AI-adoption metrics. Meanwhile, the tools themselves have become genuinely useful for routine tasks: Developers regularly use them to generate boilerplate, convert between formats, write unit tests, and explore unfamiliar APIs—giving us more time to focus on solving our real problems instead of wrestling with syntax or going down research rabbit holes.

Many team leads, managers, and instructors looking to help developers ramp up on AI tools assume the biggest challenge is learning to write better prompts or picking the right AI tool; that assumption misses the point. The real challenge is figuring out how developers can use these tools in ways that keep them engaged and strengthen their skills instead of becoming disconnected from the code and letting their development skills atrophy.

This was the challenge I took on when I developed the Sens-AI Framework. When I was updating [*Head First C#*](https://learning.oreilly.com/library/view/head-first-c/9781098141776/) (O’Reilly 2024) to help readers ramp up on AI skills alongside other fundamental development skills, I watched new learners struggle not with the mechanics of prompting but with maintaining their understanding of the code they were producing. The framework emerged from those observations—five habits that keep developers engaged in the design conversation: context, research, framing, refining, and critical thinking. These habits address the real issue: making sure the developer stays in control of the work, understanding not just what the code does but why it’s structured that way.

## What We’ve Learned So Far

When I updated *Head First C#* to include AI exercises, I had to design them knowing learners would paste instructions directly into AI tools. That forced me to be deliberate: The instructions had to guide the learner while also shaping how the AI responded. Testing those same exercises against Copilot and ChatGPT showed the same kinds of problems over and over—AI filling in gaps with the wrong assumptions or producing code that looked fine until you actually had to run it, read and understand it, or modify and extend it.

Those issues don’t only trip up new learners. More experienced developers can fall for them too. The difference is that experienced developers already have habits for catching themselves, while newer developers usually don’t—unless we make a point of teaching them. AI skills aren’t exclusive to senior or experienced developers either; I’ve seen relatively new developers develop their AI skills quickly because they’ve built these habits quickly.

## Habits Across the Lifecycle

In “ [The Sens-AI Framework](https://www.oreilly.com/radar/the-sens-ai-framework/),” I introduced the five habits and explained how they work together to keep developers engaged with their code rather than becoming passive consumers of AI output. These habits also address specific failure modes, and understanding how they solve real problems points the way toward broader implementation across teams and tools:

**Context** helps avoid vague prompts that lead to poor output. Ask an AI to “make this code better” without sharing what the code does, and it might suggest adding comments to a performance-critical section where comments would just clutter. But provide the context—“This is a high-frequency trading system where microseconds matter,” along with the actual code structure, dependencies, and constraints—and the AI understands it should focus on optimizations, not documentation.

**Research** makes sure the AI isn’t your only source of truth. When you rely solely on AI, you risk compounding errors—the AI makes an assumption, you build on it, and soon you’re deep in a solution that doesn’t match reality. Cross-checking with documentation or even asking a different AI can reveal when you’re being led astray.

**Framing** is about asking questions that set up useful answers. “How do I handle errors?” gets you a try-catch block. “How do I handle network timeout errors in a distributed system where partial failures need rollback?” gets you circuit breakers and compensation patterns. As I showed in “ [Understanding the Rehash Loop](https://www.oreilly.com/radar/understanding-the-rehash-loop/),” proper framing can break the AI out of circular suggestions.

**Refining** means not settling for the first thing the AI gives you. The first response is rarely the best—it’s just the AI’s initial attempt. When you iterate, you’re steering toward better patterns. Refining moves you from “This works” to “This is actually good.”

**Critical thinking** ties it all together, asking whether the code actually works for your project. It’s debugging the AI’s assumptions, reviewing for maintainability, and asking, “Will this make sense six months from now?”

The real power of the Sens-AI Framework comes from using all five habits together. They form a reinforcing loop: Context informs research, research improves framing, framing guides refinement, refinement reveals what needs critical thinking, and critical thinking shows you what context you were missing. When developers use these habits in combination, they stay engaged with the design and engineering process rather than becoming passive consumers of AI output. It’s the difference between using AI as a crutch and using it as a genuine collaborator.

## Where We Go from Here

If developers are going to succeed with AI, these habits need to show up beyond individual workflows. They need to become part of:

**Education**: *Teaching AI literacy alongside basic coding skills.* As I described in “ [The AI Teaching Toolkit](https://www.oreilly.com/radar/the-ai-teaching-toolkit-practical-guidance-for-teams/),” techniques like having learners debug intentionally flawed AI output help them spot when the AI is confidently wrong and practice breaking out of rehash loops. These aren’t advanced skills; they’re foundational.

**Team practice**: *Using code reviews, pairing, and retrospectives to evaluate AI output the same way we evaluate human-written code.* In my teaching article, I described techniques like AI archaeology and shared language patterns. What matters here is making those kinds of habits part of standard training—so teams develop vocabulary like “I’m stuck in a rehash loop” or “The AI keeps defaulting to the old pattern.” And as I explored in “ [Trust but Verify](https://www.oreilly.com/radar/trust-but-verify/),” treating AI-generated code with the same scrutiny as human code is essential for maintaining quality.

**Tooling**: *IDEs and linters that don’t just generate code but highlight assumptions and surface design trade-offs.* Imagine your IDE warning: “Possible rehash loop detected: you’ve been iterating on this same approach for 15 minutes.” That’s one direction IDEs need to evolve—surfacing assumptions and warning when you’re stuck. The technical debt risks I outlined in *Building AI-Resistant Technical Debt* (Radar, September 10, 2025) could be mitigated with better tooling that catches antipatterns early.

**Culture**: *A shared understanding that AI is a collaboration too (and not a teammate)*. A team’s measure of success for code shouldn’t revolve around AI. Teams still need to understand that code, keep it maintainable, and grow their own skills along the way. Getting there will require changes in how they work together—for example, adding AI-specific checks to code reviews or developing shared vocabulary for when AI output starts drifting. This cultural shift connects to the requirements engineering parallels I explored in “ [Prompt Engineering Is Requirements Engineering](https://www.oreilly.com/radar/prompt-engineering-is-requirements-engineering/) ”—we need the same clarity and shared understanding with AI that we’ve always needed with human teams.

**More convincing output will require more sophisticated evaluation.** Models will keep getting faster and more capable. What won’t change is the need for developers to think critically about the code in front of them.

The Sens-AI habits work alongside today’s tools and are designed to stay relevant to tomorrow’s tools as well. They’re practices that keep developers in control, even as models improve and the output gets harder to question. The framework gives teams a way to talk about both the successes and the failures they see when using AI. From there, it’s up to instructors, tool builders, and team leads to decide how to put those lessons into practice.

The next generation of developers will never know coding without AI. Our job is to make sure they build lasting engineering habits alongside these tools—so AI strengthens their craft rather than hollowing it out.

Post topics:

Post tags: