import numpy as np

test_pyList = [[1,2,3,4],
               [5,6,7]]
print(test_pyList)

# trans_np=np.array(test_pyList,float) ## 파이썬의 요소가 빠진 리스트를 np.array로 변환시 오류 특징 #1
# print(trans_np)


test_array = np.array([[1, 2, 3, 4, "5"]], float) # array(생성할 데이터,데이터 타입)
print(test_array)
print(type(test_array[3]))
print(test_array.dtype)
print(test_array.shape) #shape -> 넘파이 배열에서 객체의 차원에 대한 구성 정보 반환
#넘파이의 특징
#1. 배열의 경우, 텐서(다차원 배열)의 구조에 맞춰 배열을 생성 -> 행렬에서 요소 1개라도 빠지면 에러
#2. 동적 타이핑이 지원 안된다. (파이썬은 동적 타이핑으로 코드 수행 시점에 타입 결정 그래서 리스트 안에 다양한 자료형 존재 가능
#  그러나 넘파이는 동적 타이핑이 지원되지 않아, 하나의 데이터 타입만 사용 가능 -> 검색, 연산속도에 장점.
