def Addition_Of_Matrixes(Matrix1, Matrix2):
    Addition = []
    StorageFactor = len(Matrix1)-1
    y = 0
    for y in range(StorageFactor):
        Addition.append([])
        for x in range(StorageFactor):
            Factor1 = Matrix1[x] + Matrix2[x]
            Addition[y][x] = Factor1
    Addition2 = Addition
    return Addition2
            
Matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
Matrix2 = [[1,2,3],[1,2,3],[1,2,3]]

Addition3 = Addition_Of_Matrixes(Matrix1,Matrix2)
print(Addition3)
