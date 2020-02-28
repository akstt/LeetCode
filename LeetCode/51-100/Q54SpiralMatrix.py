class Solution:

    def spiralOrder(self, matrix: [[int]]) -> [int]:
        result = []
        if len(matrix) == 0:
            return result
        index_row_1 = 0
        index_row_2 = len(matrix) - 1
        index_col_1 = 0
        index_col_2 = len(matrix[0]) - 1

        while index_row_1 <= index_row_2 and index_col_1 <= index_col_2:
            for i in range(index_col_1, index_col_2 + 1):
                result.append(matrix[index_row_1][i])
            index_row_1 += 1
            for i in range(index_row_1, index_row_2 + 1):
                result.append(matrix[i][index_col_2])
            index_col_2 -= 1
            if index_row_1 > index_row_2 or index_col_1 > index_col_2:
                break
            for i in range(index_col_2, index_col_1 - 1, -1):
                result.append(matrix[index_row_2][i])
            index_row_2 -= 1
            for i in range(index_row_2, index_row_1 - 1, -1):
                result.append(matrix[i][index_col_1])
            index_col_1 += 1
        return result
