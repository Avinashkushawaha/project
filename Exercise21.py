#write a program to extract all numeric in a collection.
collection = [10, 7.5, 'bye', [7,8], 2+3j, 65]
nums = []
for item in collection:
    if type (item) in [int, float, complex]:
        nums.append(item)
        break
print(nums)
       