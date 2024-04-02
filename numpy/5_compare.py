import numpy as np
x= np.array([1,2,3,4,5])
y= np.array([3,4,5,1,2])
print(x>3) ## 요소별 비교연산 boolean형
print(x>y) ## 인덱스별 비교연산
print((x>3).any()) #  모든 값 중 하나라도 참이면 True
print((x>3).all()) #  모든 값 중 하나라도 참이 아니면 False
