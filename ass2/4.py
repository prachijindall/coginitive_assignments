a={34,56,78,90}
b={78,45,90,23}
print(a|b)

print(a&b)

print(a-b)

print(a.issubset(b))
print(b.issuperset(a))

x=int(input("enter"))
for i in a:
    if i==x:
      
        flag=1
        break
        
    else:
        flag=0

if flag==0:
    print("not present")
else:
    a.remove(x)
    print(a)