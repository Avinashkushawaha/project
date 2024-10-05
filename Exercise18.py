line = input("Enter a sentence: ")
words = line.split()
output = {}
index = 0 
while index < len (words):
    word = words[index]
    if word not in output:
        output[word] = len(word)
    index += 1
print(words)        
