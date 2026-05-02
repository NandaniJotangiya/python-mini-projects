import sys

a = [1, 2]
print(sys.getrefcount(a))

a = 10
b = a #10  ← a, b both pointing here

b = 20 #10 ← a, 20 ← b

#Mutable (can change)
#list, dict, set

lst = [1, 2, 3]
lst.append(4)

#Immutable (cannot change)
#int, float, string, tuple
x = 10
x = x + 1

#id()
a = 10
b = 10

print(id(a))
print(id(b))

#assignment behaviour : immutable

a = 5
b = a

b = b + 1

print(a)  # 5
print(b)  # 6

#mutable
a = [1, 2]
b = a

b.append(3)

print(a)  # [1, 2, 3]


c = a.copy()
