t=(45,89.5,76,45.4,89,92,58,45)
print(t)

print(max(t))
print(t.index(max(t)))

print(min(t))
print(t.count(min(t)))

temp=list(t)
print(temp)
temp.reverse()
print(temp)

x=float(input("enter"))
for i in temp:
    if i==x:
       
        flag=1
        break
    else:
        flag=0
        
if flag==1:
      print(temp.index(i))
else:
   
    print("not present")

    