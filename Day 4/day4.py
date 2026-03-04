
n=145
s=0
n1=n
while(n>0):
    res=n%10
    f=1
    for i in range(1,res+1):
        f=f*i
    s+=f
    f=1
    n=n//10
print(s)
if s==n1:
    print("Strong num")

num=18
num1=num
sum=0
while(num1>0):
    res=num1%10
    sum+=res
    num1=num1//10
if num%sum==0:
    print("Hardest num")

s="aaabbccccd"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
s=""
for i,j in d.items():
    s+=i
    s+=str(j)
print(s)

s1="engineeering"
d1={}
s2=""
max=0
for i in s1:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
print(d1)
for i,j in d1.items():
    if j>max:
        max=j
        s2=i
print(s2)

l = [2,4,3,5,7,8]
t = 7
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if i+j==t:
            print((i,j))



tup=(2,4,5,8,11,15)
t=()
ls=[]
def isprime(n) ->  bool:
    for i in range(2,n):
        if n==2:
            return True
        if n%i==0:
            return False
    return True

for i in tup:
    if isprime(i):
        ls.append(i)
        t+=(i,)
print(tuple(ls))
print(t)

t1=(1, "hi", 3, 4.5, 7)
count=0
for i in t1:
    if type(i)==int:
        count+=1
print(count)



s=["192.168.1.1","10.0.0.1","192.168.1.1"]
s1=set()
for i in s:
    if i not in s1:
        s1.add(i)
print(s1)

s1 = {1, 2, 3, 4}
s2 = {2, 3, 5}
s3 = {2, 3, 6}
res=set()
for i in s1:
    if i in s2 and i in s3:
        res.add(i)
print(res)
s4=s1&s2&s3
print(s4)

d={
"Gig0/0": "Up",
"Gig0/1": "Down",
"Gig0/2": "Up"
}
for i,j in d.items():
    if j =="Down":
        print(i)

inp=[1,2,3,4,5,6]
dic={
    "even":[],
    "odd":[]
}
for i in inp:
    if i%2==0:
        dic["even"].append(i)
    else:
        dic["odd"].append(i)
print(dic)

import re
r="Client 192.168.1.10 connected to 10.0.0.5 but failed at 256.300.1.1"
r1=re.findall(r"(?:(?:25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)",r)
print(r1)

r2="00:1A:2B:3C:4D:5E and AA-BB-CC-DD-EE-FF"
r3=re.findall(r"(?:(?:[A-F0-9:-]+)){5}(?:[A-F0-9]+)",r2)
print(r3)

p=r"(?:(?:25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)"
l=[]
with open("python/practice/Day 4/day4.txt","r") as f:
    for i in f:
        ip=i.strip()
        if re.fullmatch(p,ip):
            l.append(ip)
print(l)

n=[10,20,30,40,50]
try:
    index=int(input("Enter index:"))
    print(index,"is",n[index])
except IndexError as e:
    print("Error no foudn")
except ValueError as e:
    print("Enter a value")

finally:
    print("program finished")


class Device:
    def __init__(self,ip):
        self.ip=ip

    def display(self):
        print(self.ip)

class Switch(Device):
    def __init__(self,ip,brand):
        super().__init__(ip)
        self.brand=brand

    def display(self):
        super().display()
        print(self.brand)
s=Switch("192.74.23.7","Cisco")
s.display() 

from abc import ABC,abstractmethod
class Network(ABC):
    @abstractmethod
    def connect(self):
        pass
class Router(Network):
    def __init__(self,brand):
        self.brand=brand
    def connect(self):
        print(self.brand)
r=Router("Cisco")
r.connect()        

class TCPConnection :
    def transfer(self):
        print("hello i am tcp")
class UDPConnection:
    def transfer(self):
        print("Hello i am udp")
def net(obj):
    obj.transfer()

u=UDPConnection()
t=TCPConnection()

net(u)
net(t)


