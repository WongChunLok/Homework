for i in range(5):
    matrix=list(map(int,input().split()))
    if 1 in matrix:
        matrix_row=matrix
        row=i+1
        

for i in range(len(matrix_row)):
    if matrix_row[i] == 1:
        column=i+1

print(abs(3-row)+abs(3-column))