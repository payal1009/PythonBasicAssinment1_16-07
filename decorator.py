import time
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        begin=time.time()
        fx(*args,**kwargs)
        end=time.time()
        Total_time=end-begin
        print(Total_time)
        print("thanks...")
    return mfx

@greet
def hello(a):
    print("Hello World")
    print(a)
@greet
def add(a,b,c):
    time.sleep(5)
    print(a+b+c)
@greet
def sub(a,b):
    time.sleep(5)
    print(a-b)
l=[]
@greet
def prime(x,y):
    time.sleep(10)
    for i in range(x,y):
        for j in range(2,x):
            if i%j==0:
                break
        else:
            l.append(i)
hello("a")
add(4,5,6)
sub(10,4)
prime(2,20)
