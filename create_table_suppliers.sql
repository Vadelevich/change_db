--Спроектировать таблицу suppliers и заполнить её данными из файла suppliers.json
CREATE TABLE IF NOT EXISTS suppliers(
  suppliers_id SERIAL PRIMARY KEY,
  company_name varchar NOT NULL,
  contact varchar NOT NULL,
  address text,
  phone varchar(50) NOT NUll,
  fax varchar(50),
  homepage text
);
--Добавить информацию о поставщике в таблицу с товарами
ALTER TABLE products ADD COLUMN IF NOT EXISTS suppliers_id int;
ALTER TABLE products ADD CONSTRAINT fk_products_suppliers_id FOREIGN KEY (suppliers_id) REFERENCES suppliers(suppliers_id);
