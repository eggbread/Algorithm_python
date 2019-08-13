input = input()
arr = [-1]*26

cnt=0
for i in input:
    if arr[ord(i)-97]==-1:
        arr[ord(i)-97]=cnt
    cnt+=1

for i in range(26):
    print(arr[i], end=' ')