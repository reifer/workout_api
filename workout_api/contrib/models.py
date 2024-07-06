# from uuid import uuid4
# from sqlalchemy.dialects.postgresql import UUID as PG_UUID
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# class BaseModel(DeclarativeBase):
#     __abstract__ = True
#     id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)

from uuid import uuid4
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
