"""Модуль содержит функции для запросов в базу данных"""

from typing import List

from prettytable import PrettyTable

from sqlalchemy import select, func, CursorResult
from sqlalchemy.orm import aliased

from src.models import Book, Shop, Sale, Stock, Publisher
from src.database import Base, engine, session_factory


def create_table() -> None:
    """Функция создаёт таблицы в базе данных"""

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def add_data_in_table(data: List) -> None:
    """Функция добавляет значения в таблицы"""

    with session_factory.begin() as session:
        session.add_all(data)


def get_sale_data(value: str) -> CursorResult:
    """
    Функция выполняет запрос в базу данных и возвращает
    информацию о проданных книгах
    """

    bk = aliased(Book)
    sh = aliased(Shop)
    sl = aliased(Sale)
    st = aliased(Stock)

    if any(character.isdigit() for character in value):
        subq = select(Publisher.id).where(Publisher.id == value).scalar_subquery()
    else:
        subq = select(Publisher.id).where(Publisher.name == value).scalar_subquery()

    query = select(
        bk.title.label("book_title"),
        sh.name.label("shop_name"),
        sl.price.label("sale_price"),
        sl.date_sale.label("date_sale")
    ).select_from(bk).join(st).join(sh).join(sl).where(bk.id_publisher == subq).order_by(bk.title)
    print(query)
    with session_factory() as session:
        data = session.execute(query)

    return data


def get_publisher_name(value: int) -> tuple:
    """
    Функция выполняет запрос в базу данных и возвращает
    имена авторов книг
    """

    name_query = select(Publisher.name).where(Publisher.id == value)
    with session_factory() as session:
        name_data = session.execute(name_query).one_or_none()
        return name_data[0]


def get_publisher_count() -> int:
    """
    Функция выполняет запрос в базу данных и возвращает
    информацию о количестве авторов
    """

    count_query = select(func.count()).select_from(Publisher)
    with session_factory() as session:
        count_data = session.execute(count_query).one_or_none()
        return count_data[0]


def view_sale_info(table: PrettyTable) -> None:
    """
    Функция в интерактивном режиме позволяет просмотреть
    информацию о проданных книгах выбранного автора
    """

    print('Вы можете получить информацию о продажах для следующих авторов:')

    for i in range(1, get_publisher_count() + 1):
        print(f'{i}. {get_publisher_name(i)}')

    input_data = input('Введите порядковый номер или имя автора:\n')

    for row in get_sale_data(input_data):
        table.add_row(row)

    print(table)
