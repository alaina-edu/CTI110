# Alaina Barnes
 # 6/23/24
 # P2HW1
 # Expense tracker Part 2

budget = float(input('Enter Budget: '))
city = input('Enter Destination: ')
gas = float(input('How much will you spend on gas?: '))
hotel = float(input('How much will you need for accodations/hotel?: '))
food = float(input('Lastly, how much will you need for food?: '))
total_spend = gas + hotel + food
remaining = budget - total_spend



print('-----Travel Expenses-----')
print(f'{"Location: ":20s} {city}')
print(f'{"Inital Budget: ":20s} ${budget:.2f}')

print(f'{"Fuel: ":20s} ${gas:.2f}')
print(f'{"Accodations: ":20s} ${hotel:.2f}')
print(f'{"Food: ":20s} ${food:.2f}')

print('-------------------------')
print(f'{"Remaining Balance: ":20s} ${remaining:.2f}')

# 1. Get inital budget amount and destination name
# 2. Get totals for gas, food, and accomadations
# 3. Add gas, food, and accomadation amounts (total spend)
# 4. Subtract total spend from the orignal budget
# 5. Run program to display remaining budget balance
