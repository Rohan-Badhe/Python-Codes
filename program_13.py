#fibinacci series
num=int(input("Enter the number:"))
a,b=0,1
for i in range(num):
    print(a)
    a,b=b,a+b
