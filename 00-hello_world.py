from fastapi import FastAPI

app = FastAPI()

# Primeira rota - Hello world
@app.get("/")
def read_root():
    return {"message": "Hello World"}
