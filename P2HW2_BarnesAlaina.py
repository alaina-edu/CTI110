#Alaina Barnes
#P2HW2
#6/23/24
#Create a list for module grades to find specific grade values





module1 = float(input('Enter grade for Module 1: '))
module2 = float(input('Enter grade for Module 2: '))
module3 = float(input('Enter grade for Module 3: '))
module4 = float(input('Enter grade for Module 4: '))
module5 = float(input('Enter grade for Module 5: '))
module6 = float(input('Enter grade for Module 6: '))

class_grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(class_grades)
highest_grade = max(class_grades)
sum_grades = sum(class_grades)
avg_grades = sum_grades / len(class_grades)

print('--------Results--------')
print(f'{"Lowest Grade:":20s} {lowest_grade:.1f}')
print(f'{"Highest Grade:":20s} {highest_grade:.1f}')
print(f'{"Sum of Grades:":20s} {sum_grades:.1f}')
print(f'{"Average:":20s} {avg_grades:.2f}')
print('-----------------------')

#1. Create a variable for each module's grade
#2. Create a list that contains each module variable
#3. Create variables to find the lowest grade, highest grade, sum of grades, and average of grades
#4. Create f-strings to print the results of each variable
