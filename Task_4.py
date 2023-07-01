"""
Задание №9
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
"""
min = 2
max = 11
count = 1
for i in range(min, max):
    for j in range(min, max):
        z = j * i
        if count < 9:
            print(f"{i} * {j} = {z}")
    count += 1
    print()
