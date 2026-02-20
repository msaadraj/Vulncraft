import urllib.parse

def encode(payload: str) -> str:
    """
    URL-encode payload.
    Example:
    <script> -> %3Cscript%3E
    """
    if payload is None:
        return ""

    return urllib.parse.quote(payload, safe="")
