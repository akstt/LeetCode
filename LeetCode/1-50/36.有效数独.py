class Solution:

    # 三个列表，每个列表包含九个集合，分别保存行，列，块的已经出现的数字
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
                    continue
                index_3 = index_2 // 3 * 3 + index_1 // 3
                if (num_temp in rows[index_1]) or (num_temp in columns[index_2]) or (num_temp in chunk[index_3]):
                    return False
                else:
                    rows[index_1].add(num_temp)
                    columns[index_2].add(num_temp)
                    chunk[index_3].add(num_temp)
        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(board))
