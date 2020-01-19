from DataStructure.LinearList import ListNode, LinkList


class Solution:

    # 依次取出链表中的第一个，比较大小
    # 遍历两个链表，时间复杂度O(n + m)
    # 空间复杂度O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_head = ListNode()
        node_temp = node_head
        while l1 and l2:
            if l1.val < l2.val:
                node_temp.next = l1
                l1 = l1.next
            else:
                node_temp.next = l2
                l2 = l2.next
            node_temp = node_temp.next
        node_temp.next = l1 if l1 else l2
        return node_head.next


if __name__ == "__main__":
    l1 = LinkList([1, 2, 4])
    l2 = LinkList([1, 3, 4])
    node = Solution().mergeTwoLists(l1[1], l2[1])
    while node:
        print(node.val)
        node = node.next