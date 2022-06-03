my_dict = {}
with open("text_6.txt", "r", encoding="utf=8") as init_f:
    for line in init_f:
        lesson, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == "" or "9" >= i >= "0"]).split()))
        my_dict[lesson] = name_sum
print(f"{my_dict}")
