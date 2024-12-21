from abc import ABC, abstractmethod
from typing import TypeVar, List, Optional, Any

T = TypeVar("T")


class Repository(ABC):
    session: Any

    @abstractmethod
    async def add(self, entity: T) -> T:
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
