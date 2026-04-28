import math_utils
import math
import random
from datetime import datetime
import os
import sys



print(math_utils.add(2, 3))
print(math.sqrt(16))   
print(math.ceil(2.3))  
print(math.floor(2.9)) 
print(math.pi)         

print(random.randint(1, 10))   
print(random.choice(["A", "B", "C"]))

now = datetime.now()

print(now)
print(now.date())
print(now.time())

print(os.getcwd())     
print(os.listdir()) 

print(sys.version)
print(sys.argv)