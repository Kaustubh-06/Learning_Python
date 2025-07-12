# WAP to check if a list contains a palindrome of elements.(Hint: use copy() method and reverse() method)
#1st Method (Using Rational Check)
list = [1,2,3,2,1]
list2 = [1,2,3,4,2,1]

list.copy()
new_list = list.copy()
print("New list: ", new_list)

list2.copy()
new_list2 = list2.copy()
print("New list2: ", new_list2)


new_list.reverse()
print("Reversed list: ", new_list)

new_list2 = list2.copy()
new_list2.reverse()
print("Reversed list2: ", new_list2)

print("Is the list is a palindrome? - ", new_list == list)
print("Is the list2 is a palindrome? - ", new_list2 == list2)


#2nd Method(Using Conditional check)

if new_list == list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
if new_list2 == list2:
    print("The list2 is a palindrome.")
else:
    print("The list2 is not a palindrome.")

print("End of the program.")