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

