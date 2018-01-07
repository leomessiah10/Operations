import math

print(
    '''
        This program helps you to calculate the 
        cost of pizza according to it's size,
        So,let's enjoy!!
    '''
     )
diameter = eval(input('Enter the diameter of the pizza'))

radius = diameter/2

area = round(math.pi,2) * radius **2

print('The area of the pizza is {}'.format(area))

cost = area*1/100

print('The cost of the pizza is {}'.format(cost))
