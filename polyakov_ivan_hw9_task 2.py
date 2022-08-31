"""Задача 1. 50 баллов
Написать функцию которая будет добавлять код страны
к номеру телефона с помощью замыкания
внешний вид вызова функции."""

def user_telephone(code_country):
    def phone(number):
        return code_country + number
    return phone

my_number = user_telephone("+044")
print(my_number('838372893'))