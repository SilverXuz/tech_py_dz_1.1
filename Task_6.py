"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
a = 0
while a < 1 or a > 100000:
    a = int(input("Введите число от 1 до 100000: "))

is_prime = True

if a == 1:
    is_prime = False
else:
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Число {a} - простое!")
else:
    print(f"Число {a} - составное!")
