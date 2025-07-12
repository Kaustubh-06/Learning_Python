# WAP to count the number of students with the "A" grade in the folowing tuple.
# Given tuple: ('A', 'B', 'C', 'A', 'D', 'A', 'B', 'C').
# Store the above values in a list and sort them from "A" to "D".

tup = ('A', 'B', 'C', 'A', 'D', 'A', 'B', 'C')
count_A = tup.count('A')
print("Number of students with 'A' grade:", count_A)  # Output: 3

list_tup = list(tup)
print(list_tup)  # Output: ['A', 'B', 'C', 'A', 'D', 'A', 'B', 'C']
list_tup.sort()
print("Sorted list:", list_tup)  # Output: ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D']
