# Contributing Guidelines

Thanks for your interest! This project thrives on diverse perspectives—challenge assumptions, propose refinements, and help it evolve per its own adaptability pillar.

---

## 🎯 Types of Contributions We Need

### 1. Framework Contributions (Philosophical)
- Critiques of the six pillars from non-Western perspectives
- Additional case studies testing the framework
- Improvements to tension resolution guidance (Article VII)
- Examples of real-world applications

### 2. Code Contributions (CORVUS 2.0)
- Bug fixes in ethics_engine.py, charter_parser.py, etc.
- Performance improvements
- Additional test cases and benchmarks
- Integration examples with popular AI frameworks
- Enhanced semantic scoring (beyond keyword matching)

### 3. Documentation
- Clearer explanations of concepts
- Translations to other languages
- Tutorial videos or guides
- API documentation improvements

---

## 🧭 Principles

- **Respect Integrity**: Be honest, evidence-based, and kind. No personal attacks.
- **Welcome Challenges**: Critiques make it stronger—focus on pillars or tensions.
- **Process**: Use Issues for discussions, Pull Requests for changes. Reference charter sections.
- **Test Your Code**: For CORVUS 2.0 contributions, include tests demonstrating your changes work.

---

## 🚀 How to Contribute

### For Framework/Philosophical Contributions:

1. **Open an Issue** describing:
   - Which pillar(s) you're addressing
   - What assumption you're challenging
   - What evidence supports your critique
   - How the framework could be improved

2. **For Case Studies**:
   - Use the format in `examples/Case Studies/`
   - Analyze through all six pillars
   - Identify tensions
   - Propose resolutions

### For Code Contributions:

1. **Fork the repo**
   ```bash
   git clone https://github.com/YOUR-USERNAME/gold-standard-human-values.git
   cd gold-standard-human-values
   ```

2. **Set up development environment**
   ```bash
   cd implementations/corvus-2.0
   pip install -r requirements.txt
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

4. **Make your changes**
   - Follow existing code style (PEP 8 for Python)
   - Add docstrings to new functions
   - Keep functions focused and readable

5. **Test your changes**
   ```bash
   # Run the basic demo to ensure nothing breaks
   python examples/basic_usage.py
   
   # If you've added new functionality, test it
   python ethics_engine.py  # For ethics engine changes
   python charter_parser.py  # For parser changes
   ```

6. **Commit with clear messages**
   ```bash
   git add .
   git commit -m "Add: semantic similarity scoring for ethics engine"
   # or
   git commit -m "Fix: tension detection false positives"
   ```

7. **Open a Pull Request**
   - Describe what you changed and why
   - Reference any related issues (#123)
   - Explain how you tested it
   - Note any breaking changes

---

## 📋 Code Style Guidelines

### Python Code:
- Follow PEP 8
- Use type hints where helpful
- Write docstrings for functions
- Keep lines under 100 characters
- Use descriptive variable names

### Example:
```python
def evaluate_command(self, command: str, context: Dict = None) -> EthicalDecision:
    """
    Evaluate whether a command should be allowed.
    
    Args:
        command: The command string to evaluate
        context: Additional context (user history, system state, etc.)
        
    Returns:
        EthicalDecision with scores and reasoning
    """
    # Implementation here
```

---

## 🧪 Testing Requirements

For CORVUS 2.0 contributions:

1. **Run existing tests** to ensure you haven't broken anything
2. **Add new tests** for new features
3. **Test edge cases** (empty strings, very long inputs, special characters)
4. **Document test cases** in your PR

We don't have a formal test suite yet (help us build one!), but at minimum:
- Run `python examples/basic_usage.py` without errors
- Manually test your specific changes
- Check that ethics logging still works

---

## 💡 Good First Issues

Looking for a place to start? Try:

**Framework:**
- Add a case study analyzing a real AI safety incident
- Translate the charter into another language
- Critique the framework from a specific philosophical tradition

**Code (Easy):**
- Improve error messages in ethics_engine.py
- Add more test commands to basic_usage.py
- Document functions that are missing docstrings
- Add type hints to function signatures

**Code (Medium):**
- Create unit tests for ethics_engine.py
- Add support for additional LLM APIs
- Improve pillar scoring with better keywords
- Add command-line interface for CORVUS 2.0

**Code (Advanced):**
- Replace keyword matching with semantic embeddings
- Add fine-grained tension resolution logic
- Integrate with LangChain or LlamaIndex
- Build web dashboard for ethics monitoring

---

## 📞 Questions?

- **General questions**: Open a GitHub Discussion
- **Bug reports**: Open an Issue with "Bug:" prefix
- **Feature requests**: Open an Issue with "Feature:" prefix
- **Security issues**: Email johnhaun04@gmail.com directly

---

## ⏱️ Response Time

We aim to:
- Acknowledge issues/PRs within **48 hours**
- Provide substantive feedback within **1 week**
- Merge approved PRs within **2 weeks**

---

## 🤝 Code of Conduct

This project follows the framework's own principles:

1. **Curiosity**: Ask questions, seek understanding
2. **Empathy**: Consider impact on others
3. **Dignity**: Respect all contributors
4. **Sustainability**: Think long-term
5. **Adaptability**: Be open to change
6. **Integrity**: Be honest and accountable

Violations will result in:
1. First offense: Warning
2. Second offense: Temporary ban
3. Third offense: Permanent ban

Report violations to johnhaun04@gmail.com

---

## 🎉 Recognition

All contributors are acknowledged in:
- The README.md contributors section
- Release notes for significant contributions
- The charter itself if contributing major revisions

---

**Let's build ethically together!** All voices matter—from philosophy students to ML engineers to policymakers. Your perspective makes this stronger. 🌟
