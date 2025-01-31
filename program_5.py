#write a program which accept number from user and check number positive negative or zero
def check_number():
        num=float(input("Enter the number:"))
        
        if num >0:
            print("Positive")
            
        elif num<0:
            print("Negative")
        else:
            print("Zero")
check_number()            
            
    
