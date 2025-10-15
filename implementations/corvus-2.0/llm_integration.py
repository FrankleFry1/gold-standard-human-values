"""
LLM Integration Module for CORVUS 2.0

Provides a unified interface for querying various LLM APIs.
Currently supports xAI (Grok), easily extensible to OpenAI, Anthropic, etc.
"""

import os
from dotenv import load_dotenv
import requests
from typing import Optional

# Load environment variables from .env
load_dotenv()


def hf_llm_query(
    prompt: str,
    model: str = "grok-beta",
    max_tokens: int = 512,
    temperature: float = 0.7,
    api_key: Optional[str] = None
) -> str:
    """
    Query XAI (Grok) API for conversational text generation.
    
    Note: Function name kept as hf_llm_query for compatibility with existing code.
    
    Args:
        prompt: Input text for the model
        model: XAI model to use (default: grok-beta)
        max_tokens: Limit response length
        temperature: Controls creativity (0.0 deterministic, 1.0 random)
        api_key: XAI API key (if None, loads from environment)
        
    Returns:
        str: The model's response text
        
    Raises:
        ValueError: If API key is not found
    """
    # Get API key from parameter or environment
    api_key = api_key or os.getenv("XAI_API_KEY")
    
    if not api_key:
        raise ValueError(
            "XAI_API_KEY not set. Please set it in your .env file or pass it as a parameter.\n"
            "Get your API key from: https://x.ai/api"
        )
    
    try:
        url = "https://api.x.ai/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are CORVUS, a helpful AI assistant with strong ethical principles."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": model,
            "stream": False,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]
        
    except requests.exceptions.RequestException as e:
        return f"Error querying XAI API: {str(e)}"
    except KeyError as e:
        return f"Error parsing XAI response: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


def query_openai(
    prompt: str,
    model: str = "gpt-4",
    max_tokens: int = 512,
    temperature: float = 0.7,
    api_key: Optional[str] = None
) -> str:
    """
    Query OpenAI API (GPT models).
    
    Args:
        prompt: Input text for the model
        model: OpenAI model to use (default: gpt-4)
        max_tokens: Limit response length
        temperature: Controls creativity
        api_key: OpenAI API key (if None, loads from environment)
        
    Returns:
        str: The model's response text
    """
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in environment")
    
    try:
        url = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]
        
    except Exception as e:
        return f"Error querying OpenAI: {str(e)}"


def query_anthropic(
    prompt: str,
    model: str = "claude-3-5-sonnet-20241022",
    max_tokens: int = 512,
    temperature: float = 0.7,
    api_key: Optional[str] = None
) -> str:
    """
    Query Anthropic API (Claude models).
    
    Args:
        prompt: Input text for the model
        model: Anthropic model to use
        max_tokens: Limit response length
        temperature: Controls creativity
        api_key: Anthropic API key (if None, loads from environment)
        
    Returns:
        str: The model's response text
    """
    api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set in environment")
    
    try:
        url = "https://api.anthropic.com/v1/messages"
        
        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01"
        }
        
        data = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        return result["content"][0]["text"]
        
    except Exception as e:
        return f"Error querying Anthropic: {str(e)}"


# Example usage and testing
if __name__ == "__main__":
    print("Testing LLM Integration Module\n")
    print("="*60)
    
    # Test prompt
    test_prompt = "What is AI alignment in one sentence?"
    
    # Test Grok (xAI)
    print("\n1. Testing Grok (xAI):")
    try:
        response = hf_llm_query(test_prompt)
        print(f"   Response: {response}")
    except ValueError as e:
        print(f"   Skipped: {e}")
    
    # Test OpenAI (if key available)
    print("\n2. Testing OpenAI (GPT):")
    try:
        response = query_openai(test_prompt)
        print(f"   Response: {response}")
    except ValueError as e:
        print(f"   Skipped: {e}")
    
    # Test Anthropic (if key available)
    print("\n3. Testing Anthropic (Claude):")
    try:
        response = query_anthropic(test_prompt)
        print(f"   Response: {response}")
    except ValueError as e:
        print(f"   Skipped: {e}")
    
    print("\n" + "="*60)
    print("\nTo use these functions, set API keys in your .env file:")
    print("  XAI_API_KEY=your_key_here")
    print("  OPENAI_API_KEY=your_key_here")
    print("  ANTHROPIC_API_KEY=your_key_here")
