"""
 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
import random

attempts = 10
LOWER_LIMIT= 1
UPPER_LIMIT = 1000
random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
print("Загадано случайное число от 1 до 1000. Попробуйте угадать!")
# print("Вывод числа для проверки кода", random_number)

while attempts > 0:
    x = 0
    while not 1 <= x <= 1000:
        x = int(input("Введите число от 1 до 1000: "))
    if x == random_number:
        print("Бинго! Вы угадали число!")
        break
    elif x < random_number:
        print("Загаданное число > больше вашего")
    elif x > random_number:
        print("Загаданное число < меньше вашего")
    attempts -= 1
    print(f"Осталось {attempts} попыток")
    if attempts == 0:
        print(f"Вы исчерпали все попытки, но так и не угадали число. Правильный ответ - {random_number}")
        break
