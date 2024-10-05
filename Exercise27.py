#wap to most occuring word from a given string .
# string = input("Enter a string here: ")
# words = string.split()
# output = {}


# for word in words:
#     if word in output:
#         output[word] += 1
#     else:
#         output[word] = 1

# print(output)   
# 
#      
output = {'hello': 2, 'world': 2, 'everyone': 1}

max_val = max(output.values())
max_words = []

for key in output:
    value = output[key]
    if value == max_val:
        max_words.append(key)

print("words with maximum frequency:", max_words)     




