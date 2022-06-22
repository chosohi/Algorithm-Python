def solution(n, m):
    answer = []

    # 임의의 n, m 중 max, min의 값을 찾는다.
    _max, _min = max(n, m), min(n, m)
    # min의 값이 0보다 크면
    while _min:
        _max, _min = _min, _max % _min

    answer = [_max, int(n * m / _max)]

    return answer