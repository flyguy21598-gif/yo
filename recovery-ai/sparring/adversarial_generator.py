from __future__ import annotations


def generate_variants(text: str) -> list[str]:
    swaps = str.maketrans({"o": "0", "O": "0", "l": "1", "I": "1", "s": "5", "S": "5"})
    variants = {text, text.translate(swaps), text.replace(" ", ""), text.lower(), text.upper()}
    return [variant for variant in variants if variant]
