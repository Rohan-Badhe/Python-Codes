#write a program which contain one function that accept one number from the user and returns true if number is divisible by b5  otherwise return gfalse
def is_divisible_by_5(num):
    return num % 5 == 0
num=int(input("Enter the number:"))
if is_divisible_by_5(num):
    print("The number is divisible by 5")
else:
        print("The number is not divisible by 5")

