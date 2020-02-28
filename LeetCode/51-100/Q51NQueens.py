class Solution:


    def solveNQueens(self, n: int) -> [[str]]:
        """
        回溯法解决，
        :param n: n皇后
        :return:
        """
        result = []
        # 皇后所在列
        queens_index = []
        # 皇后所在斜线，左上至右下
        diagonal_1 = []
        # 皇后所在斜线，左下至右上
        diagonal_2 = []
        self.add_queens(0, n, queens_index, diagonal_1, diagonal_2, result)
        return result

    def add_queens(self, row_index, n, queens_index, diagonal_1, diagonal_2, result):
        if row_index < n:
            for col_index in range(n):
                # 判断是否可以放置
                dia_1 = col_index - row_index + n - 1
                dia_2 = col_index + row_index
                if not (col_index in queens_index or dia_1 in diagonal_1 or dia_2 in diagonal_2):
                    queens_index.append(col_index)
                    diagonal_1.append(dia_1)
                    diagonal_2.append(dia_2)
                    self.add_queens(row_index+1, n, queens_index, diagonal_1, diagonal_2, result)
                    queens_index.pop()
                    diagonal_1.pop()
                    diagonal_2.pop()
        else:
            result.append(self.to_str(queens_index, n))

    def to_str(self, queens_index, n):
        picture = []
        for queen in queens_index:
            queen_str = ""
            for i in range(n):
                if i == queen:
                    queen_str += "Q"
                else:
                    queen_str += "."
            picture.append(queen_str)
        return picture

def main():
    print(Solution().solveNQueens(1))

if __name__ == "__main__":
    main()

