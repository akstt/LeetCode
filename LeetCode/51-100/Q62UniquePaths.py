class Solution:

    # 排列组合
    # 右移m-1格，下移 n-1格
    def uniquePaths(self, m: int, n: int) -> int:
        num_1 = m + n - 2
        num_min = min(m, n)
        num_mul_1 = 1
        num_mul_2 = 1
        for num_2 in range(1, num_min):
            num_mul_1 *= num_1
            num_mul_2 *= num_2
            num_1 -= 1
        return num_mul_1 // num_mul_2

print(Solution().uniquePaths(7, 3))
