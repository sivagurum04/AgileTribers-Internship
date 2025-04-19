odd_count=0
even_count=0
for i in range(10,56):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"{even_count} are even and {odd_count} are odd")