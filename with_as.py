try:
    with open("data/test.txt", "r", encoding="utf-8") as file: # with as не требует прописывания закрытия файла
        print(file.read())
except FileNotFoundError:
    print("Файл не найден!!!")