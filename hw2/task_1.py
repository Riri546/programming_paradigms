# Задача 1.

# Условие
# На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# Пример вывода:

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

def multiplication_table():
    for i in range(1, n+1):
        print(1, "*", i, "=", i)


n = int(input("Введите число N: "))
result = multiplication_table()
print(result)

# Здесь присутствует и процедурная и структурная парадигма
# Структурная парадигма, поскольку используется for и нет goto.
# Процедурная парадигма, поскольку код оформлен в виде процедуры multiplication_table().
