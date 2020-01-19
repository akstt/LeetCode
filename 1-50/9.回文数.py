class Solution:

    # 判断是否是回文数，可以利用字符串反转
    # 反转字符串，时间复杂度O(n)（n为数字的位数）
    # 保存新字符串，空间复杂度O(n)
    def isPalindrome_1(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]

    # 不利用字符串反转
    # 反转数字，时间复杂度O(n)（n为数字的位数）
    # 空间复杂度O(1)
    def isPalindrome_2(self, x: int) -> bool:
        # 反转时，如果x > 0 且个位为0，下面的判断会出错
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        # 反转数字结果
        num_reverse = 0
        # 反转一半数字
        while num_reverse < x:
            num_reverse = num_reverse * 10 + x % 10
            x = x // 10
        return num_reverse == x or num_reverse // 10 == x


if __name__ == "__main__":
    x = 0
    print(Solution().isPalindrome_2(x))
