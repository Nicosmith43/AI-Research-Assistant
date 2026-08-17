from pydantic import BaseModel


class ResearchRequest(BaseModel):
    query: str


class ResearchSource(BaseModel):
    type: str
    title: str
    url: str


class ResearchResponse(BaseModel):
    id: int
    query: str
    answer: str
    sources: list[ResearchSource]