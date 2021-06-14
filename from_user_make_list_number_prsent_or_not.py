list1=[]
i=0
user=int(input("enter the  number"))
while i<=user:
    user1=int(input("enter the number"))
    list1.append(user1)
    i=i+1
print(list1)
asking_user=int(input("enter the number"))
if asking_user in list1:
    print(True)
else:
    print(False)

