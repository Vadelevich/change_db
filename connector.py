import psycopg2
import json


connect = psycopg2.connect(host='localhost', database='Northwind Traders', user='postgres', password='1991')
with connect.cursor() as cursor:
    with open('suppliers.json') as file:
        suppliers = json.load(file)
        for supplier in suppliers:
            cursor.execute('INSERT INTO suppliers (company_name,contact,address,phone,fax,homepage ) VALUES (%s, %s, %s, %s, %s, %s)',(supplier["company_name"],supplier["contact"],supplier["address"], supplier["phone"],supplier["fax"],supplier["homepage"]))
            connect.commit()






