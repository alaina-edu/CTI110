# Alaina Barnes
 # 6/14/24
 # P1HW2
 # Expense tracker

budget = int(input('Enter Budget: '))
city = input('Enter Destination: ')
gas = int(input('How much will you spend on gas?: '))
hotel = int(input('How much will you need for accodations/hotel?: '))
food = int(input('Lastly, how much will you need for food?: '))
total_spend = gas + hotel + food
remaining = budget - total_spend

print('-----Travel Expenses-----')
print('Location: ', city)
print('Inital Budget: ', budget)

print('Fuel: ', gas)
print('Accodations: ', hotel)
print('Food: ', food)

print('Remaining Balance: ', remaining)

# 1. Get inital budget amount and destination name
# 2. Get totals for gas, food, and accomadations
# 3. Add gas, food, and accomadation amounts (total spend)
# 4. Subtract total spend from the orignal budget
# 5. Run program to display remaining budget balance
