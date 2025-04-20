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

    @classmethod
    def from_mongo(cls, doc: dict):
        return cls(id=str(doc["_id"]),
                   name=doc["name"],
                   email=doc["email"])
