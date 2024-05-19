from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

class Stock(BaseModel):
    symbol: str
    stockname: str
    lastsale: str
    country: str
    ipoyear: Optional[int] = None
    
with open('stocks.json', 'r') as f:
    stocks = json.load(f)['stocks']

@app.get('/stock/{stock_symbol}', status_code=200)
def get_stock(stock_symbol: str) -> Stock:
    stock = [stock for stock in stocks if stock['symbol'] == stock_symbol]
    if len(stock) == 0:
        raise HTTPException(
            status_code=404, detail=f"No stock {stock_symbol} found."
        )

    return stock[0]
