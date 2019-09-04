n = int(input())
i=1
found=True
while n-i>0:
    n-=i
    i+=1
    if found:
        found=False
    else :
        found=True
if found:
    result=str((1+i-n),"/",n)
else:
    result=n ,"/",(1 + i - n)
print(type(result))
