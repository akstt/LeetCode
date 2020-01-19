class Solution:

    # 用栈存储左括号，每有一个右括号，从栈中弹出一个左括号与之匹配，计算当前匹配括号最长长度
    # 时间复杂度O(n)
    # 空间复杂度O(n)
    def longestValidParentheses_1(self, s: str) -> int:
        # sign_store存储左括号的索引
        # index_start的值为(最后一个左括号的索引-1)
        index_start = -1
        sign_store = [index_start]
        num_max = 0
        for index_1, sign in enumerate(s):
            # 存储左括号的索引
            if sign == "(":
                sign_store.append(index_1)
            else:
                # 当有左括号匹配时
                if sign_store[-1] != index_start:
                    sign_store.pop()
                    num_max = max(num_max, index_1 - sign_store[-1])
                # 当无左括号匹配时
                else:
                    index_start = index_1
                    sign_store[0] = index_start
        return num_max

    # 动态规划
    # 时间复杂度O(n)
    # 空间复杂度O(n)
    def longestValidParentheses_2(self, s: str) -> int:
        if not s:
            return 0
        result = [0] * len(s)
        for index_1 in range(1, len(s)):
            if s[index_1] == ")" and s[index_1-1] == "(":
                result[index_1] = result[index_1-2] + 2
            elif s[index_1] == ")" and s[index_1-1] == ")":
                index_2 = index_1 - result[index_1-1] - 1
                if index_2 >= 0 and s[index_2] == "(":
                    result[index_1] = result[index_1-1] + result[index_2-1] + 2
        return max(result)

    # 计算左括号和右括号的数量，比较得到答案
    # 在这串字符串中找到一串最长子串，这串子串左括号数量等于右括号数量
    # 时间复杂度O(n)
    # 空间复杂度O(1)
    def longestValidParentheses_3(self, s: str) -> int:
        l_num_1, r_num_1 = 0, 0
        l_num_2, r_num_2 = 0, 0
        num_max = 0
        for sign in s:
            if sign == "(":
                l_num_1 += 1
            else:
                r_num_1 += 1
            if r_num_1 == l_num_1:
                num_max = max(num_max, l_num_1 + r_num_1)
            elif r_num_1 > l_num_1:
                l_num_1, r_num_1 = 0, 0
        for sign in s[::-1]:
            if sign == "(":
                l_num_2 += 1
            else:
                r_num_2 += 1
            if r_num_2 == l_num_2:
                num_max = max(num_max, l_num_2 + r_num_2)
            elif r_num_2 < l_num_2:
                r_num_2, l_num_2 = 0, 0
        return num_max


if __name__ == "__main__":
    print(Solution().longestValidParentheses_3("(()"))
