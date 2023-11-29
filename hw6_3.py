import random
max = 0
loop_count = 0
multiply =1

while True:
    try:
        n = int(input("Введите размер списка: "))
        if n >= 2: break
        else:
            print("Значение n больше или равно 2")
    except ValueError:
        continue

while True:
    zero_count = 0
    num_list = [random.randint(-10, 10) for i in range(n)]
    for i in num_list:
        if i == 0:
            zero_count += 1
    if zero_count >= 2:
        break

for i in range(len(num_list)):
    if num_list[i] == 0:
        for j in range(len(num_list)):
            if num_list[j] == 0 and i != j:
                for k in range(i + 1, j):
                    multiply *= num_list[k]
print(f"Результат умножения элементов списка между первым и последним вхождением нуля: {num_list[k]}")


for i in num_list:
    if i > max:
        max= i
index=num_list.index(max)+1
print(f"Исходный список: {num_list}")
print(f"Максимальное значение: {max}")
print(f"Номер максимального элемента списка: {index}")
