A= [[2,5,4],
    [3,6,9]]

T= [[0,0],
    [0,0],
    [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i]=A[i][j]

for i in T:
    print(i)