alembic revision --autogenerate -m "First revision"

alembic upgrade head

python -m backend.db.create_admin