# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_division_without_remainder():  # Простое деление
    assert all_division(30, 2) == 15


@pytest.mark.smoke
def test_multiple_fission():  # Множественное деление
    assert all_division(240, 3, 2, 5, 4) == 2


@pytest.mark.acceptance
def test_float_in_args():  # Вещественные числа в аргументах и результате
    assert all_division(10.88, 2) == 5.44


@pytest.mark.acceptance
def test_data_type():  # Проверяем в результате деления тип данных
    result = all_division(7, 2)
    assert isinstance(result, float)


@pytest.mark.acceptance
def test_one_arg():  # Штатная работа при получении 1 числа
    assert all_division(5) == 5


@pytest.mark.acceptance
def test_division_by_zero():  # Проверяем запрет деления на 0
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)
