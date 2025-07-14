# Dictionary
'''
A dictionary is a collection of key:value pairs.
Dictionaries are unordered, muitable(changeable), and do not allow duplicates.
Dictionaries are written with {curly brackets}, and they have keys and values.
A key is a unique identifier for a value in the dictionary.
Values can be of any data type, including lists, tuples, or other dictionaries.
'''

info = {
    "name": "Kaustubh",
    "subject": ["Python", "Java", "C"],
    "topics": ("dictionary", "set", "tuple"),
    "age": 20,
    "is_student": True,
    "marks": 98.6,
    12.99 : 98.5
}

# # print(info)
# # print(type(info))

# print(info["name"])  # Accessing value using key
# print(info["subject"])

# info["age"] = 21  # Updating value (Overwriting)
# print(info["age"])  # Accessing updated value

# info["hobby"] = "coding"  # Adding new key-value pair 
# print(info["hobby"]) # Accessing new value

# print(info.keys())  # Getting all keys
# print(info.values())  # Getting all values

# null_dict = {}
# null_dict["Company"] = "Deloitte"  # Adding a key-value pair
# print(null_dict)

# # Deleting a key-value pair
# del info["marks"]  # Using del keyword
# print(info)

# # Using pop() method to remove a key-value pair
# removed_value = info.pop("is_student")
# print(removed_value)  # Accessing the removed value
# print(info)  # Displaying the dictionary after removal

#Nested Dictionary
'''
In a nested dictionary, a dictionary can contain another dictionary as a value.
'''
student = {
    "name": "Kaustubh",
    "age": 20,
    "subjects": {
        "Python": {
            "marks": 95,
            "teacher": "Mr. Smith"
        },
        "C": {
            "marks": 90,
            "teacher": "Ms. Johnson"
        }
    }
}
print(student["subjects"])
print(student["subjects"]["Python"])  # Accessing nested dictionary

# Dictionary Methods
'''
Not prints nested dictionary.

myDict.keys() # returns all keys in the dictionary
myDict.values() # returns all values in the dictionary
myDict.items() # returns all key-value pairs in the dictionary as tuples
myDict.get(key) # returns the value for the specified key, or None if the key does not exist
myDict.update(newDict) # insert the specific items to the dictionary from newDict
'''

print(student.keys())  # Returns all keys in the dictionary
print(student.values())  # Returns all values in the dictionary
print(student.items())  # Returns all key-value pairs in the dictionary as tuples
print(student.get("name"))  # Returns the value for the specified key
print(student.update({"hobby": "coding"}))  # Insert a new key-value pair
print(student)  # Displaying the updated dictionary
