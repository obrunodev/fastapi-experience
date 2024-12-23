from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# Path parameters
# @app.get("/items/{item_id}")
# def read_item(item_id):
#     return {"item_id": item_id}

# Path parameters with types
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Retorna um erro caso o item_id não seja um número inteiro
    """
    return {"item_id": item_id}

@app.get("/say-hi/{name}")
def say_hi(name: str):
    return {"message": f"Hello {name}"}

# Usando Enum para predefinir valores possíveis
class Color(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"

@app.get("/color/{color}")
def read_color(color: Color):
    if color is Color.RED:
        return {"color": color, "message": "Parado!"}

    if color.value == "green":
        return {"color": color, "message": "Pode avançar!"}

    return {"color": color, "message": "Restante das cores!"}

# Path parameters com caminhos
@app.get("/files/{file_path:path}")  # :path significa que o parâmetro pode receber qualquer caminho/path
def read_file(file_path: str):
    # O caminho/path sempre deve começar com /, nesse caso o caminho deve ficar assim: /files//home/user/file.txt
    return {"file_path": file_path}
