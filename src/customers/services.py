from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.config.database import MongoDBConfig
from src.customers.schemas import Customer, CustomerUpdate, CustomerOut

customers = MongoDBConfig().get_collection("customers")


class CustomerService:

    @staticmethod
    def _get_customer_or_404(customer_id: str) -> dict:
        try:
            object_id = ObjectId(customer_id)
        except Exception:
            raise HTTPException(status_code=400, detail="ID inválido")

        customer = customers.find_one({"_id": object_id})
        if not customer:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

        return customer

    @staticmethod
    def create_customer(customer: Customer) -> CustomerOut:
        if customers.find_one({"email": customer.email}):
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")

        customer_dict = customer.model_dump()
        customers.insert_one(customer_dict)
        return CustomerOut.from_mongo(customer_dict)

    @staticmethod
    def customers_list() -> list[CustomerOut]:
        customers_list = customers.find()
        return [CustomerOut.from_mongo(c) for c in customers_list]

    @staticmethod
    def get_customer_by_email(customer_email: str) -> CustomerOut:
        customer = customers.find_one({"email": customer_email})
        if not customer:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return CustomerOut.from_mongo(customer)

    @staticmethod
    def update_customer(customer_id: str, customer_data: Customer) -> CustomerOut:
        CustomerService._get_customer_or_404(customer_id)

        customer_dict = customer_data.model_dump()
        customers.update_one(
            {"_id": ObjectId(customer_id)},
            {"$set": customer_dict}
        )
        updated_customer = customers.find_one({"_id": ObjectId(customer_id)})
        return CustomerOut.from_mongo(updated_customer)

    @staticmethod
    def patch_customer(customer_id: str, customer_data: CustomerUpdate) -> CustomerOut:
        CustomerService._get_customer_or_404(customer_id)

        customer_dict = customer_data.model_dump(exclude_unset=True)
        if not customer_dict:
            raise HTTPException(status_code=400, detail="Nenhum campo enviado para alteração.")

        customers.update_one(
            {"_id": ObjectId(customer_id)},
            {"$set": customer_dict}
        )
        updated_customer = customers.find_one({"_id": ObjectId(customer_id)})
        return CustomerOut.from_mongo(updated_customer)

    @staticmethod
    def delete_customer_by_id(customer_id: str) -> dict:
        CustomerService._get_customer_or_404(customer_id)

        customers.find_one_and_delete({"_id": ObjectId(customer_id)})
        return {"message": "Cliente deletado com sucesso"}
