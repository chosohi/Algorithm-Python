def solution(id_list, report, k):
    report = list(set(report))
    res = {x: 0 for x in id_list}

    for i in report:
        res[i.split()[1]] += 1
    print(res)
    answer = [0] * len(id_list)
    for i in range(len(report)):
        if res[report[i].split()[1]] >= k:
            answer[id_list.index(report[i].split()[0])] += 1
    return answer


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer