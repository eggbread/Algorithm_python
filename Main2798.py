n,m=map(int,input().split(" "))
list=list(map(int,input().split(" ")))
result = abs(m-(list[0]+list[1]+list[2]))
a=0
b=1
c=2
for i in range(len(list)):
    for j in range(i+1,len(list)):
        for k in range(j+1,len(list)):
            if abs(m-(list[i]+list[j]+list[k]))<result and (list[i]+list[j]+list[k])<=m:
                a=i
                b=j
                c=k
                result=abs(m-(list[i]+list[j]+list[k]))
print(list[a]+list[b]+list[c])