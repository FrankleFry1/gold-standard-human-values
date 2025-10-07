# AI Prompt Templates for the Gold Standard Framework

These templates demonstrate how to integrate the six pillars into AI interactions, such as evaluating decisions or generating responses. Use them with LLMs (e.g., Claude, ChatGPT, Grok, Gemini) to ensure outputs align with the framework.

---

## Basic Evaluation Template

Use this to assess any issue or decision through the pillars.

```
Evaluate [describe the decision, issue, or scenario here, e.g., 'deploying an AI system for hiring'] through the six pillars of the Gold Standard for Human Values:

1. Curiosity and Truth-Seeking: Assess based on evidence, intellectual humility, and inclusion of diverse knowledge.

2. Empathy and Mutual Flourishing: Consider minimization of suffering, equity, and balance between outcomes and rights.

3. Dignity and Agency: Evaluate inherent worth, autonomy, participatory governance, and accountability.

4. Sustainability and Long-Term Stewardship: Weigh intergenerational impacts, ecological balance, and technological alignment.

5. Adaptability and Diversity: Check for cultural pluralism, moral evolution, and resilience.

6. Integrity and Responsibility: Ensure alignment of intentions and actions, moral courage, and reconciliation.

Provide a balanced analysis, highlight tensions, and recommend actions. Cite any relevant articles from the Charter.
```

**Example Output (Hypothetical from an LLM):**
- **Curiosity:** Ensure hiring data is evidence-based and open to revision.
- **Empathy:** Mitigate biases that could cause unfair suffering.
- **Dignity:** Protect candidate autonomy and ensure transparency in decision-making.
- **Sustainability:** Consider long-term impacts on organizational culture and workforce diversity.
- **Adaptability:** Design systems that can evolve with changing ethical standards.
- **Integrity:** Build accountability mechanisms for algorithmic decisions.

---

## Template for AI Governance Policy

Tailored for policy or regulation discussions.

```
Draft a policy recommendation for [topic, e.g., 'AI in healthcare'] using the six pillars:

1. Curiosity: Incorporate evidence-based inquiry and epistemic justice.

2. Empathy: Prioritize reducing suffering and extending moral consideration to patients/AIs.

3. Dignity: Protect autonomy and ensure participatory decision-making.

4. Sustainability: Focus on long-term health system resilience.

5. Adaptability: Allow for cultural diversity and ethical evolution.

6. Integrity: Build in accountability and forgiveness mechanisms.

Address potential tensions (e.g., innovation vs. safety) and suggest implementation pathways from Article VIII.
```

---

## Template for Ethical Dilemma Resolution

For navigating real-world conflicts.

```
Resolve this ethical dilemma [describe dilemma, e.g., 'balancing user privacy with AI personalization'] via the pillars:

Analyze through each pillar:
1. Curiosity and Truth-Seeking: [assessment]
2. Empathy and Mutual Flourishing: [assessment]
3. Dignity and Agency: [assessment]
4. Sustainability and Long-Term Stewardship: [assessment]
5. Adaptability and Diversity: [assessment]
6. Integrity and Responsibility: [assessment]

Apply Article VII for tensions, e.g., dignity/agency vs. collective flourishing.

If compromises are needed, propose safeguards based on Article VII, Section B:
- Proportionality
- Temporality
- Democratic authorization
- Independent oversight
- Transparency
- Sunset mechanisms
- Moral residue recognition
```

---

## Template for Constitutional AI Training

For AI developers building value-aligned systems.

```
Design a reward model for [AI system, e.g., 'customer service chatbot'] that embodies the six pillars:

1. Curiosity: Reward truth-seeking, fact-checking, and acknowledgment of uncertainty.

2. Empathy: Prioritize responses that minimize user frustration and respect diverse needs.

3. Dignity: Ensure user autonomy, avoid manipulation, maintain transparency about AI nature.

4. Sustainability: Optimize for long-term user trust, not short-term engagement metrics.

5. Adaptability: Build in mechanisms to update values based on user feedback.

6. Integrity: Penalize deception, reward consistency between stated values and actions.

Specify how to handle value conflicts (e.g., honesty vs. not causing distress).
```

---

## Tips for Use

**Customization:**
- Replace placeholders `[...]` with your specific scenario
- Adjust emphasis based on which pillars are most relevant
- Add domain-specific criteria as needed

**Iteration:**
- Feed LLM outputs back into the template for refinement
- Use multiple LLMs and compare their analyses
- Document unexpected tensions that emerge

**Testing:**
- Try with real dilemmas from AI ethics forums
- Compare results across different AI systems
- Share interesting findings via GitHub Issues

**Best Practices:**
- Be specific in your scenario descriptions
- Ask for explicit reasoning, not just conclusions
- Request identification of missing perspectives
- Have the AI critique its own recommendations

---

## Contributing Your Templates

Have you created a useful variation? Contribute via Pull Request!

**Good template contributions include:**
- Clear use case description
- Example scenario
- Expected output format
- Notes on when to use this vs. other templates

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

## Example: Real Application

**Scenario:** A city wants to deploy facial recognition for public safety.

**Using the Basic Template:**

```
Evaluate deploying facial recognition in public spaces through the six pillars:

1. Curiosity: Is there evidence this improves safety? What studies exist on accuracy across demographics?

2. Empathy: How might this cause suffering (false arrests, chilling effects on protest)? Who bears the costs?

3. Dignity: Does this respect citizen autonomy and privacy? Is there meaningful consent?

4. Sustainability: What are long-term impacts on social trust and democratic norms?

5. Adaptability: Can the system evolve as norms change? Is there an exit strategy?

6. Integrity: Are decision-makers transparent about limitations? Is there accountability for harms?

Identify tensions (e.g., safety vs. privacy) and recommend safeguards per Article VII.
```

**Key Insight:** This framework forces explicit consideration of tradeoffs rather than binary accept/reject decisions.
