class Solution:

    # 基本想法，一个个放，如果不符合要求，就回溯至上一个，依次类推。
    # 递归解决
    def solveSudoku(self, board: [[str]]) -> None:
        rows, columns, chunk, board_null_index = self.initialize_board(board)
        index_null = 0
        num_all = set([str(i) for i in range(1, 10)])
        result = []
        flag = self.add_num(result, rows, columns, chunk, board_null_index, index_null, num_all)
        if flag:
            for index_add, index_null in enumerate(board_null_index):
                board[index_null[0]][index_null[1]] = result[index_add]

    # 递归添加数字
    def add_num(self, result, rows, columns, chunk, board_null_index, index_null, num_all):
        try:
            index_1, index_2, index_3 = board_null_index[index_null]
        # 空缺位置填完
        except IndexError:
            return True
        # 可以填在空缺位置的值
        num_add = num_all - rows[index_1] - columns[index_2] - chunk[index_3]
        for num_temp in num_add:
            # 跟新行列块和空缺位置的信息
            result.append(num_temp)
            rows[index_1].add(num_temp)
            columns[index_2].add(num_temp)
            chunk[index_3].add(num_temp)
            flag = self.add_num(result, rows, columns, chunk, board_null_index, index_null + 1, num_all)
            # 这次添加符合要求
            if flag:
                return flag
            # 删除添加的信息
            else:
                result.pop()
                rows[index_1].remove(num_temp)
                columns[index_2].remove(num_temp)
                chunk[index_3].remove(num_temp)
        # 找不到要求的数值
        return False

    # 初始化board，存储已经出现的行列块和空缺位置
    def initialize_board(self, board):
        # 先遍历一遍board，找出每行列块的已经出现的数字，和没添加数字的索引，方便为以后添加数字
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        chunk = [set() for _ in range(9)]
        board_null_index = []
        for index_1 in range(9):
            for index_2 in range(9):
                num_temp = board[index_1][index_2]
                index_3 = index_2 // 3 * 3 + index_1 // 3
                if num_temp == ".":
                    board_null_index.append((index_1, index_2, index_3))
                rows[index_1].add(num_temp)
                columns[index_2].add(num_temp)
                chunk[index_3].add(num_temp)
        return rows, columns, chunk, board_null_index

    # 检验结果
    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        chunk = [set() for _ in range(9)]
        # 遍历board
        for index_1 in range(9):
            for index_2 in range(9):
                num_temp = board[index_1][index_2]
                # 判断现在数字是否符合要求
                if num_temp == ".":
                    return False
                index_3 = index_2 // 3 * 3 + index_1 // 3
                if (num_temp in rows[index_1]) or (num_temp in columns[index_2]) or (num_temp in chunk[index_3]):
                    return False
                else:
                    rows[index_1].add(num_temp)
                    columns[index_2].add(num_temp)
                    chunk[index_3].add(num_temp)
        return True


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(board)
    print(Solution().isValidSudoku(board))
