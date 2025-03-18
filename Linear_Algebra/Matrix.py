class Matrix:

    def __init__(self, rows:int, cols:int):
        self.rows = rows
        self.cols = cols
        self.elements = [[0]*cols]*rows

    
    def __init__(self, order:int):
        self.rows = order
        self.cols = order
        self.elements = [[0]*order]*order

    def __init__(self, elements:int, rows:int, cols:int):
        self.elements = [[0]*cols]*rows
        
        for i, element in enumerate(elements):
            row, col = divmod(i, cols)
            self.elements[row][col] = element
    
    @staticmethod    
    def __get_minor_mat(matrix, excluded_row, excluded_col):
        assert len(matrix) > 0 , "Can't Get a sub matrix from an empty matrix"

        # Initialize variables
        sub_mat = []
        ROWS, COLS = len(matrix), len(matrix[0])

        for row_idx in ROWS:

            new_row = []
            for col_idx in COLS:
                if col_idx != excluded_col and row_idx != excluded_row: 
                    new_row.append(matrix[row_idx][col_idx]) # Add the element if and only if it is not the specified excluded row or the column

            sub_mat.append(new_row)
        
        return sub_mat
    
    @staticmethod
    def __foreach(matrix:list[list], operation) -> list[list]:
        if not matrix: return matrix

        new_mat = []
        ROWS, COLS = len(matrix), len(matrix[0])

        for i in range(ROWS):
            new_row = []
            for j in range(COLS):
                new_row.append(operation(matrix[i][j]))

            new_mat.append(new_row)

        return new_mat
    
    @staticmethod
    def is_square_matrix(matrix:list[list]) -> bool:
        return len(matrix) == 0 or len(matrix) == len(matrix[0])
    
    @staticmethod
    def transpose(matrix:list[list]) -> list[list]:
        if len(matrix) == 0: return matrix # Return itself if the mat is empty
        # return [[matrix[i][j] for i in range(len(matrix))]for j in range(len(matrix[0]))] # Alt one liner

        # Initialize variables
        matrix_T = []
        ROWS, COLS = len(matrix), len(matrix[0])

        # Swap each row with each column
        for col in range(COLS):
            new_row = []
            for row in range(ROWS):
                new_row.append(matrix[row][col])
            matrix_T.append(new_row)

        return matrix_T
    
    @staticmethod
    def scalar_product(scalar, matrix:list[list]):

        def product(element):
            return scalar * element
        
        return Matrix.__foreach(matrix, product)

    @staticmethod
    def matrix_product(matrix1:list[list], matrix2:list[list]):
        pass

    @staticmethod
    def matrix_sum(matrix1:list[list], matrix2:list[list]):
        pass

    @staticmethod
    def is_diagonal(matrix:list[list]):
        pass

    @staticmethod
    def is_upper_triangular(matrix:list[list]):
        pass

    @staticmethod
    def is_lower_triangular(matrix:list[list]):
        pass

    @staticmethod   
    def determinant(matrix:list[list]):
        if len(matrix) == 0: return 0 # Return itself if the mat is empty
        assert Matrix.is_square_matrix(matrix), "Matrix must be square to have a determinant"

        if len(matrix) == 1:
            return matrix[0][0]
        
        res = 0
        sign = 1
        COLS = len(matrix[0])
        for i in range(COLS): # Go over all elements of first row

            sub_mat = Matrix.__get_minor_mat(matrix, 0, i) # Calculate the sub matrix of the current element

            res += (sign * matrix[0][i]) * Matrix.determinant(sub_mat) # Calculate part of the equation
            sign = -1 * sign # Invert the sign

        return res
      
    @staticmethod
    def cofactor(matrix:list[list]) -> list[list]:
        if matrix == []: return [] # Return [] if the mat is empty
        assert Matrix.is_square_matrix(matrix), "Matrix must be square to have cofactor"
        
        mat_res = []
        sign = 1
        ROWS, COLS = len(matrix), len(matrix[0])

        for cur_row in range(ROWS):
            new_row = []  

            for cur_col in range(COLS):
                # Calculate the current element of the current position
                cur_sub_mat = Matrix.__get_minor_mat(matrix, cur_row, cur_col) # Calculate the current sub matrix by excluding the row and the column of the current element 
                new_element = sign*Matrix.determinant(cur_sub_mat) # Calculate the det of the current sub matrix
                new_row.append(new_element) # Add the result to the current row of the cofactor matrix
                sign = -1*sign # Invert the sign

            mat_res.append(new_row)

        return mat_res

    @staticmethod 
    def adjoint(matrix:list[list]) -> list[list]:
        if matrix == [] : return []
        assert len(matrix) == len(matrix[0]), "Matrix must be square to have adjoint"
        return Matrix.transpose(Matrix.cofactor(matrix))
    
    @staticmethod
    def inverse(matrix:list[list]):
        if len(matrix) == 0: return matrix
        assert len(matrix) == len(matrix[0]) and Matrix.determinant(matrix) != 0, "Matrix must be square to have adjoint"

        adj = Matrix.adjoint(matrix)
        det = Matrix.determinant(matrix)
        return Matrix.scalar_product(1/det, adj)
    



