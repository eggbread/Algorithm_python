m = int(input())
n = int(input())
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
minValue=None
for i in range(m,n+1):
    if is_prime(i):
        if not minValue:
            minValue=i
        result+=i
if result==0:
    print(-1)
else:
    print(result)
    print(minValue)


