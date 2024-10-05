#wap to mimic replace methode in string
line = "if you are bad i will be mad"
line = line.replace(' ', '_')
output = ''
index = 0
while index < len (line):
    char = line[index]
    if char == ' ':
        output += '_'
    else:
     output += char
     index += 1
print(output)        

