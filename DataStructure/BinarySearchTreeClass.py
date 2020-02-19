"""
名称：二叉搜索树
满足如下性质：
    1.非空左子树的所有键值小于其根节点键值
    2.非空右子树的所有键值大于其根节点键值
    3.左右子树都是二叉搜索树
函数：
    1.find
    2.find_min
    3.find_max
    4.insert
    5.delete
"""


class BinarySearchTree:

    def __init__(self, data=None, left=None, right=None):
        """
        :param data: 根节点数据
        :param left: 左子树 BinarySearchTree
        :param right: 右子树 BinarySearchTree
        """
        self._data = data
        self._left = left
        self._right = right

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, val):
        self._left = val

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, val):
        self._right = val

    def find(self, val):
        """
        :param val: 寻找的值
        :return: 根节点值为val的结点
        """
        if self.data is None:
            return None
        if self.data == val:
            return self
        elif val > self.data and self.right:
            return self.right.find(val)
        elif val < self.data and self.left:
            return self.left.find(val)
        return None

    def find_min(self):
        """
        :return: 树的最小结点
        """
        return self.left if (self.left and self.left.val is not None) else self

    def find_max(self):
        """
        :return: 树的最大结点
        """
        return self.right if (self.right and self.right.val is not None) else self

    def insert(self, val):
        """
        # 插入一个数
        """
        if self.data is None:
            self.data = val
        elif val > self.data:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinarySearchTree(val)
        elif val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinarySearchTree(val)

    def delete(self, val):
        """
        当删除叶子结点时遇到一些麻烦，因为无法找回该节点的父节点，所以不太好删除，现在设定当前结点值为None时，表示该节点为None
        :param val: 删除的数值
        :return: 删除数值的结点
        """
        if self.data is None:
            return None
        if val < self.data and self.left:
            return self.left.delete(val)
        elif val > self.data and self.right:
            return self.right.delete(val)
        elif val == self.data:
            if self.left and self.right:
                node_temp = self.left.find_min()
                node_temp.data, self.data = self.data, node_temp.data
                node_temp.delete(val)
            else:
                if self.left:
                    node_temp = self.left
                    self.data, node_temp.data = node_temp.data, self.data
                    self.right = self.left.right
                    self.left = self.left.left
                    return node_temp
                elif self.right:
                    node_temp = self.right
                    self.data, node_temp.data = node_temp.data, self.data
                    self.left = self.right.left
                    self.right = self.right.right
                    return node_temp
                else:
                    self.data = None
                    self.left = None
                    self.right = None
                    return self
        else:
            return None
