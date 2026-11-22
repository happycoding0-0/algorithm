# N , M = map(int, input().split(' '))

# if N >=3 and M >=3:

#     A = []
#     B = []

#     ## 이거 아니네, M 번 이 총 N 번 일어나네
#     # for i in range(N):
#     #     for j in range(M):
#     #         x = str(input())


#     # for i in range(N):
#     #     x = str(input())
#     #     x = list(x)
#     #     for j in range(M):

    
#     # for i in range(N):
#     #     x = str(input())
#     #     A.append(list(x))
        


#     # for i in range(N):
#     #     for j in range(M):
#     #         A[i][j] = int(A[i][j])
#     #         print(type(A[i][j]))
#     # print(A)

#     # 위코드처럼 분리되어있었는데 합침
#     # 행렬 A
#     for i in range(N):
#             x = str(input())
#             A.append(list(x))
#             for j in range(M):
#                 A[i][j] = int(A[i][j])
#                 #print(type(A[i][j]))
#     #print(A)

#     # 행렬 B
#     for i in range(N):
#                 x = str(input())
#                 B.append(list(x))
#                 for j in range(M):
#                     B[i][j] = int(B[i][j])
#                     #print(type(A[i][j]))
#     #print(B)

#     print(A)
#     print(B)






    


# else:
#     print(-1)




# -----

N , M = map(int, input().split(' '))

# A = [] 
# B = []
A,B = [],[]


# 행렬 A
for i in range(N):
        x = str(input())
        A.append(list(x))
        for j in range(M):
            A[i][j] = int(A[i][j])
            #print(type(A[i][j]))
#print(A)
# 행렬 B
for i in range(N):
            x = str(input())
            B.append(list(x))
            for j in range(M):
                B[i][j] = int(B[i][j])
                #print(type(A[i][j]))
#print(B)


print(A)
print(B)

# Goal : 필요한 연산의 횟수의 최솟값을 구하는 프로그램

# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것
# 만약 A를 B로 바꿀 수 없다면 -1
# 3 x 3 의 부분 행렬을 만들 수있어야한다 그리고 A를 B로 바꿀 수 있어야 한다.
# 위에서 3 x 3 행렬을 만족했을 때 , A를 B로 바꿀 수 없는 상황을 찾았다.

# 3 3
# 000
# 111
# 101

# 101
# 010
# 101

# 조건1. 입력받은 N >= 3 , M >= 3 ?
if N >= 3 and M >= 3 :
       pass
else:
       print(-1)


# 연산 규칙: 어떤 위치의 숫자를 기준으로 양 옆 고려하기







