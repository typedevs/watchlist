#!/bin/bash

echo "Generating migration..."
alembic revision --autogenerate -m "$1"
echo "Complete"
