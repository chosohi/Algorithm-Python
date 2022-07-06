def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
            print(faillist)
        else:
            faillist[i] = 0
    print(faillist)
    sorted(faillist, key=lambda x: faillist[x], reverse=True)
    print(faillist)
    return sorted(faillist, key=lambda x: faillist[x], reverse=True)

res = solution(5,[2,3,4])
print(res)