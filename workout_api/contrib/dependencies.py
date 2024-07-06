from fastapi import Depends
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.configs.database import get_sessiont


DatanaseDependency = Annotated[AsyncSession, Depends(get_sessiont)]