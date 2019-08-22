inputStr = input().upper()
arr={}
for i in range(len(inputStr)):
    found=False
    for j in range(len(arr)):
        if inputStr[i] in arr:
            found=True
            break
    if(found):
        arr[inputStr[i]]+=1
    else:
        arr[inputStr[i]]=1

result = max(arr.values())
cnt=0
results=''
for i in arr.items():
    if i[1]==result:
        cnt+=1
        results=i[0]
if(cnt==1):
    print(results)
else:
    print('?')