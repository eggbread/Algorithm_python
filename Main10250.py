import math
T = int(input())
for i in range(T):
    H,W,N=map(int,input().split(" "))
    if N%H==0:
        print(str(H), str(math.ceil(N / H)).zfill(2), sep='')
    else:
        print(str(N%H),str(math.ceil(N/H)).zfill(2),sep='')
