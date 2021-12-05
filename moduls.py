import datetime as d  # переназначение имени модуля
from math import sqrt as s  # импорт из модуля отдельную функцию
import time
import sys, os, platform
import mymodule as m
import cowsay as c

c.cow("Hi")
c.beavis("KKKK")
print(c.get_output_string('trex', 'Hello (extinct) World'))
c.daemon("dda")
# time.sleep(3) # сон программы (секунды)
# print ("Hello")
# print(d.datetime.now().date()) # вывод даты и времени в реальном времени
print(sys.path)  # указывает полный путь к текущему файлу
print(os.name)  # указывает название операционной системы
print(platform.system())
print(s(100))  # нахождение квадратного корня
m.hello()
print(m.add_three_numbers(3, 2, 6))