#set

nums = {1, 2, 3, 3, 4}
print(nums) 

nums.add(5)

print(nums)  
nums.remove(2)

nums.discard(5)

nums.pop()

a = {1, 2, 3}
b = {3, 4, 5}

print(a.unionb(b))
print(a.intersection(b))
print(a.difference(b))

print(2 in a)

for item in a:
    print(item)


#Tuple

t = (1, 2, 3)

print(t[0])
print(t[-1])

t = (5,)

t = (1, 2, 2, 3)

print(t.count(2)) 
print(t.index(3))  

person = ("Nandani", 22)
name, age = person
print(name) 

for item in t:
    print(item)
    