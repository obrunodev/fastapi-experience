from pydantic import BaseModel, EmailStr
from typing import Optional


class Customer(BaseModel):
    name: str
    email: EmailStr


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

    class Config:
        from_attribute = True


class CustomerOut(Customer):
    id: str

    class Config:
        from_attribute = True
