t = int(input())

for _ in range(t):
    n = int(input())
    m = [0]*11

    m[0] = 1
    m[1] = 1
    m[2] = 2

    for i in range(3, n+1):
        m[i] = m[i-1] + m[i-2] + m[i-3]

    print(m[n])