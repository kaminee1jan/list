list1=[]
i=1
user=int(input("enter the  number"))
while i<=user:
    user1=int(input("enter the number"))
    list1.append(user1)
    i=i+1
copy_list2=[]
counter=len(list1)-1
while counter>=0:
    copy_list2.append(list1[counter])
    counter=counter-1
print(list1)
print(copy_list2)