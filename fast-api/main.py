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

@app.get('/user/{user_id}', response_model=schemas.User, status_code=200)
def get_user(user_id: str, db: Session = Depends(get_db)) -> models.User:
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"No user {user_id} found."
        )

    return db_user

@app.post("/create_user/")
async def post_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        crud.post_user(db, user)
    except Exception as e:
        raise e
    
    return {"response": f"User {user.user_id} was created."}

@app.put("/update_user_last_sale/")
async def update_user_last_sale(user: schemas.UserUpdateSaleAmount, db: Session = Depends(get_db)):
    try:
        crud.put_user_sale(db, user)
    except Exception as e:
        raise e
    
    return {"response": f"User {user.user_id} data was updated."}

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    try:
        crud.delete_user(db, user_id)
    except Exception as e:
        raise e
    
    return {"response": f"User {user_id} is removed."}

# def get_stock_query(
#     country: Optional[str] = Query(None, title="Country", description="Coutry of company"),
#     ipoyear: Optional[int] = Query(None, title="IPO year", description="Year of listing"),
# ):
