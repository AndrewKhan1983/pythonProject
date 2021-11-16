# country = {"code":"RU", "name": "Russia", "population": 144000000} # Создание словаря
#
# # country = dict(code="RU", name="Russian", population=144)
# #print(country.items()) # полный словарь (ключ + значение)
#
# print(country["population"]) # вывод элемента по ключу
# print(country.get("code")) # вывод элемента по ключу
# #country.clear() # очистка словаря
# #country.pop("code") # Удаление элемента по ключу
# country.popitem() # Удаление последнего элемента в словаре
# country["code"] = "RUS" # Изменение значения по ключу
#
# print(country)
#
# for key in country:
#     print(key)
#
# for key, value in country.items():
#     print(key, " - ", value)
#
# print(country.keys()) # получение ключей
# print(country.values()) # получение значений
# print(country.items()) # получение ключей и значений
person = {
    "user1":{
        "first_name": "John",
        "last_name": "Smith",
        "age":"55",
        "address":("г. Москва", "ул. Тверская", "дом 44", "квартира 1"),
        "grades":{"math":5, "phisics": 4}
    },
    "user2":{
        "first_name": "Sara",
        "last_name": "Connor",
        "age":"22",
        "address":("г. Москва", "ул. Тверская", "дом 44", "квартира 6"),
        "grades":{"math":3, "phisics":2}
    }
}
print(person["user1"]["grades"]["phisics"])
print("Оценка по математике: ", person["user2"]["grades"]["math"], "ученик: ", person["user2"]["first_name"], person["user2"]["last_name"])