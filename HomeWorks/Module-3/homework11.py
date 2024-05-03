# 1.
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).
#
# a,b,c = 59, 59, 59
# result —> Равносторонний

print('Программа принимает три положительных числа и определяет вид треугольника.')
try:
    a, b, c = map(int, input("Введите длину сторон треугольника, через запятую: ").split(","))
except Exception:
    print('Некоректнный ввод!')
    print("Пример формата ввода: 59, 59, 59")
    exit()

if a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
else:
    print("Разносторонний")