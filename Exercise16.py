word = 'Stree'
index = 0
output = {}
while index < len (word):
    char = word [index]
    if char not in output:
        output[char] = ord (char)
    index += 1

print(output)