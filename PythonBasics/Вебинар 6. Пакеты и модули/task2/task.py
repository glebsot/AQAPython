# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    """Нелокальные изменения
    :return: msg
    """
    msg = 1

    def local_function():
        pass
        # todo Здесь нужно написать код
        nonlocal msg
        msg = 2

    local_function()
    return msg


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
