"""
Корневой модуль для демонстрации работы проекта.
"""

from module2 import demo_circle_processing, demo_triangle_mapping


def showcase_demo():
    """
    Вызывает демонстрационные функции обработки кругов и треугольников.
    """
    print("Processing Circles:")
    print(demo_circle_processing())
    print("\nMapping Triangles:")
    print(demo_triangle_mapping())
