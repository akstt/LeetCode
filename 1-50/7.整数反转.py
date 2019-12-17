"""
@Author: AKSTT
@Problem:
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
"""


# 时间复杂度O(n), 空间复杂度O(n)
def reverse(x: int) -> int:
    # 数值范围为 [−231,  231 − 1],超出输出0
    if x < -2147483648 or x > 2147483647:
        return 0
    x_abs = abs(x)
    # 利用字符串反转
    # result = int(str(x_abs)[::-1])
    # 计算反转
    result = 0
    while x_abs > 0:
        result = result * 10 + x_abs % 10
        x_abs = x_abs // 10
    if x < 0:
        result = -result
    if result < -2147483648 or result > 2147483647:
        return 0
    else:
        return result


if __name__ == "__main__":
    x = 120
    print(reverse(x))
