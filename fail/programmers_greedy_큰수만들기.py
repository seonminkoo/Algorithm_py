def solution(number, k):
    """
    맨 앞에 제일 큰 수가 있어야함
    """
    answer = ''
    str = number

    #print(number)
    while k != 0:
        #반으로 자르기
        i = len(str)
        #print("str 길이 :",i )
        tmp1 = str[:i//2]
        tmp2 = str[i//2:]
        #print("tmp1: ", tmp1)
        #print("tmp2: ", tmp2)

        if len(tmp1) == 1:
            max_value = max(tmp1, tmp2)
            answer += max_value
            str = ""
            k -= 1
        elif len(tmp1) == 0:
            answer = answer[-3] + max_index(answer[-1], answer[-2])
            str = ""
            k -= 1
        else:
            max_value = max(tmp1)
            max_index = tmp1.index(max_value)
            #print("max_value 값", max_value)
            answer += max_value
            str = tmp1[max_index+1:] + tmp2

            k -= max_index

        #print("k값:", k)


        #print("answer 값", answer)
        #print("")
    answer = answer + str
    #print(answer)

    return answer

solution("1231234", 3)