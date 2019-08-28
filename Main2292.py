n = int(input())
if n==1:
    print(1)
else:
    i=6
    j=2
    cnt=2
    while j+i-1<n:
        j+=i
        i+=6
        cnt+=1
    print(cnt)