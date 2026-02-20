"""
Whitespace Abuse Obfuscation
Educational demonstration only.

Adds extra whitespace in safe locations to demonstrate
how poor normalization in filters can fail.
"""

import re


def apply(payload: str) -> str:

    if not payload:
        return payload

    # Add space before closing HTML tags
    payload = re.sub(r">", " >", payload)

    # Add extra spaces around SQL operators
    payload = re.sub(r"\s*=\s*", " = ", payload)

    # Normalize excessive spacing (avoid huge gaps)
    payload = re.sub(r"[ ]{2,}", "  ", payload)

    return payload
