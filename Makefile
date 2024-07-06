run:
	@uvicorn workout_api.main:app --reload

# create-migrations:
# 	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(s)
create-migrations:
	@powershell -Command "Set-Item -Path Env:PYTHONPATH -Value '.'; alembic revision --autogenerate -m '${d}'"

# Makefile para executar migrações com Alembic

.PHONY: run-migrations

run-migrations:
    @powershell -Command "Set-Item -Path Env:PYTHONPATH -Value '.'; python -m alembic upgrade head"
