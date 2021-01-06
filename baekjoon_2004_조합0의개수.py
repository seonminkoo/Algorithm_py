"""
- 팩토리얼 개수 구하는 함수 짜기
- nCm = n! // (n-m)!*m!
"""

def count(n, v):
    i = v
    res = 0
    while i <= n:
        res += n//i
        i *= v

    return res

n, m = map(int, input().split())

two = count(n,2) -count(n-m, 2) - count(m, 2)
five = count(n,5) -count(n-m, 5) - count(m, 5)

print(min(two, five))



