# 基本策略： 将中缀表达式转为后缀表达式
# 例子：2+9/3-5 -> 2 9 3 / + 5 -
# 转换思路：1.运算数相对顺序不变
#          2.运算符号存储起来，当前运算符号与等待运算的符号比较优先级


# 中缀表达式转后缀表达式
# 表达式只能有+-*/()
def transform_expression(exp_middle: [str])->[str]:
    exp_back = []
    # 运算符优先级
    sign_order = {'+': 0, '-': 0,
                  '*': 1, '/': 1,
                  '(': -1}
    signs = ['(']
    for str_1 in exp_middle:
        if str_1.isdigit():
            exp_back.append(str_1)
        # 符号为括号时
        elif str_1 == '(':
            signs.append(str_1)
        elif str_1 == ')':
            while True:
                sign = signs.pop()
                if sign == '(':
                    break
                exp_back.append(sign)
        # 符号为+-*/()
        else:
            while sign_order[str_1] < sign_order[signs[-1]]:
                sign = signs.pop()
                exp_back.append(sign)
            signs.append(str_1)
    while len(signs) > 1:
        exp_back.append(signs.pop())
    return exp_back


if __name__ == "__main__":
    # 2+9/3-5
    # (2+9)/(3-5)
    exp_1 = ['2', '+', '9', '/', '3', '-', '5']
    exp_2 = ['(', '2', '+', '9', ')', '/', '(', '3', '-', '5', ')']
    print(transform_expression(exp_2))
