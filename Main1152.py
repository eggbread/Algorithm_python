str = input()
result=str.count(" ")+1
if str[0]==" ":
    result-=1
if str[len(str)-1]==" ":
    result-=1
print(result)