# how to convert lists to dictionary
# using for loop
# zip

key_list = ["Name", "Age", "Gender"]
value_list = ["Rohan", 25, "M"]

# for loop
i = 0
my_dict = {}
for ikey in key_list:
    my_dict[ikey] = value_list[i]
    i += 1

# zip
my_dict = dict(zip(key_list, value_list))
print(my_dict)

