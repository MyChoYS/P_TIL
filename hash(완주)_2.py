def solution(participant,completion):
    list1 = []   #통과목록
    ano = participant
    for i in completion: #통과하지 못한 리스트
        ano.remove(i)
    for i in participant:
        if participant.count(i) == 1 and completion.count(i) == 0: #같은 이름의 참가자가 없고 완주하지 못한 경우,
            pass
        elif participant.count(i) == 1 and completion.count(i) ==1: #같은 이름의 참가자가 없고 완주한 경우,
            list1.append(i)
        elif participant.count(i) >=1 and completion.count(i) >= 1 and participant.count(i) == completion.count(i): #같은 이름의 참가자가 있고 모두 완주했을 경우,
            list1.append(i)
        elif participant.count(i) >=1 and completion.count(i) >= 1 and participant.count(i) > completion.count(i): #같은 이름의 참가자가 있고 일부만 완주한 경우,
            list1.append(i)

    return list1

print(solution(['leo', 'kiki', 'eden'],	['eden', 'kiki']))
