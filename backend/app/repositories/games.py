from typing import List, Optional, Dict
from app.core.db import db
from app.models.game import Game
from app.core.errors import AppException
from .base import BaseRepository
from app.core.config import settings

class GameRepository(BaseRepository[Game]):
    def __init__(self):
        self.collection = db.get_db().games

    async def list(
        self,
        skip: int = 0,
        limit: int = settings.default_page_size,
        filters: Optional[Dict] = None
    ) -> List[Game]:
        try:
            cursor = self.collection.find(filters or {})
            cursor = cursor.skip(skip).limit(limit)
            
            games = []
            async for game_doc in cursor:
                game_doc["id"] = str(game_doc.pop("_id"))
                games.append(Game(**game_doc))
            
            return games
        except Exception as e:
            raise AppException(
                message="Failed to fetch games",
                status_code=500,
                details={"error": str(e)}
            )

    async def count(self, filters: Optional[Dict] = None) -> int:
        try:
            return await self.collection.count_documents(filters or {})
        except Exception as e:
            raise AppException(
                message="Failed to count games",
                status_code=500,
                details={"error": str(e)}
            )
