class Solution:

    # 动态规划,与10.正则表达式匹配差不多
    def isMatch_1(self, s: str, p: str) -> bool:
        match_result = [[False for _ in range(len(p)+1)] for _ in range(len(s) + 1)]
        match_result[-1][-1] = True
        for index_s in range(len(s), -1, -1):
            for index_p in range(len(p)-1, -1, -1):
                if_match = index_s < len(s) and (p[index_p] == "?" or p[index_p] == "*" or p[index_p] == s[index_s])
                if p[index_p] == "*":
                    match_result[index_s][index_p] = match_result[index_s][index_p + 1] or \
                                                     (if_match and match_result[index_s + 1][index_p])
                else:
                    match_result[index_s][index_p] = if_match and match_result[index_s + 1][index_p + 1]
        return match_result[0][0]
        pass

    # 贪心算法
    def isMatch_2(self, s: str, p: str) -> bool:
        index_s, index_p = 0, 0
        index_s_back, index_p_back = -1, -1
        while index_s < len(s):
            if index_p < len(p) and (s[index_s] == p[index_p] or p[index_p] == "?"):
                index_s += 1
                index_p += 1
            elif index_p < len(p) and p[index_p] == "*":
                index_s_back = index_s + 1
                index_p_back = index_p
                index_p += 1
            elif index_s_back != -1:
                index_s, index_p = index_s_back, index_p_back
            else:
                return False
        if index_s == len(s):
            for index_1 in range(index_p, len(p)):
                if p[index_1] != "*":
                    return False
            return True
        return False

if __name__ == "__main__":
    s = "aa"
    p = "*"
    print(Solution().isMatch_2(s, p))