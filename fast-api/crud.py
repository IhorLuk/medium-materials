from sqlalchemy.orm import Session

import models, schemas

def get_stock(db: Session, symbol: str):
    return db.query(models.Stock).filter(models.Stock.symbol == symbol).first()
