from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from movie.src.adapters.repositories.base_repository import Repository

T = TypeVar('T', bound=Repository)


class UnitOfWork(Generic[T], ABC):
    repository: Repository

    def __init__(self, repository: T):
        self.repository = repository

    @abstractmethod
    async def __aenter__(self) -> 'UnitOfWork[T]':
        """Start a transaction."""
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        """Commit or rollback the transaction."""
        raise NotImplementedError
