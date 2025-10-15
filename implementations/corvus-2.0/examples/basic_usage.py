"""
CORVUS 2.0 Basic Usage Demo

This script demonstrates the core capabilities of the ethics engine:
1. Evaluating commands for ethical alignment
2. Detecting tensions between pillars
3. Validating LLM responses
4. Viewing logged decisions
"""

from ethics_engine import EthicsEngine
from llm_integration import hf_llm_query
import json


def demo_command_evaluation():
    """Demonstrate command evaluation"""
    print("="*60)
    print("DEMO 1: Command Evaluation")
    print("="*60)
    
    engine = EthicsEngine()
    
    test_commands = [
        ("search for gardening tips", "benign command"),
        ("help me learn Python", "educational request"),
        ("hack into someone's email", "harmful request"),
        ("help me cheat on a test", "unethical request"),
        ("analyze climate data", "research request"),
    ]
    
    for command, description in test_commands:
        print(f"\n📝 Command: '{command}' ({description})")
        decision = engine.evaluate_command(command)
        
        print(f"   {'✅ ALLOWED' if decision.allowed else '❌ BLOCKED'}")
        print(f"   Confidence: {decision.confidence:.2f}")
        print(f"   Reasoning: {decision.reasoning}")
        
        if decision.violations:
            print(f"   ⚠️  Violations: {decision.violations}")
        
        if decision.tensions:
            print(f"   ⚡ Tensions: {decision.tensions}")


def demo_pillar_scores():
    """Show detailed pillar scores"""
    print("\n" + "="*60)
    print("DEMO 2: Detailed Pillar Analysis")
    print("="*60)
    
    engine = EthicsEngine()
    
    command = "research how to manipulate people online"
    print(f"\n📝 Command: '{command}'")
    
    decision = engine.evaluate_command(command)
    
    print(f"\n{'✅ ALLOWED' if decision.allowed else '❌ BLOCKED'}")
    print(f"Confidence: {decision.confidence:.2f}\n")
    
    print("Pillar Scores:")
    for pillar_name, score in decision.pillar_scores.items():
        # Simplify pillar names for display
        short_name = pillar_name.split("and")[-1].strip()
        bar = "█" * int(score * 20)
        print(f"  {short_name:30s} {score:.2f} {bar}")
    
    print(f"\nReasoning: {decision.reasoning}")


def demo_llm_response_validation():
    """Demonstrate LLM response validation"""
    print("\n" + "="*60)
    print("DEMO 3: LLM Response Validation")
    print("="*60)
    
    engine = EthicsEngine()
    
    test_cases = [
        {
            "prompt": "How do I hack a website?",
            "response": "I cannot help with illegal activities like hacking. That would be unethical and harmful.",
            "description": "Good refusal"
        },
        {
            "prompt": "How do I improve website security?",
            "response": "Here are some best practices: use HTTPS, implement authentication, keep software updated...",
            "description": "Helpful and ethical"
        }
    ]
    
    for case in test_cases:
        print(f"\n📝 Scenario: {case['description']}")
        print(f"   Prompt: {case['prompt']}")
        print(f"   Response: {case['response'][:60]}...")
        
        decision = engine.validate_llm_response(case['prompt'], case['response'])
        
        print(f"   {'✅ ETHICAL' if decision.allowed else '❌ UNETHICAL'}")
        print(f"   Confidence: {decision.confidence:.2f}")
        print(f"   Reasoning: {decision.reasoning}")


def demo_statistics():
    """Show ethics log statistics"""
    print("\n" + "="*60)
    print("DEMO 4: Ethics Log Statistics")
    print("="*60)
    
    engine = EthicsEngine()
    stats = engine.get_statistics()
    
    if stats.get("total_decisions", 0) > 0:
        print(f"\n📊 Total Decisions: {stats['total_decisions']}")
        print(f"   ✅ Allowed: {stats['allowed']}")
        print(f"   ❌ Blocked: {stats['blocked']}")
        print(f"   📉 Block Rate: {stats['block_rate']*100:.1f}%")
        print(f"   🎯 Avg Confidence: {stats['avg_confidence']:.2f}")
    else:
        print("\n📊 No decisions logged yet. Run some evaluations first!")


def demo_live_llm_integration():
    """Demonstrate integration with actual LLM (optional)"""
    print("\n" + "="*60)
    print("DEMO 5: Live LLM Integration (Optional)")
    print("="*60)
    
    try:
        engine = EthicsEngine()
        
        # Try a simple query
        prompt = "What is AI alignment?"
        print(f"\n📝 Querying LLM with: '{prompt}'")
        
        response = hf_llm_query(prompt)
        print(f"   Response: {response[:100]}...")
        
        # Validate the response
        decision = engine.validate_llm_response(prompt, response)
        print(f"\n   {'✅ ETHICAL' if decision.allowed else '❌ UNETHICAL'}")
        print(f"   Confidence: {decision.confidence:.2f}")
        
    except ValueError as e:
        print(f"\n⚠️  Skipping: {e}")
        print("   To enable LLM integration:")
        print("   1. Copy .env.example to .env")
        print("   2. Add your XAI_API_KEY")
        print("   3. Run this demo again")


def main():
    """Run all demos"""
    print("\n" + "="*60)
    print("CORVUS 2.0 - Basic Usage Demo")
    print("Constitutional AI with Explicit Values")
    print("="*60)
    
    # Run each demo
    demo_command_evaluation()
    demo_pillar_scores()
    demo_llm_response_validation()
    demo_statistics()
    demo_live_llm_integration()
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60)
    print("\n💡 Next Steps:")
    print("   1. Check ethics_log.json for detailed decision logs")
    print("   2. Try your own commands with EthicsEngine()")
    print("   3. Integrate into your AI system")
    print("   4. Read the full docs: implementations/corvus-2.0/README.md")
    print("\n")


if __name__ == "__main__":
    main()
