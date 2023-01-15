--Посчитать количество заказчиков

SELECT COUNT(1) FROM customers

--Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики

SELECT DISTINCT city, country FROM customers

--Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.

SELECT customers.company_name,CONCAT(employees.first_name, ' ', employees.last_name) as FIO
FROM orders
INNER JOIN employees USING (employee_id)
INNER JOIN customers USING (customer_id)
WHERE customers.city = 'London' and employees.city = 'London'and ship_via = 1


--Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
