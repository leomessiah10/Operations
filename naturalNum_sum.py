print('This program evaluates the sum of the ')
print('first natural numbers that you give\n')

sum = 0
count = 0

while(count == 0):
    num = eval(input('Enter the naturral number'))

    for add in range(1,num+1):
        sum += add

    print('The sum of natural numbers upto{} is {}'.format(num,sum))
    choice = input('Find the sum of another number, [y/n]')
    if choice == 'n' or choice == 'N':
        print('Hope u find it good.!')
        break

    else:
        pass
