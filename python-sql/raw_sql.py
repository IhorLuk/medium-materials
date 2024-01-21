import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path

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
    
    sql = Path('python-sql/sql/max_horsepower.sql').read_text()
    
    cur.execute(sql)
    res = cur.fetchall()
    print(res)
    
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    main()