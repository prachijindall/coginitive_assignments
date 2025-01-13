f=open("file.txt",'w')
f.write("hello world")
f.close()

f=open("file.txt",'r')
txt=f.read()
print(txt)
f.close()
