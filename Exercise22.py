#wap to display a  dictionary whose keys are words of a sentence in the values of each
sentence = "First numeric value will be added to nums and the will stop"
words = sentence.split()
output = {}
for word in words:
    if word not in output:
     output[word] = len(word)
print(output)        