"""
팩토리얼 0의 개수
- 5의 개수를 센다 -> ex. 100/5 + 100/25
"""

res = 0
n = int(input())
i = 5

while i <= n:
    res += n//i
    i *= 5

print(res)