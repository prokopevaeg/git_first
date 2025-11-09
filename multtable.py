print('Таблица умножения'.upper(), end='\n\n')
num = int(input("Введите число для таблицы умножения: "))
print()
print(f"Таблица умножения для числа {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")