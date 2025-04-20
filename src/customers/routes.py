from fastapi import APIRouter
from src.customers.schemas import Customer, CustomerUpdate, CustomerOut
from src.customers.services import CustomerService

router = APIRouter(tags=["Clientes"], prefix="/customers")
customer_service = CustomerService()


@router.post("", response_model=CustomerOut)
def create_customer(customer: Customer):
    return customer_service.create_customer(customer)


@router.get("", response_model=list[CustomerOut])
def customers_list():
    return customer_service.customers_list()


@router.get("/{customer_email}", response_model=CustomerOut)
def get_customer_by_email(customer_email: str):
    return customer_service.get_customer_by_email(customer_email)

@router.put("/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: str, customer_data: Customer):
    return customer_service.update_customer(
        customer_id,
        customer_data
    )

@router.patch("/{customer_id}", response_model=CustomerOut)
def patch_customer(customer_id: str, customer_data: CustomerUpdate):
    return customer_service.patch_customer(
        customer_id,
        customer_data
    )

@router.delete("/{customer_id}")
def delete_customer(customer_id: str):
    return customer_service.delete_customer_by_id(customer_id)
