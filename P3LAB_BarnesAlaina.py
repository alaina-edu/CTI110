# P3LAB
# Alaina Barnes
# 6/30/24
# Coin counter program

#create variable for money
money = float(input('Enter the amount of money as a float: $'))

#convert the float into an integer and create variables for dollars and cents
money_int = int(money * 100)

dollars = money_int // 100
cents = money_int - (dollars * 100)

#deterime floor divison amounts for the value that corresponds with each coin type
quarters = cents // 25
dimes = (cents - (quarters * 25)) // 10
nickels = (cents - (quarters * 25) - (dimes * 10)) // 5
pennies = (cents - (quarters * 25) - (dimes * 10) - (nickels * 5))

#create if else statemets for each coin type to deterime how it should be printed

if dollars == 0 and cents == 0:
 print('No Change')

if dollars > 1:
 print(f'{dollars} Dollars')
elif dollars == 1:
 print(f'{dollars} Dollar')
else:
 pass

if quarters > 1:
 print(f'{quarters} Quarters')
elif quarters == 1:
 print(f'{quarters} Quarter')
else:
 pass

if dimes > 1:
 print(f'{dimes} Dimes')
elif dimes == 1:
 print(f'{dimes} Dime')
else:
 pass

if nickels > 1:
 print(f'{nickels} Nickels')
elif nickels == 1:
 print(f'{nickels} Nickel')
else:
 pass

if pennies > 1:
 print(f'{pennies} Pennies')
elif pennies == 1:
 print(f'{pennies} Penny')
else:
 pass



