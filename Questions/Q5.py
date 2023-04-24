'''
5. (2.0) Write a program that receives an employee's current salary and then
Using the following table, calculate and
show the amount of the increase and the new salary.
Up to BRL 300.00 15%
BRL 300.00 BRL 600.00 10%
BRL 600.00 BRL 900.00 5%
Above BRL 900.00 0%
'''
salary = float(input('Enter your salary: '))

if (salary > 0 and salary <= 300):
    increase = salary * 0.15
elif (salary > 300 and salary < 600):
    increase = salary * 0.10
elif (salary >= 600 and salary <= 900):
    increase = salary * 0.05
elif (salary > 900):
    increase = salary * 0
    print('You will not get a raise in salary.')
else:
    print('Enter a valid value.')

newsalary = salary + increase
print('You will get a raise of %.2f.' % increase)
print('Your new salary is %.2f .' % newsalary)
