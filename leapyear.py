year = int(input('which year do you want to check\n'))
by4 = year%4
by100 = year%100
by400 = year%400
if by4 == 0:
    if by100 !=0:
        if by400 == 0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print("not leap year")
