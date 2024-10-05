#wap to mimic string swap case methode
string = "JAmEsBoNDoo7"
output = ''
index = 0
while index < len(string):
    char = string[index]
    if char.isupper():
        output += char.lower()
    elif char.islower():
        output += char.upper()
    else:
        output += char

    index += 1
        
print(output)

