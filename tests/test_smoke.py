from pathlib import Path
from powerkit.engine import analyze_csv


def test_analyze_csv(tmp_path: Path):
    p = tmp_path / "a.csv"
    p.write_text("x,y\n1,a\n2,b\n1000,a\n", encoding="utf-8")
    out = analyze_csv(p)
    assert out["rows"] == 3
    assert "x" in out["profiles"]
