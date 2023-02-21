# 그리디

# 방법 1 (적은 수의 학생 배열에 대해서 처리 -> 모든 학생들을 고려)
# u : 체육복을 가지고 온 학생과 없는 학생이 1 과 0, 여벌을 가지고 온 학생 2로 구분됨

def solution(n, lost, reserve):
    # 바운더리를 체크하는 과정에서의 편의를 위해 맨 앞, 뒤에 여분의 1 추가
    u = [1] * (n + 2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in (range(1,n+1)):
        if (u[i-1]) ==0 and u[i]==2:
            # 리스트 슬라이스로 두명에게 1개씩 부여
            u[i-1:i+1] = [1,1]
        elif u[i] == 2 and u[i+1] == 0:
           u[i:i+2] = [1,1] 
    # u의 1번째부터 -1 전까지 에서 원소들을 꺼내는데, 단 0보다 큰 것들만 꺼내어서 길이로 반환
    return len([x for x in u[1:-1] if x > 0])

# 방법 2 (학생 수는 많지만, 여벌을 가지고 있는 학생 수가 적을때, 여벌을 가지고 있는 학생들만 고려)
# 데이터타입 set(집합): 해시테이블로 구현되어있기 때문에, key로 접근하는 시간이 상수시간임
# 딕셔너리는 키에 대해서 map되어있지만, set은 value는 없고 특정 데이터가 이 집합에 속해있는지 여부만 판단 가능

def solution2(n,lost,reserve):
    # 두 집합의 교집합을 나타냄
    s = set(lost) & set(reserve)
    # 차집합 (체육복을 빌려야하는 학생들)
    l = set(lost) - s
    # 여벌이 있는데 도난을 안당한 학생들
    r = set(reserve) - s

    for x in sorted(r):
        if x - 1 in l:
            l.remove(x-1)
        elif x +1 in l:
            l.remove(x+1)

    # 빌려야하는데 빌리지 못한 학생들만 l에 남음

    return n - len(l)
print(solution2(5,[2, 4],[1, 3, 5]))

