class Solution:
    # 动态规划
    # 一个回文字符串的起始位置为i，结束位置为j，如果i-1，j+1处的字符相同，那么i-1至j+1也一定是回文字符串
    # 共有n^2个子串，时间复杂度为O(n^2),
    # 存储n^2个子串是否回文，空间复杂度为O(n^2)
    def longestPalindrome_1(self, s: str) -> str:
        len_max = 1
        start_index, end_index = 0, 0
        # key: [index_start, index_end]
        # value: 是否是回文字符串
        if_str = {(i, j): False for j in range(len(s)) for i in range(j)}
        for j in range(len(s)):
            for i in range(j):
                if (j - i < 3 or if_str[i + 1, j - 1]) and s[i] == s[j]:
                    if_str[(i, j)] = True
                    if j - i + 1 > len_max:
                        len_max = j - i + 1
                        start_index, end_index = i, j
        return s[start_index: end_index + 1]

    # Manacher算法
    # 解释挺麻烦的，建议上网查
    # 时间复杂度为O(n) 
    # 新建立字符串，空间复杂度为O(n)
    def longestPalindrome_2(self, s: str) -> str:
        len_max = 0
        start_index, end_index = 0, 0
        # 字符串预处理
        s_new = "#".join(list(s))
        s_new = "#" + s_new + "#"
        # 存储s_new各索引处，最长回文字符串对称长度
        s_len = [0] * len(s_new)
        # 对称中心center, 对称右边界r_max(此处对称)
        center, r_max = 0, 0
        for i in range(len(s_new)):
            if i < r_max:
                s_len[i] = min(s_len[2 * center - i], r_max - i)
            while i - s_len[i] >= 0 and i + s_len[i] < len(s_new) and s_new[i - s_len[i]] == s_new[i + s_len[i]]:
                s_len[i] += 1
            if i + s_len[i] > r_max:
                center = i
                r_max = i + s_len[i]
            if s_len[i] - 1 > len_max:
                len_max = s_len[i] - 1
                start_index, end_index = i - s_len[i] + 1, i + s_len[i] - 1
        return s[start_index // 2: end_index // 2]


if __name__ == "__main__":
    s = "babad"
    s = "a"
    print(Solution().longestPalindrome_2(s))
