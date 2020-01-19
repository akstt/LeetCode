class Solution:

    # 遍历一遍数字，时间复杂度O(n)
    # 存储结果，空间复杂度O(n)
    def reverse(self, x: int) -> int:
        # 数值范围为[−231, 231 − 1], 超出输出0
        if x < -2147483648 or x > 2147483647:
            return 0
        x_abs = abs(x)
        # 利用字符串反转， 不另写函数
        # result = int(str(x_abs)[::-1])
        # 计算反转
        result = 0
        while x_abs > 0:
            result = result * 10 + x_abs % 10
            x_abs = x_abs // 10
        if x < 0:
            result = -result
        # 数值范围为[−231, 231 − 1], 超出输出0
        if result < -2147483648 or result > 2147483647:
            return 0
        else:
            return result


if __name__ == "__main__":
    x = 120
    print(Solution().reverse(x))
