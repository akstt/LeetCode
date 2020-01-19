class Solution:

    # 递归解决问题
    def generateParenthesis_1(self, n: int) -> [str]:
        result = ['(']
        # l_num: 左括号剩余添加数量
        # r_num：右括号可以添加数量
        # flag：是否下一个一定是左括号，目的是用来去重
        l_num, flag = n-1, False
        result = self.add_sign(result, l_num, n, flag)
        return result

    # 每一次添加括号都为合法添加
    def add_sign(self, result, l_num, n, flag):
        # 添加一个左括号
        if flag and l_num:
            result = [result_ + '(' for result_ in result]
            l_num -= 1
            flag = False
        # 剩余可以添加的右括号数量为2*(n-l_num)-len(result_)个
        # 依次添加0-2*(n-l_num)-len(result_)个右括号
        elif l_num:
            result = [result_ + num_sign*')' for result_ in result for num_sign in range(2*(n-l_num)-len(result_)+1)]
            flag = True
        # 左括号都添加完毕，把所有右括号都添上
        else:
            result = [result_ + (2*n-len(result_)) * ')' for result_ in result]
            return result
        return self.add_sign(result, l_num, n, flag)

    # 递归改循环
    def generateParenthesis_2(self, n: int) -> [str]:
        result = ['(']
        # l_num: 左括号剩余添加数量
        # r_num：右括号可以添加数量
        # flag：是否下一个一定是左括号，目的是用来去重
        l_num, flag = n - 1, False
        while l_num:
            # 添加一个左括号
            if flag:
                result = [result_ + '(' for result_ in result]
                l_num -= 1
                flag = False
            # 剩余可以添加的右括号数量为2*(n-l_num)-len(result_)个
            # 依次添加0-2*(n-l_num)-len(result_)个右括号
            else:
                result = [result_ + num_sign * ')' for result_ in result for num_sign in
                          range(2 * (n - l_num) - len(result_) + 1)]
                flag = True
        # 左括号都添加完毕，把所有右括号都添上
        result = [result_ + (2 * n - len(result_)) * ')' for result_ in result]
        return result


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis_2(n))
