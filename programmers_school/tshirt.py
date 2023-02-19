def solution(people, tshirts):
    answer = 0 
    people.sort()
    tshirts.sort()
    
    idx = 0
    
    for i in range(len(tshirts)):
        if idx == len(people) :
            break
    
        if tshirts[i] >= people[idx]:
            answer+=1
            idx+=1
    
    return answer

print(solution([2,3],[1,2,3]))