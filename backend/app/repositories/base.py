from typing import Generic, TypeVar, List, Optional, Any
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)

class BaseRepository(Generic[ModelType]):
    """Base repository with common CRUD operations."""
    
    async def get(self, id: Any) -> Optional[ModelType]:
        """Retrieve a single record by id."""
        raise NotImplementedError
    
    async def list(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[dict] = None
    ) -> List[ModelType]:
        """Retrieve multiple records with pagination and filtering."""
        raise NotImplementedError
    
    async def create(self, data: ModelType) -> ModelType:
        """Create a new record."""
        raise NotImplementedError
    
    async def update(self, id: Any, data: ModelType) -> Optional[ModelType]:
        """Update an existing record."""
        raise NotImplementedError
    
    async def delete(self, id: Any) -> bool:
        """Delete a record."""
        raise NotImplementedError
