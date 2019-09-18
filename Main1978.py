n = int(input())
arr=list(map(int,input().split(" ")))
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3): return True
    if n % 2 is 0 or n % 3 is 0: return False
    if n < 9: return True
    k, l = 5, n ** 0.5
    while k <= l:
        if n % k is 0 or n % (k + 2) is 0:
            return False
        k += 6
    return True
result=0
for i in arr:
    if is_prime(i):
        result+=1
print(result)


