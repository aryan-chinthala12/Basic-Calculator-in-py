#Basic Calculator....

while True:
    print("\t\t\t\t\tCalculator")
    print("-" * 90)
    x=int(input("Enter your first number : "))
    y=int(input("Enter your Second number : "))

    print("what do you wanna use ? \n1] '+' \t2] '-' \t3] '*' \t4] '/' ")
    a=int(input("Enter any option : "))
    match a:
        case 1:
            tot=x+y
            print(f"answer is {tot}.")
        case 2:
            tot=x-y
            print(f"answer is {tot}.")
        case 3:
            tot=x*y
            print(f"answer is {tot}.")
        case 4:
            tot=x/y
            print(f"answer is {tot}.")
        case _:
            print("Invalid option..")
    e=int(input("ENter 0 to end or any other digit to continue : "))
    if e == 0:
        break

    
