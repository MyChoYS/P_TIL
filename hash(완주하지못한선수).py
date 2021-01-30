#include <string> ##완주하지 못한 선수 (해시)
#include <vector>

#using namespace std;

#string solution(vector<string> participant, vector<string> completion) {
 #   string answer = "";
  #  return answer;


def solution(participant,completion):
    if len(participant) - len(completion) == 1 and len(participant) >= 1 and len(participant) <= 100000:
        for i in completion:
            if len(i) >= 1 and len(i):
                participant.remove(i)
            else:
                break
    return participant.pop()

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

def solution(participant,completion):
    [participant.remove(i) for i in completion]
    return participant.pop()
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))









# def solution(participant,completion):
 #   ano = participant
  #  for i in participant:
   #     if participant.count(i) == 1: #같은 이름의 참가자 없는 경우
    #        for x in completion: #참가자에서 통과자 빼기
     #           ano.remove(x)
      #      for y in ano: #통과하지 못한 참가자 리스트
       #         print("\"", ano[ano.index(y)], "\"", "는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.")
        #else:
         #   sum = participant.count(i) #같은 이름의 참가자 있는 경우
          #  for x in completion:
           #     ano = participant.remove(x) #참가자에서 통과자 빼기
            #for y in ano:
             #   print("\"", ano[ano.index(y)], "\"", "는 참여자 명단에는"+str(sum)+"명 있지만, 완주자 명단에는",
              #        completion.count(y),"명 밖에 없기 때문에", sum-completion.count(y)," 완주하지 못했습니다.") '''





'''
예제 #1
leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습'''

###하,,, 밑의 문구 구현하려고 오래걸렸네,,, 그냥 답만 나와도 되는거였는데 ㅆㅃ... 쓸데없이 데갈빡만 굴렸다,,