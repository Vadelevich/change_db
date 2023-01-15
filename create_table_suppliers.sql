--Удаляем столбик и табличку если существует

ALTER TABLE products DROP COLUMN IF EXISTS suppliers_id;
DROP TABLE IF EXISTS suppliers;

--Спроектировать таблицу suppliers
CREATE TABLE IF NOT EXISTS suppliers(
  suppliers_id SERIAL PRIMARY KEY,
  company_name varchar NOT NULL,
  contact varchar NOT NULL,
  country varchar(50),
  region varchar(50) DEFAULT NULL,
  postal_code varchar(50) DEFAULT NULL,
  city varchar(50),
  address text,
  phone varchar(50) NOT NUll,
  fax varchar(50),
  homepage text
);
--Добавить колонку о поставщике в таблицу с товарами
ALTER TABLE products ADD COLUMN IF NOT EXISTS suppliers_id int;
-- Связываем  две таблицы : products (suppliers_id) с suppliers(suppliers_id)
ALTER TABLE products ADD CONSTRAINT fk_products_suppliers_id FOREIGN KEY (suppliers_id) REFERENCES suppliers(suppliers_id);
