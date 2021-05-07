a=[1,6,5,8,4]
max_1=0
smax=0
i=0
while i<len(a):
    if a[i]>max_1:
        smax=max_1
        max_1=a[i]
        
        if smax<a[i] and max_1>a[i]:
            max_1=a[i]
    i=i+1
print(max_1,smax)