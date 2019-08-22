a,b =input().split()
for i in reversed(range(3)):
    if a[i]==b[i]:
        continue
    else:
        if a[i]>b[i]:
            for j in reversed(range(3)):
                print(a[j],end="")
            break
        else:
            for j in reversed(range(3)):
                print(b[j],end="")
            break