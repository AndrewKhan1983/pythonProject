# x=0
# while x == 0:
#     try:
#         x=int(input("Введите число: "))
#         x+=5
#         print(x)
#     except ValueError:
#         print("Введено не число!!!")

try:
    x = 5/0
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("QQQ")
else:
    print("else") # Срабатывает если выполнен блок try (без except)
finally:
    print("finally") # Срабатывает всегда