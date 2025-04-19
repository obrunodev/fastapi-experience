from src.customers.routes import router as customers_router
from fastapi import FastAPI

app = FastAPI()

@app.get("/health-check", tags=["Testes"])
def health_check():
    return {"message": "Ok"}

app.include_router(customers_router)
