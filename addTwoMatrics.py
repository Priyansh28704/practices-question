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
    for j in range(len(A[0])):
        result[i][j]= A[i][j]+B[i][j]

for r in result:
    print(r)