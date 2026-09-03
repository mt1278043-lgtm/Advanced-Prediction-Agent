"""
Utility functions for the prediction agent.
"""

import os
from datetime import datetime
from typing import Optional
import json


def load_api_key(key_name: str = "OPENAI_API_KEY") -> Optional[str]:
    """Load API key from environment."""
    return os.getenv(key_name)


def format_timestamp() -> str:
    """Get formatted timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_conversation(messages: list, filename: str = None) -> str:
    """Save conversation to file."""
    if filename is None:
        filename = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, 'w') as f:
        json.dump({
            "timestamp": format_timestamp(),
            "messages": [
                {
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", ""),
                    "timestamp": msg.get("timestamp", format_timestamp())
                }
                for msg in messages
            ]
        }, f, indent=2)

    return filename


def parse_confidence_level(text: str) -> Optional[float]:
    """Extract confidence level from text."""
    import re

    # Look for percentage patterns
    match = re.search(r'(\d+(?:\.\d+)?)\s*%', text)
    if match:
        return float(match.group(1)) / 100

    # Look for confidence phrases
    confidence_map = {
        "very high": 0.95,
        "high": 0.85,
        "medium": 0.60,
        "low": 0.40,
        "very low": 0.10
    }

    text_lower = text.lower()
    for phrase, level in confidence_map.items():
        if phrase in text_lower:
            return level

    return None


def extract_predictions(response_text: str) -> dict:
    """Extract structured predictions from response."""
    predictions = {
        "raw": response_text,
        "confidence": parse_confidence_level(response_text),
        "extracted_at": format_timestamp()
    }

    return predictions


def format_for_display(prediction: dict) -> str:
    """Format prediction for display in Streamlit."""
    lines = []

    if "raw" in prediction:
        lines.append(prediction["raw"])

    if "confidence" in prediction and prediction["confidence"]:
        lines.append(f"\n**Confidence Level:** {prediction['confidence']*100:.0f}%")

    return "\n".join(lines)
