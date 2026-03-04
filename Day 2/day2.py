from itertools import count
import math


a=76
b=32
l=[]
l1=[]
c=math.gcd(a,b)
print(c)
for i in range(1,a+1):
    if a%i==0:
        l.append(i)
print(l)
for i in range(1,b+1):
    if b%i==0:
        l1.append(i)
print(l1)
l2=[]
for i in l:
    for j in l1:
        if i==j:
            l2.append(i)
print(l2)
d=max(l2)
print(d)


gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD is:", gcd)

while b!=0:
    a,b=b,a%b
print(a)

s="programming"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

l=[1,2,3,4,5]
j=2
for i in l:
    if j>0:
        p=l.pop(0)
        l.append(p)
        j-=1
print(l)

t=(1, 2, 2, 3, 4, 4, 5)
t1=set(t)

print(tuple(t1))
s1= {1,2,3,4}
s2= {3,4,5,6}
s3=s1.symmetric_difference(s2)
print(s3)
s4=set()
for i in s1:
    if i not in s2:
        s4.add(i)

for i in s2:
    if i not in s1:
        s4.add(i)
print(s4)

d={'a': 1, 'b': 2, 'c': 1}
d1={}
for i,j in d.items():
    if j not in d1:
        d1[j]=[i]
    else:
        d1[j].append(i)
print(d1)

import re
r="Call me at 9876543210 or 9123456789"
r1=re.findall(r"[6-9]\d{9}",r)
print(r1)

try:
    with open("practice/day2/test2.txt","x") as f:
        f.write("Python is powerful and beautiful")
except FileExistsError as e:
    print("FIle alredy exists")


with open("practice/day2/test2.txt","r") as f:
        max=0
        s1=""
        f1=f.read()
        s=f1.split()
        for i in s:
            j=len(i)
            if j>max:
                max=j
                s1=i

print(s1)
print(max)

try:
    num=7
    div=0
    c=num/div
except ValueError as e:
    print("Invalid input enter a valid num")
except ZeroDivisionError as e:
    print("Cannot div by zero")


class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
class Manager(Employee):
    def __init__(self, name, sal,dpt):
        super().__init__(name, sal)
        self.dpt=dpt
    def display(self):
        print(f"Name:{self.name} \nSalary:{self.sal}\nDepartment:{self.dpt}")

m=Manager("Lavanya",70000,"developer")
m.display()


from abc import ABC , abstractmethod
class Vechical(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vechical):
    def start(self):
        print("i start a car")
class Bike(Vechical):
    def start(self):
        print("i start a bike")
c=Car()
b=Bike()
c.start()
b.start()

class Shape():
    def __init__(self,n):
        self.n=n
    def area(self):
        print(self.n)
class Circle(Shape):
    def __init__(self,n):
        super().__init__(n)
    def area(self):
        print(self.n*2)

class Reactangle(Shape):
    def __init__(self,n,l):
        super().__init__(n)
        self.l=l
    def area(self):
        print(self.n*self.l)


b=[Circle(2),Reactangle(2,4)]
for i in b:
    i.area()

#another mehod
def printarea(s):
    s.area()
#another method
c = Circle(2)
r = Reactangle(2, 4)

printarea(c)
printarea(r)