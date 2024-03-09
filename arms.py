def arms(a):
    rem = 0
    res = 0
    temp = a
    while a != 0:
        rem = int(a % 10)
        res = (res * 10) + rem
        a = int(a / 10)
    if res == temp:
        return 0
    else:
        return 1


a = int(input("Enter a number a"))
if arms(a) == 0:
    print("The given number is an armstrong number")
else:
    print("The given number is not an armstrong number")
