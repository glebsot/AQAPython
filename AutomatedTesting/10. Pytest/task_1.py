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
    while True:  # True для бесконечного цикла
        final_list = []  # Создаем список для хранения сгенерированных слов
        word1 = ''.join(chr(random.randint(97, 122)) for i in range(random.randint(1, 15)))
        # chr(random.randint(97, 122) рандомно выбирает букву из диапазона, join добавляет их в строку.
        # Длина определяется через for i in range(random.randint(1, 15))
        word2 = ''.join(chr(random.randint(97, 122)) for i in range(random.randint(1, 15)))
        yield f'{word1} {word2}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
