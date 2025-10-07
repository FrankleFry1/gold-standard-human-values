# Gold Standard for Human Values

**An experimental approach to ethics development through human-AI collaboration**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/FrankleFry1/gold-standard-human-values/blob/main/CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/FrankleFry1/gold-standard-human-values/releases/tag/v1.0)

## Overview
This repository contains a comprehensive ethical framework designed to address AI alignment challenges and navigate value conflicts in an increasingly AI-integrated world. It emerged from a unique methodological experiment: iterative collaboration between a human researcher and four frontier AI systems (Claude, ChatGPT, Grok, and Gemini).

**Core Question:** How do we develop ethical frameworks for AI alignment when humanity has never achieved consensus on values?

**Key Innovation:** The framework explicitly addresses how to handle tensions *between* principles—not just what the principles are.

## Quick Start
To apply this framework immediately:
- **For AI Prompting:** Use the pillars as a lens for evaluating decisions. Example prompt template for LLMs:
  ```
  Evaluate [decision/issue] through these six pillars:
  1. Curiosity and Truth-Seeking: [Assess evidence and openness]
  2. Empathy and Mutual Flourishing: [Consider suffering and equity]
  3. Dignity and Agency: [Evaluate autonomy and accountability]
  4. Sustainability and Long-Term Stewardship: [Weigh long-term impacts]
  5. Adaptability and Diversity: [Check for pluralism and evolution]
  6. Integrity and Responsibility: [Ensure alignment of actions]
  Provide balanced recommendations.
  ```
- **For Personal/Team Use:** Download [CHARTER.md](CHARTER.md) and discuss a real dilemma (e.g., AI deployment ethics) pillar-by-pillar.
- **For Developers:** See [examples/ai-prompt-template.md](examples/ai-prompt-template.md) for code snippets (coming soon—contribute yours!).

## The Six Pillars
1. **Curiosity and Truth-Seeking** - Evidence-based reasoning, intellectual humility, and diverse paths to meaning
2. **Empathy and Mutual Flourishing** - Minimizing suffering, expanding moral consideration, balancing outcomes and rights
3. **Dignity and Agency** - Inherent worth, autonomy, participatory governance, and accountability
4. **Sustainability and Long-Term Stewardship** - Intergenerational justice, ecological balance, technological alignment
5. **Adaptability and Diversity** - Cultural pluralism, moral evolution, resilience through diversity
6. **Integrity and Responsibility** - Aligning words and deeds, moral courage, accountability systems

## What Makes This Different
### Explicit Tension Navigation
Most ethical frameworks list principles but struggle when they conflict. This framework includes detailed guidance (Article VII) on navigating common tensions:
- Curiosity vs. Empathy (when truth-seeking causes harm)
- Sustainability vs. Present Well-Being (when long-term survival requires sacrifice)
- Dignity/Agency vs. Collective Flourishing (when individual freedom conflicts with social good)
- **Existential Tensions** (when defending principles requires compromising them)

### Multi-AI Collaboration Methodology
This framework was developed through structured dialogue with four different AI systems, each with distinct training approaches and constitutional principles:
- **Claude (Anthropic):** Constitutional AI approach, emphasis on harmlessness
- **ChatGPT (OpenAI):** RLHF optimization, emphasis on helpfulness
- **Grok (xAI):** "Maximum truth-seeking" positioning, less filtered
- **Gemini (Google):** Different training corpus and safety guidelines

**The process:**
1. I posed the core alignment question to each AI independently
2. Each proposed frameworks with different emphases and gaps
3. I identified convergences (robust principles) and divergences (requiring human judgment)
4. Through iterative refinement, I synthesized across perspectives
5. Where AIs disagreed, I pushed for resolution or explicit acknowledgment
6. The human role: asking hard questions, identifying missing elements, making final judgment calls

**Why this matters:** Using multiple AIs reduces single-system bias and models the framework's own principle of diverse dialogue leading to better outcomes.

## Document Structure
The framework is formatted as a **Formal Charter** with:
- **Preamble** - Philosophical foundation and scope
- **Articles I-VI** - The Six Pillars (each with principles, commitments, and rationale)
- **Article VII** - Navigating tensions between pillars, including existential threats
- **Article VIII** - Implementation pathways
- **Article IX** - Conclusion and affirmation

## Repository Structure

- **[CHARTER.md](./CHARTER.md)** - Core philosophical framework (Six Pillars)
- **[AI-ALIGNMENT-ANNEX.md](./AI-ALIGNMENT-ANNEX.md)** - Technical implementation for AI systems (v0.1 DRAFT)
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to improve this framework

### Relationship Between Documents

**Charter (Main Branch):** Establishes normative principles - *what* values should guide human-AI coexistence

**Technical Annex (v2.0 Branch):** Operationalizes those principles - *how* to enforce them against advanced AI systems

