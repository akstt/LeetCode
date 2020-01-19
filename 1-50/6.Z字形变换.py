
class Solution:

    # 输出有一定的规律
    # 遍历字符串时间复杂度O(n)
    # 保存新结果，空间复杂度O(n)
    def convert_1(self, s: str, numRows: int) -> str:
        # 这种情况下，字符串不会改变
        if numRows == 1 or numRows > len(s):
            return s
        # 保存每行结果，共有numRows行
        result = [[] for _ in range(numRows)]
        # index_row保存当前结果的行数
        index_row = 0
        # index_row移动方向
        step = 1
        for val in s:
            result[index_row].append(val)
            index_row += step
            # step改变方向
            if index_row == numRows - 1:
                step = -1
            elif index_row == 0:
                step = 1
        return "".join(["".join(_) for _ in result])


if __name__ == "__main__":
    s = "AB"
    numRows = 1
    print(Solution().convert_1(s, numRows))
