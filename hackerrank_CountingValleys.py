def sockMerchant(n, ar):
    count = {}
    ans = 0
    for i in ar:
        try: count[i] += 1
        except: count[i] = 1

    for values in count.values():
        ans += values//2

    return  ans

n = int(input())
ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
print(result)
