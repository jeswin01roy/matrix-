# getting matrix from user 
def matrixinput(x,y):
    matrix=[]
    for i in range(x):
        raw=[]
        for j in range(y):
            raw.append(int(input(f"enter the elements of metrix:")))
        matrix.append(raw)
    return matrix

#display the matrix
def displaymatrix(u,v,max):
    for i in range(u):
        for j in range(v):
            print(max[i][j],end=" ")
        print()

#addition of two matrices
def addmatrix(rows,colms,max1,max2):
    smatrix=[[0 for j in range(colms)] for i in range(rows)]
    for i in range(rows):
        for j in range(colms):
            smatrix[i][j]=(max1[i][j] + max2[i][j])
    displaymatrix(rows,colms,smatrix)
        


print("\t\tscore after flipping matrix")
matrix1=[]
matrix2=[]
r1= int(input("enter the no raws of the matrix1:"))
c1= int(input("enter the no columns of the matrix1:"))
r2= int(input("enter the no raws of the matrix2:"))
c2= int(input("enter the no columns of the matrix2:"))

print("\nelements of matrix1")
matrix1=matrixinput(r1,c1)
print("\nelements of matrix2")
matrix2=matrixinput(r2,c2)

print("the given matrix1 is:")
displaymatrix(r1,r2,matrix1)
print("\n")
print("the given matrix2 is:")
displaymatrix(r1,r2,matrix2)
print("\n")
print("the matrix after addition is")
addmatrix(r1,c1,matrix1,matrix2)
