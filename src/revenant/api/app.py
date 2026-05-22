from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from revenant.core.engine import build_launch_plan
from revenant.core.models import AudienceSegment, CampaignInput, ProductOffer

app = FastAPI(title="Revenant AI API", version="0.1.0")


class ProductOfferDTO(BaseModel):
    name: str
    price: float = Field(gt=0)
    gross_margin: float = Field(ge=0, le=1)


class AudienceSegmentDTO(BaseModel):
    name: str
    pain_point: str
    willingness_to_pay: float = Field(ge=0)


class LaunchRequestDTO(BaseModel):
    company: str
    monthly_budget: float = Field(gt=0)
    offers: list[ProductOfferDTO]
    audiences: list[AudienceSegmentDTO]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/launch-plan")
def launch_plan(request: LaunchRequestDTO) -> dict:
    try:
        model = CampaignInput(
            company=request.company,
            monthly_budget=request.monthly_budget,
            offers=[ProductOffer(**offer.model_dump()) for offer in request.offers],
            audiences=[AudienceSegment(**aud.model_dump()) for aud in request.audiences],
        )
        result = build_launch_plan(model)
        return {
            "generated_on": result.generated_on.isoformat(),
            "company": result.company,
            "expected_pipeline": result.expected_pipeline,
            "experiments": [
                {
                    "channel": e.channel.value,
                    "angle": e.angle,
                    "budget": e.budget,
                    "kpi": e.kpi,
                }
                for e in result.experiments
            ],
        }
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
