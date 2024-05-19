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

class UserBase(BaseModel):
    user_id: str

class User(UserBase):
    first_name: str
    last_name: str
    last_sale_amount: int
    
    class Config:
        orm_mode = True
        
class UserCreate(User):
    pass

class UserUpdateSaleAmount(UserBase):
    last_sale_amount: int
    
    class Config:
        orm_mode = True