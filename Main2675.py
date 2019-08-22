r = int(input())
arr=[]
for i in range(r):
    t, str = input().split()
    t = int(t)
    temp=[]
    for j in range(len(str)):
        for l in range(t):
            temp.append(str[j])
    arr.append(temp)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end="")
    print()
    # for j in range(len(input)):
    #     print(j)