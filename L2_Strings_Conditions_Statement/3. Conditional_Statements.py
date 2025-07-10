# '''
# Conditional Statements:
# - Conditional statements are used to perform different actions based on different conditions.
# - if, elif, and else statements are used to control the flow of execution based on conditions.

# if(condition):
#     # code to execute if condition is true
# elif(condition):
#     # code to execute if the previous condition is false and this condition is true
# else:
#     # code to execute if all previous conditions are false
# '''

# # Example of if, elif, and else statements
# age = 20
# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

#Grade students based on marks
marks = float(input ("Enter your marks:"))

if marks >= 90:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
else:
    print("Grade: F")

#Nesting if statements
age  = 34
if age >= 18:
    if (age >= 80):
        print("You can't drive")
    else:
        print("You can drive")
else:
    print("can't drive")
    