
text = "hello world"

print(text.upper())      
print(text.lower())      
print(text.title())      
print(text.capitalize()) 

word = "   hello   "

print(word.strip())   
print(word.lstrip())  
print(word.rstrip())  

text = "my name is Nandani"

print(text.find("Nandani"))     
print(text.index("is")) 
print("Nandani" in text)    

text = "I like Swift"

new_text = text.replace("Swift", "Python")
print(new_text)  

text = "apple,banana,mango"

fruits = text.split(",")
print(fruits)  

joined = " , ".join(fruits)
print(joined) 

text = "Hello123"

print(text.isalpha())  
print(text.isdigit()) 
print(text.isalnum()) 
print(text.islower())  
print(text.isupper())  

text = "python programming"

print(text.startswith("python"))  
print(text.endswith("ing"))       

text = "Nandani"

print(len(text))        
print(text.count("a"))  

name = "Nandani"
age = 22

print(f"My name is {name} and I am {age} years old")

print("My name is {} and I am {}".format(name, age))

text = "Nandani"

print(text[0])    
print(text[0:3])  
print(text[-1])   
print(text[::-1]) 