from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class Channel(str, Enum):
    search = "search"
    social = "social"
    email = "email"
    content = "content"


@dataclass(slots=True)
class ProductOffer:
    name: str
    price: float
    gross_margin: float


@dataclass(slots=True)
class AudienceSegment:
    name: str
    pain_point: str
    willingness_to_pay: float


@dataclass(slots=True)
class CampaignInput:
    company: str
    monthly_budget: float
    offers: list[ProductOffer] = field(default_factory=list)
    audiences: list[AudienceSegment] = field(default_factory=list)


@dataclass(slots=True)
class ExperimentPlan:
    channel: Channel
    angle: str
    budget: float
    kpi: str


@dataclass(slots=True)
class LaunchPlan:
    generated_on: date
    company: str
    experiments: list[ExperimentPlan]
    expected_pipeline: float
