#!/usr/bin/env python3
"""Yo: generate a powerful, unique blueprint from a theme."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import textwrap
from dataclasses import dataclass

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

@dataclass
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


def _seed_from(theme: str, seed: str | None) -> int:
    combo = f"{theme}::{seed or ''}"
    digest = hashlib.sha256(combo.encode("utf-8")).hexdigest()
    return int(digest, 16) % (2**32)


def _syllable_name(rng: random.Random, count: int = 3) -> str:
    return "".join(rng.choice(SYLLABLES) for _ in range(count)).title()


def _pick(rng: random.Random, items: list[str], count: int) -> list[str]:
    return rng.sample(items, count)


def build_blueprint(theme: str, seed: str | None) -> Blueprint:
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

    unique_edge = [
        f"{rng.choice(PRINCIPLES)}",
        f"{rng.choice(PRINCIPLES)}",
        f"{rng.choice(PRINCIPLES)}",
    ]

    protocol = [
        f"Name the prime target: the most consequential {theme} decision this week.",
        f"Build a minimum ritual: {rng.choice(RITUALS)}",
        f"Install a guardrail against {rng.choice(FORCES)}.",
        f"Ship one proof artifact in 72 hours.",
    ]

    metrics = _pick(rng, METRICS, 3)
    leverage = _pick(rng, LEVERAGE, 3)
    threats = _pick(rng, THREATS, 2)
    invocation = f"We are the {name} order. We {verb} {noun} with intent."

    title = f"{name} Engine: {theme.title()}"

    return Blueprint(
        title=title,
        tagline=tagline,
        power_core=power_core,
        unique_edge=unique_edge,
        protocol=protocol,
        metrics=metrics,
        leverage=leverage,
        threats=threats,
        invocation=invocation,
    )


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


def render_json(blueprint: Blueprint) -> str:
    return json.dumps(blueprint.__dict__, indent=2)


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
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    blueprint = build_blueprint(args.theme, args.seed)
    if args.json:
        print(render_json(blueprint))
    else:
        print(render_markdown(blueprint))


if __name__ == "__main__":
    main()
