def is_power_of_two(n):
    if n == 1:
        return "YES"
    elif n % 2 != 0:
        return "NO"
    else:
        return is_power_of_two(n // 2)
try:
    n = int(input("Введите число n:"))
    if n>0:
        result = is_power_of_two(n)
        print(result)
    else:
        print("Ошибка, введите натуральное число")
except Exception as a:
    print("Ошибка, введите число")


