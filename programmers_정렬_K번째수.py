def solution(array, commands):
    """
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    """
    
    answer = []

    for c in commands:
        i = c[0] - 1
        j = c[1]
        k = c[2] - 1

        answer.append(sorted(array[i:j])[k])

    return answer

solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]])