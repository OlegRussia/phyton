ls1 = [7, 8, 16, 88, 31, 17]
new_list = []
for i in ls1:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)
print(new_list)