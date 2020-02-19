class Solution:

    # 两个字符串逐个比较
    # len(haystack)=n, len(needle)=m,时间复杂度O(nm)
    def strStr_1(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for index_1 in range(len(haystack) - len(needle) + 1):
            for index_2, val_2 in enumerate(needle):
                if haystack[index_1 + index_2] != val_2:
                    break
            else:
                return index_1
        return -1

    # KMP算法，挺麻烦的，几句话解释不清楚
    # 基本想法，haystack上的指针不后退，当needle指针不匹配时，立刻移到一个前面字符都匹配好的下一个字符，一直到匹配结束
    def strStr_2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        str_length = self.get_long_str(needle)
        index_1, index_2 = 0, 0
        for index_1, val_1 in enumerate(haystack):
            while True:
                val_2 = needle[index_2]
                if index_2 == -1 or val_1 == val_2:
                    index_2 += 1
                    break
                else:
                    index_2 = str_length[index_2]
            if index_2 == len(needle):
                return index_1 - index_2 + 1
        return -1

    # 辅助列表,最长前缀后缀长度
    def get_long_str(self, str_input):
        result = [-1]
        index_1 = -1
        index_2 = 0
        while index_2 < len(str_input) - 1:
            if index_1 == -1 or str_input[index_1] == str_input[index_2]:
                index_1 += 1
                index_2 += 1
                if str_input[index_1] == str_input[index_2]:
                    result.append(result[index_1])
                else:
                    result.append(index_1)
            else:
                index_1 = result[index_1]
        return result


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr_2(haystack, needle))
