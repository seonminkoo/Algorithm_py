"""
1.앞자리가 큰 순서대로 정렬 -> 리스트로 변환해서
2. 34, 3, 30 순서로 정렬 되어야 함 -> 숫자 반복해서 비교
"""

def solution(numbers):

    numbers = sorted(list(map(str, numbers)), key = lambda x: x*4, reverse= True)

    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))