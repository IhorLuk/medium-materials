from sqlalchemy import Column, Integer, String, Float, BigInteger
from database import Base

class Stock(Base):
    __tablename__ = "nasdaq_stocks"
    
    symbol = Column(String, primary_key=True)
    stockname = Column(String)
    lastsale = Column(String)
    netchange = Column(Float)
    percentchange = Column(String)
    marketcap = Column(BigInteger)
    country = Column(String, nullable=True)
    ipoyear = Column(Integer, nullable=True)
    volume = Column(Integer)
    sector = Column(String, nullable=True)
    industry = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    last_sale_amount = Column(Integer)
