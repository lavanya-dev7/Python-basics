s="Lavanya"
v="AEIOUaeiou"
vou=0
c=0
for i in s:
    if i in v:
      
        vou+=1
    else:
        c+=1
       
print(vou)
print(c)

a="listen"
b="silent"
s="".join(sorted(a))
s1="".join(sorted(b))
if s == s1:
    print("yes")
else:
    print("no")
x="Lavanya"
f={}
for i in x:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1
print(f)

x1="aabbcde"
f1={}
for i in x1:
    if i not in f1:
        f1[i]=1
    else:
        f1[i]+=1
print(f1)

for i,j in f1.items():
    if j==1:
        print(i)
        break

y1="programming"
f2={}
s=""
for i in y1:
    if i not in f2:
        f2[i]=1
    else:
        f2[i]+=1
print(f2)

for i,j in f2.items():
    s+=i
print(s)

s="LavdNydKearhEugsn"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
u=0
l=0
for i in s:
    if i in upper:
        u+=1
    else:
        l+=1
print(u)
print(l)

d={'a':1,'b':2,'c':4}
for i, j in d.items():
    if j%2==0:
        print(i)

s1=["hi","hello","python"]
max=0
l=s1[0]
for i in s1:
    if max<len(i):
        max=len(i)
        l=i  
print(l)
print(max)

s2="madam"
s3=""
for i in s2:
    s3=i+s3
print(s3)
if s2==s3:
    print("Yes")
else:
    print("No")

s4="I love programming language"
s5=s4.split()
print(s5)

s5="Hello World Python"
s6=s5.replace(" ","-")
print(s6)