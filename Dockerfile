FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app

COPY ./alembic /alembic

COPY ./alembic.ini /alembic.ini

RUN pip install --no-cache-dir -r /app/requirements.txt