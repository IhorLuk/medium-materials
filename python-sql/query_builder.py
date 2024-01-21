import psycopg2
from dotenv import load_dotenv
import os

from pypika import Query, Table, functions, Order

def main():
    
    load_dotenv()

    conn = psycopg2.connect(
        dbname=os.getenv('DB'),
        port=os.getenv('PORT'),
        host=os.getenv('HOST'),
        user=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD')
    )
    cur = conn.cursor()
    
    cars = Table("cars")
    engines = Table("engines")
    
    query = (
        Query.from_(cars)
        .join(engines)
        .on(cars.engine_name == engines.name)
        .where(cars.country != "USA")
        .groupby(cars.country, cars.year)
        .having(functions.Max(engines.horse_power) > 200)
        .orderby(functions.Max(engines.horse_power), order=Order.desc)
        .select(
            cars.country,
            cars.year,
            functions.Max(engines.horse_power).as_("max_horse_power")
        )
    )
    
    sql = query.get_sql()
    
    cur.execute(sql)
    res = cur.fetchall()    
    print(res)
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()