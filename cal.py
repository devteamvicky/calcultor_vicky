from tabulate import tabulate

def addition (p,q):
    add1=p+q
    print("Sum of Number =\t",add1)

def substraction(p,q):
    sub = p - q
    print("substraction of Number =\t", sub)

def multiplication(p,q):
    multi = p * q
    print("multiplication of Number =\t", multi)

def division(p,q):
    div = p // q
    print("division of Number =\t", div)

while True:
        # print("1.TWO Digit NUMBERS (p,q)")
        # print("2.Three Digit Numbers(p,q,r")
        # print("3.Four Digit Numbers (p,q,r,s)")
        # print("4.Five Digit Numbers(p,q,r,s,t)")

        print("1.Addition")
        print("2.Substraction")
        print("3.Multilplication")
        print("4.Division")


        digit=int(input("Enter the Number "))

        if digit == 1:
            p=int(input("Enter the Number1 = "))
            q=int(input("Enter the Number2 = "))
            addition(p,q)
        if digit == 2:
            p = int(input("Enter the Number1 = "))
            q = int(input("Enter the Number2 = "))
            # r = input(int(" Enter the Number 3 = "))
            substraction(p, q)

        if digit == 3:
            p = int(input("Enter the Number1 = "))
            q = int(input("Enter the Number2 = "))
            multiplication(p, q)
            # r = input(int(" Enter the Number 3 = "))
            # s = input(int("Enter the Number 4 = "))
        if digit == 4:
            p = int(input("Enter the Number1 = "))
            q = int(input("Enter the Number2 = "))
            division(p, q)
            # r = input(int(" Enter the Number 3 = "))
            # s = input(int("Enter the Number 4 = "))
            # t = input(int(" Enter the Number 5 = "))





