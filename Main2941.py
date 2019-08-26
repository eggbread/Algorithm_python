inputStr = input()
arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
passCheck=False
passtCheck=False
for index,i in enumerate(inputStr):
    if passtCheck:
        passtCheck=False
        continue
    if passCheck:
        passCheck=False
        continue
    if index==len(inputStr)-1:
        cnt+=1
        break
    if i=='d'and len(inputStr)-index>2:
        if i+inputStr[index+1]+inputStr[index+2]=='dz=':
            passtCheck=True
            cnt+=1
            passCheck=True
            continue
    if i+inputStr[index+1] in arr:
        cnt+=1
        passCheck=True
    else:
        cnt+=1
print(cnt)