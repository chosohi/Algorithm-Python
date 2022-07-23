def solution(nums):
    answer = 0
    catch = len(nums) // 2
    tmp = []
    for num in nums:
        if num not in tmp and len(tmp) < catch:
            tmp.append(num)
    print(tmp)
    return len(tmp)