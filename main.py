from fastapi import FastAPI
from routers import notes

app = FastAPI()


@app.get("/")
def health_check():
    return {'status': 'Server is OK!'}


app.include_router(notes.router)
