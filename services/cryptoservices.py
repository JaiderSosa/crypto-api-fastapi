from fastapi import HTTPException
from clients.cryptoclient import fetch_crypto_price


async def get_crypto_price(crypto_id: str):
    """
    Servicio que obtiene y estructura la información de una criptomoneda
    """
    data = await fetch_crypto_price(crypto_id)

    if not data or crypto_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Criptomoneda no encontrada"
        )

    crypto_data = data[crypto_id]

    return {
        "crypto": crypto_id,
        "usd_price": crypto_data.get("usd"),
        "usd_market_cap": crypto_data.get("usd_market_cap"),
        "usd_24h_change": crypto_data.get("usd_24h_change")
    }
