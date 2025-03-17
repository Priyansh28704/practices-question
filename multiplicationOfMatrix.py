A= [[2,5,4],
    [3,6,9],
    [1,4,7]]

B= [[5,6,7],
    [2,3,4],
    [8,9,1]]

result= [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(B[0])):
            result[i][j] += A[i][k] * B[k][j]

for i in result:
    print(i)