
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
    def __get_sub_mat(matrix, excluded_row, excluded_col):
        assert len(matrix) > 0, "Can't Get a sub matrix from an empty matrix"

        sub_mat = []
        ROWS, COLS = len(matrix), len(matrix[0])
        for row_idx in ROWS:

            new_row = []
            for col_idx in COLS:
                if col_idx != excluded_col and row_idx != excluded_row:
                    new_row.append(matrix[row_idx][col_idx])

            sub_mat.append(new_row)
        
        return sub_mat


    @staticmethod   
    def determinant(matrix:list[list]):
        assert len(matrix) == len(matrix[0])

        if len(matrix) == 2 and len(matrix[0]) == 2:
            return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]) # Formula to get the determinant of a 2x2 matrix
        
        res = 0
        sign = 1
        for i in len(matrix[0]): # Go over all elements of first row

            sub_mat = Matrix.__get_sub_mat(matrix, 0, i) # Calculate the sub matrix of the current element

            res += (sign * matrix[0][i]) * Matrix.determinant(sub_mat) # Calculate part of the equation
            sign = -1 * sign

        return res

    def cofactor(matrix:list[list]):
        sign = 1
