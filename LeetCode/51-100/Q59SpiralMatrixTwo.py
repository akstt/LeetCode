class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        result = [[0] * n for i in range(n)]
        index_row_1 = 0
        index_row_2 = n - 1
        index_col_1 = 0
        index_col_2 = n - 1
        num = 1
        max_num = n * n + 1
        while num < max_num:
            for i in range(index_col_1, index_col_2 + 1):
                result[index_row_1][i] = num
                num += 1
            index_row_1 += 1
            for i in range(index_row_1, index_row_2 + 1):
                result[i][index_col_2] = num
                num += 1
            if num >= max_num:
                break
            index_col_2 -= 1
            for i in range(index_col_2, index_col_1- 1, -1):
                result[index_row_2][i] = num
                num += 1
            index_row_2 -= 1
            for i in range(index_row_2, index_row_1-1, -1):
                result[i][index_col_1] = num
                num += 1
            index_col_1 += 1
        return result

def main():
    print(Solution().generateMatrix(3))
if __name__ == "__main__":
    main()