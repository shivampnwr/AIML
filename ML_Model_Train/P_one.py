def matrix_additon (matrix1 , matrix2):
        return [
               [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] # inner loop for number of column
                for i in range(len(matrix1))
                ] # outer loop for number of rows


def matrix_substraction(matrix1 , matrix2):
        return [
               [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] # inner loop for number of column
                for i in range(len(matrix1))
                ] # outer loop for number of rows

def matrix_multiplication(matrix1 , matrix2):
        result =  [
               [sum(a * b for a,b in zip(matrix1_row , matrix2_column))
                for matrix2_column in zip(*matrix2)]
                 for matrix1_row in matrix1
                 ]
        return result

def print_matrix(matrix):
        for rows in matrix :
            print(rows)  
     
def input_matrtix(rows , cols) :
        matrix = []
        for i in range(rows) :
            row = list(map(int,input(f"ENTER ROW {i + 1} :").split()))
            matrix.append(row)
        return matrix

def main():
    rows = int(input("ENTER NUMBER OF ROWS :"))
    cols = int(input("ENTER NUMBER OF COLUMNS :"))

    print("--ENTER MATRIX 1--")
    matrix1 = input_matrtix(rows,cols)

    print("--ENTER MATRIX 2--")
    matrix2 = input_matrtix(rows,cols)

    print("\nMATRIX 1 :")
    print_matrix(matrix1)

    print("\nMATRIX 2 :")
    print_matrix(matrix2)

    print("\nADDITION :")
    print_matrix(matrix_additon(matrix1 , matrix2))

    print("\nSUBSTRACTION :")
    print_matrix(matrix_substraction(matrix1 , matrix2))

    print("\nMULTIPICATION :")
    print_matrix(matrix_multiplication(matrix1 , matrix2))


main()
       
    
                