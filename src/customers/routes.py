from fastapi import APIRouter
from src.customers.schemas import Customer, CustomerOut
from src.customers.services import CustomerService

router = APIRouter(tags=["Clientes"], prefix="/customers")
customer_service = CustomerService()


@router.post("", response_model=CustomerOut)
def create_customer(customer: Customer):
    return customer_service.create_customer(customer)


@router.get("", response_model=list[CustomerOut])
def customers_list():
    return customer_service.customers_list()
