print("enter the number of rows and the table you want in a single line")
n,a=map(int,input().split())
l=[]
for i in range(1,n+1):
    l.append(i*a)
print(*l,sep="->")
