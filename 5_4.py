rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("text_4.txt", "r", encoding="utf=8") as my_f:
    # content = file_obj.read().split('\n')
    for i in my_f:
        i = i.split(" ", 1)
        new_file.append(rus[i[0]] + "  " + i[1])
    print(new_file)

with open("file_4_new.txt", "w") as my_f_2:
    my_f_2.writelines(new_file)
