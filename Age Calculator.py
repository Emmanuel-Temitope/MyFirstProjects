# Age Calculator

name = input('Enter your name : ')

Age = input('Enter your age : ')

print(f"Your Name is {name} and You Are {Age} Years Of Age\n")
if int(Age)< 18:
    print('\nCome Later When You Are Older')
else:
    print('You Can Now Access The Calculator ')
    A = input('Enter Your First Digits: ')
    B = input('Enter Your Second Digits: ')
    op = input('Choose an operator: * , + , -, / ==> ')
    if op == '*':
        P = float(A) * float(B)
        print('The Answer is ' + str(P))
    if op == '+':
        P = float(A) + (B)
        print('The Answer is ' + str(P))
    if op == '-':
        P = float(A) - float(B)
        print('The Answer is ' + str(P))
    if op == '/':
        P = float(A) / float(B)
        print('The Answer is ' + str(P))
    print('Thanks for supporting me with your Laptop')
    