
n=[10,11,12,13,14,17,18,19]
i=0
b=[]
k=0
while i<len(n):
    j=i
    while j<len(n):
        if n[i]+n[j]==30:
            b.append([])
            b[k].append(n[i])
            b[k].append(n[j])
            k=k+1
        j=j+1
    i=i+1
print(b)
