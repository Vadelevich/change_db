<div align="center">
  <img src="https://media.giphy.com/media/l46Cy1rHbQ92uuLXa/giphy.gif" width="600" height="300"/>
</div>
### :woman_technologist: About Me :
I am a Python Developer <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30"> from Belarus.

- :telescope: I’m study as a Software Engineer and contributing to frontend and backend for building web applications.

- :seedling: Exploring Technical Content Writing.

- :zap: In my free time, I solve problems on GeeksforGeeks and read tech articles.
- ---

### :hammer_and_wrench: Languages and Tools used in the project :
<div>
  <img src ="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/java/java-original-wordmark.svg" title="Java" alt="Java" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="Postgresql"  alt="Postgresql" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-plain-wordmark.svg" title="Pycharm" alt="Pycharm" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" title="Git" **alt="Git" width="40" height="40"/>
</div>
- - ---

### :hammer_and_wrench: Project Description::

### :writing_hand: Нам предстоит работать с базой данных компании Northwind Traders. База данных фиксирует все транзакции продаж и поставки товаров, производимых компанией, своим клиентам.

### :fire: БД содержит следующую подробную информацию:

1. Клиенты Northwind Traders, которые покупают у компании товары (таблица *customers*)
2. Информация о товарах, которыми торгует компания (таблица *products*)
3. Группы / категории товаров (таблица *categories*)
4. Сведения о сотрудниках Northwind Traders (таблица *employees*)
5. Сведения о грузоперевозчиках, которые доставляют товары конечным покупателям (таблица *shippers*)
6. Сведения по договорам / заказам (таблица *orders*)
7. Детальная информация по договорам / заказам (таблица *order_details*)
- - ---
### :woman_technologist: Task :
1. Создать БД и залить в неё данных с помощью скрипта fill_db.sql
2. Спроектировать таблицу suppliers и заполнить её данными из файла suppliers.json
3. Добавить информацию о поставщике в таблицу с товарами
4. Написать SQL-запросы для выборки данных для страниц внутреннего портала Northwind Traders
5. Реализовать модуль для получения данных о продуктах из БД на языке Python
- - ---
**SQL-запросы для портала**

1. Страница «Заказчики» (customers_page.sql)
    - Посчитать количество заказчиков
    - Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики
    - Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
    - Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
2. Страница «Заказы» (orders_page.sql)
    - Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
    - Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
    - Найти сумму, на которую имеется товаров (количество * цену) причём таких, которые не сняты с продажи (см. на поле discontinued)
3. Страница «Сотрудники» (employees_page.sql)
    - Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен
    - Выбрать такие страны в которых "зарегистированы" одновременно заказчики и поставщики, но при этом в них не "зарегистрированы" работники
4. Страница «Товары» (products_page.sql)
    - Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.


- - ---
**Модуль для работы с БД**

Модуль содержит две функции (get_product_by_id,get_category_by_id), которые вызываются, когда пользователь запрашивает данные по продукту и данные по категории продуктов. Функции принимают словарь с данными для подключения к БД и id запрашиваемого объекта.
Функции возвращают данные в виде json-строки.

При запросе данных по id **продукта**, json-строка содержит следующую информацию:

- id продукта
- наименование продукта
- наименование категории продукта
- цену продукта

При запросе данных по id **категории**, json-строка содержит ледующую информацию:

- id категории
- наименование категории
- описание категории
- список продуктов, относящихся к этой категории
