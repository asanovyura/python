with open("test_5.1.txt", "w", encoding="utf-8") as my_f:
    while True:
        line = input("введите текст, для завершения введите пустую строку: ")
        if not line:
            break
        print(line, file=my_f)
