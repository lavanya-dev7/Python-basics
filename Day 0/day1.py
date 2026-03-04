l=[2,6,4,8,5,7,3] #8,2 7,3 6,4 , 55


def get_pairs(l)->list:
    l.sort() 
    i=l[0]
    j=l[len(l)-1]
    l1=[]
    while i<j:
        l1.append((i,j))
        i+=1
        j-=1
    if len(l)%2!=0:
        x=len(l)//2
        l1.append((l[x],l[x]))

    print(l1)

get_pairs(l)


t=(0,1)
first=1
sec=2
third=3
fourth=4

if t[0]==0 and t[1]==0:
    print("origin")
elif t[0]>=0 and t[1]>=0:
    print(first)
elif t[0]<0 and t[1]>=0:
    print(sec)
elif t[0]<0 and t[1]<0:
    print(third)
else:
    print(fourth)



def frequency(s:str):
    d={}
    s=s1.replace(" ","")
    for i in s: 
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
    s2=""
    for i,j in d.items():
        s2+=i
        s2+=str(j)
    print(s2)

    s3=""
    s4=set(s)
    for i in s4:
        s3+=i
        s3+=str(s.count(i))
    print(s3)
if __name__=="__main__":

    s1="Hello world this is python"
    frequency(s1)






