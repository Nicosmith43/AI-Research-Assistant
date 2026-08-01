from datetime import datetime

from pydantic import BaseModel


class HistoryResponse(BaseModel):
    id: int
    query: str
    answer: str
    source: str
    favorite: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }