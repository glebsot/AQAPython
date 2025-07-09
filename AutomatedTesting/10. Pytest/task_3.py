# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните
import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, result',
                         [
                             pytest.param((30, 2), 15, marks=pytest.mark.smoke),
                             pytest.param((240, 3, 2, 5, 4), 2, marks=pytest.mark.smoke),
                             ((10.88, 2), 5.44),
                             pytest.param((7, 2), float, marks=pytest.mark.skip('Тип данных может отличаться')),
                             ((5, ), 5),
                             pytest.param((10, 0), pytest.raises(ZeroDivisionError),
                                          marks=pytest.mark.skip('Проще скипнуть чем проверить'))
                         ],
                         ids=[
                             "smoke test_division_without_remainder",
                             "smoke test_multiple_fission",
                             "test_float_in_args",
                             "test_data_type",
                             "test_one_arg",
                             "test_division_by_zero"
                         ])
def test_all_division(a, result):
    assert all_division(*a) == result
