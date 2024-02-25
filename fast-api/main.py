from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NASDAQ stocks",
    description="Start using FastAPI in development",
    version="0.1"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


@app.get('/stock/{symbol}', response_model=schemas.Stock, status_code=200)
def get_stock(symbol: str, db: Session = Depends(get_db)) -> models.Stock:
    db_stock = crud.get_stock(db, symbol=symbol)
    if db_stock is None:
        raise HTTPException(
            status_code=404, detail=f"No stock {symbol} found."
        )

    return db_stock

# def get_stock_query(
#     country: Optional[str] = Query(None, title="Country", description="Coutry of company"),
#     ipoyear: Optional[int] = Query(None, title="IPO year", description="Year of listing"),
# ):
    