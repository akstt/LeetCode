"""
@Author: AKSTT
@Problem:
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为3
"""


# 暴力求解，时间复杂度为O(n^3)（两个循环外加列表转集合），空间复杂度为O(n)
def lengthOfLongestSubstring_1(s: str) -> int:
    max_len = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            len_1 = len(set(s[i:j]))
            if len_1 > max_len and len_1 == j - i:
                max_len = len_1
    return max_len


# 滑动窗口,i指向窗口起始位置，j指向窗口结束位置
# 最多循环2n次(时间复杂度为O(n))，每一次循环内都要判断是否有重复元素(时间复杂度为O(n))，所以总时间复杂度为O(n^2)
# 空间复杂度为O(n)
def lengthOfLongestSubstring_2(s: str) -> int:
    max_len, i, j = 0, 0, 1
    while j < len(s) + 1:
        len_1 = len(set(s[i:j]))
        # 无重复元素
        if len_1 == j - i:
            j += 1
            if len_1 > max_len:
                max_len = len_1
        # 有重复元素
        else:
            i += 1
    return max_len


# 滑动窗口优化，使用集合保存当前子串，集合查询，添加，删除操作的平均时间复杂度都是O(1)
# 时间复杂度为O(n),空间复杂度为O(n)
def lengthOfLongestSubstring_3(s: str) -> int:
    max_len, i, j = 0, 0, 0
    set_temp = set()
    while j < len(s):
        while s[j] in set_temp:
            set_temp.remove(s[i])
            i += 1
        set_temp.add(s[j])
        j += 1
        max_len = max(max_len, j - i)
    return max_len


# 滑动窗口优化，利用字典保存子串中各元素的索引位置，查询的平均时间复杂度为O(1),同时子串的头索引每次的可以直接移动到重复元素的位置
# 时间复杂度为O(n),空间复杂度为O(n)
def lengthOfLongestSubstring_4(s: str) -> int:
    max_len, i, j = 0, 0, 0
    dict_temp = {}
    while j < len(s):
        try:
            i = max(dict_temp[s[j]]+1, i)
        except KeyError:
            pass
        dict_temp[s[j]] = j
        j += 1
        max_len = max(j - i, max_len)
    return max_len


# lengthOfLongestSubstring_4的for循环版本,一些细节优化，逻辑更严谨
def lengthOfLongestSubstring_5(s: str) -> int:
    max_len, i = 0, 0
    dict_temp = {}
    for j, val in enumerate(s):
        # 每次新输入一个元素x
        # 如果x存在子串中，则将起始索引移到字串中x位置的下一个位置
        if val in dict_temp and i <= dict_temp[val]:
            i = dict_temp[val]+1
        # x不存在在子串中，此时max_len才有可能增加
        else:
            max_len = max(j - i + 1, max_len)
        # 不管什么结果，都要更新x的位置信息
        dict_temp[val] = j
    return max_len


if __name__ == "__main__":
    s_1 = "abcadebc"
    print(lengthOfLongestSubstring_4(s_1))
