import math
def expression(a, b):
    return math.sqrt(a**2 + b**2 + math.sin(a*b)**2)
try:
    def s():
        x = float(input("Введите значение x: "))
        y = float(input("Введите значение y: "))
        z = float(input("Введите значение z: "))
        result = expression(x, y) + expression(x, z) + expression(y, z)
        print("Результат вычисления выражения S:", result)
    s()
except Exception as a:
    print("Ошибка, введите число")




