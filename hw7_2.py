import random
matrix = []
try:
    m = int(input("Введите количество строк: "))
    n = int(input("Введите количество столбцов: "))
    if m>0 and n>0:
        matrix=[]

        for i in range(m):
            row = []
            for j in range(n):
                element = random.randint(1, 100)
                row.append(element)
            matrix.append(row)

        max_elements = []
        for i in range(len(matrix)):
            max_element = max(matrix[i])
            max_elements.append((max_element, i, matrix[i].index(max_element)))

        min_max_element = min(max_elements, key=lambda x: x[0])

        print("Исходный список:")
        for row in matrix:
            print(row)
        print("Минимальный элемент среди максимальных элементов строк:", min_max_element[0])
        print("Индекс строки: ", min_max_element[1]+1)
        print("Индекс столбца:", min_max_element[2]+1)
    else:
        print("Введите m и n больше нуля")



except Exception as a:
    print("Ошибка, введите целое число")


