def solution(numbers, hand):
    num = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    l = [3,0]
    r = [3,2]

    answer = ''

    for i in range(len(numbers)):
        tmp = numbers[i]
        if tmp == 1 or tmp == 4 or tmp == 7:
            answer += 'L'
            l = num[tmp]
        elif tmp == 3 or tmp == 6 or tmp == 9:
            answer += 'R'
            r = num[tmp]
        else:
            w = num[tmp]
            distance_l = abs(w[0] - l[0]) + abs(w[1] - l[1])
            distance_r = abs(w[0] - r[0]) + abs(w[1] - r[1])
            if distance_l > distance_r:
                answer += 'R'
                r = num[tmp]
            elif distance_l < distance_r:
                answer += 'L'
                l = num[tmp]
            else:
                if hand == 'right':
                    answer += 'R'
                    r = num[tmp]
                else:
                    answer += 'L'
                    l = num[tmp]

    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")