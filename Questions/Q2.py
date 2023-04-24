'''
2. (1.0) Make a program that receives the radius, for pi=3.14,
calculate and show:
● the length of a sphere; it is known that C = 2 * piR;
● the area of a sphere; it is known that A = piR2;
● the volume of a sphere; it is known that V = ¾ * p R

'''

# Data input
radius = float(input("Enter the radius: "))
pi = 3.14

# Calculate the length of a sphere
length = 2 * pi * radius

# Calculate the area of ​​a sphere
area = pi * radius ** 2

# or

'''

area = pi * (radius * radius)

'''
# The calculation of the sphere is 4/3 and not 3/4
# Calculate the volume of a sphere
volume = 4/3 * pi * radius ** 3

# or

'''
volume = 3/4 * pi * (radius * radius * radius)
'''

# Result
print("The length of a sphere is:", length)
print("The area of a sphere is:", area)
print("The volume of a sphere is:", volume)
