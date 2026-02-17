# strings & their operations (string slicing)
my_string = "Hello this is DYPEMR College"

# print(my_string[0])
# print(my_string[1])
# print(my_string[0:3])
# print(my_string[len(my_string)-1])
# print(my_string[-1])
# print(my_string[0:10:2])
# # # print(my_string[::-1])
# # print(my_string.count('l'))
# # print(my_string.replace("H", "Z"))
# # print(my_string.upper())
# # print(my_string.lower())

# # list 
# my_list = ["Apple", "Banana", "mango"]
# print(my_list[0])
# print(my_list[-1])
# my_list[1] = "Guava"
# print(my_list)

# my_list2 = ["Tomoto", "Carrot", "Cabbage"]

# my_list.append("Banana")
# print(my_list)

# my_list.extend(my_list2)
# print(my_list)

# my_list = ["Apple", "Banana", "mango"]
# my_list.append(my_list2)
# print(my_list)

# print(my_list.pop())

# dictionary 
my_dict = {
    "Name" : "Rohan",
    "Age" : 25,
    "Gender" : "M"
}

my_dict = {
    123445  : {
        "Name" : "Rohan",
        "Age" : 25
    },
    456789 : {
        "Name" : "SOham",
        "Age" : 25
    }
}

# print(my_dict["Name"])
# my_dict["Name"] = "Soham"
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# #my_dict.update({"Religion" : "Hindu"})
# my_dict["Religion"] = "Hindu"
# print(my_dict)

# key_list = ["A", "B", "C"]
# value_list = [1, 2, 3]

# my_dict = dict(zip(key_list, value_list))
# print(my_dict)

# tuples
# my_tuples = ("A", "B", "C", "A")

# print(my_tuples[0])
# print(my_tuples.count("A"))

#######
# sets
my_sets = {"A", "B", "C", "A"}








#########################
#               Ordered             Call            mutable         define bracket
# list              Y               idx                 Y           []
# dict              Y               keys                Y           {}
# tuples            Y               idx                 N(add/rem)  ()
# Sets              N               N                   N           {}