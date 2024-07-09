#P4Lab2
#Alaina Barnes
#7/9/24
#Incrementing Multiplication table



integer_choice = int(input("Enter an integer: "))
i = 1
while i <= 12:
 print(f'{integer_choice} * {i} = {integer_choice * i}')
 i += 1
if integer_choice < 0:
 print("This program does not handle negative numbers.")

again = input("Would you like to run the program again? Type 'yes' or 'no': ")
if again == "yes":
 print(integer_choice)
else:
 print("Exiting program...")
        
