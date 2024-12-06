from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"item_name": "Item 1"},
    {"item_name": "Item 2"},
    {"item_name": "Item 3"},
    {"item_name": "Item 4"},
    {"item_name": "Item 5"},
]

# Query parameters
# Parâmetros de query são passados como uma string de consulta, separados por & e começando por ?, exemplo: ?skip=10&limit=20

@app.get("/items")
def read_items(skip: int = 0, limit: int = 10):
    return fake_db[skip:skip + limit]
