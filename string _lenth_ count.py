list=["abc","xyz","aba","1221"]
i=0
c=0
while i<len(list):
    if len(list[i])>=2 and list[i][0]==list[i][-1]:
        c=c+1
    i=i+1
print(c)