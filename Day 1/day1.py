a=153
a1=a
res=0
a3=len(str(a))
while(a1>0):
    res+=(a1%10)**a3
    a1=a1//10
print(res)
if a==res:
    print("it is amstrong num")
else:
    print("Not aamstrong num")

s="swiss"
s1={}
for i in s:
    if i not in s1:
        s1[i]=1
    else:
        s1[i]+=1
print(s1)
for i,j in s1.items():
    if j==1:
        print(i)
        break

l1=[1,2,3,6,5,7,4,8]
max=0
max1=0
for i in l1:
    if max<i:
        max=i
print(max)

for i in l1:
    if max1<i and max>i:
        max1=i
print(max1)

t=[1,2,3,4,5,6,7,8,9]
c=0
for i in t:
    if i%2==0:
        c+=1
print(c)

st={1,2,3}
st1={2,3,4}
s3=st.isdisjoint(st1)
print(s3)
f=0
for i in st:
    for j in st1:
        if i==j:
            f=1
            break
if f==0:
    print("True")
else:
    print("False")


d={"Ram": 85, "Lavi": 92, "John": 88}
max=0
str=""
for i,j in d.items():
    if j>max:
        max=j
        str=i
print(max)
print(str)

from abc import ABC, abstractmethod
import re
r="Contact us at test@gmail.com or admin@yahoo.com"
r1=re.findall(r"\b[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,}\b",r)
print(r1)

try:
    a=1
    b=0
    print(a/b)
except ZeroDivisionError as e:
    print("Num  canot be div by zero")

# with open("practice/day1/test1.txt","x")as f:
#     f.write("i love python")
    
c=0
with open("practice/day1/test1.txt","r")as f:
    for i in f:
        w=i.split()
        for j in w:
            if j=="python":
                c+=1
print(c)

with open("practice/day1/test1.txt","r")as f1:
    c1=re.findall(r"\bpython\b",f1.read(),re.IGNORECASE)
print(len(c1))

class Animal:
    def sound(self):
        print("Iuse rto sound")
class Dog(Animal):

    def sound(self):
        # super().sound()
        print("i sound like bowbow")
class Cat(Animal):

    def sound(self):

        print("i sound like meow")


d=Dog()
c=Cat()
d.sound()
c.sound()
a=[Dog(),Cat()]
for i in a:
    i.sound()


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,num):
        self.num=num

    def area(self):
        print(2*self.num)

c=Circle(2)
c.area()

