
# 최대공약수
A = int(input())
B = int(input())
while A % B != 0:
    A, B = B, A% B

print(B)