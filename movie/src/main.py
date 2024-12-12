from fastapi import FastAPI
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from movie.src.core.containers import AppContainer
from movie.src.infrastructures.fastapi.api.routes import routers
from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor, BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
app = FastAPI()

container = AppContainer()
app.container = container

app.include_router(routers)

resource = Resource(attributes={
    SERVICE_NAME: "fs-app"
})
traceProvider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
traceProvider.add_span_processor(processor)
trace.set_tracer_provider(traceProvider)

FastAPIInstrumentor.instrument_app(app)
HTTPXClientInstrumentor().instrument()
