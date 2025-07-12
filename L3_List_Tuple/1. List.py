#List in Python
'''
It stores set of values in a single variable.
It is mutable, ordered and allows duplicate values.
It is defined by square brackets [].
It can contain mixed data types, like integers, strings, float and other lists.
'''

#Palindrome
'''
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
For example, "madam", "racecar", and "level" are palindromes.
["madam", "racecar", "level"]
[1,2,3,2,1]
'''

# Example of a list
marks = [87,64,33,95,76]
print(marks)  # Output: [87, 64, 33, 95, 76]
print(type(marks))  # Output: <class 'list'>
print(len(marks))  # Output: 5 (length of the list)


# Accessing elements in a list
print(marks[0])  # Output: 87
print(marks[1])  # Output: 64

#Changing elements in a list
student = ["Karan", 95.5, 18, "Delhi"]
print(student)  # Output: ['Karan', 95.5, 18, 'Delhi']
student[0] = "Karan Singh"
print(student[0])  # Output: Karan Singh
print(student)  # Output: ['Karan Singh', 95.5, 18, 'Delhi']

# Adding elements to a list
student.append("Python")  # Adds "Python" to the end of the list
print(student)  # Output: ['Karan Singh', 95.5, 18, 'Delhi', 'Python'] 

#List Slicing
'''
list_name[starting_index:ending_index:step] #
'''
student = ["Karan", 95.5, 18, "Delhi", "Python"]
print(student[1:3])  # Output: [95.5, 18] (elements from index 1 to 2)
print(student[:2])  # Output: ['Karan', 95.5] (elements from start to index 1)
print(student[2:])  # Output: [18, 'Delhi', 'Python'] (elements from index 2 to end)
print(student[-3:])  # Output: [18, 'Delhi', 'Python'] (last three elements)
print(student[:-1])  # Output: ['Karan', 95.5, 18, 'Delhi'] (all elements except the last one)

#List Functions
list = [5,4,6,9,3,2]
print(list.append(0))  # Output: None (Because append modifies the list in place and returns None due to in-place modification)
list.append(1) # Adds 1 to the end of the list
print(list)  # Output: [5, 4, 6, 9, 3, 2, 6] 
list.sort()  # Sorts the list in ascending order
print(list) # Output: [2, 3, 4, 5, 6, 6, 9]
list.sort(reverse=True)  # Sorts the list in descending order
print(list)
list.reverse()  # Reverses the order of the list
print(list)  # Output: [9, 6, 6, 5, 4, 3, 2]
#list.insert(idx,el) 
list.insert(2, 10)  # Inserts 10 at index 2
print(list)
list.remove(6)  # Removes the first occurrence of 6 from the list
print(list)  # Output: [9, 6, 5, 4, 3, 2]
#list.pop(idx)
list.pop(3)  # Removes and returns the element at index 3
print(list)  # Output: [9, 6, 5, 3, 2] (4 is removed)
#list.count(el)
print(list.count(6))  # Output: 1 (Counts the occurrences of 6 in the list)
#list.index(el)
print(list.index(5))  # Output: 2 (Returns the index of the first occurrence of 5)
#list.clear()
list.clear()  # Clears all elements from the list
print(list)  # Output: [] (Empty list)

