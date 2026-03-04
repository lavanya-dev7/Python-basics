

def slice(start,end,step,lst):
    if end==-1:
        end=len(lst)

    l=lst[start:end+1:step]
    print(l)

if __name__=="__main__":
    lst=[1,2,3,4,5,6,7,8,9,10]
    slice(3,-1,1,lst)