#!/bin/bash

if [ -z "$1" ]; then
  echo "No revision ID provided. Reverting the last migration..."
  alembic downgrade -1
else
  echo "Reverting to the specified revision ID: $1"
  alembic downgrade "$1"
fi

echo "Migration reverted successfully."
