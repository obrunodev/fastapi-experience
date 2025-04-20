from passlib.context import CryptContext
from typing import Optional
from src.users.schemas import UserInDB
from datetime import datetime, timedelta
from jose import jwt
from decouple import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    "bruno": {
        "username": "bruno",
        "full_name": "Bruno Souza",
        "hashed_password": pwd_context.hash("123456")
    }
}

def get_user(username: str) -> Optional[UserInDB]:
    user_dict = fake_users_db.get(username)
    if user_dict:
        return UserInDB(**user_dict)
    return None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config("SECRET_KEY"), algorithm=config("ALGORITHM"))
