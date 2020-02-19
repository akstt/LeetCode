class Solution:

    # 滑动窗口,i指向窗口起始位置，j指向窗口结束位置
    # 利用集合保存子串中各元素，空间复杂度为O(n)
    # 循环遍历字符串，时间复杂度为O(n),集合查询，添加，删除的平均时间复杂度为O(1),总体时间复杂度为O(n)
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        i, len_max = 0, 0
        # 保存滑动窗口中的元素
        set_temp = set()
        for j, val in enumerate(s):
            # 字符在子串中，删除i处元素，子串起始位置向右移动一位
            while val in set_temp:
                set_temp.remove(s[i])
                i += 1
            set_temp.add(val)
            len_max = max(len_max, j-i+1)
        return len_max

    # 利用字典保存子串中各元素的索引，空间复杂度为O(n)
    # 循环遍历字符串，时间复杂度为O(n),字典查询，添加，修改的平均时间复杂度为O(1),总体时间复杂度为O(n)
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        len_max, i = 0, 0
        # 保存元素在遍历过的字符串中最后出现过的位置
        dict_temp = {}
        for j, val in enumerate(s):
            # 每次新输入一个元素x,查询字典保存的x索引位置，i每次移动到该索引位置+1的位置
            if val in dict_temp and i <= dict_temp[val]:
                i = dict_temp[val] + 1
            else:
                len_max = max(j - i + 1, len_max)
            dict_temp[val] = j
        return len_max


# 测试
if __name__ == "__main__":
    s_1 = "abcadebc"
    print(Solution().lengthOfLongestSubstring_1(s_1))
