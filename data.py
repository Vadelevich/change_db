import psycopg2
from psycopg2 import OperationalError


db = {
    'host': 'localhost',
    'database' : 'Northwind Traders',
    'user' : 'postgres',
    'password' :'1991',
    'port' : '5432'
}

def create_connection(db):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db.get('database'),
            user=db.get('user'),
            password=db.get('password'),
            host=db.get('host'),
            port=db.get('port'),
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def get_product_by_id(config, id):
    connection = create_connection(config)
    request = 'SELECT * FROM products WHERE product_id = ' + str(id)
    with connection.cursor() as cursor:
        cursor.execute(request)
        rows = cursor.fetchall()
        return print(rows)
        # for row in rows:
        #     if row[0] == id:
        #         return print(row)



def get_category_by_id(config, id):
    pass



get_product_by_id(db,5)