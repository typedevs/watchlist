FROM python:3.11.4-alpine

RUN apk add gcc python3-dev musl-dev linux-headers

WORKDIR /app/movie

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "movie.src.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
