#WAP to check if a number enterd by the user is odd or even.
num = int(input("Enter a Number:"))

if num %2 ==0:
    print("The number is Even")  # Output: The number is Even
else:
    print(("The number is Odd")) # Output: The number is Odd

# WAP to find the grearest of 3 numbers entered by the user.
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))

if num1 >=num2 and num1 >= num3:
    print("First number is greatest:", num1)  # Output: The greatest number is: num1
elif num2 >= num1 and num2 >= num3:
    print("Second number is greatest:", num2)  # Output: The greatest number is: num2
else:
    print("Third number is greatest:", num3)  # Output: The greatest number is: num3

# WAP to check if a number is multiple of 7 or not.
num = int(input("Enter number:"))
if num %7 == 0:
    print("The number is a multiple of 7")  # Output: The number is a multiple of 7
else:
    print("The number is not a multiple of 7")