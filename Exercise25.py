#wap to Swap key and value from a given dictionary using for loop.
dict1 = {'a':10, 'b':20, 'c':30}
output = {}
for key in dict1:
    value = dict1[key]
    if type(value)not in (list, set, dict):
        output[value] = key
print(output)