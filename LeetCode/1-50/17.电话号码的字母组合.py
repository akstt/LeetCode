class Solution:

    # 循环遍历digits，求对应字母集合的笛卡尔积
    #
    def letterCombinations(self, digits: str) -> [str]:
        nums_2_letter = {'2': "abc", '3': "def", '4': "ghi",
                         '5': "jkl", '6': "mno", '7': "pqrs",
                         '8': "tuv", '9': "wxyz"}
        result =[]
        for num in digits:
            result_temp = result if result else ['']
            result = []
            # 遍历每个字母，添加到的组合过的字符串的末尾
            for letter_combine in result_temp:
                for letter in nums_2_letter[num]:
                    result.append(letter_combine + letter)
        return result


if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))