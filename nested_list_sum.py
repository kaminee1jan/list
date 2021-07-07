list1=[[1,5,6],[2,9,8],[5,9,10]]
i=0
while i<len(list1):
    sum=0
    j=0
    while j<len(list1[i]):
        sum=sum+list1[i][j]
        j=j+1
    i=i+1
    print(sum)
