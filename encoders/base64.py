import base64 as b64


def encode(payload: str) -> str:

    if payload is None:
        return ""

    encoded = b64.b64encode(payload.encode("utf-8"))
    return encoded.decode("utf-8")