The separation is intentional:
- Philosophy should remain stable and broadly applicable
- Technical requirements must evolve rapidly with AI capabilities
- Different stakeholders focus on different documents (ethicists vs. engineers)
Full charter: [CHARTER.md](CHARTER.md)  
Google Doc for comments: [https://docs.google.com/document/d/1Quo-LtVhkIRg6Nu3pGOG3U89bC-M_-RW/edit?usp=sharing](https://docs.google.com/document/d/1Quo-LtVhkIRg6Nu3pGOG3U89bC-M_-RW/edit?usp=sharing)

## Key Contributions
### 1. Article VII, Section B: Existential Tensions
Perhaps the most novel element—guidance on when defending ethical principles requires temporary deviation from those principles. Includes:
- Seven safeguards for emergency compromises (proportionality, temporality, democratic authorization, oversight, transparency, sunset clauses, moral residue recognition)
- What can *never* be compromised (prohibition of torture/genocide, fundamental equality, right to challenge authority)
- Warning against abuse of "existential" rhetoric

### 2. Integration of Economic Justice
Explicit acknowledgment (Article III) that dignity and agency require addressing resource constraints and economic systems—not just abstract rights.

### 3. Reconciliation and Forgiveness
Unlike many frameworks that focus only on punishment, this includes commitment to repairing harm and reintegrating after ethical failures (Article VI).

## Intended Applications
This framework could inform:
- **Constitutional AI development** - Providing richer value specifications for training
- **AI governance policy** - Guiding regulation that balances innovation and safety
- **Institutional ethics review** - Framework for assessing AI deployment decisions
- **Cross-cultural dialogue** - Common ground for values discussions across traditions
- **Education** - Teaching ethical reasoning in the AI age

## Limitations and Acknowledgments
**This framework is incomplete and culturally situated:**
- Emerged primarily from Western philosophical traditions (Enlightenment liberalism, utilitarianism, deontology)
- Training data for all four AIs is predominantly English-language and Western-centric
- Human synthesizer (me) brings own cultural assumptions and blind spots
- Needs critique from non-Western philosophical traditions
- Implementation mechanisms are underspecified

**This is explicitly version 1.0.** The framework itself calls for adaptation based on evidence and experience.

## Roadmap
- **Short-Term (Q4 2025):** Add examples folder with AI integration code, case studies, and prompt templates.
- **Medium-Term (Q1 2026):** Incorporate initial feedback from EA Forum and X discussions; release v1.1 with revisions.
- **Long-Term:** Build community tools (e.g., online pillar evaluator), seek translations, and test in real AI projects.
- **Ongoing:** Monitor issues/PRs and update based on critiques.

## How to Contribute
I'm seeking rigorous critique and improvement:

### Specific Questions
1. **For AI safety researchers:** Could this inform Constitutional AI or reward modeling approaches? Where does it fail under adversarial pressure?
2. **For philosophers:** What cultural assumptions am I missing? Which philosophical traditions would critique this framework?
3. **For policymakers:** Is this practical for actual governance decisions? What real-world case breaks it?
4. **For implementers:** How would you operationalize these principles in an organization?
5. **For anyone:** What's the most important thing missing?

### Ways to Contribute
- **Open an Issue** - Point out flaws, gaps, or unclear sections
- **Pull Request** - Suggest specific improvements to the Charter text
- **Discussions** - Share how you'd apply this to real dilemmas
- **Translations** - Help make this accessible in other languages
- **Case Studies** - Test the framework against actual AI ethics dilemmas

**All contributions welcome.** The goal is refinement through dialogue, not defense of a fixed position.

## Methodology Transparency
### What Worked in Multi-AI Collaboration
- **Complementary strengths:** Each AI emphasized different principles (Grok pushed on curiosity/truth, Claude on dignity/integrity, etc.)
- **Bias detection:** When all four agreed strongly, likely a robust principle; when they diverged, required human judgment
- **Iterative refinement:** Each conversation improved on the last

### What Was Difficult
- **Synthesis burden:** Human role in resolving contradictions was significant
- **Style homogenization:** AIs tend toward similar formal language despite different "personalities"
- **Verification:** Hard to know if convergence reflects training data overlap vs. genuine principle strength

### What I'd Change Next Time
- More structured disagreement protocols
- Explicit red-teaming phase (have AIs attack the framework)
- Earlier involvement of human domain experts
- Cross-cultural validation throughout, not just at the end

## Citation
If you reference this work:
```
Six-Pillar Framework for AI Alignment and Human Values (2025)
Developed through human-AI collaboration (Claude, ChatGPT, Grok, Gemini)
https://github.com/FrankleFry1/gold-standard-human-values
```

## License
This framework is released under MIT License to maximize accessibility and adaptation while requiring attribution.

## Contact
- **GitHub Issues:** For technical questions and suggestions
- **Discussions:** For philosophical debates and applications
- **Email:** johnhaun04@gmail.com

## Acknowledgments
This framework builds on centuries of moral philosophy and recent AI safety research. Particular intellectual debts to:
- Constitutional AI research (Anthropic)
- Value alignment work (Stuart Russell, Nick Bostrom, Toby Ord)
- Democratic deliberation theory
- Effective altruism and longtermism communities
- All those who will critique and improve this

---
**Status:** Version 1.0 - Released 10/07/2025 - Open for critique and revision  
**Last Updated:** 10/07/2025
