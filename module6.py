"""
Модуль, содержащий функции работы с locale.
"""

import locale

from module7 import random_uniform_demo


def format_currency(value):
    """
    Форматирует число как валюту в соответствии с текущей локалью.
    """
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(value, grouping=True)


def locale_numeric_demo():
    """
    Форматирует число с использованием разделителя тысяч в соответствии с локалью.
    """
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%d", 1234567, grouping=True)


def combine_random_and_locale():
    """
    Генерирует случайное число и форматирует его как валюту.
    """
    value = random_uniform_demo()
    return format_currency(value)
