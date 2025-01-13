a=str(input("enter the string"))
count=0
for i in a:
    if i in 'aeiouAEIOU':
        count=count+1
print(count)
