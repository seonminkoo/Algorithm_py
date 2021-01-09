def is_vps(s):

    vps = 0

    for s in string:
        if s == '(':
            vps += 1
        elif s == ')':
            vps -= 1

        if vps < 0:
            return "NO"

    if vps == 0:
        return "YES"
    else:
        return "NO"

t = int(input())

for _ in range(t):
    string = list(max(input().split()))
    print(is_vps(string))


