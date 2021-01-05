def prime(x):
    if (x < 2):
        return False

    i = 2
    while (i*i <= x):
        if x % i == 0:
            return False
        i += 1

    return True

n = int(input())
a = list(map(int, input().split()))
ans = 0
for value in a:
    if prime(value):
        ans += 1

print(ans)
