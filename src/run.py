"""Точка входа в программу"""

from prettytable import PrettyTable

from src.models import Book, Stock, Shop, Sale, Publisher
from src.query import create_table, add_data_in_table, view_sale_info

data_table = [
    [
        Shop(name='Буквоед'),
        Shop(name='Лабиринт'),
        Shop(name='Книжный дом')
    ],
    [
        Publisher(name='Пушкин'),
        Publisher(name='Толстой'),
        Publisher(name='Гоголь')
    ],
    [
        Book(title='Капитанская дочка', id_publisher=1),
        Book(title='Руслан и Людмила', id_publisher=1),
        Book(title='Евгений Онегин', id_publisher=1),
        Book(title='Война и мир', id_publisher=2),
        Book(title='Анна Каренина', id_publisher=2),
        Book(title='Кавказский пленник', id_publisher=2),
        Book(title='Нос', id_publisher=3),
        Book(title='Мёртвые души', id_publisher=3),
        Book(title='Шинель', id_publisher=3)
    ],
    [
        Stock(id_book=1, id_shop=1, count=24),
        Stock(id_book=2, id_shop=1, count=12),
        Stock(id_book=3, id_shop=1, count=12),
        Stock(id_book=4, id_shop=1, count=11),
        Stock(id_book=5, id_shop=1, count=9),
        Stock(id_book=6, id_shop=1, count=32),
        Stock(id_book=7, id_shop=1, count=2),
        Stock(id_book=8, id_shop=1, count=10),
        Stock(id_book=9, id_shop=1, count=12),
        Stock(id_book=1, id_shop=2, count=14),
        Stock(id_book=2, id_shop=2, count=12),
        Stock(id_book=3, id_shop=2, count=21),
        Stock(id_book=4, id_shop=2, count=9),
        Stock(id_book=5, id_shop=2, count=9),
        Stock(id_book=6, id_shop=2, count=12),
        Stock(id_book=7, id_shop=2, count=27),
        Stock(id_book=8, id_shop=2, count=19),
        Stock(id_book=9, id_shop=2, count=12),
        Stock(id_book=1, id_shop=3, count=25),
        Stock(id_book=2, id_shop=3, count=28),
        Stock(id_book=3, id_shop=3, count=32),
        Stock(id_book=4, id_shop=3, count=11),
        Stock(id_book=5, id_shop=3, count=5),
        Stock(id_book=6, id_shop=3, count=3),
        Stock(id_book=7, id_shop=3, count=24),
        Stock(id_book=8, id_shop=3, count=15),
        Stock(id_book=9, id_shop=3, count=16)
    ],
    [
        Sale(price=249.99, date_sale='2021-10-18', id_stock=1, count=13),
        Sale(price=102.00, date_sale='2022-09-06', id_stock=2, count=9),
        Sale(price=720.50, date_sale='2023-06-11', id_stock=3, count=2),
        Sale(price=530.90, date_sale='2024-10-22', id_stock=4, count=10),
        Sale(price=600.50, date_sale='2022-09-11', id_stock=5, count=5),
        Sale(price=420.50, date_sale='2023-09-18', id_stock=6, count=18),
        Sale(price=450.99, date_sale='2023-06-11', id_stock=7, count=2),
        Sale(price=749.99, date_sale='2024-10-06', id_stock=8, count=10),
        Sale(price=335.50, date_sale='2024-06-06', id_stock=9, count=5),
        Sale(price=230.00, date_sale='2022-05-18', id_stock=10, count=11),
        Sale(price=140.50, date_sale='2022-10-11', id_stock=11, count=10),
        Sale(price=680.00, date_sale='2022-12-27', id_stock=12, count=10),
        Sale(price=599.90, date_sale='2024-10-11', id_stock=13, count=8),
        Sale(price=489.50, date_sale='2023-09-18', id_stock=14, count=4),
        Sale(price=410.99, date_sale='2023-09-11', id_stock=15, count=9),
        Sale(price=468.50, date_sale='2024-12-11', id_stock=16, count=22),
        Sale(price=700.00, date_sale='2023-10-26', id_stock=17, count=12),
        Sale(price=370.50, date_sale='2024-10-11', id_stock=18, count=8),
        Sale(price=299.00, date_sale='2022-11-11', id_stock=19, count=22),
        Sale(price=179.99, date_sale='2022-10-27', id_stock=20, count=18),
        Sale(price=599.99, date_sale='2023-09-26', id_stock=21, count=30),
        Sale(price=659.50, date_sale='2023-06-11', id_stock=22, count=6),
        Sale(price=480.90, date_sale='2024-06-11', id_stock=23, count=2),
        Sale(price=419.99, date_sale='2022-05-11', id_stock=24, count=2),
        Sale(price=450.50, date_sale='2024-10-11', id_stock=25, count=12),
        Sale(price=900.50, date_sale='2023-11-19', id_stock=26, count=11),
        Sale(price=300.90, date_sale='2022-11-12', id_stock=27, count=7)
    ]
]

table = PrettyTable()
table.field_names = ['Название книги', 'Название магазина', 'Цена', 'Дата продажи']


# Главная функция для запуска программы
def main():
    # добавление таблиц
    create_table()

    # добавление данных в таблицу
    for data in data_table:
        add_data_in_table(data)

    # Показ таблицы продаж
    view_sale_info(table)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
