# Дан файл test_file/task_2.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    # todo Здесь нужно написать код
    with open('test_file/task_2.txt', 'r', encoding='utf-8') as purchases:  # Открываем файл в purchases
        line_list = [i.strip() for i in purchases]  # Пишем в переменную словарь со всеми значениями построчно
        new_list = []  # Пустой словарь под суммы покупок
        sum_purchase = 0  # Сумма покупок
        for i in line_list:  # Итерируемся по всем значениям словаря со строчками из файла
            if i.isdigit():  # Если число, то складываем в общую сумму покупок
                sum_purchase += int(i)
            else:  # Если не число, значит дошли до пустой строки.
                # Записываем значение в новый словарь и начинаем считать сумму следующей покупки
                new_list.append(int(sum_purchase))
                sum_purchase = 0  # Обнуляем для следующей итерации

        # new_list_sorted = sorted(new_list, reverse=True) - решил не усложнять ещё одной переменной
        new_list.sort()  # Сортируем список покупок
        most_expensive_purchases = sum(new_list[-3:])  # Суммируем срез из 3 последних, т.е. самых дорогих

    return most_expensive_purchases


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
assert three_most_expensive_purchases() == 202346
