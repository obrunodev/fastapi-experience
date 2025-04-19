from pydantic import BaseModel, EmailStr


class Customer(BaseModel):
    name: str
    email: EmailStr


class CustomerOut(Customer):
    id: str

    class Config:
        from_attribute = True
