import psycopg2
from psycopg2 import OperationalError
from filling_tables import filling_tables

db = {
    'host': 'localhost',
    'database': 'Northwind Traders',
    'user': 'postgres',
    'password': '1991',
    'port': '5432'
}


def create_connection(db):
    """ Функция установки соединения с БД"""
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
    except OperationalError as e:     # Здесь будем ловить все ошибки связанные с подключением к БД
        print(f"The error '{e}' occurred")
    return connection



def create_table_suppliers(connect, file):
    """ Функция удаляет старую и создает новую таблицу suppliers , скрипты в файлике create_table_suppliers.sql """
    with connect.cursor() as cursor:
        with open(f'{file}') as file:
            request = file.read()
            cursor.execute(request)


def get_product_by_id(config, id):
    """ Функция возвращает id продукта, наименование продукта, наименование категории продукта, цену продукта по указанному ID """
    connection = create_connection(config)
    request = f'SELECT product_id,product_name,categories.category_name,unit_price ' \
              f'FROM products INNER JOIN categories USING(category_id) ' \
              f'WHERE product_id = {id}'
    with connection.cursor() as cursor:
        cursor.execute(request)
        rows = cursor.fetchall()
        for row in rows:
            return print(
                f' id продукта : {row[0]}, наименование продукта : {row[1]}, наименование категории продукта : {row[2]}, ценa продукта : {row[3]}')


def get_category_by_id(config, id):
    """Функция возвращает  id категории, наименование категории, описание категории, список продуктов, относящихся к этой категории  по указан ID"""
    products = list()
    connection = create_connection(config)
    request = f'SELECT categories.category_id,categories.category_name,categories.description, product_name ' \
              f'FROM products INNER JOIN categories USING (category_id) ' \
              f'WHERE category_id = {id}'
    with connection.cursor() as cursor:
        cursor.execute(request)
        rows = cursor.fetchall()
        for row in rows:
            products.append(row[3])

        return print(
            f' id категории : {row[0]}, наименование категории : {row[1]}, описание категории : {row[2]}, список продуктов, относящихся к этой категории: {products}')


if __name__ == "__main__":
    connect = create_connection(db)
    create_table_suppliers(connect, 'create_table_suppliers.sql')
    filling_tables(connect, 'suppliers.json')
    get_product_by_id(db, 8)
    get_category_by_id(db, 1)
