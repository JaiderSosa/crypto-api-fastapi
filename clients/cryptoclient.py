import httpx

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"


async def fetch_crypto_price(crypto_id: str):
    params = {
        "ids": crypto_id,
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_change": "true"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(COINGECKO_URL, params=params)
        response.raise_for_status()
        return response.json()

