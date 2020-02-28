class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0:
            if s[i] != " ":
                break
            i -= 1
        end = i
        while i >= 0:
            if s[i] == " ":
                break
            i -= 1
        return end - i
