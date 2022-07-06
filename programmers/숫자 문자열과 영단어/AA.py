def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

def solution(s):
    answer = ''
    chart = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    eng = ''
    for i in range(len(s)):
        if s[i].isdecimal():
                answer+= s[i]
        else:
            eng += s[i]
            if eng in chart:
                answer+= str(chart[eng])
                eng = ''
    print(answer)
    return int(answer)