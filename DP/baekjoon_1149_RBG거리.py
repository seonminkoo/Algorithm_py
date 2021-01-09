"""
이웃하는 집끼리 색 겹치면 안됨
집 색깔 빨, 초, 파 중 하나로 고정
"""
n = int(input())
a = [(0,0,0)] + [tuple(map(int, input().split())) for _ in range(n)]
m = [[0,0,0] for i in range(n+1)]

for i in range(1, n+1):
    m[i][0] = min(m[i - 1][1], m[i - 1][2]) + a[i][0]
    m[i][1] = min(m[i - 1][0], m[i - 1][2]) + a[i][1]
    m[i][2] = min(m[i - 1][0], m[i - 1][1]) + a[i][2]

print(min(m[n][0], m[n][1], m[n][2]))