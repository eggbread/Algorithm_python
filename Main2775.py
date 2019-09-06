t = int(input())
arr=([[0 for i in range(15)] for j in range(15)])
arr[0]=list(range(1,15))
for i in range(t):
    k = int(input())
    n = int(input())
    for floor in range(1,k+1):
        for room in range(n):
            arr[floor][room]=arr[floor][room-1]+arr[floor-1][room]
    print(arr[k][n-1])
