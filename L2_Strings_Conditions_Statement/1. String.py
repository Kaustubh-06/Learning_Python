#String(Alphabets)
str = "Hello" # Output: Hello
str2 = 'Hi' # Output: Hi
str3 = '''Hey''' #  Output: Hey 

# It helps to create multi-line strings.
str4 = """Hello
World""" # Output: Hello World
#It helps to write apstorophes in strings.
str5 = "It's a beautiful day" # Output: It's a beautiful day
str6 = 'She said, "Hello!"' # Output: She said, "Hello!"

str7 = "Hello" + "World" # Output: HelloWorld
str8 = "Hello" + " " + "World" # Output: Hello World

#length of string (Space is also counted)
length = len(str7)# Output: 10
length2 = len(str8) # Output: 11
str8 = "Hello" * 3 # Output: HelloHelloHello
str9 = "This is a string.\nThis is a new line." 
# Output: 
# This is a string.
# This is a new line.
str10 = "This is a string.\tThis is a tab." # Output: This is a string.    This is a tab.

# String Indexing
str = "Hello"
first_char = str[0]  # Output: H
last_char = str[-1]  # Output: o
substring = str[1:4]  # Output: ell
substring2 = str[:3]  # Output: Hel
substring3 = str[2:]  # Output: llo
substring4 = str[-3:]  # Output: llo
substring5 = str[::2]   # Output: Hlo
substring6 = str[::-1]  # Output: olleH (Reverses the string)       

#Note: Strings are immutable, meaning they cannot be changed after creation.

# Slicing Strings (start:stop:step)
# Slicing allows you to extract a portion of the string.

str = "Hello, World!"
sliced_str1 = str[0:5]  # Output: Hello
sliced_str2 = str[7:12]  # Output: World
sliced_str3 = str[:5]  # Output: Hello
sliced_str4 = str[7:]  # Output: World! 

#For accessing the last string
sliced_str5 = str[7:len(str)]  # Output: World!
print(sliced_str5)  # Output: World!

#Negative Indexing
sliced_str6 = str[-6:-1]  # Output: World
sliced_str7 = str[-6:]  # Output: World!
sliced_str8 = str[:-7]  # Output: Hello,

#String Functions
str = "I love Python programming!"
print(str.upper())  # Output: I LOVE PYTHON PROGRAMMING!
print(str.lower())  # Output: i love python programming!
print(str.title())  # Output: I Love Python Programming!
print(str.capitalize())  # Output: I love python programming!
print(str.strip())  # Output: I love Python programming! (removes leading and trailing spaces)
print(str.replace("Python", "Java"))  # Output: I love Java programming! (Replaces "Python" with "Java")
print(str.split())  # Output: ['I', 'love', 'Python', 'programming!'] (splits the string into a list of words)
print(str.find("Python"))  # Output: 7 (returns the index of the first occurrence of "Python")
print(str.count("o"))  # Output: 2 (counts the occurrences of "o")
print(str.startswith("I love"))  # Output: True (checks if the string starts with "I love")
print(str.endswith("programming!"))  # Output: True (checks if the string ends with "programming!")
print(str.isalpha())  # Output: False (checks if all characters are alphabetic)
print(str.isalnum())  # Output: False (checks if all characters are alphanumeric)
print(str.isdigit())  # Output: False (checks if all characters are digits)
print(str.islower())  # Output: False (checks if all characters are lowercase)
print(str.isupper())  # Output: False (checks if all characters are uppercase)
print(str.isnumeric())  # Output: False (checks if all characters are numeric)
print(str.isprintable())  # Output: True (checks if all characters are printable)
print(str.swapcase())  # Output: i LOVE pYTHON PROGRAMMING! (swaps case of each character)
print(str.center(50, '*'))  # Output: *********I love Python programming!********* (centers the string within a specified width, filling with '*')
print(str.ljust(50, '-'))  # Output: I love Python programming!------------------ (left-justifies the string within a specified width, filling with '-')
print(str.rjust(50, '-'))  # Output: ------------------I love Python programming! (right-justifies the string within a specified width, filling with '-')
