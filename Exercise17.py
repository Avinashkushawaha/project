string = 'stree'
output = {}
index = 0
while index < len (string):
    char = string[index]
    if char in output:
        output[char] += 1
    else:
        output[char] = 1
    index += 1
print(output)