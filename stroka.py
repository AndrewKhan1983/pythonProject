#word = "football, basketball, skate"
#print(len(word)) # Показывает длину строки
#print(word.count("p")) # Показывает количество элементов "" в строке
# print(word.upper()) # приводит строку в верхнем регистре
# print(word.lower()) # приводит строку к нижнему регистру
# print(word.isupper()) # сообщает находится ли вся строка в верхнем регистре
# print(word.islower()) # сообщает находится ли вся строка в нижнем регистре
# print(word.capitalize()) # приводит первый символ строки в верхний регистр
# print(word.find("o")) # ищет символ в строке и выводит его индекс

# Программа для приведения всех первых элементов строки в верхний регистр
# hobby = word.split(", ") # Разделяет строку по определенному символу и заносит их в список
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
# result = ", ".join(hobby) # Приводит список к строке (исправленной)
# print(result)

# индексы и срезы
word = "football"
print(word[0:4]) #Срез индексов от и до (если нужно выводить от и до конца [5: ] [от:до:шаг(если -1 переверн)