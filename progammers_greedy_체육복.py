"""
1. lost와 reserve 배열에 일치하는 요소 있으면 reserve에서 제거
2. lost 요소 뽑아서(l) l+1 l-1 reserve에 있는지 확인 
3. ans = n - 못빌린 수(f)
"""


def solution(n, lost, reserve):
    answer = 0
    new_reverse = list(set(reserve) - set(lost))
    lost = list(set(lost) - set(reserve))
    reserve = new_reverse
    f = len(lost)

    if not reserve:
        answer = n - f
        return answer

    for l in lost:
        if l - 1 > 0 and l - 1 in reserve:
            f -= 1
            reserve.remove(l - 1)
        elif l + 1 <= n and l + 1 in reserve:
            f -= 1
            reserve.remove(l + 1)

    answer = n - f

    return answer