with open("test_5.1.txt", "r", encoding="utf-8") as my_f:
    strings = my_f.readlines()
    for index, value in enumerate(strings, 1):
        words = len(value.split())
        print(f"String {index} have {words} words")
