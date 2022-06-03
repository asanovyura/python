with open("text_3.txt", "r", encoding="utf=8") as my_f:
    x = {line.split()[0]: float(line.split()[1]) for line in my_f}
    print(f"Средний доход сотрудников = {round(sum(x.values()) / len(x), 3)}\n"
          f"Сотрудники, ЗП которых менее 20000: {[e[0]for e in x.items() if e[1] < 20000]}")

