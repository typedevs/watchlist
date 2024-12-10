up:
    docker compose up -d

build:
    docker compose up --build -d

deps:
    pip install \
    -r requirements.txt \
    -r movie/requirements.txt \
    -r user/requirements.txt \
    -r watchlist/requirements.txt \
    -r director/requirements.txt
