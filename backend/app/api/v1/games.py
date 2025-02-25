from fastapi import APIRouter, Query
from app.repositories.games import GameRepository
from app.models.api.games import PaginatedGamesResponse
from app.core.config import settings

router = APIRouter()

@router.get("/games", response_model=PaginatedGamesResponse)
async def list_games(
    page: int = Query(1, ge=1),
    limit: int = Query(default=settings.default_page_size, le=settings.max_page_size)
) -> PaginatedGamesResponse:
    
    print(">>> list_games", page, limit)
    repo = GameRepository()
    
    # Calculate skip for pagination
    skip = (page - 1) * limit
    
    # Get total count and items
    total = await repo.count()
    items = await repo.list(skip=skip, limit=limit)
    
    # Calculate pagination metadata
    total_pages = (total + limit - 1) // limit
    
    return PaginatedGamesResponse(
        items=items,
        metadata={
            "total_items": total,
            "total_pages": total_pages,
            "current_page": page,
            "items_per_page": limit
        }
    )
