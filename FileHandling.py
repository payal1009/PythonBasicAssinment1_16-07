f=open("file.txt",'r')
text=f.read()
print(text)
f.close()
c=dict()
w=text.split()
print(w)
for word in w:
    if word in c:
        c[word]+=1
    else:
        c[word]=1
print(c)
str=str(c) 
f2=open('output.txt','w')
f2.write(str)
