from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class Repository(ABC, Generic[T]):
    @abstractmethod
    async def add(self, entity: T) -> None:
        """Add a new entity to the repository."""
        pass

    @abstractmethod
    async def get(self, entity_id: int) -> Optional[T]:
        """Retrieve an entity by its ID."""
        pass

    @abstractmethod
    async def get_multi(self) -> List[T]:
        """Retrieve a list of all entities."""
        pass

    @abstractmethod
    async def delete(self, entity_id: int) -> None:
        """Delete an entity by its ID."""
        pass
