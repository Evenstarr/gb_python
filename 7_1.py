class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = {len(r) for r in self.matrix}
        if len(self.size) != 1:
            raise ValueError("Incorrect matrix format")

    def __str__(self):
        m = '\n'.join(['\t'.join([str(el1) for el1 in el]) for el in self.matrix])
        return '\n' + m

    def __add__(self, other):
        if self.size != other.size or len(self.matrix) != len(other.matrix):
            return "Dimension error - can add just matrices with same dimensions"
        else:
            return Matrix([list(map(sum, zip(*t))) for t in zip(self.matrix, other.matrix)])


matrix_1 = Matrix([[1, 2, 3, 5], [3, 4, 5, 6], [3, 7, 9, 10]])
matrix_2 = Matrix([[7, 8, 9, 8], [9, 10, 11, 12], [8, 90, 45, 5]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
