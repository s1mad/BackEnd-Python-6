"""
Модуль, содержащий функции работы с random и decimal.
"""

import random
from decimal import Decimal


def random_choice_demo():
    """
    Выбирает случайный элемент из списка строк.
    """
    return random.choice(["Apple", "Banana", "Cherry"])


def random_uniform_demo():
    """
    Генерирует случайное число с плавающей запятой в диапазоне от 1 до 10.
    """
    return random.uniform(1, 10)


def decimal_operations():
    """
    Выполняет операции деления и умножения с использованием Decimal.
    """
    d1 = Decimal("10.5")
    d2 = Decimal("3.2")
    return d1 / d2, d1 * d2
