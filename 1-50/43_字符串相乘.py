class Solution:

    # 模仿手工乘法
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        for index_1 in range(0, len(num1)):
            for index_2 in range(0, len(num2)):
                result_temp = int(num1[index_1]) * int(num2[index_2])
                index_temp = index_1 + index_2 + 1
                while result_temp > 0:
                    result_temp += result[index_temp]
                    result[index_temp] = result_temp % 10
                    result_temp = result_temp // 10
                    index_temp -= 1
        index_temp = 0
        while index_temp < len(result):
            if result[index_temp] != 0:
                break
            index_temp += 1
        else:
            return "0"
        result_str = ""
        for index_1 in range(index_temp, len(result)):
            result_str += str(result[index_1])
        return result_str
        pass


if __name__ == "__main__":
    num1 = "9"
    num2 = "99"
    print(Solution().multiply(num1, num2))
    print(int(num1) * int (num2))
