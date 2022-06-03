import json

with open("text_77.json", "w", encoding="utf=8") as my_file, open("text_7.txt", encoding="utf-8") as my_object:
    prof = {string.split()[0]: int(string.split()[2]) - int(string.split()[3] for string in my_object)}
    f_up = [el for el in prof.values() if el > 0]
    result = [prof, {"profit": round(sum(f_up) / len(f_up))}]

    json.dump(result, my_file, ensure_ascii=False, indent=4)