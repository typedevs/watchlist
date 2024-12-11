from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar("T")


class Service(ABC, Generic[T]):
    @abstractmethod
    async def create(self, entity: T) -> T:
        """Create a new entity."""
        pass

    @abstractmethod
    async def get(self, entity_id: int) -> T:
        """Retrieve an entity by its ID."""
        pass

    @abstractmethod
    async def get_list(self) -> List[T]:
        """List all entities."""
        pass

    @abstractmethod
    async def delete(self, entity_id: int) -> None:
        """Delete an entity by its ID."""
        pass
