def crypto_to_dto(data: dict):
    return {
        "name": data.get("name"),
        "symbol": data.get("symbol"),
        "price_usd": data["market_data"]["current_price"]["usd"],
        "market_cap": data["market_data"]["market_cap"]["usd"],
        "price_change_24h": data["market_data"]["price_change_percentage_24h"]
    }
