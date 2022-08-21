name = "ben-billion"

print(len(name))               # This will print the length of the name value.
print(name.find('e'))          # Here we are saying find us the index of letter 'E'
print(name.capitalize())       # This will capitalize the first letter of the name
print(name.upper())            # This will make all the string an upper case
print(name.lower())            # This will make all the string a lower case
print(name.isdigit())          # This will return a boolean depending on if our string is a digit
print(name.isalpha())          # We use this to check if our string contains only alphabetical letters
print(name.count("l"))         # We use this to count how many characters are within a String
print(name.replace("e", "a"))  # Here we will replace 'e' with 'a'.
print(name*3)                  # This is not technically a method, we can use it to display a string multiple times.
