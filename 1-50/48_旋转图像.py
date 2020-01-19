class Solution:

    # 利用数学旋转公式
    def rotate(self, matrix: [[int]]) -> None:
        height, width = len(matrix), len(matrix[0])
        # 旋转中心
        center = (height / 2 - 0.5, width / 2 - 0.5)
        # 转过的索引记录一下，防止多次旋转
        index_rotated = set()
        for index_1 in range(height):
            for index_2 in range(width):
                coo = (index_1, index_2)
                if coo in index_rotated:
                    continue
                coo_first = coo
                matrix_val = matrix[index_1][index_2]
                while True:
                    # 计算的顺时针寻转90度的公式
                    coo_next = (int(coo[1] - center[1] + center[0]), int(center[0] - coo[0] + center[1]))
                    index_rotated.add(coo_next)
                    matrix[coo_next[0]][coo_next[1]], matrix_val = matrix_val, matrix[coo_next[0]][coo_next[1]]
                    if coo_next == coo_first:
                        break
                    coo = coo_next





        pass


if __name__ == "__main__":
    x = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(x)
    print(x)
