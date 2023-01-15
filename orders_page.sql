--Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)

SELECT * FROM orders
ORDER BY required_date DESC, shipped_date;

--Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA

SELECT AVG (shipped_date - order_date) FROM orders
WHERE ship_country = 'USA';

--Найти сумму, на которую имеется товаров (количество * цену) причём таких, которые не сняты с продажи (см. на поле discontinued)


SELECT SUM (unit_price * quantity) FROM order_details
WHERE discount != 0;
