class Solution:

    # 跟12题想法一样
    def romanToInt_1(self, s: str) -> int:
        num_int = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        num_roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = 0
        for int_1, roman_1 in zip(num_int, num_roman):
            while s.startswith(roman_1):
                result += int_1
                s = s[len(roman_1):]
        return result

    # 罗马数字字符，左侧字符应该是大于等于右侧字符
    # 罗马数字两个字符的，左字符都比右字符小
    # 遍历罗马字符
    def romanToInt_2(self, s: str) -> int:
        roman_2_int = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                       'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                       'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        result = 0
        for index_1, roman_1 in enumerate(s):
            try:
                if roman_2_int[s[index_1 + 1]] > roman_2_int[roman_1]:
                    result -= roman_2_int[roman_1]
                else:
                    result += roman_2_int[roman_1]
            except IndexError:
                result += roman_2_int[roman_1]
        return result


if __name__ == "__main__":
    s = "III"
    print(Solution().romanToInt_1(s))
