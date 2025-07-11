def get_list_info(lst):
    """Получение информации о списке
    :param lst: список из чисел
    :return: min_elem, max_elem, sum_list, average
    """
    # todo Здесь нужно написать код
    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = sum(lst)
    average = round((sum_list / len(lst)), 2)
    # сумма элементов, деленная на длину строки, с округлением до 2 знаков
    response = (min_elem, max_elem, sum_list, average)
    return response

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    (1, 7, 28, 4.0), (-7, -1, -28, -4.0), (-308, 209, 68, 9.71), (-3, 3, 0, 0.0)
]


for i, d in enumerate(data):
    assert get_list_info(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
