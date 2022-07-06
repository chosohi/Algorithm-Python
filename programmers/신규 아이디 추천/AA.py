def solution(new_id):

    new_id = list(new_id)
    # 1단계 대문자를 소문자로 치환
    for i in range(len(new_id)):
        if new_id[i].isalpha():
            new_id[i] = new_id[i].lower()

    # 2단계 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdecimal() or new_id[i] in ['-','_','.']:
            continue
        else:
            new_id[i] = ''
    new_id = list(''.join(new_id))
    # 3단계 . 2번 이상 연속이면 1개로 치환
    for i in range(len(new_id)):
        if new_id[i] == '.':
            for j in range(i, len(new_id)):
                if new_id[j] == '.':
                    # 마지막 차례면
                    if j == len(new_id)-1:
                        for k in range(i, len(new_id)):
                            new_id[k] = ''

                else:
                    for k in range(i+1, j):
                        new_id[k] = ''
                    break


    new_id = list(''.join(new_id))

    # 4단계 . 처음 혹은 끝 제거
    while True:
        if len(new_id) < 1:
            break
        if new_id[0] != '.' and new_id[-1] != '.':
            break
        if new_id[0] == '.':
            new_id[0] = ''
        if new_id[-1] == '.':
            new_id[-1] = ''
        new_id = list(''.join(new_id))
    # 5단계 빈문자열이면 'a'러
    new_id = list(''.join(new_id))
    if len(new_id) == 0:
        new_id = ['a']
    # 6단계 16자 이상이면 0~15까지만 살리고, 마지막에 . 있으면 제거
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id[-1] = ''

    if len(new_id) <= 2:

        while True:
            if len(new_id) == 3:
                break
            new_id.append(new_id[-1])

    return ''.join(new_id)