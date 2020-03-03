from DataStructure.LinearList import ListNode, LinkList
class Solution:

    # 遍历链表，找到变换后的头节点，组合新链表
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node_temp = head
        length = 0
        # 把链表首尾相接应该也可以，我用的是余数
        while node_temp:
            length += 1
            node_temp = node_temp.next
        if length == 0:
            return head
        k_new = k % length
        if k_new == 0:
            return head
        node_1 = head
        node_2 = head
        for i in range(k_new):
            node_2 = node_2.next
        while node_2.next:
            node_1 = node_1.next
            node_2 = node_2.next
        new_head = node_1.next
        node_1.next = node_2.next
        node_2.next = head
        return new_head

def main():
    list = LinkList([0, 1, 2, 3, 4])
    print(Solution().rotateRight(list.head.next, 2))
if __name__ == "__main__":
    main()