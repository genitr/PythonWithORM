"""Основные параметры базы данных"""

import os
from typing import Annotated

from dotenv import load_dotenv, find_dotenv

from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column

load_dotenv(find_dotenv())

DSN = os.getenv('POSTGRES_URL')

engine = create_engine(DSN, echo=False)
session_factory = sessionmaker(engine)

# анотация типов для подстановки в модели
int_pkey = Annotated[int, mapped_column(primary_key=True)]
str_40 = Annotated[str, 40]


class Base(DeclarativeBase):
    """Родительский класс для всех моделей"""
    type_annotation_map = {
        str_40: String(40),
    }
