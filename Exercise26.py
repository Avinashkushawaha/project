#wap to filter a set to have only single value data type using for loop.
items = {15, 10.5, 7+2j, "hello",(10,20)}
filtered_items = set()
for item in items:

    if type(item) in (str,tuple):
           filtered_items.add(item)
      
items -= filtered_items  
print(items,"final set: ")