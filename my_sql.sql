--Спроектировать таблицу suppliers и заполнить её данными из файла suppliers.json
CREATE TABLE suppliers(
	company_name varchar NOT NULL,
	contact varchar NOT NULL,
	address text,
	phone varchar(50) NOT NUll,
	fax varchar(50),
	homepage text,
	suppliers_id int UNIQUE NOT NULL GENERATED ALWAYS AS IDENTITY,

	CONSTRAINT pk_suppliers_suppliers_id PRIMARY KEY (suppliers_id)

);
--Добавить информацию о поставщике в таблицу с товарами
ALTER TABLE products ADD COLUMN suppliers_id int
ALTER TABLE products ADD CONSTRAINT fk_products_suppliers_id FOREIGN KEY (suppliers_id) REFERENCES suppliers(suppliers_id)