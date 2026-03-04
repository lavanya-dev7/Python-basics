n=2
sum=(n)//2
print(sum)
for i in range(1,sum+1):
    print(i,n-1)
    n-=1

a="silent"
b="listen"

c="".join(sorted(a))
d="".join(sorted(b))
print(c)
print(d)
if c==d:
    print("It is anagram")
else:
    print("It is not")


l=[1,2,3,4,[1,2,3,4,[9,8,7,6]],5,6]
l1=[]
def nested_list(l)->list:
    for i in l:
        if type(i)==list:
            nested_list(i)
        else:
            l1.append(i)
nested_list(l)
print(l1)

l=[2,6,4,8,5,7,3] #8,2 7,3 6,4 , 55
l.sort()
print(l)


