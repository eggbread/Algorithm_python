import math
t = int(input())
for i in range(t):
    x, y = map(int, input().split(" "))
    end=y-x
    result=round(math.sqrt(end))
    if math.pow(result,2)>=end:
        print(result+result-1)
    else:
        print(result*2)