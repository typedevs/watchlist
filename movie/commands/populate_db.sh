#!/bin/bash

echo "Populating database with sample data..."

# Define database connection parameters
DB_NAME=movie      # Replace with your database name
DB_USER=postgres     # Replace with your database username
DB_PASSWORD=postgres  # Replace with your database password
DB_HOST=localhost         # Change if your database is on a different host
DB_PORT=5432              # Default PostgreSQL port

export PGPASSWORD=$DB_PASSWORD

psql -h $DB_HOST -U $DB_USER -d $DB_NAME <<EOF

-- Insert sample data into the movies table with timestamps
INSERT INTO movies (name, director_id, created_at, updated_at) VALUES ('Inception', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO movies (name, director_id, created_at, updated_at) VALUES ('The Matrix', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO movies (name, director_id, created_at, updated_at) VALUES ('Interstellar', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO movies (name, director_id, created_at, updated_at) VALUES ('The Godfather', 3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO movies (name, director_id, created_at, updated_at) VALUES ('Pulp Fiction', 4, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
EOF

echo "Database populated successfully with 5 movies."
