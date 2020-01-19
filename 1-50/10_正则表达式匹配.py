class Solution:

    # 使用re模块直接匹配
    def isMatch_1(self, s: str, p: str) -> bool:
        import re
        return bool(re.match(r"^"+p+"$", s))

    # 回溯法
    def isMatch_2(self, s: str, p: str):
        s_index, p_index = 0, 0
        return self.match_sign(s, p, s_index, p_index)

    # 递归主体
    def match_sign(self, s, p, s_index, p_index):
        if s_index == len(s) and p_index == len(p):
            return True
        if p_index + 1 < len(p) and p[p_index + 1] == "*":
            if self.match_sign(s, p, s_index, p_index + 2):
                return True
            while s_index < len(s) and s[s_index] == p[p_index]:
                s_index += 1
                if self.match_sign(s, p, s_index, p_index + 2):
                    return True
            if p[p_index] == ".":
                while s_index < len(s):
                    s_index += 1
                    if self.match_sign(s, p, s_index, p_index + 2):
                        return True
        elif s_index == len(s) or p_index == len(p):
            return False
        elif p[p_index] == "." or s[s_index] == p[p_index]:
            s_index += 1
            p_index += 1
            return self.match_sign(s, p, s_index, p_index)
        return False

    # 动态规划
    def isMatch_3(self, s: str, p: str):
        # match_result[i][j]代表s[i:]和p[j:]匹配的结果
        match_result = [[False for _ in range(len(p) + 1)]for _ in range(len(s) + 1)]
        match_result[-1][-1] = True
        for s_index in range(len(s), -1, -1):
            for p_index in range(len(p)-1, -1, -1):
                if_match = s_index < len(s) and (p[p_index] == '.' or p[p_index] == s[s_index])
                if p_index + 1 < len(p) and p[p_index+1] == "*":
                    match_result[s_index][p_index] = match_result[s_index][p_index+2] or (if_match and match_result[s_index+1][p_index])
                else:
                    match_result[s_index][p_index] = if_match and match_result[s_index + 1][p_index+1]
        return match_result[0][0]
    #
    # def match_sign_3(self, s, p, s_index, p_index, match_result):
    #     if p_index <0:
    #         return
    #     if s_index < 0:
    #         s_index
    #     if p[p_index] == "*":
    #         match_result[s_index][p_index-1] = True
    #         self.match_sign_3(s, p, s_index, p_index-2, match_result)
    #         if s[s_index] == p[p_index-1] or p[p_index-1] == ".":
    #             match_result[s_index-1][p_index] = True
    #             self.match_sign_3(s, p, s_index-1, p_index, match_result)
    #     elif s[s_index] == p[p_index] or p[p_index] == ".":
    #         match_result[s_index][p_index] = True
    #         self.match_sign_3(s, p, s_index-1, p_index-1, match_result)




if __name__ == "__main__":
    s = "ab"
    p = ".*.."
    print(Solution().isMatch_3(s, p))
