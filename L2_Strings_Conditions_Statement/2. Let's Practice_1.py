# WAP to input user's first name and print its length.
first_name = str(input("Enter First Name :"))
print(first_name, "has", len(first_name), "characters.")  # Output: First Name has X characters.

#WAP to find the occurance of "₹" in a string.
str = "\nThe price of a Mango is ₹50 per kg.\nThe price of a Banana is ₹30 per kg.\nThe price of an Apple is ₹40 per kg."
print("The string is: ", str)  # Output: The string is: The price of a Mango is ₹50 per kg. ...
print("The occurance of '₹' in the string are: ", str.count("₹"))  # Output: The occurance of '₹' in the string are: 3

