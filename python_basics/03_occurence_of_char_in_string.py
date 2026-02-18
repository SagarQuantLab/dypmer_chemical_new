# how to count number of letter in the string
# 1. Count
# 2. For Loop
# 3. Counter

my_string = "Hello, This is Chemical Students"

# 1
count = my_string.count('l')
print(count)

# 2
count = 0
for iChar in my_string:
    if iChar == 'l':
        count += 1
        
# 3
from collections import Counter

count = Counter(my_string)
print(count['l'])

