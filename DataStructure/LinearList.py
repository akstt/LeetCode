"""
@Author: AKSTT
@Name: List/线性表
@定义: 由同类型数据元素构成有序序列的线性结构
       1.表中元素个数称为线性表的长度
       2.线性表没有元素时，称为空表
       3.表起始位置称为表头，表结束位置称为表尾
@数据对象集：线性表时n(>=0)个元素构成的有序序列
@操作集：1.初始化一个空线性表L
        2.根据位序i返回相应元素
        3.在线性表中查找某个元素x第一次出现位置
        4.在位序i前插入一个新元素X
        5.删除指定位序i的元素
        6.返回线性表L的长度

"""

"""
首先是线性表的顺序存储
"""


# 可以用python中的list代替。有些细节部分不太一样：线性表的顺序存储要求同类型数据元素，同时要求输入最大长度maxsize
class List(list):

    # 添加一个返回线性表长的的方法
    def len(self):
        return len(self)

    pass


# 自定义一个LinearList类，自定义List的方法和属性，有助于了解线性表顺序存储是如何进行存储，插入和删除等操作
class LinearList:

    # 用tuple(list)的格式代表LinearList
    def __init__(self, maxsize=0, iterator_input=()):
        self._maxsize = maxsize
        self._linear_list = tuple([None] for _ in range(maxsize))
        self._last = len(iterator_input)
        for i, x in enumerate(iterator_input):
            try:
                self._linear_list[i][0] = x
            except IndexError:
                break

    @property
    def maxsize(self):
        return self._maxsize

    @property
    def last(self):
        return self._last - 1

    # 根据位序i返回相应元素
    def __getitem__(self, key):
        return self._linear_list[key][0]

    # 对应索引位置元素修改
    def __setitem__(self, key, value):
        self._linear_list[key][0] = value
        return None

    # 查找 时间复杂度O(n)
    def find(self, x):
        for i in range(self._last):
            if x == self._linear_list[i][0]:
                return i
        return None

    # 插入 默认插在末尾 时间复杂度O(n)
    def insert(self, insert_value, insert_index=None):
        if insert_index is None:
            insert_index = self._last
        # 判断表满
        if self._last == self._maxsize:
            print("表满")
        # 判断位置是否合法
        elif insert_index > self._last or insert_index < 0:
            print("索引位置出错")
        # 插入元素
        else:
            for i in range(self._last, insert_index, -1):
                self._linear_list[i][0] = self._linear_list[i-1][0]
            self._linear_list[insert_index][0] = insert_value
            self._last += 1
        return None

    # 删除 默认删除最后一个 时间复杂度O(n)
    def delete(self, delete_index=None):
        if delete_index is None:
            delete_index = self._last-1
        # 判断删除位置是否合法
        if delete_index < 0 or delete_index > self._last-1:
            print("索引位置出错")
        # 删除元素
        else:
            for i in range(delete_index, self._last-1):
                self._linear_list[i][0] = self._linear_list[i+1][0]
            self._linear_list[self._last-1][0] = None
            self._last -= 1

    # 返回线性表L的长度
    def len(self):
        return self._last

    def __repr__(self):
        return str(self._linear_list)


# 测试LinearList
def LinearList_test():
    # 生成线性表a
    a = LinearList(5, [0, 1, 2])
    print(a[1])
    a[1] = 2
    print(a)
    print(a.find(0))
    print(a.len())
    a.insert(3)
    print(a)
    print(a.find(3))
    a.insert(4, 5)
    a.insert(4, 0)
    print(a.len())
    print(a)
    a.delete(0)
    print(a)
    a.delete()
    print(a)
    a.delete(5)
    a.delete(3)
    print(a)


"""
接下来是线性表的链式存储,通过链建立元素之间的逻辑关系,不需要事先确定maxsize
"""


# 链式存储的结点类
class ListNode:
    def __init__(self, node_value=None, node_next=None):
        self._value = node_value
        self._next = node_next

    @property
    def val(self):
        return self._value

    @val.setter
    def val(self, change_value):
        self._value = change_value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, change_next):
        self._next = change_next


# 带头结点的链表类，
class LinkList:
    def __init__(self, iterator_input=(), head_node=None):
        # 设定头结点
        self._head = ListNode(head_node)
        old_node = self._head
        for val in iterator_input:
            new_node = ListNode(val)
            old_node.next = new_node
            old_node = new_node
        # self._rear = old_node

    # 头指针
    @property
    def head(self):
        return self._head

    # 尾指针，指向最后一个元素
    # @property
    # def rear(self):
    #     return self._rear

    # 根据位序i返回相应元素,头节点索引为0，时间复杂度为O(n)
    def __getitem__(self, key):
        node_temp = self._head
        if key < 0:
            return None
        while node_temp and key:
            key -= 1
            node_temp = node_temp.next
        return node_temp

    # 在线性表中查找某个元素x第一次出现位置，时间复杂度为O(n)
    def find(self, x):
        node_temp = self._head
        while node_temp and node_temp.val != x:
            node_temp = node_temp.next
        return node_temp

    # 在位序i前插入一个新元素,默认插在第一个位置,查找时间复杂度O(n),插入O(1)
    def insert(self, insert_value, insert_index=1):
        node_temp = self[insert_index-1]
        if node_temp:
            new_node = ListNode(insert_value)
            new_node.next = node_temp.next
            node_temp.next = new_node
        else:
            print("索引位置出错")

    # 删除指定位序i的元素, 默认删除第一个，查找时间复杂度O(n),删除O(1)
    def delete(self, delete_index):
        node_temp = self[delete_index-1]
        if node_temp and node_temp.next:
            node_temp.next = node_temp.next.next
        else:
            print("索引位置出错")

    # 返回线性表L的长度,时间复杂度O(n)
    def len(self):
        node_temp = self._head.next
        length = 0
        while node_temp:
            length += 1
            node_temp = node_temp.next
        return length

    def __repr__(self):
        result = []
        node_temp = self.head.next
        while node_temp:
            result.append(node_temp.val)
            node_temp = node_temp.next
        return str(result)
    pass


if __name__ == "__main__":
    # LinearList_test()
    linklist = LinkList([1, 2, 3, 4, 5])
    linklist.delete(6)
    print(linklist)
    pass

