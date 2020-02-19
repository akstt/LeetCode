class Solution:

    # 遍历字符串，时间复杂度O(n)
    # 存储尚未对应的括号，空间复杂度O(n)
    def isValid(self, s: str) -> bool:
        sign_map = {')': '(', ']': '[', '}':"{"}
        # result，堆栈，后入先出。存储尚未匹配的括号
        result = []
        for sign in s:
            # sign为右括号时
            try:
                sign_1 = sign_map[sign]
                sign_2 = result.pop()
            # sign为左括号时
            except KeyError:
                result.append(sign)
            except IndexError:
                return False
            else:
                if sign_1 != sign_2:
                    return False
        return not result


if __name__ == "__main__":
    s = "()[]"
    print(Solution().isValid(s))