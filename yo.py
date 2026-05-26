#!/usr/bin/env python3
"""Yo: generate powerful, unique blueprints from a theme."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import textwrap
from dataclasses import asdict, dataclass
from pathlib import Path

SYLLABLES = [
    "ka",
    "zu",
    "mi",
    "ra",
    "to",
    "shi",
    "va",
    "no",
    "lu",
    "xe",
    "tri",
    "zen",
    "or",
    "py",
    "el",
    "un",
]

VERBS = [
    "amplify",
    "forge",
    "liberate",
    "reframe",
    "synthesize",
    "accelerate",
    "anchor",
    "transmute",
    "orchestrate",
    "architect",
    "ignite",
]

NOUNS = [
    "signal",
    "momentum",
    "clarity",
    "energy",
    "trust",
    "curiosity",
    "alignment",
    "resilience",
    "craft",
    "velocity",
    "gravity",
]

FORCES = [
    "time",
    "attention",
    "complexity",
    "ambiguity",
    "entropy",
    "surprise",
    "pressure",
    "distance",
    "noise",
]

PRINCIPLES = [
    "Make the invisible measurable.",
    "Design for compounding wins.",
    "Favor rituals over heroics.",
    "Treat feedback as fuel.",
    "Move slow only on irreversible bets.",
    "Make constraints your signature.",
]

RITUALS = [
    "Dawn scan: capture the strongest signal in 60 seconds.",
    "Two-horizon planning: now vs. next.",
    "90-minute creation sprint, no switching.",
    "Weekly friction review: name the drag, remove it.",
    "End-of-day resonance check: what echoed?",
]

METRICS = [
    "Signal-to-noise ratio",
    "Momentum half-life",
    "Decision latency",
    "Insight yield",
    "Trust delta",
]

LEVERAGE = [
    "automation",
    "community",
    "code",
    "capital",
    "craft",
    "partnerships",
    "distribution",
    "reputation",
]

THREATS = [
    "drift",
    "fragmentation",
    "over-optimization",
    "unclear ownership",
    "premature scaling",
    "stale narratives",
    "context switching",
]

THEME_RE = re.compile(r"[^a-z0-9\s\-]", flags=re.IGNORECASE)

PROFILE_HINTS = {
    "general": {
        "target": "decision",
        "cadence": "weekly",
        "artifact": "proof artifact",
    },
    "founder": {
        "target": "strategic bet",
        "cadence": "daily",
        "artifact": "customer-facing artifact",
    },
    "product": {
        "target": "product outcome",
        "cadence": "weekly",
        "artifact": "validated learning artifact",
    },
    "creator": {
        "target": "audience outcome",
        "cadence": "daily",
        "artifact": "publishable artifact",
    },
}


@dataclass(eq=True)
class Blueprint:
    title: str
    tagline: str
    power_core: list[str]
    unique_edge: list[str]
    protocol: list[str]
    metrics: list[str]
    leverage: list[str]
    threats: list[str]
    invocation: str


class YoError(Exception):
    """Raised for user-facing command errors."""


def _seed_from(theme: str, seed: str | None) -> int:
    combo = f"{theme}::{seed or ''}"
    digest = hashlib.sha256(combo.encode("utf-8")).hexdigest()
    return int(digest, 16) % (2**32)


def _syllable_name(rng: random.Random, count: int = 3) -> str:
    return "".join(rng.choice(SYLLABLES) for _ in range(count)).title()


def _pick(rng: random.Random, items: list[str], count: int) -> list[str]:
    return rng.sample(items, count)


def _sanitize_theme(theme: str) -> str:
    cleaned = THEME_RE.sub("", theme).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    if len(cleaned) < 3:
        raise YoError("theme must be at least 3 valid characters")
    return cleaned


def build_blueprint(theme: str, seed: str | None) -> Blueprint:
    theme = _sanitize_theme(theme)
    rng = random.Random(_seed_from(theme, seed))
    name = _syllable_name(rng)
    verb = rng.choice(VERBS)
    noun = rng.choice(NOUNS)
    force = rng.choice(FORCES)
    tagline = f"{verb.title()} {noun} by mastering {force}."

    power_core = [
        f"Harness {rng.choice(NOUNS)} to sharpen the {theme} signal.",
        f"Turn {rng.choice(FORCES)} into a repeatable advantage.",
        f"Convert {rng.choice(NOUNS)} into collective leverage.",
    ]

    unique_edge = [rng.choice(PRINCIPLES) for _ in range(3)]

    protocol = [
        f"Name the prime target: the most consequential {theme} decision this week.",
        f"Build a minimum ritual: {rng.choice(RITUALS)}",
        f"Install a guardrail against {rng.choice(FORCES)}.",
        "Ship one proof artifact in 72 hours.",
    ]

    metrics = _pick(rng, METRICS, 3)
    leverage = _pick(rng, LEVERAGE, 3)
    threats = _pick(rng, THREATS, 2)
    invocation = f"We are the {name} order. We {verb} {noun} with intent."

    return Blueprint(
        title=f"{name} Engine: {theme.title()}",
        tagline=tagline,
        power_core=power_core,
        unique_edge=unique_edge,
        protocol=protocol,
        metrics=metrics,
        leverage=leverage,
        threats=threats,
        invocation=invocation,
    )


def apply_profile(blueprint: Blueprint, theme: str, profile: str) -> Blueprint:
    hints = PROFILE_HINTS[profile]
    protocol = blueprint.protocol.copy()
    protocol[0] = (
        f"Name the prime target: the most consequential {theme} {hints['target']} "
        f"this {hints['cadence']}."
    )
    protocol[3] = f"Ship one {hints['artifact']} in 72 hours."
    return Blueprint(
        title=blueprint.title,
        tagline=blueprint.tagline,
        power_core=blueprint.power_core,
        unique_edge=blueprint.unique_edge,
        protocol=protocol,
        metrics=blueprint.metrics,
        leverage=blueprint.leverage,
        threats=blueprint.threats,
        invocation=blueprint.invocation,
    )


def build_blueprints(
    theme: str,
    seed: str | None,
    count: int,
    profile: str = "general",
) -> list[Blueprint]:
    if count < 1 or count > 20:
        raise YoError("count must be between 1 and 20")
    if profile not in PROFILE_HINTS:
        allowed = ", ".join(PROFILE_HINTS)
        raise YoError(f"profile must be one of: {allowed}")
    blueprints = [build_blueprint(theme, f"{seed or 'seed'}:{idx}") for idx in range(count)]
    return [apply_profile(blueprint, theme, profile) for blueprint in blueprints]


def render_markdown(blueprint: Blueprint) -> str:
    lines = [
        f"# {blueprint.title}",
        "",
        f"**{blueprint.tagline}**",
        "",
        "## Power Core",
        *[f"- {item}" for item in blueprint.power_core],
        "",
        "## Unique Edge",
        *[f"- {item}" for item in blueprint.unique_edge],
        "",
        "## Protocol",
        *[f"{idx + 1}. {item}" for idx, item in enumerate(blueprint.protocol)],
        "",
        "## Signature Metrics",
        *[f"- {item}" for item in blueprint.metrics],
        "",
        "## Leverage Stack",
        *[f"- {item.title()}" for item in blueprint.leverage],
        "",
        "## Threats to Disarm",
        *[f"- {item}" for item in blueprint.threats],
        "",
        "## Invocation",
        textwrap.fill(blueprint.invocation, width=72),
        "",
    ]
    return "\n".join(lines)


def render_markdown_many(blueprints: list[Blueprint]) -> str:
    return "\n---\n\n".join(render_markdown(blueprint).strip() for blueprint in blueprints)


def render_json(data: Blueprint | list[Blueprint]) -> str:
    if isinstance(data, list):
        payload = [asdict(item) for item in data]
    else:
        payload = asdict(data)
    return json.dumps(payload, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a powerful, unique blueprint from a theme.",
    )
    parser.add_argument("theme", help="Theme or mission for the blueprint")
    parser.add_argument("--seed", help="Optional seed for deterministic output")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of Markdown",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Generate multiple blueprint variations (1-20)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Write output to a file instead of stdout",
    )
    parser.add_argument(
        "--profile",
        default="general",
        choices=sorted(PROFILE_HINTS.keys()),
        help="Tailor protocol language for a target workflow",
    )
    return parser.parse_args()


def _write_output(output: str, output_path: str) -> None:
    try:
        path = Path(output_path)
        if path.parent and not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output + "\n", encoding="utf-8")
    except OSError as exc:
        raise YoError(f"failed to write output: {exc}") from exc


def main() -> None:
    args = parse_args()
    try:
        payload: Blueprint | list[Blueprint]
        payload = build_blueprints(args.theme, args.seed, args.count, profile=args.profile)
        if args.count == 1:
            payload = payload[0]

        if args.json:
            output = render_json(payload)
        elif isinstance(payload, list):
            output = render_markdown_many(payload)
        else:
            output = render_markdown(payload)

        if args.output:
            _write_output(output, args.output)
        else:
            print(output)
    except YoError as exc:
        print(f"yo: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
