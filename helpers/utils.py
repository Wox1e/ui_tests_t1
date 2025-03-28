"""Вспомогательный модуль с функциями общего назначения"""
import random


def generate_str_digit(lenght: int) -> str:
    """Возвращает случайное число длинной lenght в виде строки"""
    digit = ""
    for _ in range(lenght):
        digit += str(random.randint(0, 10))
    return digit


def code_to_letter(code: int) -> str:
    """ Превращает код в букву на основе:\n
        0 -> a 
        ... 
        25 -> z
        26 -> a
        ...
    """
    if code > 25:
        code = code % 26
    offset_from_ascii = 97
    return chr(code + offset_from_ascii)


def average_str_len(l: list[str]) -> int:
    """Возвращает среднюю длину строки в списке"""
    sum_len = 0
    for el in l:
        sum_len += len(el)
    return int(sum_len / len(l))


def find_closest_el_by_len(l: list, target_len: int) -> str:
    """Находит строку в листе в длиной максимально приближенной к target_len"""
    closest = l[0]
    min_closure = len(closest)
    for i in range(1, len(l)):
        current_el = l[i]
        current_closure = abs(target_len - len(current_el))
        if current_closure < min_closure:
            closest = current_el
            min_closure = current_closure

    return closest

