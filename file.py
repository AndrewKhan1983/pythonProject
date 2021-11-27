# data = input("Введите текст: ")
#
# file = open('data/test.txt', 'a')# 'w' - метод write -информация каждый раз стирается и записывается заново
#                                     # 'a' - метод append - добавление информации
# file.write(data + "\n")             # 'r' - метод read -чтение из файла
#
# file.close()

file = open('data/test.txt', 'r')

#print(file.read()) # в () можно указать количество выведенных символов

for line in file:
    print(line, end=" ")

file.close