t = int(input())

for _ in range(t):
    s = input()
    stack = []

    for c in s:
        if c == " ":
            print(''.join(stack[::-1]), end='')
            stack.clear()
            print(c, end='')
        else:
            stack.append(c)

    print(''.join(stack[::-1]))


