"""
优先队列（Priority Queue）: 特殊“队列”，取出元素的顺序是依照元素的优先权（关键字）大小，而不是元素进入队列的先后顺序。
优先队列的完全二叉树表示：
堆的两个特性：
1.结构性：用数组表示完全二叉树
2.有序性：任一结点的关键字是其子树所有结点的最大值（最大堆，大顶堆，MaxHeap）或最小值（最小堆，小顶堆，MinHeap）
操作集：
1.创建一个空的最大堆
2.判断最大堆是否已满
3.插入元素
4.判断最大堆是否为空
5.返回最大元素
"""


class MaxHeap:

    def __init__(self, size, val_input=None):
        """
        :param size: 堆的最大容量
        :param val_input: 堆得初始值，默认为None
        """
        self._size = size
        self._maxHeap = [None] * size
        self._rear = 0
        if val_input is not None:
            for val in val_input:
                self._maxHeap[self._rear] = val
                self._rear += 1
            self._build_heap()

    def _build_heap(self):
        """
        将一个数据乱的列表转为最大堆
        """
        for index_val in range((self._rear-1)//2, -1, -1):
            self._build_heap_node_exchange(index_val)

    def _build_heap_node_exchange(self, index_node):
        """
        交换结点值，使该节点满足最大堆要求,递归解决
        :param index_node 需要转换结点的index
        """
        index_left = index_node * 2 + 1
        index_right = index_node * 2 + 2
        if index_left >= self._rear:
            pass
        elif index_right >= self._rear:
            if self._maxHeap[index_node] < self._maxHeap[index_left]:
                self._maxHeap[index_node], self._maxHeap[index_left] = \
                    self._maxHeap[index_left], self._maxHeap[index_node]
        else:
            if self._maxHeap[index_left] > self._maxHeap[index_node] \
                    or self._maxHeap[index_right] > self._maxHeap[index_node]:
                if self._maxHeap[index_left] > self._maxHeap[index_right]:
                    self._maxHeap[index_node], self._maxHeap[index_left] = \
                        self._maxHeap[index_left], self._maxHeap[index_node]
                    self._build_heap_node_exchange(index_left)
                else:
                    self._maxHeap[index_node], self._maxHeap[index_right] = \
                        self._maxHeap[index_right], self._maxHeap[index_node]
                    self._build_heap_node_exchange(index_right)

    def insert(self, val_insert):
        """
        插入数据
        :param val_insert: 插入值
        """
        if self.if_full():
            print("堆满")
        else:
            self._maxHeap[self._rear] = val_insert
            self._insert_node_exchange(self._rear)
            self._rear += 1

    def _insert_node_exchange(self, index_node):
        """
        插入数据后调整堆
        :param index_node:
        """
        index_parent = (index_node-1)//2
        if index_parent >= 0 and self._maxHeap[index_parent] < self._maxHeap[index_node]:
            self._maxHeap[index_parent], self._maxHeap[index_node] = \
                self._maxHeap[index_node], self._maxHeap[index_parent]
            self._insert_node_exchange(index_parent)

    def delete(self):
        """
        删除最大值
        :return:删除后的值
        """
        if self.if_empty():
            print("堆空")
            return None
        else:
            result = self._maxHeap[0]
            self._maxHeap[0] = self._maxHeap[self._rear-1]
            self._rear -= 1
            # 删除操作就是把最后一个元素放到首位，再通过结点交换让整个列表满足最大堆的要求
            self._build_heap_node_exchange(0)
            return result

    def if_full(self):
        """
        :return: 堆是否已满
        """
        return self._rear == self._size

    def if_empty(self):
        """
        :return: 堆是否为空
        """
        return self._rear == 0

    def __repr__(self):
        index_val = 0
        index_not_leaf_last = (self._rear-1)//2
        result = ""
        while index_val < self._rear:
            for index_val_1 in range(index_val, min(index_val * 2 + 1, index_not_leaf_last + 1)):
                result += str(self._maxHeap[index_val_1])
                if 2 * index_val_1 + 1 < self._rear:
                    result += "->" + str(self._maxHeap[2 * index_val_1 + 1]) + ","
                    if 2 * index_val_1 + 2 < self._rear:
                        result += str(self._maxHeap[2 * index_val_1 + 2])
                    result += ";"
            result += "\n"
            index_val = index_val * 2 + 1
        return result


def main():
    list1 = list(range(40))
    max_heap1 = MaxHeap(50, list1)
    print(max_heap1)
    for i in range(35, 55):
        max_heap1.insert(i)
    print(max_heap1)
    for i in range(55):
        print(max_heap1.delete())


if __name__ == "__main__":
    main()
