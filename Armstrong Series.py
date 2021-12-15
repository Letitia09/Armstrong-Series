a=int(input())
b=int(input())
print("Armstrong Series :\n")
for i in range(a,b):
    t=i
    sum=0
    n=len(str(i))
    while(i!=0):
        d=i%10
        sum=sum+(d**n)
        i=i//10
    if t==sum:
       print(t)
