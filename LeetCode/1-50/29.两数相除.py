class Solution:

    # 将手算除法的方法编写成程序
    def divide_1(self, dividend: int, divisor: int) -> int:
        dividend_str, divisor_abs = str(abs(dividend)), abs(divisor)
        # 结果和余数
        result = 0
        remainder = 0
        # 从最高位开始取
        for num in dividend_str:
            num = int(num)
            num += remainder * 10
            result *= 10
            while num >= divisor_abs:
                result += 1
                num -= divisor_abs
            remainder = num
        # 判断结果正负
        if (dividend > 0) ^ (divisor > 0):
            result = -result
        # 越界情况
        if result < -2147483648 or result > 2147483647:
            result = 2147483647
        return result

    # 位运算的方法
    # 简单的说就是让除数*2 去逼近被除数
    # 可以写递归，下面利用的是循环
    def divide_2(self, dividend: int, divisor: int) -> int:
        dividend_abs, divisor_abs = abs(dividend), abs(divisor)
        # 除数的倍数
        time = 1
        result = 0
        # 找到最大的除数倍数
        while divisor_abs < dividend_abs:
            # 除数乘2
            divisor_abs = divisor_abs << 1
            time = time << 1
        while time:
            while divisor_abs <= dividend_abs:
                result += time
                dividend_abs -= divisor_abs
            # 除数除2
            divisor_abs = divisor_abs >> 1
            time = time >> 1
        # 判断结果正负
        if (dividend > 0) ^ (divisor > 0):
            result = -result
        # 越界情况
        if result < -2147483648 or result > 2147483647:
            result = 2147483647
        return result

if __name__ == "__main__":
    print(Solution().divide_2(1, 1))
