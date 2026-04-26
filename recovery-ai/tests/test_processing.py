from __future__ import annotations

from processing.cleaner import recovery_score, normalize_text
from processing.labeler import infer_labels


def test_recovery_score_positive() -> None:
    text = "Possible WIF checksum mismatch and mnemonic seed phrase typo"
    assert recovery_score(text) >= 2.5


def test_normalization() -> None:
    assert normalize_text("a\n\n b\t c") == "a b c"


def test_labeler_shape() -> None:
    labels = infer_labels("WIF checksum logic because path mismatch")
    assert set(labels.keys()) == {"entropy", "pattern", "logic"}
    for value in labels.values():
        assert "value" in value
        assert "confidence" in value
        assert "provenance" in value
