#Set
'''
It is a collection of unordered items that are unique and immutable.
Therefore, output 
Sets are written with {curly brackets} or using the set() constructor.
List and dictionary not be stored in a set because they are mutable.

'''
num = {1, 2, 5, 2, "Hello", "World", "Hello"}
print(num)  #Output: {1, 2, 5, 'Hello', 'World'} (duplicates are removed)
print(type(num))  
