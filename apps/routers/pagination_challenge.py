from fastapi import APIRouter
import time


router = APIRouter(
    prefix="/pagination-challenge",
    tags=["pagination-challenge"]
)


@router.get("/dashboard/ruim")
def dashboard_ruim():
    time.sleep(5)
    return {"message": "Dashboard ruim"}


@router.get("/dashboard/bom")
def dashboard_bom():
    time.sleep(1)
    return {"message": "Dashboard bom"}
