from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias
from workout_api.centro_treinamento.controller import router as centro_treinamento

apit_router = APIRouter()
# apit_router.include_router(atleta, prefix=['/atletas'], tags=['atletas'])
apit_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
apit_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
apit_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['centros_treinamento'])