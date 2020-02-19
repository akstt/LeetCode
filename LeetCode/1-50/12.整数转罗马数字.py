class Solution:

    # 从最大到最小依次匹配
    # 贪心算法
    def intToRoman(self, num: int) -> str:
        # 整数与罗马数字的对应
        num_int = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        num_roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for num_1, roman_1 in zip(num_int, num_roman):
            num_temp = num // num_1
            result.extend([roman_1] * num_temp)
            num %= num_1
            # 下面的循环体和上面作用是一样的
            # 因为罗马数字相同字母出现次数最多为3个，所以用下面的循环体会好一些
            # while num_1 <= num:
            #     result.append(roman_1)
            #     num -= num_1

        return ''.join(result)


if __name__ == "__main__":
    num = 3
    print(Solution().intToRoman(num))
