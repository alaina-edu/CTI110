# P3HW2
# Alaina Barnes
# 6/28/24
# Creating a program that calculates a paycheck


# create variables for name, hours worked, and pay rate 
full_name = input("Enter employee's name or enter \"Done\" to terminate: ")
#hours_worked = float(input('Enter number of hours worked: '))
#pay_rate = float(input("Enter employee's pay rate: "))
#print('------------------------')

# print employee name and first time of text
##while full_name != "Done":
## print(f'Employee name: {full_name}')
## hours_worked = float(input('Enter number of hours worked: '))
## pay_rate = float(input("Enter employee's pay rate: "))
## print('------------------------')
## full_name = input("Enter employee's name or enter \"Done\" to terminate: ")
 
##else:
## print(f'{end}')    


#print(f'Employee name: {full_name}')

while full_name != "Done":
 print(f'Employee name: {full_name}')
 hours_worked = float(input('Enter number of hours worked: '))
 pay_rate = float(input("Enter employee's pay rate: "))
 print('------------------------')
 print(f'{"Hours Worked":15s} {"Pay Rate":10s} {"OverTime":10s} {"OverTime Pay":15s} {"RegHour Pay":15s} {"Gross Pay":10s}')
 print('-' * 80)
 if hours_worked > 40:
  overtime_hours = hours_worked - 40
 else:
  overtime_hours = 0

 if overtime_hours > 0:
  reg_hours = hours_worked - overtime_hours
 else:
  reg_hours = hours_worked

 reg_pay = reg_hours * pay_rate

 overtime_rate = pay_rate * 1.5

 overtime_pay = overtime_hours * overtime_rate

 gross_pay = reg_pay + overtime_pay

 ending = print(f'{hours_worked:<15.1f} {pay_rate:<10.1f} {overtime_hours:<10.1f} {overtime_pay:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<10.2f}')
 full_name = input("Enter employee's name or enter \"Done\" to terminate: ")
else:
 print(f'{ending}')   
#print(f'{hours_worked:<15.1f} {pay_rate:<10.1f} {overtime_hours:<10.1f} {overtime_pay:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<10.2f}')


