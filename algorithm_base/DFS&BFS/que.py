from collections import deque 
# double ended que -> 양쪽에서 연산이 가능하다.

que = deque()


que.append(1)
que.append(2)
que.append(3)

que.popleft()
que.popleft()
que.popleft()
  
# que.pop(0) => O(n) 시간이 걸려 쓰면 안됨 왜냐면 앞에 거를 꺼내면 뒤에 있는 것들을 앞으로 옮기는 연산을 처리하기 때문 
