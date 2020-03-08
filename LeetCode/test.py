def fun(s):
    postfix = [0] * (len(s) + 1)
    index_1 = -1
    index_2 = 0
    postfix[0] = -1
    while index_2 < len(s):
        if index_1 == -1 or s[index_1] == s[index_2]:
            index_1 += 1
            index_2 += 1
            postfix[index_2] = index_1
        else:
            index_1 = postfix[index_1]
    index_1 = postfix[len(s)]
    postfix_index = []
    while index_1 > 0:
        postfix_index.append(len(s) - index_1)
        index_1 = postfix[index_1]

    return postfix, postfix_index


import sys
while True:
    num = sys.stdin.readline()
    if num == "\n":
        break
    set_1 = set()
    for i in range(int(num)):
        set_1.add(int(sys.stdin.readline()))
    list_1 = list(set_1)
    list_1.sort()
    for i in list_1:
        print(i)