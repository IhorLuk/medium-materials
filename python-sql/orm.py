from dotenv import load_dotenv
import os

from sqlalchemy import URL, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.types import Integer, String

class Base(DeclarativeBase):
    pass

class Cars(Base):
    __tablename__ = "cars"
    
    manufacturer: Mapped[str] = mapped_column(String(64))
    model: Mapped[str] = mapped_column(String(64))
    country: Mapped[str] = mapped_column(String(64))
    engine_name: Mapped[str] = mapped_column(String(64), primary_key=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer)
    
class Engines(Base):
    __tablename__ = "engines"
    
    name: Mapped[str] = mapped_column(String(64), primary_key=True, nullable=False)
    horse_power: Mapped[int] = mapped_column(Integer)
    

def main():
    
    load_dotenv()
    
    connection_string = URL.create(
        'postgresql',
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        database=os.getenv('DB'),
        #connect_args={'sslmode':'require'}
        )
    
    engine = create_engine(connection_string)
    session = Session(engine)
    
    sql = (
        select(
            Cars.country,
            Cars.year,
            func.max(Engines.horse_power).label("max_horse_power"),
        )
        .join(Engines, Cars.engine_name == Engines.name)
        .where(Cars.country != 'USA')
        .group_by(Cars.country, Cars.year)
        .having(func.max(Engines.horse_power) > 200)
        .order_by(func.max(Engines.horse_power).label("max_horse_power").desc())
    )
    
    for i in session.execute(sql):
        print(i)
    
if __name__ == '__main__':
    main()