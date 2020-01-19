from DataStructure.LinearList import ListNode, LinkList
class Solution:

    # node_1 为当前结点， node_2为node_1的第后n个结点。
    # 如果node_2为最后一个结点，删除node_1后一个结点
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 设立头节点，方便删除第一个结点
        node_1 = node_2 = ListNode(None)
        node_1.next = head
        head = node_1
        for i in range(n):
            node_2 = node_2.next
        while node_2.next:
            node_1 = node_1.next
            node_2 = node_2.next
        node_1.next = node_1.next.next
        return head.next


if __name__ == "__main__":
    linklist_1 = LinkList([1, 2, 3, 4, 5])
    Solution().removeNthFromEnd(linklist_1.head.next, 2)
    print(linklist_1)
