from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from apps.schemas.health import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["Monitoramento"],
)


@router.get(
    "/check",
    description="Retorna 200 e mensagem para sinalizar que API está em funcionamento",
    summary="Verifica saúda da API",
    status_code=status.HTTP_200_OK,
    response_model=HealthResponse,
)
def health_check():
    response = HealthResponse(message="OK")
    return response
