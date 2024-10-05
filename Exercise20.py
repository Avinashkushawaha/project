  # write a program to extrac all the lower case char in using for loop
string = "Hello World"
lower = ''
for char in string:
    if 'a' <= char <= 'z':
     lower += char
print(lower)    
# 
# 
# 
# string = "Hello World123"
# lower = ''
# for char in string:
#     if 'a' <= char <= 'z':  # Checks if the character is a lowercase letter
#         lower += char
# print(lower)
    