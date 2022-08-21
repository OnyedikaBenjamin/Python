# We can either use single or double quotes to create a string data

first_name = "Ben"  # Here we initialized a string and assigned a value to it
last_name = "Billion"
full_name = first_name + " " + last_name  # In python, we can concatenate strings.
print("Hello " + full_name)  # Here we printed out the value of the string.
print(type(full_name))  # Here we printed the data type of full_name.

# ------- Integer ------------#

age = 21
age += 1  # Here I incremented the value of age by one
print(age)  # Here we printed the value of age
print(type(age))  # Here we printed the data type of age

# If we intend to concatenate different data type, we will do some casting as shown below.

print(full_name + ", age is : " + str(age))

# ------- Floating point values ------------#

height = 34.66
print("Your height is " + str(height) + "cm")
print(type(height))

# ------- Boolean ------------#

human = True
print("Are you are human? " + str(human))
print(type(human))

# There are 4 basic data types in Python, namely String, Boolean, Float and Integer.