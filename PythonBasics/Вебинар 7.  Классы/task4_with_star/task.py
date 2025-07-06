# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

class RomanNums:
    def __init__(self, roman_num):
        self.arab_num = 0
        self.roman_num = roman_num

    def from_roman(self):
        """Перевод римской записи числа в арабскую"""
        # todo Здесь нужно написать код
        num = [1000, 500, 100, 50, 10, 5, 1]
        r_num = ["M", "D", "C", "L", "X", "V", "I"]
        roman_num_list = [self.roman_num[i] for i in range(len(self.roman_num))]
        # получение списка римских цифр из строки
        circle = 0  # считаем номер цифры из числа
        for i in roman_num_list:  # перебираем список римских цифр
            roman_num_list[circle] = num[r_num.index(i)]  # заменяем их на арабские числа
            circle += 1
        circle = 0
        for i in range(len(self.roman_num) - 1):  # проходимся по числам списка, кроме последнего
            if roman_num_list[circle] >= roman_num_list[circle + 1]:
                # если число больше или равно следующему за ним, прибавляем
                self.arab_num += roman_num_list[circle]
                circle += 1
            elif roman_num_list[circle] < roman_num_list[circle + 1]:  # если меньше, вычитаем
                self.arab_num -= roman_num_list[circle]
                circle += 1
        self.arab_num += roman_num_list[circle]  # складываем общее число с последним безусловно
        return self.arab_num

    def is_palindrome(self):
        """Является ли число палиндромом """
        # todo Здесь нужно написать код
        self.from_roman()
        arab_str = str(self.arab_num)
        return arab_str == arab_str[::-1]

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]


test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')