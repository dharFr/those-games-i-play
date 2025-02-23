from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Game(BaseModel):
    steam_id: int
    title: str
    genres: List[str]
    tags: List[str]
    price: float
    release_date: datetime
    review_score: Optional[float] = None
    review_count: Optional[int] = None
