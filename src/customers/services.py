from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.config.database import MongoDBConfig
from src.customers.schemas import Customer, CustomerUpdate, CustomerOut

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
    
    @staticmethod
    def get_customer_by_email(customer_email: str) -> CustomerOut:
        customer = customers.find_one({"email": customer_email})
        if not customer:
            return JSONResponse(
                status_code=200,
                content={"message": "Nenhum cliente encontrado"}
            )
        return CustomerOut(
            id=str(customer["_id"]),
            **customer
        )
    
    @staticmethod
    def update_customer(customer_id: str,
                        customer_data: Customer) -> CustomerOut:
        customer_dict = customer_data.model_dump(exclude_unset=True)
        customers.update_one(
            {"_id": ObjectId(customer_id)},
            {"$set": customer_dict},
        )
        updated_customer = customers.find_one({"_id": ObjectId(customer_id)})
        return CustomerOut(
            id=str(updated_customer["_id"]),
            **updated_customer
        )

    @staticmethod
    def patch_customer(customer_id: str,
                       customer_data: CustomerUpdate) -> CustomerOut:
        customer_dict = customer_data.model_dump(exclude_unset=True)
        if not customer_dict:
            raise ValueError("Nenhum campo enviado para alteração.")
        
        customers.update_one(
            {"_id": ObjectId(customer_id)},
            {"$set": customer_dict},
        )
        updated_customer = customers.find_one({"_id": ObjectId(customer_id)})
        return CustomerOut(
            id=str(updated_customer["_id"]),
            **updated_customer,
        )
        