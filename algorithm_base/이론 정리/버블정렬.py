# 1

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
arr = [8,5,3,9,1,7,0]
bubble_sort(arr)
print(arr)

#2
# 어떤 패스의 원소 교환 횟수가 0이면 모든 원소가 정렬을 완료한 경우이므로 그 이후의 패스는 불필요하다고 판단하여 정렬 중단
# 정렬을 모두 마쳤거나 정렬이 거의 다된 배열에서는 비교 연산이 크게 줄어 실행 시간을 단축
def bubble_sort2(a):
    n = len(a)
    for i in range(n-1):
        exchange=0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j], a[j-1]
                exchange += 1
        if exchange == 0:
            break

bubble_sort2(arr)
print(arr)