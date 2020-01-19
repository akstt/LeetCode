"""
名称: 线性表
定义: 由同类型数据元素构成有序序列的线性结构
       1.表中元素个数称为线性表的长度
       2.线性表没有元素时，称为空表
       3.表起始位置称为表头，表结束位置称为表尾
数据对象集：线性表时n(>=0)个元素构成的有序序列
操作集：1.初始化一个空线性表L
        2.根据位序i返回相应元素
        3.在线性表中查找某个元素x第一次出现位置
        4.在位序i前插入一个新元素X
        5.删除指定位序i的元素
        6.返回线性表L的长度
"""

"""
顺序表是在计算机内存中以数组的形式保存的线性表，是指用一组地址连续的存储单元依次存储数据元素的线性结构。
线性表采用顺序存储的方式存储就称之为顺序表。顺序表是将表中的结点依次存放在计算机内存中一组地址连续的存储单元中。
特点： 1.在顺序表中，各个表项的逻辑顺序与其存储的物理顺序一致，即第 i 个表项存储于第 i 个物理位置（1 < i < n）
       2.对顺序表中的所有表项，即可以进行顺序的访问，也可以随机的访问，也就是说，
既可以从表的第一个表项开始逐个访问表项，也可以按照表项的序号（下标）直接的访问。
       3.无需为表示结点间的逻辑关系而增加额外的存储空间，存储利用率提高。
       4.可以方便的存储表中的任一结点，存储速度快。
"""


from DataStructure.ErrorClass import StorageSmallError


# 下面的线性表类不要求同类型数据元素
# SequenceList线性表的顺序存储
class SequenceList:

    def __init__(self, maxsize=0, input_list=()):
        if len(input_list) > maxsize:
            raise StorageSmallError
        self._maxsize = maxsize
        self._last = len(input_list)
        self._sequence_list = list(input_list)
        self._sequence_list.extend([None] * (maxsize - len(input_list)))

    @property
    def maxsize(self):
        return self._maxsize

    @property
    def last(self):
        return self._last - 1

    # 根据位序i返回相应元素
    def __getitem__(self, key):
        return self._sequence_list[key]

    # 修改位序i元素
    def __setitem__(self, key, value):
        self._sequence_list[key] = value
        return None

    # 在线性表中查找某个元素x第一次出现位置 时间复杂度O(n)
    def find(self, x):
        for i in range(self._last):
            if x == self._sequence_list[i]:
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
                self._sequence_list[i] = self._sequence_list[i-1]
            self._sequence_list[insert_index] = insert_value
            self._last += 1
        return None

    # 删除指定位序i的元素 默认删除最后一个 时间复杂度O(n)
    def delete(self, delete_index=None):
        if delete_index is None:
            delete_index = self._last-1
        # 判断删除位置是否合法
        if delete_index < 0 or delete_index > self._last-1:
            print("索引位置出错")
        # 删除元素
        else:
            for i in range(delete_index, self._last-1):
                self._sequence_list[i] = self._sequence_list[i+1]
            self._sequence_list[self._last-1] = None
            self._last -= 1

    # 返回线性表L的长度
    def len(self):
        return self._last

    def __repr__(self):
        return str(self._sequence_list[:self._last])


# 测试LinearList
def SequenceList_test():
    # 生成线性表a
    a = SequenceList(7, [0, 1, 2])
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
链表是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表中的指针链接次序实现的。
链表由一系列结点（链表中每一个元素称为结点）组成，结点可以在运行时动态生成。
每个结点包括两个部分：一个是存储数据元素的数据域，另一个是存储下一个结点地址的指针域。 
相比于线性表顺序结构，操作复杂。
特点： 1.可以方便的进行扩充。
       2.可以方便的删除和插入
"""


# ListNode节点类
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

    def __repr__(self):
        return str(self._value)


# LinkList线性表的链式存储
# 带头结点，头节点索引为0
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
    def delete(self, delete_index=1):
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


def LinkList_test():
    # 生成线性表a
    a = LinkList([0, 1, 2])
    print(a[1])
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
    pass


if __name__ == "__main__":
    SequenceList_test()
    print('------------')
    LinkList_test()
