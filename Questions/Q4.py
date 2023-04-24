'''
4. (1.0) Make a program that receives the year of birth
of a person and the current year,
calculate and show:
● that person's age in years;
● that person's age in months;
● that person's age in days;
● that person's age in hours.

'''

# Data input
year_birth = int(input("Enter year of birth: "))
current_year = int(input("Enter the current year: "))

# Calculation of conversions
age_years = current_year - year_birth
age_months = age_years * 12
age_days = age_years * 365
age_hours = age_days * 24

# Result
print('\nAge in years:', age_years)
print('Age in months:', age_months)
print('Age in days:', age_days)
print('Age in hours:', age_hours)
