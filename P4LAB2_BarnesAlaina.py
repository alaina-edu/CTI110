#P4Lab2
#Alaina Barnes
#7/9/24
#Incrementing Multiplication table with while and for loops


mult_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


##if integer_choice >= 0:
## for i in mult_table:
##  print(f'{integer_choice} * {mult_table[i]} = {integer_choice * mult_table[i]}')
## i += 1
##if integer_choice < 0:
## print("This program does not handle negative numbers.")

#again = input("Would you like to run the program again? Type 'yes' or 'no': ")
#if again == "yes":
# print(integer_choice)
#else:
# print("Exiting program...")

while True:
 integer_choice = int(input("Enter an integer: "))  
 if integer_choice >= 0:
  for i in mult_table:
   print(f'{integer_choice} * {mult_table[i]} = {integer_choice * mult_table[i]}')
  i += 1
 if integer_choice < 0:
  print("This program does not handle negative numbers.")
 again = input("Would you like to run the program again? Type 'yes' or 'no': ")
 if again == "yes":
  continue
 else:
  break
 print("Exiting program...")