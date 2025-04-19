from bson import ObjectId
from fastapi import HTTPException
from src.config.database import MongoDBConfig
from src.customers.schemas import Customer, CustomerOut

customers = MongoDBConfig().get_collection("customers")


class CustomerService:

    @staticmethod
    def create_customer(customer: Customer) -> CustomerOut:
        if customers.find_one({"email": customer.email}):
            raise HTTPException(
                status_code=400,
                detail="E-mail já cadastrado"
            )
        result = customers.insert_one(customer.model_dump())
        return CustomerOut(
            id=str(result.inserted_id),
            **customer.model_dump()
        )
    
    @staticmethod
    def customers_list() -> list[CustomerOut]:
        customers_list = customers.find()
        return [
            CustomerOut(
                id=str(c["_id"]),
                name=c["name"],
                email=c["email"]
            )
            for c in customers_list
        ]
        