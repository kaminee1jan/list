num=int(input("enter the number"))
i=0
while i<num:
    num1=int(input("enter the number"))
    if num1>=0:
        if num==0:
            print("zer0")
        else:
            print("positive number")
        i=i+1
    else:
        print("nigetive number")
    if num1%2==0:
        print("even",num1)
    else:
        print("odd",num1)
 
