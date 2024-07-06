from typing import Annotated
from uuid import UUID
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT da Fiel', max_length=20)]
    endereco: Annotated[str, Field(description='Nome do Endereco', example='Rua X, quadra 2', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', example='Reinaldo Junior', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut():
    id: Annotated[UUID, Field(description='Identificador do Centro de Treinamento')]
    pass