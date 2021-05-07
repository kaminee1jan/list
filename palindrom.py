list=["m","a","d","a","m"]
index=-1
b=[]
while index>=(-len(list)):
    b.append(list[index])
    index=index-1
if list==b:
    print("palindrom number")
else:
    print("not palindrom number")