#Wap to check if user enter word polindrome or not
word = input("Enter a word: ")
reversed_word = word[::-1]
if word == reversed_word:
    print(f"{word} is a polindrome...")