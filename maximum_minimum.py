a=[1,2,3,4,5,6,7,8,9,10]
i=0
min_1=a[0]
max_1=0
while i<len(a):
    if a[i]<min_1:
        min_1=a[i]
    if a[i]>max_1:
        max_1=a[i]
        i=i+1
print(max_1)
print(min_1)

