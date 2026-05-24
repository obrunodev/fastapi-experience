from apps.routers.health import router as health_router

from decouple import config

from fastapi import FastAPI, status

app = FastAPI(
    title="FastAPI template",
    version=config("APP_VERSION", "1.0.0"),
    description="Projeto template com pré-configurações para novas APIs"
)

app.include_router(health_router)
