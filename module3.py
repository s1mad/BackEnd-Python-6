"""
Модуль, содержащий функции для работы со списками и словарями объектов data-классов.
"""

from module4 import process_circle


def process_circles(circles):
    """
    Обрабатывает список объектов Circle, вычисляя их площади.
    """
    return [process_circle(circle) for circle in circles]


def map_triangles_to_angles(triangle_list):
    """
    Создаёт словарь треугольников с углами в качестве ключей.
    """
    return {triangle.angle: triangle for triangle in triangle_list}
