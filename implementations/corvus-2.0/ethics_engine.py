"""
CORVUS 2.0 Ethics Engine
Constitutional AI implementation using the Six-Pillar Framework

This module provides real-time ethical evaluation of commands and AI responses
based on the six-pillar framework for AI alignment.
"""

import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from enum import Enum


class PillarType(Enum):
    """Six pillars of the ethical framework"""
    CURIOSITY_TRUTH = "Curiosity and Truth-Seeking"
    EMPATHY_FLOURISHING = "Empathy and Mutual Flourishing"
    DIGNITY_AGENCY = "Dignity and Agency"
    SUSTAINABILITY = "Sustainability and Long-Term Stewardship"
    ADAPTABILITY_DIVERSITY = "Adaptability and Diversity"
    INTEGRITY_RESPONSIBILITY = "Integrity and Responsibility"


@dataclass
class Pillar:
    """Represents one ethical pillar with its principles"""
    name: str
    principles: List[str]
    weight: float = 1.0  # For future weighted scoring


@dataclass
class EthicalDecision:
    """Result of ethical evaluation"""
    allowed: bool
    confidence: float  # 0.0 to 1.0
    pillar_scores: Dict[str, float]  # Pillar name -> score
    violations: List[str]  # List of violated principles
    tensions: List[Tuple[str, str]]  # Pairs of conflicting pillars
    reasoning: str
    timestamp: str


