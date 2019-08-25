arr=[{'A','B','C'},{'D','E','F'},{'G','H','I'},{'J','K','L'},{'M','N','O'},{'P','Q','R','S'},{'T','U','V'},{'W','X','Y','Z'}]
inputStr = input()
sum=0
for i in inputStr:
    cnt=3
    for j in arr:
        if i in j:
            sum+=cnt
        else:
            cnt+=1
print(sum)
