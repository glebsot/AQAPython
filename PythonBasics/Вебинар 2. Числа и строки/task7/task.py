# Даны две строки из неповторяющихся символов first_string и second_string. Первая строка first_string длиной 3
# символа. Вторая строка second_string точно содержит символы первой строки в любом порядке. Внутри функции
# minimum_length_slice напишите код - без использования циклов и условий, который находит срез минимальной длины во
# второй строке, содержащий все символы первой строки.
#
# Входные данные:
#
# строка first_string - строка длиной 3 символа
# Например, first_string='wtf'
# строка second_string - содержит символы первой строки в любом порядке
# Например, second_string='brick quz jmpy veldt whangs fox'
# Символы первой строки здесь - 'brick quz jmpy veldt whangs fox'
# Выходные данные:
#
# строка min_slice - срез минимальной длины во второй строке second_string, содержащий все символы первой строки
# first_string. Например, min_slice='t whangs f'


def minimum_length_slice(first_string, second_string):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    # todo Здесь нужно написать код
    # one, two, three = first_string[0], first_string[1], first_string[2]
    one, two, three = first_string
    # задал переменным значения букв из строки 1
    kor_list = second_string.find(one), second_string.find(two), second_string.find(three)
    # получил список с индексами знаков в строке
    min_kor, max_kor = min(kor_list), max(kor_list)
    # получил минимальное и максимальное значения списка
    min_slice = second_string[min_kor:max_kor + 1]
    # получил срез от мин до макс значения
    return min_slice
