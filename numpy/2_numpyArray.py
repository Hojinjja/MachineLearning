import numpy as np

class matrix:
    def __init__(self):
        matirx=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        print("shape",np.array(matirx,int).shape) ## shape = 차원 설명 (n행 m열)
        print("dtype:",np.array(matirx,int).dtype) ## dtype = 데이터 타입 반환
        print('--------------------------------------------------')
        # 1  2  3  4
        # 5  6  7  8
        # 9 10 11 12  -> 이 형태를 갖추게 된다.
        ## 파이썬 리스트인 matrix를 numpy의 array로 바꾸고.shape를 해서 구조를 출력
        ## (3,4)값이 출력되는데 *3은 행*,  *4는 열*
# matrix()



class attributeDrill:
    def __init__(self):
        tensor_rank3 = [
            [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
            [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
            [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
        ]
        # 이렇게 하면
        # 1,2,3,4
        # 1,2,3,4
        # 1,2,3,4
        # 1,2,3,4 <- 이 행렬이 3장(rank=차원) 있는 3차원 행렬이 된다.
        # (4,3,4)가 출력되는데 (rank,raw,column) 순이 된다.

        print("shape 결과:",np.array(tensor_rank3,int).shape)
        print("ndim 결과:",np.array(tensor_rank3,int).ndim) ##ndim = (number of dimension) 랭크(차원)을 나타냄
        print("size 결과:",np.array(tensor_rank3,int).size) ##size = 넘파이 배열에 있는 모든 데이터의 개수를 나타낸다.

        int_array=np.array(tensor_rank3,dtype=int) ## dtype 생략 가능, 어지간하면 생략 x
        float_array=np.array(tensor_rank3,float)
        print("int_array의 메모리 크기:",int_array.itemsize,"byte")
        print("float_array의 메모리 크기:",float_array.itemsize,"byte")
        print("----------------------------------------------------------")
# attributeDrill()





#배열의 구조 다루기 (p.90)
class control_structure:
    def __init__(self):

        x= np.array([[1,2,3,4], [5,6,7,8]] ) ## 2x4의 배열 (2차원)
        print(x)
        print(x.shape)

        test1 = x.reshape(-1,) # -1 = 해당 차원(행)은 알아서 계산해라 , 열은 x =>즉 1차원
        print("Test1:",test1)

        # testError = x.reshape(2,2) # 2,2 -> 2행 2열로 만들어라, 만약 요소의 개수가 안 맞으면 오류 -> x는 8개의 요소 , 2x2 = 4개 (자리부족)
        test2 = x.reshape(2,4) # 2행 4열로 만들어라
        print("Test2:","\n",test2)

        test3 = x.reshape(2,2,-1) # 4차원 3차원 2차원의 크기는 각각 2로 하고 남은 차원은 알아서 계산
        print("Test3:","\n",test3)
# control_structure()

#인덱싱
class indexingSlicing:
    def __init__(self):
        x=np.array([[1,2,3,4],[4.5,5,6,7],[1,1,2,3]], int) # 4.5가 int로 변환되어 4로 바뀜
        print("int로 변환:","\n",x)
        print("")

        #인덱싱
        print("0-2번 출력:",x[0][2]) ##  (인덱스 기준)
        print("2-2번 출력",x[2,2])
        print("")

        #슬라이싱
        print("전체 행 2열 이상:","\n",x[:,2:])
        print("")
        print("1행 1~2열:","\n",x[1,1:3])
        print("")
        print("0행~2행 전체 :","\n",x[0:3])

# indexingSlicing()

#배열 생성 함수
class arrayFunction:
    def __init__(self):
        #arange(시작 인덱스,마지막 인덱스, 증가값)
        print("")
        print("0부터 9까지:",np.arange(10))
        print("-5부터 4까지:",np.arange(-5,5))
        print("0부터 4까지 0.5마다::",np.arange(0,5, 0.5)) # 실수형도 증가값으로 가능
        print("")


        #ones,zero,empty
        print("ones:","\n",np.ones(shape=(5,2),dtype=np.int8)) #5행 2열을 1로(int8 타입)
        print("zeros:","\n",np.zeros(shape=(5,2),dtype=np.float32))#5행 2열을 0으로 (float32 타입)
        print("empty:","\n",np.empty(shape=(5,2),dtype=np.float32))#5행 2열을 float32로 채울 수 있는 메모리 할당만.
        print("")

        # ones_like,zero_like,empty_like
        x=np.arange(12).reshape(3,-1) # 0부터 11까지 3행 4열로
        print("0~11을 3x4 배열로:","\n",x)
        print("ones_like","\n",np.ones_like(x))
        print("zeros_like","\n",np.zeros_like(x))
        print("")

        #indentity, eye, diag
        print("identity:","\n",np.identity(n=3,dtype=int)) # n -> nxn 행렬로 단위행렬 생성
        print("eye:","\n",np.eye(3,5,0)) # 1을 생성하는데 행렬크기, 시작점 지정 가능 //np.eye(N=3,M=5) 인데 N=,M= 생략 가능
        print("eye2:","\n",np.eye(3,5,2)) # k=2 -> 2번 인덱스부터 1 생성

        #diag
        matrix= np.arange(9).reshape(3,3) # 0~8까지 3x3 행렬로
        print(matrix)
        print("diag:","\n",np.diag(matrix)) #대각행렬만 뽑아서 관리
        print("")

        #uniform / normal
        uniformFunction = np.random.uniform(0,5,10) # 0이상 5미만 범위내에 균일한 분포된 길이가 10인 배열 생성
        normalFunction = np.random.normal(0,2,10) # 평균은 0이고 표준편차는 1인 길이가 10인 분포
        print("uniform 결과:",uniformFunction)
        print("uniform 결과:",uniformFunction)
        print("normal 결과",normalFunction)


# arrayFunction()






