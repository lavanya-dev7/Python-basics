def fibbo(n:int)->int:
    a=0
    b=1
    print(a,b)
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
        
    

def is_fibonacci(n)->bool:
    a=0
    b=1
    if n==0:
        return True
    while b<=n:
        if b==n:
            return True
        c=a+b
        a=b
        b=c
    return False


if __name__=="__main__":
    n=5
    fibbo(n)
    n=0
    if is_fibonacci(n):
        print("It is ibonoci")
    else:
        print("Not a fibbo")
