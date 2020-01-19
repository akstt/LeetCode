"""
名称: 队列
定义: 具有一定操作约束的线性表，只在一端（栈顶，top）做插入，删除
先入先出（FIFO）
数据对象集：有0个或多个元素的有穷线性表
操作集：1.生成空队列，其最大长度为MaxSize
        2.判断队列是否已满
        3.入队
        4.判断是否为空
        5.删除并返回队头元素
"""

from DataStructure.ErrorClass import StorageSmallError


# SequenceQueue堆栈的顺序存储
# 循环队列
class SequenceQueue:

    def __init__(self, maxsize, input_list=()):
        self._maxsize = maxsize
        if len(input_list) > maxsize - 1:
            raise StorageSmallError
        self._maxsize = maxsize
        self._front = 0
        self._rear = len(input_list)
        self._sequence_queue = list(input_list)
        # self._sequence_queue = [None]
        # self._sequence_queue.extend(list(input_list))
        self._sequence_queue.extend([None] * (maxsize - len(input_list)))

    @property
    def maxsize(self):
        return self._maxsize

    def __repr__(self):

        if self._front <= self._rear:
            return str(self._sequence_queue[self._front: self._rear])
        else:
            return str(self._sequence_queue[self._front:] + self._sequence_queue[: self._rear])

    # 入队
    def add(self, input_value):
        if self.is_full():
            print("队列满")
        else:
            self._sequence_queue[self._rear] = input_value
            self._rear = (self._rear + 1) % self._maxsize

    # 删除并返回队首元素
    def delete(self):
        if self.is_empty():
            print("队列为空")
        else:
            val = self._sequence_queue[self._front]
            self._sequence_queue[self._front] = None
            self._front = (self._front + 1) % self._maxsize
            return val

    # 判断队列是否已满
    def is_full(self):
        return self._front == (self._rear + 1) % self._maxsize

    # 判断是否为空
    def is_empty(self):
        return self._front == self._rear


def SequenceQueue_test():
    new_queue = SequenceQueue(5, [1, 2, 3])
    print(new_queue)
    print(new_queue.is_empty())
    print(new_queue.is_full())
    new_queue.add(4)
    new_queue.add(4)
    new_queue.add(4)
    print(new_queue)
    print(new_queue.is_empty())
    print(new_queue.is_full())
    new_queue.delete()
    new_queue.delete()
    new_queue.delete()
    print(new_queue)
    print(new_queue.is_empty())
    print(new_queue.is_full())
    new_queue.delete()
    new_queue.delete()
    new_queue.delete()
    print(new_queue)
    print(new_queue.is_empty())
    print(new_queue.is_full())
    new_queue.add(4)
    new_queue.add(4)
    new_queue.add(4)
    print(new_queue)
    print(new_queue.is_empty())
    print(new_queue.is_full())


from DataStructure.LinearList import ListNode


# LinkQueue堆栈的链式存储
class LinkQueue:

    def __init__(self, input_list=(), head_value=None):
        self._front = ListNode(head_value)
        old_node = self._front
        for value in input_list:
            new_node = ListNode(value)
            old_node.next = new_node
            old_node = new_node
        self._rear = old_node

    def __repr__(self):
        result = []
        node_temp = self._front.next
        while node_temp:
            result.append(node_temp.val)
            node_temp = node_temp.next
        # result.reverse()
        return str(result)

    # 入队
    def add(self, input_value):
        node_temp = ListNode(input_value)
        self._rear.next = node_temp
        self._rear = node_temp

    # 删除并返回队首元素
    def delete(self):
        if self.is_empty():
            print("队列为空")
        else:
            node_temp = self._front.next
            if node_temp == self._rear:
                self._rear = self._front
            self._front.next = node_temp.next
            return node_temp.val

    # 判断是否为空
    def is_empty(self):
        return bool(not self._front.next)


def LinkQueue_test():
    new_queue = LinkQueue([1, 2, 3])
    print(new_queue)
    print(new_queue.is_empty())
    new_queue.add(4)
    new_queue.add(4)
    new_queue.add(4)
    print(new_queue)
    print(new_queue.is_empty())
    new_queue.delete()
    new_queue.delete()
    print(new_queue)
    new_queue.delete()
    print(new_queue)
    print(new_queue.is_empty())
    new_queue.delete()
    new_queue.delete()
    # new_queue.add(4)
    #     # new_queue.add(4)
    new_queue.delete()
    new_queue.delete()
    print(new_queue)
    print(new_queue.is_empty())
    new_queue.add(4)
    new_queue.add(4)
    new_queue.add(4)
    print(new_queue)
    print(new_queue.is_empty())


if __name__ == "__main__":
    # SequenceQueue_test()
    LinkQueue_test()
