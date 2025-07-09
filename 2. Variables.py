#variable:
#Var = Val

name = "Kaustubh"
age = 19
price = 25.99
print("My name is: ", name) #
print("My age is: ", age) #
print("Price: ", price) #

#Varying of variable
name = "Aakanksha"
age = 18
price = 18.99
print("My name is: ", name) #
print("My age is: ", age) #
print("Price: ", price) #

'''
Identifier:
1. So myVariable, variable_1, variable_for_print all are valid python identifiers.
2. An Identifier can not start with digit. So while variable1 is valid, 1variable is not valid.
3. We can't use special symbols like !,#,@,%,$ etc in our Identifier.
3. Identifier can be of any length.
'''

#Data Types
#1. Integer(+ve,-ve)
num1 = 25 #
num2 = -4 #
#2. String(Alphabets)
str = "Hello" #
str2 = 'Hi' #
str3 = '''Hey''' # 
#3. Float(Decimals)
float = 25.99 # 
#4. Boolean(True/False)
age = 23
old = False#
#5. None (No val stored)
e = None

print(type(num1))
print(type(num2))
print(type(str))
print(type(str2))
print(type(str3))
print(type(float))
print(type(old))
print(type(e))

a = 5
b = 2
sum = a + b
print("Sum: ", sum)

#Comments
# Single line comment.
"""Multi
 line 
Comment"""
# Multiple comments - Select the lines the press 'Ctrl + /'.

#Types f Operators
# 1. Arithmetic Operators(+,-,*,/,%,**)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) # a^b

# 2. Relational/Comparison Operatios(==,!=,<,>,%=,**=)
a = 50
b = 20
print(a == b) #Output: False
print(a != b) #Output: True
print(a > b) #Output: True
print(a < b) #Output: False
print(a <= b) #Output: False
print(a >= b) #Output: True

#3. Assignment Operator(=,+=,-=,/=,%=,**=)
a = 5
b = 10
print(a + b)
# or
a += b
print(a)  # a = a + b
print(a - b)
a -= b
print(a)  # a = a - b
print(a * b)
a *= b
print(a)  # a = a * b
print(a / b)
a /= b
print(a)  # a = a / b
print(a % b)
a %= b
print(a)  # a = a % b
print(a ** b)
a **= b

#4. Logical Operators(not, and, or)
num = 10
num1 = num + 10
print(num1)
        #or
num += 10
print(num)
num *= 5
print(num)
num /= 5
print(num)
num **= 5
print(num)

#Type Conversion
#1. Type Conversion: Automatic conversion of one data type to another by Python.
a = 5
b = 2.5
c = a + b  # Here, int is converted to float automatically.
print(c)  # Output: 7.5

#2. Type Casting: Manual conversion of one data type to another by the user.
a = 5
b = 2.5
c = int(a + b) # Here, we are explicitly converting the result to int.
print(c)  # Output: 7 (int)
str = str(a+b) # Converting the result to string
print(str)  # Output: '7.5' (str)

# Note:
#1. Type Conversion is automatic and happens when different data types are used together.
#2. Type Casting is manual and is done using functions like int(), float(), str().
#3. Type Conversion is also known as implicit conversion.
#4. Type Casting is also known as explicit conversion.

'''
Input Function:
1. The input function is used to take input from the user.
2. It always returns a string, so we need to convert it to the desired data type.
'''
# Example:
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Converting input to int
marks = float(input("Enter the marks: "))  # Converting input to float
print("Your name is:", name) #Output: Your name is: Kaustubh
print("Your age is:", age) #Output: Your age is: 19
print("Marks:", price) #Output: Marks: 25.99
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(marks))  # Output: <class 'float'>



