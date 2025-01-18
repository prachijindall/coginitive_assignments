import random
list=random.sample(range(100,900),100)
print(list)

count=0
count1=0
for i in list:
    if i%2==0:
        count=count+1
    else:
        count1=count1+1
print(f"even number {count} and odd number {count1}")

c=0
for k in list:
    def prime(n):
        if n<=1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    if prime(k): 
        c=c+1
print(f"prime numbers are {c}")