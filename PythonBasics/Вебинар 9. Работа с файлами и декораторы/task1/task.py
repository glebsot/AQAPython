# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

# todo Здесь нужно написать код
with open('test_file/task1_answer.txt', 'a', encoding='utf-8') as answer_out, \
        open('test_file/task1_data.txt', 'r', encoding='utf-8') as data_in:
    # Открываем оба файла с защитой от ошибок
    for line in data_in:  # Перебираем строки файла
        for char in line:  # Перебираем символы строки
            if not char.isdigit():  # Если не число - записываем в новый файл
                answer_out.write(char)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')

