from DataStructure.LinearList import *


class Solution:

    # DataStructure.LinearList 有自定义的链表类
    # 循环每次取出链表中一个数字进行相加，时间复杂度为O(max(m,n))
    # 用于存储计算结果,空间复杂的为O(max(m,n))
    # 递归解决方法易于理解，写起来也比较方便
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 结果的头节点
        result = ListNode(0)
        # 保存每次相加后进位的数字，因为只有两个数字，所以只可能是0或1
        num_temp = 0
        # 逐个数字相加
        self.add_num(result, l1, l2, num_temp)
        return result.next

    # 递归相加每对数字
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def add_num(self, result, l1, l2, num_temp):
        # 如果l1或l2还未迭代完，则相加
        if l1 or l2:
            if l1:
                num_temp += l1.val
                l1 = l1.next
            if l2:
                num_temp += l2.val
                l2 = l2.next
            result.next = ListNode(num_temp % 10)
            num_temp = num_temp // 10
            result = result.next
            return self.add_num(result, l1, l2, num_temp)
        else:
            if num_temp == 1:
                result.next = ListNode(num_temp)

    # 可以看出上面的递归为尾递归，不过python没有尾递归优化，所以写成循环会好一些
    # 第二个方法为循环
    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        node_temp = result
        num_temp = 0
        while l1 or l2:
            if l1:
                num_temp += l1.val
                l1 = l1.next
            if l2:
                num_temp += l2.val
                l2 = l2.next
            node_temp.next = ListNode(num_temp % 10)
            num_temp = num_temp // 10
            node_temp = node_temp.next
        if num_temp:
            node_temp.next = ListNode(num_temp)
        return result.next


# 测试
def int_2_list(num):
    result = []
    while num:
        num, y = num // 10, num % 10
        result.append(y)
    # result = list(str(num))
    # result.reverse()
    # result = [int(n) for n in result]
    return result


def node_2_int(lnode):
    result = []
    while lnode:
        result.append(str(lnode.val))
        lnode = lnode.next
    result.reverse()
    return int(''.join(result))


if __name__ == "__main__":
    num_1, num_2 = 644, 4652
    linklist_1 = LinkList(int_2_list(num_1))
    linklist_2 = LinkList(int_2_list(num_2))
    node_result = Solution().addTwoNumbers_1(linklist_1[1], linklist_2[1])
    print(node_2_int(node_result))
