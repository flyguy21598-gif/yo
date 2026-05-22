from revenant.core.engine import build_launch_plan
from revenant.core.models import AudienceSegment, CampaignInput, ProductOffer


def test_build_launch_plan_has_four_experiments() -> None:
    payload = CampaignInput(
        company="Acme",
        monthly_budget=10000,
        offers=[ProductOffer(name="Pro", price=199, gross_margin=0.8)],
        audiences=[AudienceSegment(name="Founder", pain_point="No pipeline", willingness_to_pay=1000)],
    )
    plan = build_launch_plan(payload)
    assert len(plan.experiments) == 4
    assert round(sum(e.budget for e in plan.experiments), 2) == 10000


def test_negative_budget_rejected() -> None:
    payload = CampaignInput(company="Acme", monthly_budget=-1)
    try:
        build_launch_plan(payload)
    except ValueError as exc:
        assert "monthly_budget" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
