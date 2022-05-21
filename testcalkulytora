import pytest
from calculator import *

number1 = 2
number2 = 4

def test_add():
    assert calculate(number1, '+', number2) == 6, f"ОШИБКА: ===== проверки сложения {number1} и {number2} ====="


def test_subtract():
    assert calculate(number1, '-', number2) == -2, f"ОШИБКА: ===== проверки вычитания {number1} и {number2} ====="


def test_division2():
    if number1 == 0 and operation == '/' or number2 == 0 and operation == '/':
        print('Деление на 0')
    else:
        assert calculate(number1, '/', number2) == 0.5, f"ОШИБКА: ===== проверки деления {number1} и {number2} ====="


def test_multiply():
    assert calculate(number1, '*', number2) == 8, f"ОШИБКА: ====== проверки умножения {number1} и {number2} ======="


def test_square():
    assert calculate(number1, '^', number2) == 16, f"ОШИБКА: ====== проверки возведения в cтепень ======"
