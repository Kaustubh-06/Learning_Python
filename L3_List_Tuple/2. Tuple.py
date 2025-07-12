tup = (2,1,3,1)
print(tup[0]) # Output: 2
print(tup[1]) # Output: 1
tup =()
print(tup)  # Output: () (Empty tuple)
print(type(tup))  # Output: <class 'tuple'>
print(len(tup))  # Output: 0 (length of the tuple)
#Correcrt way to create a tuple with one element otherwise it will be considered as an integer.
tup = (1,)
print(tup)  # Output: (1,)

#Tuple Methods
tup = (1,2,3,4,5)
print(tup.count(1))  # Output: 1 (Counts the occurrences of 1 in the tuple)
print(tup.index(3))  # Output: 2 (Returns the index of the first occurrence of 3)

