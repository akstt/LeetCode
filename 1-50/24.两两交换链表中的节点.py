from DataStructure.LinearList import ListNode, LinkList


class Solution:

    # 取出一个结点a，如果a 和 a.next 为节点则交换，a为a.next 重复这一步，一直到遍历链表
    # 循环版本，可以写递归
    def swapPairs(self, head: ListNode) -> ListNode:
        node_head = ListNode(None)
        node_head.next = head
        node_temp_1 = node_head
        node_temp_2 = node_temp_1.next
        while node_temp_2 and node_temp_2.next:
            # 调换
            node_temp_1.next = node_temp_2.next
            node_temp_2.next = node_temp_1.next.next
            node_temp_1.next.next = node_temp_2
            # 更换后后面两个结点
            node_temp_1 = node_temp_2
            node_temp_2 = node_temp_1.next
        return node_head.next


if __name__ == "__main__":
    node_ = Solution().swapPairs(LinkList([1, 2, 3, 4, 5])[1])
    while node_:
        print(node_.val)
        node_ = node_.next
    pass
