'''Write a menu driven python program to accept the values of two integers and perform the following arithmetic operations on them
1. ADD
2. SUB
3. DIV
4. MUL
5. EXIT
'''

import sys   #sys is a built-in module 

num1 = int(input('Enter First No.::'))
num2 = int(input('Enter Second No.::'))

print("TODAY's MENU\n")
print("1.Add\n2.Sub\n3.Div\n4.Mul\n5.Exit\n")
ch = int(input('Enter your choice::'))

if ch==1:
    print("Addition = ", num1+num2)
elif ch==2:
    print("Subtraction = ", num1-num2)
elif ch==3:
    print("Division = ", num1/num2)
elif ch==4:
    print("Multiplication = ", num1*num2)
elif ch==5:
    print("You choose to exit...")
    sys.exit(0)
else:
    print("Enter proper choice...")
    