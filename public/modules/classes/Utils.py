import os
import json

from pygame import Vector2, Vector3, Rect

shapes_base_path = os.path.join(os.getcwd(), "public/modules/Shapes")

def printArr(arr, indentation = 4):
    print(json.dumps(arr, indent = indentation))

def createVector(tup) -> Vector2:
    return Vector2(*tup)

def createVector3(tup) -> Vector3:
    return Vector3(*tup)

def createRect(rec):
    return Rect(*rec)

def getMatrixRows(mat) -> int:
    rows = False if not mat else False if type(mat) is not list else len(mat)
    
    return rows
    
def getMatrixCols(mat) -> int:
    cols = False if not mat else False if type(mat[0]) is not list else len(mat[0])
    
    return cols

def loadJSON(name, path = False):
    global shapes_base_path

    f = ""

    if(not path):
        f = open(os.path.realpath(f"{shapes_base_path}/{name}.json"))
    else:
        f = open(os.path.realpath(f"{path}/{name}.json"))

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    return data

#Solo servira para matrices, debe tener minimo un array dentro ([[1, 2, 3]]), arrays planos no son validos ([1, 2, 3])
def mat_mult(mat1, mat2):
    rows_mat1 = getMatrixRows(mat1)
    cols_mat1 = getMatrixCols(mat1)

    if not isinstance(mat2, int):
        rows_mat2 = getMatrixRows(mat2)
        cols_mat2 = getMatrixCols(mat2)

        pln_mat1 = str(rows_mat1) + "x" + str(cols_mat1)
        pln_mat2 = str(rows_mat2) + "x" + str(cols_mat2)

        if(rows_mat1 != False and cols_mat1 != False and rows_mat2 != False and cols_mat2 != False):
            compatible = cols_mat1 == rows_mat2
        
            res = [[0] * cols_mat2 for row in range(rows_mat1)] if compatible else False

            if compatible:
                for i in range(rows_mat1):
                    for j in range(cols_mat2):
                        mul = 0

                        for x in range(rows_mat2):
                            mul += (mat1[i][x] * mat2[x][j])
                        
                        res[i][j] = mul

            else:
                res = "La matriz " + pln_mat1 + " no es compatible con la matriz: " + pln_mat2
                    
            return res

        return "No se ha podido reconcer el numero de filas o columnas de las matrices de manera correcta!"

    else:
        newMat = [[0] * cols_mat1 for row in range(rows_mat1)]

        for x in range(rows_mat1):
            for y in range(cols_mat1):
                newMat[x][y] = mat1[x][y]
                newMat[x][y] *= mat2

        return newMat