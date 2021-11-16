#Цикл for

#for i in range(1,100,2):
#    print(i)

# count = 0
# word = "Hello, world!"
# for i in word:
#     if i == "l":
#        count += 1
# print("Count:",count)

# for i in range(1, 1100):
#     if i == 566:
#         break
#
#     if i%2 == 0:
#         continue
#
#     print(i)
found = None
for i in "hello":
    if i == "l":
        found = True
        break
else:
    found = False
print(found)



#Цикл while

# i = 2
# while i < 100:
#     print(i)
#     i +=3

# isHasCar = True
# while isHasCar:
#     if input("Enter data: ") == "stop":
#         isHasCar = False