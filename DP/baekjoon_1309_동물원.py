n = int(input()) #우리의 크기

m = [[0]*3 for _ in range(n+1)]
print(m)
m[0][0] = 1

for i in range(1, n+1):
    m[i][0] = m[i-1][0] + m[i-1][1] + m[i-1][2]
    m[i][1] = m[i-1][0] + m[i-1][2]
    m[i][2] = m[i-1][1] + m[i-1][1]

    for j in range(3):
        m[i][j] %= 9901

print(sum(m[i]) % 9901)