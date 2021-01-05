#최대 공약수, 최소 공배수 출력
a, b = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

g = gcd(a, b)

print(g)
print(a*b//g)