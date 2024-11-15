"""
Модуль, демонстрирующий обработку списков и словарей data-классов.
"""
from decimal import Decimal

from module3 import process_circles, map_triangles_to_angles
from module4 import Circle, Triangle


def demo_circle_processing():
    """
    Демонстрация обработки списка кругов.
    """
    circles = [Circle(radius=Decimal(5)),
               Circle(radius=Decimal(10)),
               Circle(radius=Decimal(15))]
    return process_circles(circles)


def demo_triangle_mapping():
    """
    Демонстрация создания словаря треугольников.

    Возвращает:
        dict: Словарь треугольников.
    """
    triangles = [Triangle(angle=Decimal(30)),
                 Triangle(angle=Decimal(60)),
                 Triangle(angle=Decimal(90))]
    return map_triangles_to_angles(triangles)
