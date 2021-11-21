# программа для создания списка произвольной длины (пользователь)

n = int(input("Введите длину списка: "))

user_list = []

i = 0
while i < n:
    string = "Введите элемент #"+ str(i + 1)+ ": "
    user_list.append(input(string))
    i +=1

for el in user_list:
    print(el)







# nums = [5, 6, 8, "jjjj", True, False,[2,5,6,77]]
# nums[0] = 33
# nums[-2] = False
# print(nums[-1][-1])

#numbers = [2, 3, 5]
#numbers.append(55) # добавление элемента в список
#numbers.append(False)
#numbers.insert(1,66) # добавление элемента по индексу

#b = [33, 44, 55, True]
#numbers.extend(b) # добавление элементов в список
#numbers.sort() # Сортировка списка по порядку
#numbers.reverse()
#numbers.pop(0) # удаляет выбранный элемент из списка
#numbers.remove(True) # удаляет выбранный элемент из списка

#numbers.clear() #очищает весь список
#print(numbers)
#print(numbers.count(55)) # вычисление количества элементов в списке (шт)
#print(len(numbers)) # вычисление длины списка (количество элементов)

# nums = [3, 4, 5, 6, "66", True]
# nums.append(88)
# for elem in nums:
#     elem *= 3 # Умножение элементов списка на
#
#     print(elem)