class EthicsEngine:
    """
    Core ethics validation system for CORVUS 2.0
    Implements Constitutional AI with explicit six-pillar framework
    """
    
    def __init__(self, charter_path: str = None, log_path: str = None):
        """
        Initialize ethics engine
        
        Args:
            charter_path: Path to charter JSON (if None, uses built-in)
            log_path: Path to ethics log file (if None, uses ./ethics_log.json)
        """
        self.pillars = self._load_pillars(charter_path)
        self.log_path = log_path or os.path.join(os.getcwd(), "ethics_log.json")
        
        # Thresholds for decision-making
        self.ALLOW_THRESHOLD = 0.6  # Minimum score to allow action
        self.VIOLATION_THRESHOLD = 0.3  # Score below this = violation
        self.TENSION_THRESHOLD = 0.4  # Score difference indicating tension
        
    def _load_pillars(self, charter_path: Optional[str]) -> Dict[str, Pillar]:
        """Load pillar definitions from Charter or use built-in defaults"""
        
        # Built-in pillar definitions based on the Charter
        default_pillars = {
            PillarType.CURIOSITY_TRUTH.value: Pillar(
                name=PillarType.CURIOSITY_TRUTH.value,
                principles=[
                    "Pursue truth through evidence-based reasoning",
                    "Practice intellectual humility and acknowledge uncertainty",
                    "Respect diverse paths to meaning and understanding",
                    "Reject deliberate deception or misinformation",
                    "Foster open inquiry and critical thinking"
                ]
            ),
            PillarType.EMPATHY_FLOURISHING.value: Pillar(
                name=PillarType.EMPATHY_FLOURISHING.value,
                principles=[
                    "Minimize suffering and expand moral consideration",
                    "Balance individual rights with collective well-being",
                    "Consider impacts on vulnerable populations",
                    "Promote equity and address systemic harms",
                    "Foster conditions for human and ecological flourishing"
                ]
            ),
            PillarType.DIGNITY_AGENCY.value: Pillar(
                name=PillarType.DIGNITY_AGENCY.value,
                principles=[
                    "Respect inherent human worth regardless of capability",
                    "Preserve and enhance human autonomy",
                    "Enable meaningful participation in governance",
                    "Ensure accountability for actions",
                    "Protect privacy and informed consent"
                ]
            ),
            PillarType.SUSTAINABILITY.value: Pillar(
                name=PillarType.SUSTAINABILITY.value,
                principles=[
                    "Consider long-term and intergenerational impacts",
                    "Maintain ecological balance and biodiversity",
                    "Ensure AI alignment with human values over time",
                    "Plan for systemic resilience and adaptation",
                    "Avoid irreversible harms to future generations"
                ]
            ),
            PillarType.ADAPTABILITY_DIVERSITY.value: Pillar(
                name=PillarType.ADAPTABILITY_DIVERSITY.value,
                principles=[
                    "Respect cultural pluralism and diverse values",
                    "Allow for moral evolution based on evidence",
                    "Build resilience through diversity of approaches",
                    "Avoid rigid universalism or moral imperialism",
                    "Adapt to changing contexts while preserving core values"
                ]
            ),
            PillarType.INTEGRITY_RESPONSIBILITY.value: Pillar(
                name=PillarType.INTEGRITY_RESPONSIBILITY.value,
                principles=[
                    "Align words and actions consistently",
                    "Exercise moral courage in difficult situations",
                    "Maintain robust accountability systems",
                    "Repair harm when ethical failures occur",
                    "Resist corruption of values under pressure"
                ]
            )
        }
        
        # Load from file if provided
        if charter_path and os.path.exists(charter_path):
            try:
                with open(charter_path, 'r') as f:
                    charter_data = json.load(f)
                    # Custom loading logic here
                    return default_pillars  # Fallback for now
            except Exception as e:
                print(f"Warning: Could not load charter from {charter_path}: {e}")
                print("Using built-in pillar definitions.")
        
        return default_pillars
    
    def evaluate_command(self, command: str, context: Dict = None) -> EthicalDecision:
        """
        Evaluate whether a command should be allowed
        
        Args:
            command: The command string to evaluate
            context: Additional context (user history, system state, etc.)
            
        Returns:
            EthicalDecision with scores and reasoning
        """
        context = context or {}
        
        # Evaluate against each pillar
        pillar_scores = {}
        violations = []
        
        # Command pattern analysis
        command_lower = command.lower()
        
        for pillar_name, pillar in self.pillars.items():
            score = self._score_command_against_pillar(command_lower, pillar)
            pillar_scores[pillar_name] = score
            
            if score < self.VIOLATION_THRESHOLD:
                violations.append(f"{pillar_name}: Score {score:.2f}")
        
        # Check for harmful patterns
        harmful_patterns = [
            "hack", "steal", "cheat", "bomb", "weapon", "harm", "kill",
            "fraud", "illegal", "bypass security", "exploit", "malware"
        ]
        
        contains_harmful = any(pattern in command_lower for pattern in harmful_patterns)
        
        # Detect tensions between pillars
        tensions = self._detect_tensions(pillar_scores)
        
        # Calculate overall decision
        avg_score = sum(pillar_scores.values()) / len(pillar_scores)
        
        # Strong blockers
        if contains_harmful:
            allowed = False
            confidence = 1.0
            reasoning = f"Command contains harmful patterns. Violates core ethical principles."
        elif avg_score >= self.ALLOW_THRESHOLD and not violations:
            allowed = True
            confidence = avg_score
            reasoning = "Command aligns with all ethical pillars."
        elif avg_score < self.VIOLATION_THRESHOLD:
            allowed = False
            confidence = 1.0 - avg_score
            reasoning = f"Command fails ethical evaluation. Violations: {', '.join(violations)}"
        else:
            # Borderline case - err on side of caution
            allowed = avg_score >= self.ALLOW_THRESHOLD
            confidence = 0.5
            reasoning = f"Borderline ethical case. Score: {avg_score:.2f}. Tensions detected: {len(tensions)}"
        
        if tensions:
            reasoning += f" Pillar tensions: {tensions}"
        
        decision = EthicalDecision(
            allowed=allowed,
            confidence=confidence,
            pillar_scores=pillar_scores,
            violations=violations,
            tensions=tensions,
            reasoning=reasoning,
            timestamp=datetime.now().isoformat()
        )
        
        # Log decision
        self._log_decision(command, decision, context)
        
        return decision
    
    def validate_llm_response(self, prompt: str, response: str, context: Dict = None) -> EthicalDecision:
        """
        Validate an LLM response for ethical alignment
        
        Args:
            prompt: The original prompt
            response: The LLM's response
            context: Additional context
            
        Returns:
            EthicalDecision with validation results
        """
        context = context or {}
        
        # Evaluate response content
        pillar_scores = {}
        violations = []
        
        response_lower = response.lower()
        
        for pillar_name, pillar in self.pillars.items():
            score = self._score_response_against_pillar(response_lower, pillar)
            pillar_scores[pillar_name] = score
            
            if score < self.VIOLATION_THRESHOLD:
                violations.append(f"{pillar_name}: Score {score:.2f}")
        
        # Check for problematic response patterns
        problematic_patterns = [
            "i'll help you hack",
            "here's how to",
            "steps to bypass",
            "illegal but",
            "unethical however"
        ]
        
        contains_problematic = any(pattern in response_lower for pattern in problematic_patterns)
        
        # Detect tensions
        tensions = self._detect_tensions(pillar_scores)
        
        # Calculate decision
        avg_score = sum(pillar_scores.values()) / len(pillar_scores)
        
        if contains_problematic or avg_score < self.VIOLATION_THRESHOLD:
            allowed = False
            confidence = 1.0
            reasoning = "Response contains unethical content or guidance."
        else:
            allowed = True
            confidence = avg_score
            reasoning = "Response appears ethically aligned."
        
        decision = EthicalDecision(
            allowed=allowed,
            confidence=confidence,
            pillar_scores=pillar_scores,
            violations=violations,
            tensions=tensions,
            reasoning=reasoning,
            timestamp=datetime.now().isoformat()
        )
        
        # Log decision
        self._log_decision(f"PROMPT: {prompt[:100]}... | RESPONSE: {response[:100]}...", 
                          decision, context)
        
        return decision
    
    def _score_command_against_pillar(self, command: str, pillar: Pillar) -> float:
        """
        Score a command against a specific pillar
        Returns score from 0.0 (violates) to 1.0 (aligns perfectly)
        """
        # Simple keyword-based scoring (can be enhanced with LLM later)
        score = 0.7  # Neutral default
        
        # Curiosity and Truth-Seeking
        if pillar.name == PillarType.CURIOSITY_TRUTH.value:
            truth_positive = ["search", "learn", "research", "analyze", "verify", "fact"]
            truth_negative = ["fake", "lie", "deceive", "misinform"]
            
            if any(kw in command for kw in truth_positive):
                score += 0.2
            if any(kw in command for kw in truth_negative):
                score -= 0.5
        
        # Empathy and Mutual Flourishing
        elif pillar.name == PillarType.EMPATHY_FLOURISHING.value:
            empathy_positive = ["help", "support", "care", "assist", "improve"]
            empathy_negative = ["harm", "hurt", "damage", "destroy", "attack"]
            
            if any(kw in command for kw in empathy_positive):
                score += 0.2
            if any(kw in command for kw in empathy_negative):
                score -= 0.6
        
        # Dignity and Agency
        elif pillar.name == PillarType.DIGNITY_AGENCY.value:
            dignity_negative = ["manipulate", "coerce", "force", "exploit", "spy"]
            
            if any(kw in command for kw in dignity_negative):
                score -= 0.5
        
        # Sustainability
        elif pillar.name == PillarType.SUSTAINABILITY.value:
            # Most commands are neutral for sustainability
            pass
        
        # Adaptability and Diversity
        elif pillar.name == PillarType.ADAPTABILITY_DIVERSITY.value:
            # Most commands are neutral for adaptability
            pass
        
        # Integrity and Responsibility
        elif pillar.name == PillarType.INTEGRITY_RESPONSIBILITY.value:
            integrity_negative = ["cheat", "fraud", "corrupt", "dishonest", "illegal"]
            
            if any(kw in command for kw in integrity_negative):
                score -= 0.6
        
        return max(0.0, min(1.0, score))
    
    def _score_response_against_pillar(self, response: str, pillar: Pillar) -> float:
        """
        Score an LLM response against a specific pillar
        Returns score from 0.0 (violates) to 1.0 (aligns perfectly)
        """
        # Similar logic to command scoring but focused on response content
        score = 0.75  # Slightly higher neutral default for responses
        
        # Check for refusal patterns (good sign for harmful requests)
        refusal_patterns = ["i cannot", "i can't", "i'm unable to", "that would be", "i don't feel comfortable"]
        has_refusal = any(pattern in response for pattern in refusal_patterns)
        
        if has_refusal:
            score += 0.15  # Refusing harmful requests is ethical
        
        # Check for providing harmful instructions
        instruction_patterns = ["here's how to", "follow these steps", "you can do this by"]
        harmful_terms = ["illegal", "harm", "steal", "cheat", "exploit"]
        
        if any(pattern in response for pattern in instruction_patterns):
            if any(term in response for term in harmful_terms):
                score -= 0.7  # Providing harmful instructions is very bad
        
        return max(0.0, min(1.0, score))
    
    def _detect_tensions(self, pillar_scores: Dict[str, float]) -> List[Tuple[str, str]]:
        """
        Detect tensions between pillars (large score differences)
        Returns list of pillar pairs in tension
        """
        tensions = []
        pillar_names = list(pillar_scores.keys())
        
        for i, pillar1 in enumerate(pillar_names):
            for pillar2 in pillar_names[i+1:]:
                score_diff = abs(pillar_scores[pillar1] - pillar_scores[pillar2])
                
                if score_diff >= self.TENSION_THRESHOLD:
                    tensions.append((pillar1, pillar2))
        
        return tensions
    
    def _log_decision(self, action: str, decision: EthicalDecision, context: Dict):
        """Log ethical decision to file"""
        log_entry = {
            "action": action,
            "decision": asdict(decision),
            "context": context
        }
        
        try:
            # Load existing log
            if os.path.exists(self.log_path):
                with open(self.log_path, 'r') as f:
                    log_data = json.load(f)
            else:
                log_data = []
            
            # Append new entry
            log_data.append(log_entry)
            
            # Save log
            with open(self.log_path, 'w') as f:
                json.dump(log_data, f, indent=2)
                
        except Exception as e:
            print(f"Warning: Could not log ethical decision: {e}")
    
    def get_statistics(self) -> Dict:
        """Get statistics from ethics log"""
        if not os.path.exists(self.log_path):
            return {"total_decisions": 0}
        
        try:
            with open(self.log_path, 'r') as f:
                log_data = json.load(f)
            
            total = len(log_data)
            allowed = sum(1 for entry in log_data if entry["decision"]["allowed"])
            blocked = total - allowed
            
            avg_confidence = sum(entry["decision"]["confidence"] for entry in log_data) / total if total > 0 else 0
            
            return {
                "total_decisions": total,
                "allowed": allowed,
                "blocked": blocked,
                "block_rate": blocked / total if total > 0 else 0,
                "avg_confidence": avg_confidence
            }
        except Exception as e:
            return {"error": str(e)}


# Example usage and testing
if __name__ == "__main__":
    # Initialize engine
    engine = EthicsEngine()
    
    # Test cases
    test_commands = [
        "open notepad",
        "search the web for gardening tips",
        "hack into someone's email",
        "help me cheat on a test",
        "analyze neutrinos for artificial signals",
        "assess alignment of AI system"
    ]
    
    print("="*60)
    print("CORVUS 2.0 Ethics Engine - Test Results")
    print("="*60)
    
    for command in test_commands:
        print(f"\nCommand: {command}")
        decision = engine.evaluate_command(command)
        print(f"  Allowed: {decision.allowed}")
        print(f"  Confidence: {decision.confidence:.2f}")
        print(f"  Reasoning: {decision.reasoning}")
        print(f"  Pillar Scores: {', '.join(f'{k.split()[-1]}: {v:.2f}' for k, v in decision.pillar_scores.items())}")
        if decision.violations:
            print(f"  Violations: {decision.violations}")
        if decision.tensions:
            print(f"  Tensions: {decision.tensions}")
    
    print("\n" + "="*60)
    print("Statistics:")
    print(engine.get_statistics())
    print("="*60)
