class Solution:

    # 遍历上一次的数列，记录下每种数字和出现次数，组成新的字符串，重复n-1次
    def countAndSay(self, n: int) -> str:
        result = "1"
        i = 1
        while i < n:
            # 下一个字符串
            result_temp = ""
            # 出现的数字
            num_temp = result[0]
            # 出现的次数
            num_amount = 0
            for num in result:
                if num == num_temp:
                    num_amount += 1
                else:
                    # 出现新数字时，记录老数字的结果
                    result_temp += str(num_amount) + str(num_temp)
                    num_temp = num
                    num_amount = 1
            result_temp += str(num_amount) + str(num_temp)
            result = result_temp
            i += 1
        return result


if __name__ == "__main__":
    print(Solution().countAndSay(6))