#! /usr/bin/env bash

# Let the DB start
python ./app/db_pre_start/backend_pre_start.py

# Run migrations
alembic revision --autogenerate -m "first commit"

alembic upgrade head

# Create initial data in DB
python ./app/initial_data.py
