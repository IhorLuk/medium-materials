from sqlalchemy.orm import Session

import models, schemas

def get_stock(db: Session, symbol: str):
    return db.query(models.Stock).filter(models.Stock.symbol == symbol).first()

def post_stock(db: Session):
    pass

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def post_user(db: Session, user_data: schemas.UserCreate):
    db.begin()
    db.add(models.User(user_id=user_data.user_id,
                       first_name=user_data.first_name,
                       last_name=user_data.last_name,
                       last_sale_amount=user_data.last_sale_amount))
    db.commit()
    
def put_user_sale(db: Session, user_data: schemas.UserUpdateSaleAmount):
    db.query(models.User).filter(models.User.user_id == user_data.user_id).update(
        {
            "last_sale_amount": user_data.last_sale_amount,
        }
    )
    db.commit()
    
def delete_user(db: Session, user_id: str):
    db.query(models.User).filter(models.User.user_id == user_id).delete()
    db.commit()
