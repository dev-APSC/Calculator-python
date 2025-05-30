# matrix_calculator.py

import numpy as np

def get_matrix(prompt):
    rows = int(input(f"Enter number of rows for {prompt}: "))
    cols = int(input(f"Enter number of columns for {prompt}: "))
    print(f"Enter the elements row-wise for {prompt}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Invalid number of elements!")
            return None
        matrix.append(row)
    return np.array(matrix)

def main():
    print("===== Matrix Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")

    choice = input("Choose operation (1/2/3/4): ")

    if choice in ['1', '2', '3']:
        A = get_matrix("Matrix A")
        B = get_matrix("Matrix B")
        if A is None or B is None:
            return

        if choice == '1':
            if A.shape != B.shape:
                print("Error: Matrices must be of same dimensions for addition.")
                return
            result = A + B

        elif choice == '2':
            if A.shape != B.shape:
                print("Error: Matrices must be of same dimensions for subtraction.")
                return
            result = A - B

        elif choice == '3':
            if A.shape[1] != B.shape[0]:
                print("Error: Columns of A must equal rows of B for multiplication.")
                return
            result = np.dot(A, B)

    elif choice == '4':
        A = get_matrix("Matrix")
        if A is None:
            return
        result = A.T

    else:
        print("Invalid choice!")
        return

    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()