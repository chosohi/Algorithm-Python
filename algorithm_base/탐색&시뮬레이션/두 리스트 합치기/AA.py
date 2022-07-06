# import sys
# sys.stdin = open("input.txt", "rt")

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_pointer = 0
M_pointer = 0
res = []
while N_pointer < N and M_pointer < M:
    if N_list[N_pointer] < M_list[M_pointer]:
        res.append(N_list[N_pointer])
        N_pointer += 1
    else:
        res.append(M_list[M_pointer])
        M_pointer += 1

if N_pointer < N :
    res+=N_list[N_pointer:]
else:
    res+=M_list[M_pointer:]
print(*res)