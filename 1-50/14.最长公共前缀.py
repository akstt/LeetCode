class Solution:

    # 依次找出每对字符串的最长公共前缀
    # 时间复杂度O(mn)(m为字符串长度， n为len(s))
    # 空间复杂度为O(m)
    def longestCommonPrefix_1(self, s: [str]) -> str:
        if len(s) == 0:
            return ''
        result = list(s[0])
        for str_1 in s:
            for index_1, val in enumerate(result):
                if index_1 == len(str_1) or str_1[index_1] != val:
                    result = result[: index_1]
                    break
        return ''.join(result)

    # 按照索引，依次检查每个字符串对应索引位置是否相同
    # 时间复杂度O(mn)(m为字符串长度， n为len(s))
    # 空间复杂度为O(m)
    def longestCommonPrefix_2(self, s: [str]) -> str:
        if len(s) == 0:
            return ''
        # 最大索引位置
        index_max = len(s[0])
        for index_1, val in enumerate(s[0]):
            for str_1 in s:
                if index_1 == len(str_1) or str_1[index_1] != val:
                    break
            else:
                continue
            index_max = index_1
            break
        return s[0][:index_max]

    # longestCommonPrefix_2的另一种写法
    def longestCommonPrefix_3(self, s: [str]) -> str:
        result = []
        for vals in zip(*s):
            if len(set(vals)) == 1:
                result.append(vals[0])
            else:
                break
        return ''.join(result)

    # 利用python内置函数解决：
    # 时间复杂度O(m*nlogn)(m为字符串长度， n为len(s))
    # 空间复杂度为O(m)
    def longestCommonPrefix_4(self, s: [str]) -> str:
        if len(s) == 0:
            return ''
        # 字符串排序
        s = sorted(s)
        result = []
        # 只比较第一个和最后一个
        for val_1, val_2 in zip(s[0], s[-1]):
            if val_1 == val_2:
                result.append(val_1)
            else:
                break
        return ''.join(result)

if __name__ == "__main__":
    s = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix_3(s))