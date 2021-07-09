a=[[5,6,7,8],[2,1,3,4]]
i=0
sum1=0
k=1
while i<len(a):
    j=0
    list1=[]
    while j<len(a[i]):
        sum1=a[i][j]+a[k][j]
        list1.append(sum1)
        j=j+1
    print(list1)
    break
    i=i+1