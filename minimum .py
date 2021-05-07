a=[3,6,4,7,5,7,5,7,5,3,2,2,3,3]
min=a[0]
i=0
while i<len(a):
    if a[i]<min:
        min=a[i]
    i+=1
print(min)