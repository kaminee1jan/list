elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even_count=0
odd_count=0
s_count=0
even_sum=0
odd_sum=0
s_sum=0

while i<len(elements):
    if elements[i]%2==0:
        even_count=even_count+1
        even_sum=even_sum+elements[i]
    else:
        odd_count=odd_count+1
        odd_sum=odd_sum+elements[i]
    s_sum=s_sum+even_sum+odd_sum
    i=i+1
print("even_count",even_count)
print("even_sum",even_sum)
print("even_average",even_sum/even_count)
print("odd_count",odd_count)
print("odd_sum",odd_sum)
print("odd_average",odd_sum/odd_count)
print("s_count",i)
print("s_sum",s_sum)
print("s_average",s_sum/i)