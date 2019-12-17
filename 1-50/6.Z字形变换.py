"""
@Author: AKSTT
@Problem:
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
"""


# 输出有一定的规律
# 转化结果以numRows*2-2为周期，输出以每周期首尾分别输出
# 时间复杂度O(n),空间复杂度O(n)
def convert_1(s: str, numRows: int) -> str:
    if numRows == 1 or numRows > len(s):
        return s
    result = []
    cycle = 2 * numRows - 2
    for i in range(numRows):
        j = 0
        if i == 0 or i == numRows - 1:
            while j * cycle + i < len(s):
                result.append(s[j * cycle + i])
                j += 1
        else:
            while j * cycle + i < len(s):
                result.append(s[j * cycle + i])
                if (j + 1) * cycle - i < len(s):
                    result.append(s[(j + 1) * cycle - i])
                j += 1
    return "".join(result)


if __name__ == "__main__":
    s = "AB"
    numRows = 1
    print(convert_1(s, numRows))