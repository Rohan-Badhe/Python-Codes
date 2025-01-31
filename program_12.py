#create a calculator  to perform basic operation
num1=float(input("Enter the number:"))
num2=float(input("Enter the number:"))
operation=input("Enter the operation(+,-,*,/):")
if operation =='+':
        print(num1+num2)
elif operation =='-':
        print(num1-num2)
elif operation =='*':
        print(num1*num2)
elif operation =='/':
        print(num1/num2 if num2 != 0 else "Error:Division by zero")
else:
        print("Invalid operation")
        



   
