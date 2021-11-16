# Изучение кортежей (tuple)

data = (3, 4, 5, 8, True, "jjjj")
print(data[1:6])

print(data.count(5)) # поиск количества элементов в кортеже
print(len(data)) # длина кортежа
for i in data:
    print(i)

nums = [3, 4, 77, 0]

new_data = tuple(nums) # создание кортежа из списка
word = "Hello world!"
new_word = tuple(word) # создание кортежа из строки
print(new_word)