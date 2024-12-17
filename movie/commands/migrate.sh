#!/bin/bash

echo "Applying migration..."
alembic upgrade head
echo "Migration complete."
