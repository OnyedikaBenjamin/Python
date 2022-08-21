# Type casting : converting the data type of a value to another data type

x = 1     # int
y = 2.0  # float
z = "3"   # str

x = float(x)  # This re-assignment changes the data type of the variables permanently
y = int(y)
z = float(z)

print(x)
print(y)
print(z)

#------- We cannot display variables of different data-type i.e print("y is : " + y).. where y is an integer

print('y is : ' + str(y))  # We type-casted x to a string here






