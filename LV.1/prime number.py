def solution(n):
    counts = set()
    for i in range(1, n + 1):
        sum = 0
        for x in range(1,i+1):
            if i % x == 0:
                sum +=1
        if sum ==2:
            counts.add(i)
    answer = len(counts)
    return answer
print(solution(5))

def solution(n):
    for i in range(1,n+1):
        count = 0
        if n == i*i:
            count +=1
        if count == 1:
            return (i + 1) * (i + 1)
    else:
        return -1
print(solution())

##처음이라 그런지 어버버거리다 시간 내 제출도 못하고 코드 구경만했다.. 앞으로 정신 빠짝 차리자