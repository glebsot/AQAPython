# Дана функция hello_world.
# Внутри этой функции:
#
# Создайте переменную hello со значением 'Hello';
# создайте переменную world со значением 'world';
# в переменную hello_and_world запишите сумму переменных
# hello и world через пробел и в конце добавьте восклицательный знак.


def hello_world():

    # todo Здесь нужно написать код
    hello, world = 'Hello', 'world'
    hello_and_world = f"{hello} {world}!"
    # hello_and_world = hello + ' ' + world + "!"
    return hello_and_world


