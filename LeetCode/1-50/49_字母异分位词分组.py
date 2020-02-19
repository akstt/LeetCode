class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        result = []
        # key为组成字符串的字母，并经过排序的元组
        # value是结果列表
        result_dict = {}
        for str_1 in strs:
            str_list = list(str_1)
            str_list.sort()
            str_set = tuple(str_list)
            try:
                # 有相同字母组成时
                result_dict[str_set].append(str_1)
            except KeyError:
                # 没有相同字母组成时
                new_list = [str_1]
                result_dict[str_set] = new_list
                result.append(new_list)
        return result


if __name__ == "__main__":
    x = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(x))
