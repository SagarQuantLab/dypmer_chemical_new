# how to reverse a string
# indexing
# for loop
# join reverse 

my_string = "Hello, This is Chemical Students"

#1
reveresed_string = my_string[::-1]

#2
reveresed_string = ""
for iChar in my_string:
    reveresed_string = iChar + reveresed_string
print(reveresed_string)


#3
reveresed_string = "".join(reversed(my_string))
