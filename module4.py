"""
Модуль, содержащий data-классы и функции для работы с ними.
"""

from dataclasses import dataclass
from decimal import Decimal

from module5 import calculate_circle_area


@dataclass
class Circle:
    """
    Представление круга.
    """
    radius: Decimal


@dataclass
class Logarithm:
    """
    Представление логарифма с основанием и значением.
    """
    base: int
    value: int


@dataclass
class Triangle:
    """
    Представление треугольника с углом.
    """
    angle: Decimal


def process_circle(circle):
    """
    Вычисляет площадь круга, переданного как объект Circle.
    """
    return calculate_circle_area(circle.radius)


def create_triangle(angle):
    """
    Создаёт объект треугольника на основе переданного угла.
    """
    return Triangle(angle)


def modify_logarithm(log_obj, new_value):
    """
    Изменяет значение в объекте логарифма.
    """
    log_obj.value = new_value
    return log_obj
