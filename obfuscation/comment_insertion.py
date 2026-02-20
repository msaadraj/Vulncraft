"""
Comment Insertion Obfuscation
Educational demonstration only.

Inserts inline comments into common keywords to demonstrate
how naive filters may fail to normalize input properly.

Works for both XSS and SQLi payloads.
"""

import re


KEYWORDS = [
    # XSS related
    "script",
    "javascript",

    # SQLi related
    "select",
    "union",
    "where",
    "and",
    "or",
    "from"
]


def _insert_comment(word: str) -> str:
    """Insert comment at middle of keyword."""
    mid = len(word) // 2
    return word[:mid] + "/**/" + word[mid:]


def apply(payload: str) -> str:

    if not payload:
        return payload

    for kw in KEYWORDS:
        payload = re.sub(
            rf"(?i){kw}",
            lambda m: _insert_comment(m.group(0)),
            payload
        )

    return payload
