"""
SQLi Case Variation Logic
Educational demonstration only.

Randomizes keyword casing to demonstrate
case-sensitive filter weaknesses.
"""

import random
import re


KEYWORDS = [
    "select",
    "union",
    "where",
    "and",
    "or",
    "from"
]


def random_case(word):
    return "".join(
        c.upper() if random.choice([True, False]) else c.lower()
        for c in word
    )


def apply(payload: str) -> str:
    if not payload:
        return payload

    for kw in KEYWORDS:
        payload = re.sub(
            rf"(?i){kw}",
            lambda m: random_case(m.group(0)),
            payload
        )

    return payload
