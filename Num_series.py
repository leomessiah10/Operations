print('This program lets you calculate the sum of a series ')

count = 0
listi = []
sum = 0

while(count == 0):
    num = eval(input('Enter the number'))
    listi.append(num)
    choice = input('Want to enter another number,[y/n]')
    if choice == 'n' or choice == 'N':
        print('The series of num you entered is here\n')
        for  i in listi:
            print(i)
        for add in listi:
            sum+=add
        print('The sum of the series is {}'.format(sum))
        break
    else:
        pass
