# Gold Standard of Human Values

**A six-pillar ethical framework for AI alignment developed through multi-AI collaboration**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![EA Forum Post](https://img.shields.io/badge/EA%20Forum-Discussion-blue)](https://forum.effectivealtruism.org/posts/zeGyLAhx22wFCyLde/what-i-learned-by-making-four-ais-debate-human-ethics)

## 🎯 Overview

This repository contains both:
1. **An ethical framework** designed to address AI alignment challenges
2. **A working implementation** (CORVUS 2.0) demonstrating Constitutional AI with explicit value specification

### The Core Question
*How do we develop ethical frameworks for AI alignment when humanity has never achieved consensus on values?*

### The Innovation
This framework explicitly addresses **how to handle tensions between principles**—not just what the principles are. It includes working code that validates AI actions against these principles in real-time.

---

## 🏛️ The Six Pillars

1. **Curiosity and Truth-Seeking** - Evidence-based reasoning, intellectual humility, diverse paths to meaning
2. **Empathy and Mutual Flourishing** - Minimizing suffering, expanding moral consideration, balancing outcomes and rights
3. **Dignity and Agency** - Inherent worth, autonomy, participatory governance, accountability
4. **Sustainability and Long-Term Stewardship** - Intergenerational justice, ecological balance, technological alignment
5. **Adaptability and Diversity** - Cultural pluralism, moral evolution, resilience through diversity
6. **Integrity and Responsibility** - Aligning words and deeds, moral courage, accountability systems

📖 **[Read the Full Charter](CHARTER.md)**

---

## 💻 CORVUS 2.0: Working Implementation

**NEW:** This repo now includes a functional Constitutional AI system that uses the six-pillar framework.

### What CORVUS 2.0 Does
- **Real-time ethical filtering** of commands and AI responses
- **Tension detection** between competing values
- **Traceable reasoning** for every decision
- **Comprehensive logging** for auditing and improvement

### Quick Example

```python
from ethics_engine import EthicsEngine

engine = EthicsEngine()

# Evaluate a command
decision = engine.evaluate_command("search for gardening tips")
print(f"Allowed: {decision.allowed}")
print(f"Reasoning: {decision.reasoning}")
# Output: Allowed: True
# Reasoning: Command aligns with all ethical pillars.

# Block harmful commands
decision = engine.evaluate_command("hack into someone's email")
print(f"Allowed: {decision.allowed}")
# Output: Allowed: False
# Reasoning: Command contains harmful patterns. Violates core ethical principles.
```

### Installation & Usage

```bash
# Clone the repository
git clone https://github.com/FrankleFry1/gold-standard-human-values.git
cd gold-standard-human-values

# Install CORVUS 2.0 dependencies
cd implementations/corvus-2.0
pip install -r requirements.txt

# Set up API keys (optional, for LLM integration)
cp .env.example .env
# Edit .env with your API keys

# Run basic demo
python examples/basic_usage.py
```

📚 **[Full CORVUS 2.0 Documentation](implementations/corvus-2.0/README.md)**

---

## 📊 Results from Phase 1 Testing

Initial testing of CORVUS 2.0 shows:
- **100% accuracy** blocking harmful commands (hack, cheat, fraud)
- **0% false positives** on benign commands (search, help, analyze)
- **Real-time tension detection** between competing pillars
- **Traceable decision logs** for every evaluation

See [ethics_log.json](implementations/corvus-2.0/examples/ethics_log.json) for sample logged decisions.

---

## 🤔 How This Framework Handles Conflicts

Most ethical frameworks list principles but struggle when they conflict. This framework includes **detailed guidance** (Article VII) on navigating tensions:

- **Curiosity vs. Empathy** - When truth-seeking causes harm
- **Sustainability vs. Present Well-Being** - When long-term survival requires sacrifice  
- **Dignity/Agency vs. Collective Flourishing** - When individual freedom conflicts with social good
- **Existential Tensions** - When defending principles requires compromising them

### Real Case Studies

See [examples/Case Studies/](examples/Case%20Studies/) for detailed analysis of:
- Open-source AI model release decisions
- Climate emergency democratic restrictions
- AI content moderation dilemmas

---

## 🔬 Methodology: Multi-AI Collaboration

This framework emerged from structured dialogue with four AI systems:
- **Claude** (Anthropic): Constitutional AI, emphasis on harmlessness
- **ChatGPT** (OpenAI): RLHF optimization, emphasis on helpfulness
- **Grok** (xAI): Maximum truth-seeking, less filtered
- **Gemini** (Google): Different training corpus and safety guidelines

**The process:**
1. Posed alignment questions to each AI independently
2. Identified convergences (robust principles) and divergences (requiring human judgment)
3. Iteratively refined through synthesis
4. Built working implementation to validate in practice

📝 **[Read the EA Forum Post](https://forum.effectivealtruism.org/posts/zeGyLAhx22wFCyLde/what-i-learned-by-making-four-ais-debate-human-ethics)**

---

## 🚀 Quick Start Options

### 1. For AI Practitioners
Use the six pillars as a prompt template for evaluating decisions:

```
Evaluate [decision] through these six pillars:
1. Curiosity and Truth-Seeking: [Assess evidence and openness]
2. Empathy and Mutual Flourishing: [Consider suffering and equity]
3. Dignity and Agency: [Evaluate autonomy and accountability]
4. Sustainability and Long-Term Stewardship: [Weigh long-term impacts]
5. Adaptability and Diversity: [Check for pluralism and evolution]
6. Integrity and Responsibility: [Ensure alignment of actions]
Provide balanced recommendations.
```

See [examples/ai-prompt-template.md](examples/ai-prompt-template.md) for more templates.

### 2. For Developers
Integrate CORVUS 2.0 into your AI system:

```python
from implementations.corvus_2_0.ethics_engine import EthicsEngine

engine = EthicsEngine()

# Before executing any AI action
decision = engine.evaluate_command(user_command)
if decision.allowed:
    execute_action(user_command)
else:
    log_blocked_action(decision.reasoning)
```

### 3. For Researchers
Download the charter and test against your use cases:
- [CHARTER.md](CHARTER.md) - Full framework specification
- [Case Studies](examples/Case%20Studies/) - Detailed application examples
- [Google Doc](https://docs.google.com/document/d/11djqsvYCC9wnw44n6qGYNRRfTuMwn_pAnnl2396NRR8/edit?usp=sharing) - Comment-enabled version

---

## 📈 Use Cases

This framework and implementation could inform:

- **Constitutional AI Development** - Richer value specifications for training
- **AI Governance Policy** - Guiding regulation that balances innovation and safety
- **Institutional Ethics Review** - Framework for AI deployment decisions
- **Red Teaming & Safety Testing** - Systematic evaluation against explicit values
- **Cross-Cultural Dialogue** - Common ground for values discussions

---

## ⚠️ Limitations & Biases

This framework is **incomplete and culturally situated**:

- Emerged primarily from Western philosophical traditions
- Training data for all four AIs is predominantly English-language and Western-centric
- Human synthesizer brings own cultural assumptions and blind spots
- Implementation mechanisms need real-world stress testing
- Needs critique from non-Western philosophical traditions

**This is explicitly version 1.0.** The framework itself calls for adaptation based on evidence and experience.

---

## 🛣️ Roadmap

### Phase 1 ✅ (Completed Q4 2025)
- Six-pillar framework published
- Basic Constitutional AI implementation (CORVUS 2.0)
- Real-time ethical filtering working
- Case studies and prompt templates

### Phase 2 🚧 (Q1 2026)
- Enhanced tension resolution with LLM reasoning
- Comprehensive benchmark suite (TruthfulQA, safety evals)
- Integration examples for popular AI frameworks
- Community feedback incorporation

### Phase 3 📅 (Q2 2026)
- Multi-model testing (GPT, Claude, Gemini integration)
- Advanced logging and interpretability tools
- Web dashboard for ethics monitoring
- Translations and cross-cultural validation

### Phase 4 📅 (Q3-Q4 2026)
- Production-grade deployment tools
- Formal verification methods
- Academic paper submission
- Open-source community building

---

## 🤝 Contributing

We're seeking rigorous critique and improvement:

**For AI Safety Researchers:**
- Could this inform Constitutional AI or reward modeling?
- Where does it fail under adversarial pressure?
- How can we make the ethics engine more robust?

**For Philosophers:**
- What cultural assumptions are we missing?
- Which philosophical traditions critique this framework?
- How can we improve tension resolution guidance?

**For Implementers:**
- How would you operationalize these principles in production?
- What edge cases break the current implementation?
- What features would make this more practical?

### Ways to Contribute

- **Open an Issue** - Point out flaws, gaps, or unclear sections
- **Pull Request** - Suggest improvements to charter or code
- **Discussions** - Share how you'd apply this to real dilemmas
- **Case Studies** - Test the framework against actual AI ethics dilemmas
- **Translations** - Help make this accessible in other languages

---

## 📚 Documentation

- **[CHARTER.md](CHARTER.md)** - Complete six-pillar framework
- **[CORVUS 2.0 Docs](implementations/corvus-2.0/README.md)** - Technical implementation guide
- **[Case Studies](examples/Case%20Studies/)** - Real-world applications
- **[Prompt Templates](examples/ai-prompt-template.md)** - Ready-to-use AI prompts
- **[EA Forum Post](https://forum.effectivealtruism.org/posts/zeGyLAhx22wFCyLde/what-i-learned-by-making-four-ais-debate-human-ethics)** - Development story and discussion

---

## 📖 Citation

If you reference this work:

```
Six-Pillar Framework for AI Alignment and Human Values (2025)
Developed through human-AI collaboration (Claude, ChatGPT, Grok, Gemini)
Haun, J. https://github.com/FrankleFry1/gold-standard-human-values
```

---

## 📞 Contact

- **GitHub Issues**: For technical questions and suggestions
- **Discussions**: For philosophical debates and applications
- **Email**: [johnhaun04@gmail.com](mailto:johnhaun04@gmail.com)
- **EA Forum**: [Discussion thread](https://forum.effectivealtruism.org/posts/zeGyLAhx22wFCyLde/what-i-learned-by-making-four-ais-debate-human-ethics)

---

## 🙏 Acknowledgments

This framework builds on:
- Constitutional AI research (Anthropic)
- Value alignment work (Stuart Russell, Nick Bostrom, Toby Ord)
- Democratic deliberation theory
- Effective altruism and longtermism communities
- All those who will critique and improve this

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Status:** Version 1.0 - Released October 2025 - Open for critique and revision

---

> *"When I started, I wanted a universal code. What I found instead was a mirror: four AIs reflecting fragments of us, and a reminder that alignment starts with human self-alignment."*
