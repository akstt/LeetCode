"""
@Author: AKSTT
@Problem:
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
from DataStructure.LinearList import *


# 我感觉这道题没什么可说的，主要是了解一下链表结构，可以参考DataStructure.LinearList中定义的线性表类
# 两个方法的时间复杂度为O(max(m,n)),空间复杂的为O(max(m,n))(用于存储计算结果)
# 第一个方法为递归
# 可以看出这是个尾递归。python没有尾递归的，所以尾递归都应该写成循环，可以避免递归消耗
from functools import lru_cache
@lru_cache(maxsize=None)
def add_num(result, l1, l2, num_temp):
    if l1 or l2:
        try:
            num_temp += l1.val
            l1 = l1.next
        except AttributeError:
            pass
        try:
            num_temp += l2.val
            l2 = l2.next
        except AttributeError:
            pass
        result.next = ListNode(num_temp % 10)
        num_temp = num_temp // 10
        result = result.next
        return add_num(result, l1, l2, num_temp)
    else:
        if num_temp:
            result.next = ListNode(num_temp)


def addTwoNumbers_1(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    num_temp = 0
    add_num(result, l1, l2, num_temp)
    return result.next


# 第二个方法为循环
def addTwoNumbers_2(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    node_temp = result
    num_temp = 0
    while l1 or l2:
        try:
            num_temp += l1.val
            l1 = l1.next
        except AttributeError:
            pass
        try:
            num_temp += l2.val
            l2 = l2.next
        except AttributeError:
            pass
        node_temp.next = ListNode(num_temp % 10)
        num_temp = num_temp // 10
        node_temp = node_temp.next
    if num_temp:
        node_temp.next = ListNode(num_temp)
    return result.next


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
    node_result = addTwoNumbers_1(linklist_1[1], linklist_2[1])
    print(node_2_int(node_result))
