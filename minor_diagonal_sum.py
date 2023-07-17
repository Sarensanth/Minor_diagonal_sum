def minor_diagonal_sum(matrix,rows,columns):

    sum=0
    j=rows-1
    for i in range(rows):
        sum+=matrix[i][j]
        j-=1
    return sum

matrix=[]
rows=int(input("Enter number of rows : "))
columns=int(input("Enter number of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))

print(minor_diagonal_sum(matrix,rows,columns))