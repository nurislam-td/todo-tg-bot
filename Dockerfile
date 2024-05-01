# for startup build
FROM python:3.12-slim as builder

RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache


RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root


# for runtime
FROM python:3.12-slim as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"\
    PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

EXPOSE 8000

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY . .
RUN chmod +x /docker/app.sh


ENTRYPOINT ["/docker/app.sh"]