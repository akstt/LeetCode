"""
名称: 堆栈
定义: 具有一定操作约束的线性表，只在一端（栈顶，top）做插入，删除
后入先出（LIFO）
数据对象集：有0个或多个元素的有穷线性表
操作集：1.生成空堆栈，其最大长度为MaxSize
        2.判断堆栈S是否已满
        3.入栈
        4.判断是否为空
        5.删除并返回栈顶元素
"""
from DataStructure.ErrorClass import StorageSmallError


# SequenceStack堆栈的顺序存储
class SequenceStack:

    def __init__(self, maxsize, input_list=()):
        self._maxsize = maxsize
        if len(input_list) > maxsize:
            raise StorageSmallError
        self._maxsize = maxsize
        self._top = len(input_list)
        self._sequence_stack = list(input_list)
        self._sequence_stack.extend([None] * (maxsize - len(input_list)))

    @property
    def maxsize(self):
        return self._maxsize

    @property
    def top(self):
        return self._top - 1

    def __repr__(self):

        return str(self._sequence_stack[:self._top])

    # 入栈
    def push(self, input_value):
        try:
            self._sequence_stack[self._top] = input_value
            self._top += 1
        except IndexError:
            print("堆栈满")

    # 删除并返回栈顶元素
    def pop(self):
        if self._top == 0:
            result = None
            print("堆栈空")
        else:
            result = self._sequence_stack[self._top-1]
            self._sequence_stack[self._top-1] = None
            self._top -= 1
        return result

    # 判断堆栈S是否已满
    def is_full(self):
        return self._top == self._maxsize

    # 判断是否为空
    def is_empty(self):
        return not bool(self._top)


# 测试SequenceStack
def SequenceStack_test():
    new_stack = SequenceStack(5, [1, 2, 3])
    print(new_stack)
    print(new_stack.is_empty())
    print(new_stack.is_full())
    new_stack.push(4)
    new_stack.push(4)
    new_stack.push(4)
    print(new_stack)
    print(new_stack.is_empty())
    print(new_stack.is_full())
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    print(new_stack)
    print(new_stack.is_empty())
    print(new_stack.is_full())
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    print(new_stack)
    print(new_stack.is_empty())
    print(new_stack.is_full())


from DataStructure.LinearList import ListNode


# LinkStack堆栈的链式存储
# 带头结点
class LinkStack:

    def __init__(self, input_list=(), head_value=None):
        self._head = ListNode(head_value)
        old_node = self._head
        for value in input_list[::-1]:
            new_node = ListNode(value)
            old_node.next = new_node
            old_node = new_node

    @property
    def head(self):
        return self._head

    def __repr__(self):
        result = []
        node_temp = self._head.next
        while node_temp:
            result.append(node_temp.val)
            node_temp = node_temp.next
        result.reverse()
        return str(result)

    # 入栈
    def push(self, input_value):
        node_temp = ListNode(input_value)
        node_temp.next = self._head.next
        self._head.next = node_temp

    # 删除并返回栈顶元素
    def pop(self):
        try:
            result = self._head.next
            self._head.next = result.next
            result = result.val
        except AttributeError:
            result = None
            print("堆栈空")
        return result

    # 判断是否为空
    def is_empty(self):
        return not bool(self._head.next)


def LinkStack_test():
    new_stack = LinkStack([1,2,3])
    print(new_stack)
    print(new_stack.is_empty())
    new_stack.push(4)
    new_stack.push(4)
    print(new_stack)
    print(new_stack.is_empty())
    print(new_stack.pop())
    new_stack.pop()
    print(new_stack)
    print(new_stack.is_empty())
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    print(new_stack)
    print(new_stack.is_empty())
    new_stack.push(4)
    new_stack.push(4)
    print(new_stack)
    print(new_stack.is_empty())


if __name__ == "__main__":
    # SequenceStack_test()
    LinkStack_test()
