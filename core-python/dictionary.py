employee = {
    "name": "Nandani",
    "age": 22,
    "course": "Python"
}

print(employee["name"])    
print(employee.get("age"))  

employee["city"] = "Surat"
employee["age"]  = 23

print(employee.keys())
print(employee.values())
print(employee.items())

employee.update({"age": 25, "city": "Ahmedabad"})

print(employee.get("name"))
print(employee.get("salary", "Not Found"))

employee.setdefault("country", "India")

new_employee = employee.copy()

for key in employee:
    print(key)

for value in employee.values():
    print(value)

for key, value in employee.items():
    print(key, ":", value)

if "name" in employee:
    print("Exists")

employee.pop("age")
employee.popitem()

del employee["course"]

employee.clear()


students = {
    "s1": {"name": "Niharika", "age": 20},
    "s2": {"name": "Riddhi", "age": 21}
}

print(students["s1"]["name"])  