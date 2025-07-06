# Дан абсолютный путь до файла file_path.
# Внутри функции test_file_path напишите код, который:
#
# в переменной file_name вычисляет название файла без расширения;
# в переменной disk_name вычисляет название диска;
# в переменной root_folder вычисляет корневую папку.
# Входные данные:
#
# строка file_path - абсолютный путь до файла
# Например, file_path=r'C:\Python311\python.exe'
# Выходные данные:
#
# file_name - название файла без расширения
# Например, file_name='python'
# disk_name - название диска
# Например, disk_name='C'
#
# root_folder - корневая папка
# Например, root_folder='Python311'


def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, названия диска и корневую папку
    """
    # todo Здесь нужно написать код
    tochka, slash = file_path.rfind('.', 0), file_path.rfind('\\', 0)
    # с конца строки нашёл индекс указанного символа
    file_name = file_path[slash + 1:tochka]  # срез от \ до .
    colon = file_path.find(':')  # индекс двоеточия
    disk_name = file_path[:colon]  # диск это весь текст до двоеточия
    path_list = file_path.split('\\')  # поделил строку через разделитель
    root_folder = path_list[1]  # получил 2-й из списка элемент
    return file_name, disk_name, root_folder
