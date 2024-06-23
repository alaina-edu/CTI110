#Alaina Barnes
#6/20/2024
#P2Lab1
#Using Math Expressions
import math

radius = float(input('Enter the radius: '))

circum = 2 * math.pi * radius
diameter = 2 * radius
area = math.pi * (radius ** 2)

print(f'The diameter of the circle is {diameter:.1f}')
print(f'The circumference of the circle is {circum:.2f}')
print(f'The area of the circle is {area:.3f}')
