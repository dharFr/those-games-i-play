from typing import List
from pydantic import BaseModel
from app.models.game import Game

class PaginatedGamesResponse(BaseModel):
    items: List[Game]
    metadata: dict[str, int]
