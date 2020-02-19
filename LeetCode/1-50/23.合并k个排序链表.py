from DataStructure.LinearList import ListNode, LinkList


class Solution:

    # 1.首先对所有链表的第一个元素排序，组成一个列表
    # 2.取出最小元素，再将该元素的下一个元素放入列表的合适位置
    # 3.重复第二步一直到所有元素取出
    # n：所有结点个数，m: 链表数。如果第二步排序用的是逐个比较的方法，时间复杂度为O(nm);如果为二分法则为O(nlogm)
    # 空间复杂度O(m),在原输入列表操作则是O(1)
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        # 删除空结点,并排序
        lists_new = []
        for node_ in lists:
            if node_:
                lists_new.append(node_)
        lists = lists_new
        lists.sort(key=lambda lnode: -lnode.val)
        node_first = ListNode(None)
        node_temp = node_first
        while True:
            try:
                # 取出列表中最小结点
                node_add = lists.pop()
            except IndexError:
                break
            node_temp.next = node_add
            node_temp = node_add
            # 取出结点的下一个结点
            node_new = node_add.next
            # 将该节点放入lists中
            if node_new:
                # 排序
                lists.append(node_new)
                for index_node in range(len(lists)-1, 0, -1):
                    if lists[index_node].val > lists[index_node-1].val:
                        lists[index_node], lists[index_node-1] = \
                            lists[index_node-1], lists[index_node]
                    else:
                        break
                # 排序可以用下面的方法代替
                # lists.append(node_new)
                # lists.sort(key=lambda lnode: -lnode.val)
        return node_first.next


if __name__ == "__main__":
    lists = [LinkList([1, 4, 5])[1], LinkList([3, 3, 4])[1], LinkList([2, 6])[1]]
    lists = [LinkList([])[1], LinkList([])[1]]
    node_ = Solution().mergeKLists(lists)
    while node_:
        print(node_.val)
        node_ = node_.next
    pass