def generator():
    for i in range(2,100):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i

g=generator()
for j in g:
    print(j)