#!/bin/bash

export PYTHONPATH=$(pwd)/.

alembic upgrade head


python3.12  app/main.py

# gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000