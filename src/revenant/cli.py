from __future__ import annotations

import argparse
import json

from revenant.core.engine import build_launch_plan
from revenant.core.models import AudienceSegment, CampaignInput, ProductOffer


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Revenant launch plan")
    parser.add_argument("--company", required=True)
    parser.add_argument("--budget", type=float, required=True)
    args = parser.parse_args()

    sample = CampaignInput(
        company=args.company,
        monthly_budget=args.budget,
        offers=[ProductOffer(name="Flagship", price=499.0, gross_margin=0.74)],
        audiences=[AudienceSegment(name="Ops Lead", pain_point="Manual reporting", willingness_to_pay=700)],
    )
    plan = build_launch_plan(sample)
    print(
        json.dumps(
            {
                "company": plan.company,
                "expected_pipeline": plan.expected_pipeline,
                "experiments": [
                    {"channel": e.channel.value, "budget": e.budget, "kpi": e.kpi}
                    for e in plan.experiments
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
