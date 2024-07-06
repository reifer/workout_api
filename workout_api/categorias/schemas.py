from typing import Annotated
from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categorias', example='Scale', max_length=10)]

class CategoriaOut(CategoriaIn):
    nome: Annotated[UUID4, Field(description='Identificador da categoria')]
    