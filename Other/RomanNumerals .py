def arabictoroman():
    user_num = int(input("what is the number you want translated? (Up to 1000):"))
    global number
    number = [char for char in str(user_num)]

    if len(number) == 1:
        st_digit = one_digit()
        print(st_digit)
    elif len(number) == 2:
        nd_digit = two_digits()
        st_digit = one_digit()
        print(nd_digit, st_digit, sep='')
    elif len(number) == 3:
        rd_digit = three_digits()
        nd_digit = two_digits()
        st_digit = one_digit()
        print(rd_digit, nd_digit, st_digit, sep='')
    if user_num == 1000:
        print("M")


def romantoarabic():
    user_num = int(input("what is the roman numeral you want translated? (Up to 1000):"))
    number = [char for char in str(user_num)]
    for i in range(len(number)):
        total = 0
        if number[i] == "I":
            total = + 1
        elif number[i] == "V":
            total += 5
        elif number[i] == "X":
            total += 10
        elif number[i] == "L":
            total += 50
        elif number[i] == "C":
            total += 100
        elif number[i] == "D":
            total += 500
        elif number[i] == "M":
            total += 1000
        print(total)


def one_digit():
    first_digit = ""
    if int(number[-1]) <= 3:
        first_digit = "I" * int(number[-1])
    elif int(number[-1]) == 4:
        first_digit = "IV"
    elif 5 <= int(number[-1]) < 9:
        first_digit = "V" + ("I" * (int(number[-1]) - 5))
    elif int(number[-1]) == 9:
        first_digit = "IX"
    return first_digit


def two_digits():
    second_digit = ""
    if int(number[-2]) <= 3:
        second_digit = "X" * int(number[-2])
    elif int(number[-2]) == 4:
        second_digit = "XL"
    elif 5 <= int(number[-2]) < 9:
        second_digit = "L" + ("X" * (int(number[-2]) - 5))
    elif int(number[-2]) == 9:
        second_digit = "XC"
    return second_digit


def three_digits():
    third_digit = ""
    if int(number[-3]) <= 3:
        third_digit = "C" * int(number[-3])
    elif int(number[-3]) == 4:
        third_digit = "CD"
    elif 5 <= int(number[-3]) < 9:
        third_digit = "D" + ("C" * (int(number[-3]) - 5))
    elif int(number[-2]) == 9:
        third_digit = "CM"
    return third_digit

while True:
    print("would you like to translate denary into roman numerals (dtr)?")
    which_one = input("or roman numerals into denary (rtd)?")
    if which_one == "dtr":
        arabictoroman()
    else:
        romantoarabic()
    continuee = input("would you like to translate another number?:")
    if continuee in ["no"]:
        break
