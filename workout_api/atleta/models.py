# from datetime import datetime
# from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
# from sqlalchemy import Mapped, mapped_column, relationship

# from workout_api.contrib.models import BaseModel



# class AtletaModel(BaseModel):
#     pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     nome: Mapped[str] = mapped_column(String(50), nullable=False)
#     cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
#     idade: Mapped[int] = mapped_column(Integer(11), nullable=False)
#     peso: Mapped[float] = mapped_column(Float, nullable=False)
#     altura: Mapped[float] = mapped_column(Float, nullable=False)
#     sexo: Mapped[str] = mapped_column(String(1), nullable=False)
#     created_at: Mapped[datetime] = mapped_column(datetime, nullable=False)
#     categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
#     categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
#     centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
#     centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))

from sqlalchemy import Column, Integer, String, ForeignKey
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import relationship

class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.pk_id"))
    centro_treinamento_id = Column(Integer, ForeignKey("centro_treinamento.pk_id"))
    categoria = relationship("CategoriaModel", back_populates="atletas", lazy='selectin')
    centro_treinamento = relationship("CentroTreinamentoModel", back_populates="atletas", lazy='selectin')
