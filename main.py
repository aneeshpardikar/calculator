num1 = float(input("Enter 1st no.: "))
num2 = float(input("Enter 2nd no.: "))

operator = input("Select an operator + - * / : ")

if operator == "+" :
    print("\nSum of two numbers is: ",num1+num2)
elif operator == "-" :
    print("\nDifference of two numbers is: ", num1-num2)
elif operator == "*" :
    print("\nProduct of two numbers is: ", num1*num2)
elif operator == "/" :
    print("\nQuotient of two numbers is: ", num1/num2)
else :
    print("Select a valid operator")