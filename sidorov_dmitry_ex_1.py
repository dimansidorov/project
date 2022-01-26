class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __len__(self):  # без этого метода не хотел делать проверку длин списков матрицы
        return len(self.matrix)

    def __add__(self, other_matrix):
        if len(self.matrix[0]) != len(other_matrix[0]):
            raise ValueError('Матрицы нельзя сложить, так как колличество столбцов не совпадает')
        else:
            new_matrix = [[0] * (len(self.matrix[0])) for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    new_matrix[i][j] = self.matrix[i][j] + other_matrix[i][j]
            return Matrix(new_matrix)

    def __getitem__(self, index):      # без этого метода не хотел складывать матрицы, прочитал, что достаточно его просто опередлить
        return self.matrix[index]


n = int(input('Введите колличество строк для Матриц: '))  # можно было задать второй параметр и не потребовалась бы проверка на длины и передавать через range(m)
matrixA = Matrix([[int(j) for j in input(f'Введите {i + 1} строку для матрицы А: ').split()] for i in range(n)])
matrixB = Matrix([[int(k) for k in input(f'Введите {l + 1} строку для матрицы B: ').split()] for l in range(n)])
matrixC = matrixA + matrixB
print(f'Новая матрица, полученная путем сложения двух матриц имеет вид:\n{matrixC}')
