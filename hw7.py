import random

try:
    n = int(input("Введите размер списка: "))
    if n >0:
        matrix = []
        for x in range(n):
            row = []
            for x in range(n):
                value = random.randint(1, 100)
                row.append(value)
            matrix.append(row)

        print("Исходный список:")
        for row in matrix:
            print(row)

        for i in range(len(matrix)):
            j = len(matrix) - 1 - i
            matrix[i][i], matrix[i][j] = matrix[i][j], matrix[i][i]
        print("Список после замены элементов в диагоналях:")
        for row in matrix:
            print(row)
    else: print("Введите n больше нуля")

except Exception as a:
    print("Ошибка, введите целое число ")


