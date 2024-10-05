#wap to check if given words in list polindrome or not and append use

item = eval(input("Enter any collection here : "))
polindrome = []
index1 = 0
while index1 < len(item):
    item = item[index1]
    if type (item) == str:
        index2 = 0
        rev = ''
        while index2 < len(item):
            char = item [index2]
            rev = char + rev
            index2 += 1
    if rev == item:
        polindrome.append(item)
        index1 += 1
print(polindrome,"in the collection: ")            
            
            
          
    