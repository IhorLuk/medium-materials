import csv
import boto3
import time

CSV_FILE = '../sql-data/nasdaq_data.csv'
TABLE_NAME = 'Nasdaq-code'

def main():
    
    db = boto3.client('dynamodb')
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        
        write_data = []
        for row in reader:
            write_row = {}       
            for k, v in row.items():
                # if value is number write it as this data type
                if v.isnumeric():
                    value = {'N': v}
                else:
                    value = {'S': v}
                    
                write_row[k.capitalize()] = value
            write_data.append(write_row)
            
            # if list is full for batching
            if len(write_data) == 25:
                # list comprehension for correct format
                write_data = [{'PutRequest': {'Item': i}} for i in write_data]
                
                # write data with this simple response
                response = db.batch_write_item(
                    RequestItems = {
                        TABLE_NAME: write_data,
                    }
                )
                
                write_data = []

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))