def solution(number, k):
    """
    1. number 리스트로 변환
    2.스택에 문자열 넣기

    """
    answer = ''

    number = list(map(int, number))
    max_index = number.index(max(number))
    print("max_index = {0}" .format(max_index))

    if max_index <= k:
        #max_index 앞의 수 모두 제거
        for i in range(max_index):
            number.pop(0)

        for i in range(k-max_index):
            number.pop(number.index(min(number)))
    else:
        for i in range(k):
            number.pop(number.index(min(number[:max_index])))
            max_index -= 1

        #k -= max_index-k

        #for i in range(k):
            #print(k)
            #number.pop(number.index(min(number[max_index:])))

    #print(number)
    number = "".join(map(str, number))
    #print(number)

    answer = number
    print(answer)
    return answer

solution("423239123", 4)