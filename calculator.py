while True:
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    expression = input("Please choose one of these +,-,*,/ ")

    if expression == "+":
        print(num1+num2)

    elif expression == "-":
        print(num1-num2)

    elif expression == "*":
        print(num1*num2)

    elif expression == "/":
        if num2 == 0:
            print("Invalid cant divide by 0")
        else:
            print(num1/num2)
    else:
        print("Invalid operation. Check again from the options given.")

    if input("Do you wanna do another calculation  (yes/no)").lower() != "yes":
        print("Thanks for using the app")
        break
