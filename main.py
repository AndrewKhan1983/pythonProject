# продолжение обучения в Pycharm

name = input("Введите имя ")
surname = input("Введите фамилию ")
age = int(input("Введите возраст "))

#Тернарный оператор
print ("Привет ", name, surname) if age >= 9 else print ("Привет ", name, surname, " тебе еще мало лет")


#Условные операторы
if age >= 9:
    print ("Привет ", name, surname)
else:
    print ("Привет ", name, surname, " тебе еще мало лет")
print("Привет ", name, surname, ",Ваш возраст", age, "лет")