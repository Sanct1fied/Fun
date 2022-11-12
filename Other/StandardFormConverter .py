userinput = input('is your number less than or greater than 1?:')

if userinput in ['greater']:
    number = int(input('what number do you want turned into a power'))
    if number > 0:
        while number < 1000:
            print("that number is too small")
            number = int(input('what number do you want turned into a power'))
        else:
            temp = [char for char in str(number)]
            standardform = ['', '', '', '']
            for i in range(4):
                standardform[i] = temp[i]
            rounder = int(standardform[2])
            if int(standardform[3]) >= 5:
                rounder += 1
            else:
                pass
    else:
        print('error')

    power = len(temp) - 1
    finalnum = standardform[0] + '.' + standardform[1] + str(rounder) + 'x10' + '^' + str(power)
    print(finalnum)
else:
    number = input('what number do you want turned into a power')
    decimal = float(number)
    if decimal < 1:
        temp = [char for char in str(decimal)]
        standardform = ['', '', '', '']
        temp.remove('.')
        print(temp)
    if len(temp) > 7:
        if int(temp[2]) >= 5:
            temp[1] += 1
        else:
            pass

    power = (temp[-3]+ temp[-2]+ temp[-1])
    finalnum = temp[0] + '.' + temp[1] + 'x10' + '^' + str(power)
    print(finalnum)
