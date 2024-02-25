from pydantic import BaseModel
from typing import Optional

class StockBase(BaseModel):
    symbol: str
    stockname: str
    lastsale: str
    country: str
    ipoyear: Optional[int] = None
    volume: int
    
class StockCreate(StockBase):
    pass

class Stock(StockBase):
    
    class Config:
        orm_mode = True
