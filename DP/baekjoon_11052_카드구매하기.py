n = int(input())
p = [0] + list(map(int, input().split()))
m = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        m[i] = max(m[i], m[i-j]+p[j])

print(m[n])








