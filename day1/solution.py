from typing import List

id_list : List[int] = []
with open("input.txt", "r") as f:
    for line in f:
        id_list.append(int(line))

# Task 1
for i in range(len(id_list)):
    for j in range(i, len(id_list)):
        if id_list[i] + id_list[j] == 2020:
            print(id_list[i], id_list[j],  id_list[i] * id_list[j], sep=", ")

# Task 2
for i in range(len(id_list)):
    for j in range(i, len(id_list)):
        for k in range(j, len(id_list)):
            if id_list[i] + id_list[j] + id_list[k] == 2020:
                print(id_list[i], id_list[j], id_list[k],  id_list[i] * id_list[j] * id_list[k], sep=", ")
