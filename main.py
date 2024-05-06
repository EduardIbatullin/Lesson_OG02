# main.py

import math_calc

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '1':
    print("Результат:", math_calc.add(num1, num2))
elif choice == '2':
    print("Результат:", math_calc.subtract(num1, num2))
elif choice == '3':
    print("Результат:", math_calc.multiply(num1, num2))
elif choice == '4':
    print("Результат:", math_calc.divide(num1, num2))
else:
    print("Неверный ввод")
