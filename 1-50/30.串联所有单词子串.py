class Solution:

    # 思路类似3.无重复字符最长子串
    # 滑动窗口的想法
    # word长度为m， s长度为n，时间复杂度为O(nm)
    # words程度为l，空间复杂度为O(l)
    def findSubstring(self, s: str, words: [str]) -> [int]:
        result = []
        if not words:
            return result
        # 字符串起始位置
        for index_start in range(len(words[0])):
            result = self.findSubstringStartIndex(result, s, words, index_start)
        return result

    def findSubstringStartIndex(self, result, s, words, index_start):
        start_sub_string = index_start
        index_dict = {}
        # 因为words中word不唯一，所以用列表（起到队列的作用）保存索引
        for word in words:
            index_dict.setdefault(word, []).append(-1)
        word_length = len(words[0])
        words_length = word_length * len(words)
        # 索引位置每次加word_length，下面的算法的想法和3.无重复字符最长子串几乎一模一样，不同之处在于用列表保存每次出现word的索引
        for index_1 in range(index_start, len(s), word_length):
            word_temp = s[index_1: index_1 + word_length]
            if word_temp in index_dict.keys():
                if index_dict[word_temp][0] >= start_sub_string:
                    start_sub_string = index_dict[word_temp][0] + word_length
                index_dict[word_temp].pop(0)
                index_dict[word_temp].append(index_1)
            else:
                start_sub_string = index_1 + word_length
            # 判断子串是否完整
            if index_1 - start_sub_string == words_length - word_length:
                result.append(start_sub_string)
        return result
    

if __name__ == "__main__":
    print(Solution().findSubstring("aaaaaaaa", ["aa", "aa", "aa"]))
