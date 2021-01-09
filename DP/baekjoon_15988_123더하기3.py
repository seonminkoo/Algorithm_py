t = int(input())
m = [0]*1000001

m[0] = 1
m[1] = 1
m[2] = 2

for i in range(3, len(m)):
    m[i] = m[i-1] + m[i-2] + m[i-3]
    m[i] %= 1000000009

for _ in range(t):
    n = int(input())
    print(m[n])