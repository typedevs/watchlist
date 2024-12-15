from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from movie.src.infrastructures.database import IS_RELATIONAL_DB, initialize_db
from movie.src.infrastructures.fastapi.api.routes import routers


@asynccontextmanager
async def lifespan(app: FastAPI):

    kwargs = {}
    if IS_RELATIONAL_DB:
        from movie.src.infrastructures.database.sql_models.base import Base
        kwargs = {'declarative_base': Base}

    await initialize_db(**kwargs)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(routers)


@app.exception_handler(Exception)
async def universal_exception_handler(_, exc):
    return JSONResponse(content={'error': f'{type(exc).__name__}: {exc}'}, status_code=500)


resource = Resource(attributes={SERVICE_NAME: "fs-app"})
traceProvider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
traceProvider.add_span_processor(processor)
trace.set_tracer_provider(traceProvider)

FastAPIInstrumentor.instrument_app(app)
HTTPXClientInstrumentor().instrument()
