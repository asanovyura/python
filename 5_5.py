def summary():
    try:
        with open("file_5.txt", "w+", encoding="utf=8") as my_f:
            line = input("Введите цифры через пробел \n")
            my_f.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print("Ошибка")
    except ValueError:
        print("Неправильно набран номер")


summary()

