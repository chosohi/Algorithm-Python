def change_time(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def solution(booked, unbooked):
    answer = []
    booked = [(change_time(t), name) for t, name in booked] + [(24 * 60, None)]
    unbooked = [(change_time(t), name) for t, name in unbooked] + [(24 * 60, None)]
    b, u, time = 0, 0, 0

    while b < len(booked) and u < len(unbooked):
        t1, t2 = booked[b][0], unbooked[u][0]
       
        if t1 <= time :
            answer.append(booked[b][1])
            b += 1
            time += 10
        elif t2 <= time :
            answer.append(unbooked[u][1])
            u += 1
            time += 10
        else:
            time = min(t1, t2)
    answer.pop()
    return answer
print(solution([["09:10", "lee"]],	[["09:00", "kim"], ["09:05", "bae"]]))
print(solution([["09:55", "hae"], ["10:05", "jee"]],	[["10:04", "hee"], ["14:07", "eom"]]))