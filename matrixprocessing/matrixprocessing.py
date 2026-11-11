def read_matrix():
    """Считывает матрицу из ввода."""
    try:
        line = input().strip()
        if not line:
            return None
        parts = line.split()
        if len(parts) == 1:
            rows, cols = int(parts[0]), int(input().strip())
        else:
            rows, cols = int(parts[0]), int(parts[1])

        matrix = []
        for _ in range(rows):
            row = [float(x) if '.' in x or 'e' in x.lower() else int(x) for x in input().split()]
            matrix.append(row)
        return matrix
    except Exception:
        return None


def format_num(val):
    """Форматирует число (убирает лишние .0 для целых чисел для красоты вывода)."""
    if isinstance(val, float) and val.is_integer():
        return int(val)
    return round(val, 4)


def print_matrix(matrix):
    for row in matrix:
        print(*(format_num(x) for x in row))


def add_matrices():
    print("Enter size of first matrix: ", end="")
    m1 = read_matrix()
    print("Enter size of second matrix: ", end="")
    m2 = read_matrix()

    if not m1 or not m2 or len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("The operation cannot be performed.")
        return

    result = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    print("The result is:")
    print_matrix(result)


def multiply_by_constant():
    print("Enter size of matrix: ", end="")
    m = read_matrix()
    print("Enter constant: ", end="")
    try:
        const_input = input().strip()
        const = float(const_input) if '.' in const_input else int(const_input)
    except:
        print("The operation cannot be performed.")
        return

    if not m:
        print("The operation cannot be performed.")
        return

    result = [[cell * const for cell in row] for row in m]
    print("The result is:")
    print_matrix(result)


def multiply_matrices():
    print("Enter size of first matrix: ", end="")
    m1 = read_matrix()
    print("Enter size of second matrix: ", end="")
    m2 = read_matrix()

    if not m1 or not m2 or len(m1[0]) != len(m2):
        print("The operation cannot be performed.")
        return

    rows1, cols1 = len(m1), len(m1[0])
    cols2 = len(m2[0])

    result = [[sum(m1[i][k] * m2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    print("The result is:")
    print_matrix(result)


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: > ").strip()

    print("Enter matrix size: ", end="")
    m = read_matrix()
    if not m:
        print("The operation cannot be performed.")
        return

    rows, cols = len(m), len(m[0])
    if choice == '1':
        result = [[m[j][i] for j in range(rows)] for i in range(cols)]
    elif choice == '2':
        result = [[m[rows - 1 - j][cols - 1 - i] for j in range(rows)] for i in range(cols)]
    elif choice == '3':
        result = [[row[::-1] for row in m]]  # исправлено для корректного среза
        result = [row[::-1] for row in m]
    elif choice == '4':
        result = m[::-1]
    else:
        print("The operation cannot be performed.")
        return

    print("The result is:")
    print_matrix(result)


def get_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(n):
        sign = (-1) ** c
        sub_det = determinant(get_minor(matrix, 0, c))
        det += sign * matrix[0][c] * sub_det
    return det


def calculate_determinant():
    print("Enter matrix size: ", end="")
    m = read_matrix()
    if not m or len(m) != len(m[0]):
        print("The operation cannot be performed.")
        return
    det = determinant(m)
    print("The result is:")
    print(format_num(det))


def inverse_matrix():
    print("Enter matrix size: ", end="")
    m = read_matrix()
    if not m or len(m) != len(m[0]):
        print("This matrix doesn't have an inverse.")
        return

    n = len(m)
    det = determinant(m)
    if abs(det) < 1e-9:
        print("This matrix doesn't have an inverse.")
        return

    if n == 1:
        print("The result is:")
        print(format_num(1 / m[0][0]))
        return

    cofactors = []
    for i in range(n):
        cof_row = []
        for j in range(n):
            minor = get_minor(m, i, j)
            sign = (-1) ** (i + j)
            cof_row.append(sign * determinant(minor))
        cofactors.append(cof_row)

    # Транспонируем матрицу алгебраических дополнений (союзная матрица)
    adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]

    inv_det = 1 / det
    inverse = [[adjugate[i][j] * inv_det for j in range(n)] for i in range(n)]

    print("The result is:")
    print_matrix(inverse)


def main():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        choice = input("Your choice: > ").strip()
        if choice == '1':
            add_matrices()
        elif choice == '2':
            multiply_by_constant()
        elif choice == '3':
            multiply_bytes = multiply_matrices()
        elif choice == '4':
            transpose_matrix()
        elif choice == '5':
            calculate_determinant()
        elif choice == '6':
            inverse_matrix()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
