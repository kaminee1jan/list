name="navgurukul"
i=0
new_list=[]
count=0
empty=[]
while i<len(name):
    new_list.append(name[i])
    count=count+1
    j=0
    c=0
    while j<len(name):
        if name[j] ==name[i]:
            c=c+1
        j=j+1
    if [name[i],c] not in empty:
        empty.append([name[i],c])
    i=i+1
print(new_list)
print(count)
print(empty)
