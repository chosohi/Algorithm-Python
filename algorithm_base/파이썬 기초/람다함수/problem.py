# map(함수, 인자)
# map(int, [1,2,3])
# 각 배열의 요소들을 int로 전환해라
def plus_one(x):
    return x+1
a= [1,2,3]
print(list(map(plus_one, a)))
# 람다는 익명함수 x를 x+1로 바꿔라
# 내장함수의 인자로 쓰기에 람다는 편하다
print(list(map(lambda x:x+1,a)))


