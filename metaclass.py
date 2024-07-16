import sample1, sample2
from sample1 import Testclass1
from sample2 import Testclass2
Test=type('Test',(sample1.TestClass1,sample2.TestClass2,),{"x":5,"y":6,})
t = Test()
print(t.x)
