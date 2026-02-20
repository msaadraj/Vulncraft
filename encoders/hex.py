"""
Hex Encoder
Educational encoding demonstration.
"""


def encode(payload: str) -> str:
    """
    Convert payload to hex representation.
    Example:
    A -> 41
    """
    if payload is None:
        return ""

    return payload.encode("utf-8").hex()
