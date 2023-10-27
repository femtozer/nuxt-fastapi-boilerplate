FROM python:3.11-slim-bullseye as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --dev

# ---
FROM python:3.11-slim-bullseye

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --no-cache-dir --upgrade pip && \
    pip install debugpy && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./.env* /code/.env
COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic
COPY ./src /code/src

CMD alembic upgrade head; PYDEVD_DISABLE_FILE_VALIDATION=1 python -m debugpy --listen 0.0.0.0:5678 -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
