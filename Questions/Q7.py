'''
7. (2.0) Read an integer value. Next, calculate the smallest
number of possible bankgrades (grades) into which the value can be decomposed.
The grades considered are 100, 50, 20, 10, 5, 2 and 1.
Next, show the value read and the list of necessary grades.
Prohibited
The input value contains an integer N (0 < N < 1000000).

Exit
Print the read value and then the minimum amount of
grades of each type required as per the example provided
Don't forget to print the end of line after each line,
otherwise your program will display the message: “Error”.

Entrance exit
576 576
5 note(s) of BRL 100.00
1 bill(s) of BRL 50.00
1 bill(s) of BRL 20.00
0 note(s) of BRL 10.00
1 note(s) of BRL 5.00
0 note(s) of BRL 2.00
1 note(s) of BRL 1.00

'''
value = int(input('Enter a value: '))

'''
'//' is integer division

'%' is the remainder of the division

'''
# Calculation of conversions
grades100 = value // 100
value = value % 100

grades50 = value // 50
value = value % 50


grades20 = value // 20
value = value % 20

grades10 = value // 10
value = value % 10

grades5 = value // 5
value = value % 5

grades2 = value // 2
value = value % 2

grades1 = value // 1

# Exit
# print the value read and the minimum amount of grades of each type
print(grades100, "BRL 100.00 note(s)")
print(grades50, "BRL 50.00 note(s)")
print(grades20, "BRL 20.00 note(s)")
print(grades10, "BRL 10.00 note(s)")
print(grades5, "BRL 5.00 note(s)")
print(grades2, "BRL 2.00 note(s)")
print(grades1, "BRL 1.00 note(s)")
