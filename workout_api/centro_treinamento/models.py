# from sqlalchemy import Integer, Integer, String
# from sqlalchemy import Mapped, mapped_column,relationship

# from workout_api.contrib.models import BaseModel

# class CentroTreinamentoModel(BaseModel):
#     __tablename__ = 'centros_treinamento'
#     pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
#     endereco: Mapped[str] = mapped_column(String(60), nullable=False)
#     proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
#     categoria: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')

from sqlalchemy import Column, Integer, String
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import relationship
from pydantic import BaseModel as PydanticBaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centro_treinamento"

    pk_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    atletas = relationship("AtletaModel", back_populates="centro_treinamento")

class CentroTreinamentoOut(PydanticBaseModel):
    pk_id: int
    nome: str

class Config:
    orm_mode = True