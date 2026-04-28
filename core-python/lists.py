numbers = [1, 2, 3, 4]
names = ["Nandani", "Rahul", "Priya"]
mixed = [1, "hello", 3.5]

print(mixed[0])  
print(mixed[-1]) 

nums = [1, 2, 3, 4, 5]

print(nums[1:4])   
print(nums[::-1])  

nums.append(6)
print(nums)

nums.extend([7, 8])
print(nums)

nums.insert(8, 9)
print(nums)

nums.remove(2)
print(nums)

nums.pop()
nums.pop(0)
print(nums)

print(nums.index(6))

nums = [1, 2, 2, 3]
print(nums.count(2)) 

nums = [4, 1, 3, 2]
nums.sort()
print(nums)  

nums = [1, 2, 3]
nums.reverse()
print(nums)

nums = [1, 2, 3]
new_nums = nums.copy()

print(len(nums))  
print(max(nums))  
print(min(nums))  
print(sum(nums))  

for item in [1, 2, 3]:
    print(item)

nums = [1, 2, 3]
nums[0] = 10

print(nums)  