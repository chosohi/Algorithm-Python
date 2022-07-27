def solution(numbers, hand):
    answer = ''
    position = ['*', '#']
    left = [1, 4, 7]
    right = [3, 6, 9]
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    for num in numbers:
        if num in left:
            answer += 'L'
            position[0] = num
        elif num in right:
            answer += 'R'
            position[1] = num
        else:
            near_hand = get_near_hand(position[0], position[1], keypad, num, hand)
            print(near_hand)
            if near_hand == 'L':
                answer+= 'L'
                position[0] = num
            else:
                answer += 'R'
                position[1] = num

    return answer


def get_near_hand(l, r, keypad, num, hand):
    left_distance = abs(keypad[num][0] - keypad[l][0]) + abs(keypad[num][1] - keypad[l][1])
    right_distance = abs(keypad[num][0] - keypad[r][0]) + abs(keypad[num][1] - keypad[r][1])
    near_hand = 'L' if left_distance > right_distance else 'R'
    if left_distance == right_distance:
            near_hand = 'R' if hand == "right" else 'L'
    return near_hand
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	, "right")