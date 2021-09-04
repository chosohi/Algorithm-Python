A, B = map(int, input().split())

result = 0
for i in range(1, 999999999):
    if 2*-i == 2*A and i**2 == B:
        result = i
print(i)