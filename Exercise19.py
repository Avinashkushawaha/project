files = ['start.py', 'demo.txt', 'hello.py','new.py', 'bye.txt','some.csv']
output = {}
index = 0
while index < len (files):
    file = files[index]
    item = file.split('.')
    name = item[0]
    ext = item[1]
    if ext in output:
        output[ext]+= [name]        
    else:
        output[ext] = [name]
    index += 1
print(output)    