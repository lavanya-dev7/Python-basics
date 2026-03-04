l=[1,2,4,5,3,1,2]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

max=0
s=0
for i in l1:
    if max<i:
        max=i
print(max)
for i in l1:
    if s<i and max>i:
        s=i
print(s)

a=[1,8,3,5]
b=[4,6,7,2]
c=a+b
for i in range(len(c)):
    for j in range(len(c)-1-i):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
        
print(c)

x=[1,2,3,4,5,7]
y=[2,7,6,9,8,3]
z=set(x).intersection(set(y))
print(z)

keys = ['a','b','c']
values = [1,2,3]
d={}
for i in range(len(keys)):
    d[keys[i]]=values[i]
    
print(d)

q=2
y=[1,2,3,4]
for i in y:
    y1=y.pop()
    y.insert(0,y1)
    q-=1
    if q==0:
        break
print(y)

a1=[1,2,4,5,7]
b1=[2,3,8,7,9]
c1=[]
for i in a1:
    for j in b1:
        if i==j:
            c1.append(i)
print(c1)

l3=[1,2,3,4,5]
p=l3.pop()
p1=l3.pop(0)
l3.insert(0,p)
l3.insert(len(l3),p1)
print(l3)

t=[('a',1),('b',2)]
d1={}
for i in t:
    key,val=i
    d1[key]=val
print(d1)

o=[1,2,3,4,5,6]
odd=[]
even=[]
for i in o:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

t=(5,12,7,20,15)
l=[]
for i in t:
    if i>10:
        l.append(i)
print(l)

l1=[1,2,3]
l2=[1,2,4]
if len(l1)!=len(l2):
    print("False")
else:
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            print("False")
            break
    print("true")

A = {1,2,3,4}
B = {3,4,5}
c=A-B
print(c)

n=["apple","banana","orange","grape","umbrella"]
c=0

for i in n:
    if i.startswith(('a','e','i','o','u')):
        c+=1
print(c)

