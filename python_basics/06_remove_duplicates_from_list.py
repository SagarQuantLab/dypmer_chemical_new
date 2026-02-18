my_list = ["A", "B", "C", "F", "A"]

# for loop
unique_list = []
for iChar in my_list:
    if iChar not in unique_list:
        unique_list.append(iChar)

# set
#print(list(set(my_list)))

# dict
print(list(dict.fromkeys(my_list)))