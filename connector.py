import psycopg2
import json


products_suppliers = dict()

connect = psycopg2.connect(host='localhost', database='Northwind Traders', user='postgres', password='1991')
with connect.cursor() as cursor:
    with open('suppliers.json') as file:
        suppliers = json.load(file)
        for supplier in suppliers:
            cursor.execute('INSERT INTO suppliers (company_name,contact,address,phone,fax,homepage ) VALUES (%s, %s, %s, %s, %s, %s)  RETURNING suppliers_id',(supplier["company_name"],supplier["contact"],supplier["address"], supplier["phone"],supplier["fax"],supplier["homepage"]))
            id_of_new_row = cursor.fetchone()[0]
            connect.commit()
            for product in supplier["products"]:
                products_suppliers[product] = id_of_new_row
        big_sql_row =''
        for i,v in products_suppliers.items():
            name = i
            name = name.replace("'", "''")
            big_sql_row += f"UPDATE products SET suppliers_id = {v} WHERE product_name = '{name}';"
        print(big_sql_row)
        cursor.execute(big_sql_row)
        connect.commit()








