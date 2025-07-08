# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
def generate_random_name():
    final_list = []
    iteration = 0
    while iteration < 2:
        word = ''
        for i in range(random.randint(1, 15)):
            word += chr(random.randint(97, 122))
        final_list.append(word)
        iteration += 1
    yield f'{final_list[0]} {final_list[1]}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
