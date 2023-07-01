"""
Задание №7
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
"""

def main():
    number = 0
    len_num = 0
    msg = None
    min = 1
    max = 999
    while number < min or number > max:
        num = num_input()
        len_num = len(num)
        number = int(num)
    if number >= min and number <= max:
        if len_num == 1:
            msg = one_lenght(number)
        elif len_num == 2:
            msg = two_lenght(number)
        elif len_num == 3:
            msg = three_lenght(str(number))
    go_to_print(msg)

def num_input():
    n = input("Введите число от 1 до 999: ")
    return n

def go_to_print(msg: str):
    print(msg)

def one_lenght(num: int) -> str:
    x = num * num
    msg = f"Это цифра! Её квадрат = {x}"
    return msg

def two_lenght(num: int) ->str:
    x = num // 10
    y = num % 10
    z = x + y
    msg = f"Это двузначное число! Составное произведение = {z}"
    return msg

def three_lenght(num: str) -> str:
    x = int(num[::-1])
    msg = f"Это трехзначное число! Зеркальное значение = {x}"
    return msg


if __name__ == '__main__':
    main()
