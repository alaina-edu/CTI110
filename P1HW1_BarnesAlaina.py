# Alaina Barnes
 # 6/13/24
 # P1HW1
 # Recreating mathematical expressions

print('-----Calculating Exponets-----')

base_value = int(input('Enter an integer as the base value: '))
ex_value = int(input('Enter an integer as the exponent: '))
ex_solve = pow(base_value, ex_value)

print(base_value, 'raised to the power of', ex_value, 'is', ex_solve, '!!!')


print('-----Addition and Subraction-----')

first_val = int(input('Enter a starting integer: '))
sec_val = int(input('Enter an integer to add: '))
thrd_val = int(input('Enter an integer to subtract: '))
as_solve = first_val + sec_val - thrd_val

print(first_val, '+', sec_val, '-', thrd_val, 'is equal to', as_solve)
