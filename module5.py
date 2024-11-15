"""
Модуль, содержащий функции работы с math.
"""

import math


def calculate_circle_area(radius):
    """
    Вычисляет площадь круга по радиусу.
    """
    return math.pi * math.pow(radius, 2)


def calculate_logarithm(base, value):
    """
    Вычисляет логарифм числа по заданному основанию.
    """
    return math.log(value, base)


def advanced_trigonometry(angle):
    """
    Вычисляет синус, косинус и тангенс угла.
    """
    return math.sin(angle), math.cos(angle), math.tan(angle)
