import sys 
print("START") 
num1 = int(input('Enter First No.::'))
num2 = int(input('Enter Second No.::'))

while True: 
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
   
    response = input('Wish to continue?(yes/no) ::') 
    
    if response.lower() == "no":
        finalResponse = input("Are you sure(yes/no) ? ::")
        if finalResponse.lower()=="yes":
            print("Thank you. Visit again !")
            break      
            
print("END")