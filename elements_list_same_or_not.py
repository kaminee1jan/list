list_numbers = [2,3,15,15,3,2]
i=0
first_element = list_numbers[i]
while i<len(list_numbers):
    if first_element != list_numbers[i]:
        print(i,"all elements are not equal")
    else:
        print(i,"all elements are equal")
    i=i+1
      