name = "JAZ"

def solution(name):
    """
    ord : 문자열 -> 아스키코드
    chr : 아스키 코드 -> 문자열
    1. 커서 이동 거리 최소로
    2. 알파벳 이동 최소로
    """
    answer = 0
    m = [min(ord(c) - 65, 91 - ord(c)) for c in name] #알파벳 이동
    print(m) #[9, 0, 1]
    i = 0

    while True:
        answer += m[i]
        m[i] = 0
        print("m 리스트 {0}" .format(m))
        print("answer = {0}" .format(answer))

        if sum(m) == 0:
            print(answer)
            return answer

        left = 1
        right = 1

        while m[i + right] <= 0:
            right += 1

        while m[i - left] <= 0:
            left += 1

        if left < right:
            i -= left
        else:
            i += right

        print("i는 {0}" .format(i))
        answer += min(left, right)

solution(name)
