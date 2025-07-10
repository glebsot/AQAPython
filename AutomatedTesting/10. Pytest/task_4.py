# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
from task_3 import all_division


class TestAllDivision:
    @pytest.mark.smoke
    def test_division_without_remainder(self):  # Простое деление
        assert all_division(30, 2) == 15

    @pytest.mark.smoke
    def test_multiple_fission(self):  # Множественное деление
        assert all_division(240, 3, 2, 5, 4) == 2

    @pytest.mark.acceptance
    def test_float_in_args(self, start_stop_time_method):  # Вещественные числа в аргументах и результате
        assert all_division(10.88, 2) == 5.44

    @pytest.mark.acceptance
    def test_data_type(self):  # Проверяем в результате деления тип данных
        result = all_division(7, 2)
        assert isinstance(result, float)

    @pytest.mark.acceptance
    def test_one_arg(self):  # Штатная работа при получении 1 числа
        assert all_division(5) == 5

    @pytest.mark.acceptance
    def test_division_by_zero(self):  # Проверяем запрет деления на 0
        with pytest.raises(ZeroDivisionError):
            all_division(10, 0)
