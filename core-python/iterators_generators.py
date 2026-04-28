#Iteretator

nums = [1, 2, 3]

it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

print(next(it))  # StopIteration error

#generator

def count_up(n):
    for i in range(n):
        yield i

gen = count_up(3)

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2