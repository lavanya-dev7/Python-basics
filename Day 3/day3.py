n=6
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
print(sum)
if sum==n:
    print("It is perfect num")
else:
    print("Not a perect num")

s="Hello World"
st=""
s1=s.split()
for i in s1:
    rev=""
    for j in i:
        rev=j+rev
    st+=rev +" "
print(st)

l=[10, 20, 4, 45, 99]
max=0
smax=0
for i in l:
    if i>max:
        max=i
for j in l:
    if j>smax and j<max:
        smax=j
print(smax)

t=(3, 5, 9, 12, 14)
c=0
for i in t:
    if i%3==0:
        c+=1
print(c)

A = {1,2,3,4}
B = {3,4,5,6}
C=A.intersection(B)
print(C)
s=set()
for i in A:
    for j in B:
        if i==j:
            s.add(i)
print(s)

d={"Ram": 85, "Lavi": 92, "John": 70}
m=d["Ram"]
s=""
print(m)
for i,j in d.items():
    if j<m:
        m=j
        s=i
print(m,s)

import re
r="My marks are 85 and 90"
r1=re.findall(r"\d+",r)
print(r1)
try:
    with open("python/practice/Day 3/day3.txt","x") as f:
        f.write("Java\nPyhon\nC++")
except FileExistsError as e:
    print("File found")
with open("python/practice/Day 3/day3.txt","r") as f:
   s=f.readlines()
   count=0
   for i in s:
       count+=1
print(count)


try:
    a=int(input("Enter a num"))
except ValueError as e:
    print("Invalid number")


class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Student(Person):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
    def display(self):
        super().display()
        print(self.age)

s=Student("KArthi",22)
s.display()

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        print(self.a*self.a)

s1=Square(4)
s1.area()

class Dog:
    def sound(self):
        print("I sound like bow bow")
class  Cat:
    def sound(self):
        print("I sound like meow moew")

def animalsound(obj):
    obj.sound()

d=Dog()
c=Cat()

animalsound(d)
animalsound(c)


