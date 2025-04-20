from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


class UserInDB(User):
    hashed_password: str
