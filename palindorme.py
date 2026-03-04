
print("I hvave change this thig for a git just a print line")
print("***********************")
import math

p1=121
p=121

r=0
while p>0:
    res=p%10
    r=r*10 + res
    p=p//10
print(r)
if p1 == r:
    print("yes")
else:
    print("no")

a=7
def prime(a):

    for i in range(2,a):
        if a%i==0:
            print("No a prime")
            return
    print("Prime")

if __name__=="__main__":
    prime(a)

x=456
s=0
while x>0:
    s+=x%10
    x=x//10

print(s)

n=5
d1={}
for i in range(1,n):
    d1[i]=int(math.pow(i,2))
print(d1)