'''
6. (2.0) A bank branch has two types of investments,
according to the chart below. Make a program that receives the
type of investment and its value, calculate and display the
value corrected after one month and twelve months of investment,
according to the type of investment.


1 - 3% savings
2 - Fixed income funds 4%

'''

investment_value = float(input('Enter the investment amount: '))
print('1 - Savings 3%, 2 - Fixed income funds 4%')
investment_type = int(input('Enter investment type: '))

# Calculation of conversions
if (investment_type == 1):
    corrected_value = investment_value * 1.03
    twelve_month_corrected_value = corrected_value * 1.03 ** 12

elif (investment_type == 2):
    corrected_value = investment_value * 1.04
    twelve_month_corrected_value = corrected_value * 1.04 ** 12
else:
    print('Enter a valid value.')

print('Value corrected after one month: %.2f' % corrected_value)
print('Amount corrected after twelve months: %.2f' %
      twelve_month_corrected_value)
