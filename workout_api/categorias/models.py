# from sqlalchemy import Integer, Integer, String
# from sqlalchemy import Mapped, mapped_column,relationship

# from workout_api.contrib.models import BaseModel

# class CategoriaModel(BaseModel):
#     __tablename__ = 'categorias'
#     pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
#     categoria: Mapped['AtletaModel'] = relationship(back_populates='atleta')

from sqlalchemy import Column, Integer, String
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import relationship

class CategoriaModel(BaseModel):
    __tablename__ = "categorias"

    pk_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    atletas = relationship("AtletaModel", back_populates="categoria")
