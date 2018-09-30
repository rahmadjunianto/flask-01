#!/bin/sh
alembic downgrade base
rm migrations/versions/*.py
alembic revision --autogenerate -m "initial DB"
alembic upgrade head


