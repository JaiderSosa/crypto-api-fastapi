from fastapi import APIRouter, HTTPException
from services.cryptoservices import get_crypto_price

router = APIRouter(
    prefix="/api/crypto",
    tags=["Cryptocurrency"]
)


@router.get("/{crypto_id}")
async def get_crypto(crypto_id: str):
    """
    Consulta el precio actual de una criptomoneda
    Ejemplos:
    - bitcoin
    - ethereum
    - dogecoin
    """
    try:
        return await get_crypto_price(crypto_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error interno consultando la API de criptomonedas"
        )
