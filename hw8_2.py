def RadToDeg(R):
    pi = 3.14
    deg = R * (180 / pi)
    return deg
try:
    n1 = float(input("Введите угол 1 в радианах:"))
    n2 = float(input("Введите угол 2 в радианах:"))
    n3 = float(input("Введите угол 3 в радианах:"))
    n4 = float(input("Введите угол 4 в радианах:"))
    n5 = float(input("Введите угол 5 в радианах:"))
    if 0<(n1 and n2 and n3 and n4 and n5)<2:
        deg1 = RadToDeg(n1)
        deg2 = RadToDeg(n2)
        deg3 = RadToDeg(n3)
        deg4 = RadToDeg(n4)
        deg5 = RadToDeg(n5)

        print("Угол 1 в градусах:" , deg1)
        print("Угол 2 в градусах:" , deg2)
        print("Угол 3 в градусах:" , deg3)
        print("Угол 4 в градусах:" , deg4)
        print("Угол 5 в градусах:" , deg5)
    else: print("Ошибка, угол в радианах больше нуля и меньше двух (нуль и двойка не включены)")
except Exception as a:
    print("Ошибка, введите число")
