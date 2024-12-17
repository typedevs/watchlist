from datetime import datetime

from sqlalchemy import Column, DateTime, BigInteger
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    id = Column(BigInteger, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __name__: str
