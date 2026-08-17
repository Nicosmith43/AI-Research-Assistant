from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    query: str = Field(..., min_length=1)


class ResearchSource(BaseModel):
    type: str
    title: str
    url: str


class ResearchResponse(BaseModel):
    id: int
    query: str
    answer: str
    sources: list[ResearchSource]