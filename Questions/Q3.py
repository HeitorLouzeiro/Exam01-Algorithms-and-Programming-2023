'''
3. (1.0) Write a program that receives the amount of money
in Reais that a person who is going to travel has.
She will pass through several countries and needs to convert her money into
dollars, German mark and British pound.
It is known that the exchange rate for the dollar is R$5.04;
for the German mark, R$ 2.83; and the pound sterling, of BRL 6.27
The program must do the conversions and display them.

'''

# Data input
money = float(input("Enter the amount of money in dollars: "))

dollar = 5.04
milestone = 2.83
pound = 6.27

# Calculation of conversions
dollar = money / dollar
milestone = money / milestone
pound = money / pound

# Result
print('Converted to Dollar:', dollar)
print('Converted to German mark:', milestone)
print('Converted to sterling:', pound)
