class Solution:

    # 字符串逐步查找，时间复杂度O(n)
    # 保存结果，空间复杂度O(n)
    def myAtoi_1(self, s: str) -> int:
        # index_start, index_end目标子字符串的起始位置和结束位置
        # flag 寻找起始位置
        index_start, index_end, flag_1, flag_2 = 0, len(s), False, False
        # 找到字符串中数字起始位置
        for index_1, val in enumerate(s):
            # 结束位置
            if flag_1 and val.isdigit():
                flag_2 = True
                index_end = index_1
            # 起始位置
            elif not flag_1:
                if val == "-" or val == "+":
                    flag_1 = True
                    index_start = index_1
                elif val.isdigit():
                    flag_1, flag_2 = True, True
                    index_start, index_end = index_1, index_1
                elif val != " ":
                    break
            else:
                break
        if flag_1 and flag_2:
            result = int(s[index_start: index_end + 1])
        else:
            result = 0
        if result < -2147483648:
            result = -2147483648
        elif result > 2147483647:
            result = 2147483647
        return result

    # 使用python的内置方法
    def myAtoi_2(self, s: str) -> int:
        # 去除左边空格
        s_new = s.lstrip()
        index_end = 0
        for index_1, val in enumerate(s_new[1:], 1):
            if not val.isdigit():
                break
            index_end = index_1
        try:
            result = int(s_new[:index_end + 1])
            return max(-2147483648, min(result, 2147483647))
        except ValueError:
            return 0

    # 正则表达式
    def myAtoi_3(self, s: str) -> int:
        import re
        s_new = s.lstrip()
        result = re.search(r'^[\+-]?\d+', s_new)
        if result:
            return max(min(int(result.group(0)), 2 ** 31 - 1), -2 ** 31)
        else:
            return 0


if __name__ == "__main__":
    s = "4193 with words"
    print(Solution().myAtoi_3(s))