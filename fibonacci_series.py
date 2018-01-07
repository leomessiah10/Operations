print('In this program we will play with fibonacci sequence')

first_num = 1
sec_num = 1
fibo_list = [1,1]
count = 0

while(count == 0):
    num = eval(input('Upto which number you want the sequence\n:-'))

    for i in range(num-2):
        temp = sec_num + first_num
        first_num = sec_num
        sec_num = temp
        fibo_list.append(temp)

    print(fibo_list,'\n')

    res_num = eval(input('Which number you want to see from the sequence\n:-'))

    print(fibo_list[res_num])

    choice = input("Wanna try once again,[y/n]")
    if choice == 'n' or choice == 'N':
        print('Hope you have enjoyed!!')
        break
    else:
        pass
