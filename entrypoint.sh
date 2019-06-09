#!/bin/sh

export PYTHONPATH=/app

python3 /app/create_tables.py


exec "$@"