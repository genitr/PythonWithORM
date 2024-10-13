"""Модели таблиц базы данных"""

from datetime import date

from sqlalchemy import ForeignKey, Numeric, text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, int_pkey, str_40


class Shop(Base):
    """Модель магазина"""
    __tablename__ = 'shop'

    id: Mapped[int_pkey]
    name: Mapped[str_40]


class Publisher(Base):
    """Модель издателя"""
    __tablename__ = 'publisher'

    id: Mapped[int_pkey]
    name: Mapped[str_40]


class Book(Base):
    """Модель книги"""
    __tablename__ = 'book'

    id: Mapped[int_pkey]
    title: Mapped[str_40]
    id_publisher: Mapped[int] = mapped_column(ForeignKey('publisher.id'))


class Stock(Base):
    """Модель склада"""
    __tablename__ = 'stock'

    id: Mapped[int_pkey]
    id_book: Mapped[int] = mapped_column(ForeignKey('book.id'))
    id_shop: Mapped[int] = mapped_column(ForeignKey('shop.id'))
    count: Mapped[int]

    __table_args__ = (
        CheckConstraint("count >= 0", name="check_stock_count_positive"),
    )


class Sale(Base):
    """Модель продажи"""
    __tablename__ = 'sale'

    id: Mapped[int_pkey]
    price: Mapped[float] = mapped_column(Numeric(7, 2), server_default=text('0.0'))
    date_sale: Mapped[date] = mapped_column(server_default=text('now()'))
    id_stock: Mapped[int] = mapped_column(ForeignKey('stock.id'))
    count: Mapped[int]

    __table_args__ = (
        CheckConstraint("count >= 0", name="check_sale_count_positive"),
        CheckConstraint('price >= 0', name='check_sale_price_positive')
    )
