class Solution:

    # 基本想法，用x^n_num逼近x^n
    # 1.第一次循环中，令x = x * x； n_num: 代表x的倍率, n_num = n_num*2,直到n_num >n
    # 2.第二次循环中，如果n_num >n 则n_num /= 2, x = sqrt(x),否则n -= n_num, result *= x,知道n为0

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        result = 1
        # x的倍率
        n_num = 1
        x_list = []
        while n >= n_num:
            x_list.append(x)
            x = x * x
            n_num *= 2
        while n > 0:
            n_num /= 2
            x = x_list.pop()
            while n >= n_num:
                result = result * x
                n -= n_num
        return result


if __name__ == "__main__":
    x, y = 2.1, 3
    print(Solution().myPow(x, y))
