# def test_func(word):
#     #pass # Аналог "Ничего"
#     print(word, end="")
#     print("!")
#
# test_func("Hi")
# test_func(5)
# test_func(True)
from unittest import result


# def summa(a, b):
#     return a + b
#     #print("Result:", result)
#
#
# result= summa(5,7)
# print(result)
# print(summa("H", "i"))
def minimal(l):  # создание функции
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el

    # print(min_number)
    return min_number


nums1 = [6, 4, 5, 7, 99, 1]
min1 = minimal(nums1)

nums2 = [6.4, 4.1, 5.1, 7.9, 99, 1.1]
min2 = minimal(nums2)

if min1 < min2:
    print(min1)
else:
    print(min2)

func = lambda x, y: x * y # анонимная функция (маленькая функция)
res = func(5, 2)
print(res)