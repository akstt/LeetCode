"""
@Author: AKSTT
@Problem:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""


# 暴力求解, 时间复杂度为O(n^3)。存储结果，空间复杂度为O(n)
def longestPalindrome_1(s: str) -> str:
    max_len = 1
    start_index, end_index = 0, 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            # s_temp = s[i:j + 1]
            # 判断s_temp是否是回文字符
            l, m = i, j
            while m > l:
                if s[l] != s[m]:
                    break
                l += 1
                m -= 1
            # 如果为回文字符
            else:
                len_str = j - i + 1
                if len_str > max_len:
                    max_len = len_str
                    start_index, end_index = i, j
    return s[start_index:end_index + 1]


# 从中间开始朝两边找回文字符串
# 时间复杂度为O(n^2), 空间复杂度为O(n)
def longestPalindrome_2(s: str) -> str:
    max_len = 1
    start_index, end_index = 0, 0
    for i in range(len(s)):
        # 两种情况
        # 以i为中心，回文字符串长度为奇数, 以i和i+1为中心，回文字符串长度为偶数
        index_ = [[i - 1, i + 1], [i, i + 1]]
        for index_1, index_2 in index_:
            while index_1 > -1 and index_2 < len(s):
                if s[index_1] != s[index_2]:
                    break
                index_1 -= 1
                index_2 += 1
            len_temp = index_2 - index_1 - 1
            if len_temp > max_len:
                max_len = len_temp
                start_index, end_index = index_1 + 1, index_2 - 1
    return s[start_index: end_index+1]


# 动态规划
# 一个回文字符串的起始位置为i，结束位置为j，如果i-1，j+1处的字符相同，那么i-1至j+1也一定是回文字符串
# 时间复杂度为O(n^2), 空间复杂度为O(n^2)
def longestPalindrome_3(s: str) -> str:
    max_len = 1
    start_index, end_index = 0, 1
    # key: [index_start, index_end)
    # value: 是否是回文字符串
    if_str = {(i, j): False for j in range(len(s) + 1) for i in range(j-1)}
    for j in range(len(s) + 1):
        for i in range(j-1):
            if (j - i < 4 or if_str[i+1, j-1]) and s[i] == s[j-1]:
                if_str[(i, j)] = True
                if j - i > max_len:
                    max_len = j - i
                    start_index, end_index = i, j
    return s[start_index: end_index]


# Manacher算法
# 解释挺麻烦的，建议上网查
# 时间复杂度为O(n), 空间复杂度为O(n)
def longestPalindrome_4(s: str) -> str:
    max_len = 1
    start_index, end_index = 0, 2
    # 字符串预处理
    s_new = "#".join(list(s))
    s_new = "#" + s_new + "#"
    # 存储字符串各处回文字符串长度
    s_len = [0 for _ in s_new]
    # 对称中心center, 对称右边界r_max
    center, r_max = 0, 0
    for i in range(len(s_new)):
        if i < r_max:
            s_len[i] = min(s_len[2*center-i], r_max-i)
        while i - s_len[i] >= 0 and i + s_len[i] < len(s_new) and s_new[i - s_len[i]] == s_new[i + s_len[i]]:
            s_len[i] += 1
        if i + s_len[i] > r_max:
            center = i
            r_max = i + s_len[i]
        if s_len[i] - 1 > max_len:
            max_len = s_len[i] - 1
            start_index, end_index = i - s_len[i] + 1, i + s_len[i] - 1
    return s[start_index//2: end_index//2]


if __name__ == "__main__":
    s = "a"
    print(longestPalindrome_4(s))
