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
    word1 = ''
    word2 = ''
    for i in range(random.randint(1, 15)):
        word1 += chr(random.randint(97, 122))
    for i in range(random.randint(1, 15)):
        word2 += chr(random.randint(97, 122))
    yield f'{word1} {word2}'


print(next(generate_random_name()))
