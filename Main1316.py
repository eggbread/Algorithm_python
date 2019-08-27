n = int(input())
result=0
for i in range(n):
    inputStr=input()
    arr=[]
    found=False
    for index,j in enumerate(inputStr):
        if j in arr:
            if arr[index-1] != j:
                found=True
                break
            else:
                arr.append(j)
        else:
            arr.append(j)
    if not found:
        result+=1
print(result)