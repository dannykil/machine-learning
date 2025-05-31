import numpy as np

# list_data = [1, 2, 3, 4, 5]
# print("list_data : ", list_data)
# print("list_data : ", len(list_data))

# array = np.array(list_data)
# print("array : ", array)
# print("array.size : ", array.size)
# print("array.dtype : ", array.dtype)
# print("array : ", array[2])

# # 0부터 3까지의 배열 만들기
# print("#############################################")
# array1 = np.arange(4)
# print("array1 : ", array1)

# array2 = np.zeros((4, 4), dtype=float)
# # array2 = np.zeros((4, 4, 4, 4), dtype=float)
# print("array2 : ", array2)

# array3 = np.ones((3, 3), dtype=str)
# print("array3 : ", array3)

# # 0부터 9까지 랜덤하게 초기화
# array4 = np.random.randint(0, 10, (3, 3))
# print("array4 : ", array4)

# # 평균이 0이고 표준편차가 1인 정규분포를 따르는 배열 생성
# array5 = np.random.normal(0, 1, (3, 3))
# print("array5 : ", array5)


# print("#############################################")
# # 배열 합치기
# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# array3 = np.concatenate([array1, array2])

# print(array3.size)
# print(array3.shape)
# print(array3)

# print("#############################################")
# # *배열 형태 바꾸기(중요!)
# array1 = np.array([1, 2, 3, 4])
# print(array1)
# array2 = array1.reshape((2, 2))
# print(array2)

# print("#############################################")
# # 배열 새로축 합치기
# array1 = np.arange(4).reshape((1, 4))
# array2 = np.arange(8).reshape((2, 4))
# print(array1)
# print(array2)
# array3 = np.concatenate([array1, array2], axis=0) # 위에 있는 행의 다음 행으로 합쳐짐
# print(array3)

# print("#############################################")
# # 배열 나누기
# array = np.arange(8).reshape((2, 4))
# left, right = np.split(array, [2], axis=1) # 열 기준으로 index 2에서 나누기
# print("left : ", left)
# print("right : ", right)
# print("left.shape : ", left.shape)
# print("right.shape : ", right.shape)
# print("right[1][1] : ", right[1][1])
# # left, right = np.hsplit(array, 2) # 수평으로 나누기

print("#############################################")
# # linspace
# array = np.linspace(0, 1, 5) # 0부터 1까지 5개로 나누기
# print(array)
# array = np.linspace(0, 10, 11)
# print(array)
# array = np.linspace(0, 10)
# print(array)
# array = np.linspace(0, 10, 11, endpoint=False) # endpoint=False는 마지막 숫자 포함 안함
# print(array)
# array = np.linspace(0, 10, 10, endpoint=False, retstep=True) # step=True은 배열의 간격을 의미
# print(array)

# x = np.linspace(0, 10, 10, endpoint=False)
# y = 2 * x + 1.5
# print("x : ", x)
# print("y : ", y)
# print(type(x))
# print(type(y))

# 난수를 사용해 잡음 추가
# array5 = np.random.normal(0, 1, (1, 10)) # minus값도 생성됨
# print("array5 : ", array5)
import numpy as np
import random as rd
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 11)
y1 = 2 * x + 1.5
y2 = y1 * rd.random() # 0.0 ~ 1.0 사이의 난수 생성
print("x : ", x)
print("y1 : ", y1)
print("y2 : ", y2) 

# 1차 함수에 잡음 섞기
# 1) 배열과 linspace를 사용하기 위한 numpy
# 2) 난수를 사용하기 위한 random
# 3) 그래프를 그리기 위한 matplotlib
# import matplotlib.pyplot as plt
# %matplotlib inline

# 자동으로 전표처리(명세서, 계산서 등의 내용을 읽어서 DB에 Insert하는 것)하는 어플리케이션을 개발하고 싶어.
# google의 agent builder(현재 ai application)이나 혹은 다른 제품을 사용해서 아래의 기능을 하는 어플리케이션 개발이 가능한지 확인해줘.
# 1) pdf 파일 GCS 업로드(현재 백엔드는 파이썬, 프론트엔드는 리액트로 개발 완료됨)
# 2) 미리 프롬프트를 정해놓고 GCS에 파일이 업로드 완료되면 해당 파일에서 프롬프트에 명시된 내용을 추출하는 기능. 예를 들면 업체명(발주처), 발주일자, 발주금액, 발주수량, 담당자 연락처 등

# 너가 알려준 방법들 중 Vertex AI Document AI를 사용해서 진행해보고 싶어.
# 일단 GCP 콘솔에서 Document AI의 Form Parcer를 사용해 테스트 해봤는데 추출되는 것 까지 확인했어. 그럼 이제 파이썬으로 파싱한 값을 가져오는 api를 개발하고 싶은데 아래 방법이 가능한지 확인해줘.
# 1) 확인하고자 하는 파일의 GCS 경로를 전달해서 Form Parcer 호출
# 2) 파싱된 값 리턴
# 3) 특정값만 DB Insert