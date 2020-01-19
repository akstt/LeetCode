from DataStructure.LinearList import ListNode, LinkList


class Solution:

    # 和上题思路类似
    # 循环版本，可以写递归
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node_head = ListNode(None)
        node_head.next = head
        node_temp = node_head
        while True:
            # 需要翻转的链表部分，存储在列表中
            node_list = []
            node_temp_1 = node_temp.next
            for i in range(k):
                if node_temp_1:
                    node_list.append(node_temp_1)
                else:
                    break
                node_temp_1 = node_temp_1.next
            else:
                # 翻转链表
                while node_list:
                    node_ = node_list.pop()
                    node_temp.next = node_
                    node_temp = node_
                node_temp.next = node_temp_1
                # node_temp = node_temp_1
                continue
            break
        return node_head.next


if __name__ == "__main__":
    node_ = Solution().reverseKGroup(LinkList([1, 2, 3, 4, 5, 6, 7, 8])[1], 3)
    while node_:
        print(node_.val)
        node_ = node_.next
