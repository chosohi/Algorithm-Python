import heapq


def solution(scoville, K) :
    answer = 0
    heapq.heapify(scoville)

    # 모든 음식의 스코빌 지수가 K이상 혹은 남은 음식 갯수가 0개인데 K미만일때 break
    while True:
        # 1번째로 덜 매운 음식(최솟값)
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) ==0:
            answer = -1
            break
        # 2번째로 덜 매운 음식
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + min2*2
        heapq.heappush(scoville,new_scoville)
        answer += 1
    return answer


print(solution([1,2,3,9,10,12],7))