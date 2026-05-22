from __future__ import annotations

from datetime import date

from .models import CampaignInput, Channel, ExperimentPlan, LaunchPlan


ANGLE_TEMPLATES = {
    Channel.search: "Problem-aware high-intent query capture",
    Channel.social: "Founder-led story + proof clip",
    Channel.email: "Case-study nurture + irresistible CTA",
    Channel.content: "Comparison page + ROI calculator",
}


KPI_MAP = {
    Channel.search: "CAC",
    Channel.social: "CTR",
    Channel.email: "SQL rate",
    Channel.content: "Organic MQLs",
}


def _channel_weights(offers_count: int, audiences_count: int) -> dict[Channel, float]:
    base = {
        Channel.search: 0.3,
        Channel.social: 0.3,
        Channel.email: 0.2,
        Channel.content: 0.2,
    }
    if offers_count > 3:
        base[Channel.search] += 0.05
        base[Channel.content] += 0.05
        base[Channel.social] -= 0.05
        base[Channel.email] -= 0.05
    if audiences_count > 2:
        base[Channel.social] += 0.05
        base[Channel.email] += 0.05
        base[Channel.search] -= 0.05
        base[Channel.content] -= 0.05
    return base


def build_launch_plan(payload: CampaignInput) -> LaunchPlan:
    if payload.monthly_budget <= 0:
        raise ValueError("monthly_budget must be positive")

    weights = _channel_weights(len(payload.offers), len(payload.audiences))
    experiments: list[ExperimentPlan] = []

    for channel, weight in weights.items():
        experiments.append(
            ExperimentPlan(
                channel=channel,
                angle=ANGLE_TEMPLATES[channel],
                budget=round(payload.monthly_budget * weight, 2),
                kpi=KPI_MAP[channel],
            )
        )

    weighted_margin = (
        sum(offer.price * offer.gross_margin for offer in payload.offers) / max(len(payload.offers), 1)
    )
    audience_factor = 1.0 + min(0.6, len(payload.audiences) * 0.12)
    expected_pipeline = round(payload.monthly_budget * (2.4 + weighted_margin / 100) * audience_factor, 2)

    return LaunchPlan(
        generated_on=date.today(),
        company=payload.company,
        experiments=experiments,
        expected_pipeline=expected_pipeline,
    )
