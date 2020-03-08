# LeetCode 第28题

"""
文本Text: 是一个长度为n的字符串
模式Pattern: 是一个长度为m的字符串,  并且m<=n.
Text和Pattern的元素都属于有限的字母表
"""


# 朴素算法（Naive Algorithm）即暴力匹配法
def naive_algorithm(text, pattern):
    """
    时间复杂度：O(n * m)
    空间复杂度O(1)
    :param text: 是一个长度为n的字符串
    :param pattern: 是一个长度为m的字符串
    :return: pattern在text第一次出现的索引位置
    """
    index_result = -1
    for index_text in range(len(text) - len(pattern) + 1):
        index_text_now = index_text
        for index_pattern in range(len(pattern)):
            if text[index_text_now] != pattern[index_pattern]:
                break
            index_text_now += 1
        else:
            index_result = index_text
            break
    return index_result


# KMP算法
def KMP(text, pattern):
    """
    平均时间复杂度：O(n)
    空间复杂度O(m)
    :param text: 是一个长度为n的字符串
    :param pattern: 是一个长度为m的字符串
    :return: pattern在text第一次出现的索引位置
    """
    # 辅助数组, 获得最长相同前缀后缀子字符串
    def get_same_substring(s):
        result = [0] * len(s)
        result[0] = -1
        index_1 = -1
        index_2 = 0
        while index_2 < len(s) - 1:
            if index_1 == -1 or s[index_1] == s[index_2]:
                index_1 += 1
                index_2 += 1
                if s[index_1] != s[index_2]:
                    result[index_2] = index_1
                else:
                    result[index_2] = result[index_1]
            else:
                index_1 = result[index_1]
        return result

    if len(pattern) == 0:
        return 0
    index_result = -1
    index_text = 0
    index_pattern = 0
    index_pattern_next = get_same_substring(pattern)
    while index_text < len(text):
        if index_pattern == -1 or text[index_text] == pattern[index_pattern]:
            index_text += 1
            index_pattern += 1
        else:
            index_pattern = index_pattern_next[index_pattern]
        if index_pattern == len(pattern):
            index_result = index_text - index_pattern
            break
    return index_result


# BM算法
def BM(text, pattern):
    """
    平均时间复杂度：O(n)
    空间复杂度O(m)
    :param text: 是一个长度为n的字符串
    :param pattern: 是一个长度为m的字符串
    :return: pattern在text第一次出现的索引位置
    """


    def get_prefix(s):
        postfix = [0] * (len(s) + 1)
        index_1 = -1
        index_2 = 0
        postfix[0] = -1
        while index_2 < len(s):
            if index_1 == -1 or s[index_1] == s[index_2]:
                index_1 += 1
                index_2 += 1
                postfix[index_2] = index_1
            else:
                index_1 = postfix[index_1]
        index_1 = postfix[len(s)]
        postfix_index = []
        while index_1 > 0:
            postfix_index.append(len(s) - index_1)
            index_1 = postfix[index_1]
        return postfix_index

    # 好后缀
    prefix_index_all = get_prefix(pattern)

    # 坏字符
    pattern_char_index = dict()
    for index_char in range(len(pattern)-1, -1, -1):
        pattern_char = pattern[index_char]
        if pattern_char in pattern_char_index.keys():
            pattern_char_index[pattern_char].append(index_char)
        else:
            pattern_char_index[pattern_char] = [index_char]

    index_text_end = len(pattern) - 1
    index_result = -1
    while index_text_end < len(text):
        index_text = index_text_end
        for index_pattern in range(len(pattern)-1, -1, -1):
            if text[index_text] != pattern[index_pattern]:
                # BM算法的特点就在于此，选择上述两种启发法规则（坏字符和好后缀）计算结果中最大的一个值来对模式P的比较位置进行滑动。
                # 我感觉上面这句话不太对
                # 我认为应该是坏字符失效时，才会采用好后缀的规则
                # 坏字符
                char_text = text[index_text]
                index_text_step = index_pattern + 1
                if char_text in pattern_char_index.keys():
                    for index_char_text_pattern in pattern_char_index[char_text]:
                        if index_char_text_pattern < index_pattern:
                            index_text_step = index_pattern - index_char_text_pattern
                            break
                # 好后缀
                if index_text_step == index_pattern + 1:
                    index_text_step = len(pattern);
                    for index_prefix in prefix_index_all:
                        if index_prefix > index_pattern:
                            index_text_step = index_prefix
                            break
                # index_text_step_1 = index_pattern + 1
                # for index_prefix in prefix_index_all:
                #     if index_prefix > index_pattern:
                #         index_text_step_1 = index_prefix - index_pattern + index_prefix
                #         break
                index_text_end += index_text_step
                break
            index_text -= 1
        else:
            index_result = index_text_end - len(pattern) + 1
            break
    return index_result

# Sunday 算法
def Sunday(text, pattern):
    """
    平均时间复杂度：O(n)
    空间复杂度O(m)
    :param text: 是一个长度为n的字符串
    :param pattern: 是一个长度为m的字符串
    :return: pattern在text第一次出现的索引位置
    """
    index_pattern_char = dict()
    for index_1, pattern_char in enumerate(pattern):
        index_pattern_char[pattern_char] = len(pattern) - index_1
    index_text_start = 0
    index_result = -1
    while index_text_start <= len(text) - len(pattern):
        index_text = index_text_start
        for index_pattern in range(len(pattern)):
            if text[index_text] != pattern[index_pattern]:
                index_rear = index_text_start + len(pattern)
                if index_rear < len(text) and text[index_rear] in index_pattern_char.keys():
                    index_text_start += index_pattern_char[text[index_rear]]
                else:
                    index_text_start = index_rear
                break
            index_text += 1
        else:
            index_result = index_text_start
            break
    return index_result


def main():
    text = "ababbbbaaabbbaaa"
    pattern = "bbbb"
    # print(naive_algorithm(text, pattern))
    print(BM(text, pattern))
if __name__ == "__main__":
    main()