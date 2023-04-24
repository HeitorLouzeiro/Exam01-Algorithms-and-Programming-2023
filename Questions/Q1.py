'''
1. (1.0) Make a program that receives two grades, calculates and
show the weighted average of these grades, considering weight 2
for the first and weight 3 for the second.

'''

# Data input
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))

# Calculate the weighted average
average = (grade1 * 2 + grade2 * 3) / 5

# Result
print("The weighted average is: ", average)
