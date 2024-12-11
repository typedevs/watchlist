from abc import ABC, abstractmethod

from movie.app.adapters.repositories.base_repository import Repository


class UnitOfWork(ABC):
    def __init__(self, repository: Repository):
        self.repository = repository

    @abstractmethod
    async def __aenter__(self):
        """Start a transaction."""
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Commit or rollback the transaction."""
        pass
