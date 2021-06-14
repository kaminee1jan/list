i=0
empty=[]
empty1=[]
user=int(input("enter the number"))
while i<=user:
    user1=int(input("enter the number"))
    empty.append(user1)
    while i<len(empty):
        if empty[i] not in empty1:
            empty1.append(empty[i])
        i=i+1
print(empty)
print(empty1)