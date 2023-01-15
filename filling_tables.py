import json

products_suppliers = dict()   # { product_name : supplier_id}

def filling_tables(connect,file):
    """ Функция заполняет новыми данными таблицу suppliers из файла  и добавляет suppliers_id в products"""
    with connect.cursor() as cursor:
        with open(f'{file}') as file:
            suppliers = json.load(file)
            for supplier in suppliers:
                new_address = supplier["address"].split(';')     # Создаем список из "address", будем делать разные колонки (country,region,postal_code,city,address)
                cursor.execute('INSERT INTO suppliers (company_name,contact,country,region,postal_code,city,address,phone,fax,homepage ) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)  RETURNING suppliers_id',(supplier["company_name"],supplier["contact"],new_address[0],new_address[1],new_address[2],new_address[3],new_address[4], supplier["phone"],supplier["fax"],supplier["homepage"]))
                id_of_new_row = cursor.fetchone()[0]     # Получаем назад supplier_id
                for product in supplier["products"]:     # Делаем словарик product_name : supplier_id
                    products_suppliers[product] = id_of_new_row
            big_sql_row =''                         # Делаем один большой запрос (обновляем базу)
            for i,v in products_suppliers.items():
                name = i
                name = name.replace("'", "''")       # В запросе есть строки с " ' ", заменяем или будет ошибка
                big_sql_row += f"UPDATE products SET suppliers_id = {v} WHERE product_name = '{name}';"
            cursor.execute(big_sql_row)
            connect.commit()








