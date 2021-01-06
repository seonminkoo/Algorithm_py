"""
1. GCD 구하는 함수
2. 변수: 테스트케이스 t, 결과 res
"""

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

t = int(input())

for i in range(len(t)):
    s = map(int, input().split())

