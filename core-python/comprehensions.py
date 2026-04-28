#List comprehension

nums = [1, 2, 3, 4]

squares = [x*x for x in nums]
print(squares)

nums = [1, 2, 3, 4, 5, 6]

evens = [x for x in nums if x % 2 == 0]
print(evens) 

#loop vs comprehensions

result = []
for x in range(5):
    result.append(x * 2)

result = [x * 2 for x in range(5)]

#Dictionary comprehension

nums = [1, 2, 3]

squares = {x: x*x for x in nums}
print(squares)

nums = [1, 2, 3, 4]

even_squares = {x: x*x for x in nums if x % 2 == 0}

# Set comprehension

nums = [1, 2, 2, 3]

unique_squares = {x*x for x in nums}
print(unique_squares)  # {1, 4, 9}

#Nested Comprehension

matrix = [[1, 2], [3, 4]]

flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4]

#with if-else

nums = [1, 2, 3, 4]

labels = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(labels)

names = ["nandani", "Nidhi"]

upper_names = [name.upper() for name in names]