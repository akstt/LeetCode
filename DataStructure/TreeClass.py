"""
名称: 树
定义: n(n>=0)个结点构成的有限集合
     空树:n=0;
     树的度为2，子树有左右之分：二叉树
性质：树中有一个称为“根（Root）”的特殊节点，用r表示
     其余节点可分为m(m>0)个互不相交的有限集T1,...,Tm,
  其中每个集合本身又是一棵树，称为原来树的“子树（SubTree）”
基本术语：节点的度（Degree）
         树的度（max(Degrees)）
         叶节点（Leaf）（Degree=0）
         父节点(Parent)
         子节点（Child）
         兄弟结点（Sibling）
         路径和路径长度
         祖先节点（Ancestor）
         子孙节点（Descendant）
         结点的层次（Level）(root.Level = 1)
         树的深度（Depth）（max(Levels)）
"""

"""
查找：根据某个给定关键词K,从集合R中找出关键字与K相同的记录
静态查找：集合中记录是固定的；没有插入和删除操作，只有查找
动态查找：集合中记录是动态变化的；可能发生插入和删除操作
"""


# 顺序查找，找不到返回-1
# 时间复杂度O(n)
def sequential_search(tb, x):
    for index_1, x_temp in enumerate(tb):
        if x_temp == x:
            return index_1
    return -1


# 二分查找，找不到返回-1
# 要求数组有序
# 时间复杂度O(logn)
def binary_search(tb, x):
    index_start, index_end = 0, len(tb) - 1
    while index_start < index_end:
        index_middle = (index_start + index_end) // 2
        if x < tb[index_middle]:
            index_end = index_middle - 1
        elif x > tb[index_middle]:
            index_start = index_middle + 1
        else:
            return index_middle
    return -1


"""
二叉树T:一个有穷的结点集合（可以为空），由根节点和左子树TL和右子树TR两个互不相交的二叉树构成
特殊二叉树：斜二叉树；完美二叉树（满二叉树）；完全二叉树
重要性质：1.第i层最大结点数为2^(i-1)
         2. 深度为k的最大节点数2^k-1
         3.n0为叶节点个数，n2为度为2的非叶节点个数，n0 = n2 +1
基本操作:1.判断是否为空；
         2.遍历（先序：根左右；中序：左根右；后序：左右根；层次遍历：上到下，左到右）
         3.创建
"""


# 二叉树链式存储,方法大部分使用递归实现
class LinkListBinaryTree:

    def __init__(self, data=None, left=None, right=None, parent=None, tree_list=None, index_tree=0):
        """
        :param data: 该节点数据
        :param left: 左子树，LinkListBinaryTree
        :param right: 右子树，LinkListBinaryTree
        :param parent: 父节点，LinkListBinaryTree
        :param tree_list: 一个表示树的列表,形如[[data, left_index, right_index]...]
        ，如无左/右结点，则用-1表示；根节点放在首位；如果输入此参数，则只需输入此参数
        :param index_tree: tree_list中该结点所在索引
        """
        if tree_list:
            # self._get_tree(tree_list, index_tree)
            try:
                self._get_tree(tree_list, index_tree, parent)
            except:
                print("输入树有误")
        else:
            self._parent = parent
            self._data = data
            self._left = left
            self._right = right

    @property
    def parent(self):
        return self._parent

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def height(self):
        """
        求树的高度；递归实现
        :return: 树的高度，int
        """
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return max(left_height, right_height) + 1

    def _get_tree(self, tree_list, index_tree, parent=None):
        """
        将tree_list转成二叉树链式存储;递归解决
        :param tree_list: tree_list: 一个表示树的列表，[[data, int, int]]
        :param index_tree: tree_list中根节点的位置
        :param parent: 父节点位置
        """
        node = tree_list[index_tree]
        self._data = node[0]
        self._parent = parent
        self._left = LinkListBinaryTree(parent=self, tree_list=tree_list, index_tree=node[1]) if node[1] != -1 else None
        self._right = LinkListBinaryTree(parent=self, tree_list=tree_list, index_tree=node[2]) if node[2] != -1 else None

    def sequence2link(self, sequence_list, index_tree=0):
        """
        顺序存储的二叉树转为链式存储,递归实现
        :param sequence_list:一个顺序存储的二叉树类， SequenceListBinaryTree
        :param index_tree: 当前结点在顺序存储的索引位置，int，[0, len(sequence_list))
        :return: 一个链式存储二叉树类， LinkListBinaryTree
        """

        self._data = sequence_list[index_tree]

        left_index = sequence_list.get_left_index(index_tree)
        if left_index == -1 or sequence_list[left_index] is None:
            self._left = None
        else:
            left_tree = LinkListBinaryTree(parent=self)
            left_tree.sequence2link(sequence_list, left_index)
            self._left = left_tree

        right_index = sequence_list.get_right_index(index_tree)
        if right_index == -1 or sequence_list[right_index] is None:
            self._right = None
        else:
            right_tree = LinkListBinaryTree(parent=self)
            right_tree.sequence2link(sequence_list, right_index)
            self._right = right_tree

    def pre_order_traversal(self, tree=None):
        """
        先序遍历：根左右；递归实现
        :param tree: 遍历结果的列表，list
        :return: 遍历结果的列表，list
        """
        if tree is None:
            tree = []
        tree.append(self.data)
        if self.left:
            self.left.pre_order_traversal(tree)
        if self.right:
            self.right.pre_order_traversal(tree)
        return tree

    def in_order_traversal(self, tree=None):
        """
        中序遍历：左根右；递归实现
        :param tree: 遍历结果的列表，list
        :return: 遍历结果的列表，list
        """
        if tree is None:
            tree = []
        if self.left:
            self.left.in_order_traversal(tree)
        tree.append(self.data)
        if self.right:
            self.right.in_order_traversal(tree)
        return tree

    def post_order_traversal(self, tree=None):
        """
        后序遍历：左右根；递归实现
        :param tree: 遍历结果的列表，list
        :return: 遍历结果的列表，list
        """
        if tree is None:
            tree = []
        if self.left:
            self.left.post_order_traversal(tree)
        if self.right:
            self.right.post_order_traversal(tree)
        tree.append(self.data)
        return tree

    def level_order_traversal(self, tree=None):
        """
        层次遍历：从左到右，从上到下；循环实现
        :param tree: 遍历结果的列表，list
        :return: 遍历结果的列表，list
        """
        if tree is None:
            tree = []
        nodes_list = [self]
        LinkListBinaryTree._level_order_traversal(tree, nodes_list)
        return tree

    @staticmethod
    def _level_order_traversal(tree, nodes_list):
        nodes = nodes_list
        nodes_list = []
        for node in nodes:
            tree.append(node.data)
            if node.left:
                nodes_list.append(node.left)
            if node.right:
                nodes_list.append(node.right)
        if nodes_list:
            LinkListBinaryTree._level_order_traversal(tree, nodes_list)


# 二叉树顺序存储,方法多用循环实现
from collections import deque


class SequenceListBinaryTree:

    def __init__(self, complete_binary_tree=None, index_tree=0, tree_list=None, index_tree_1=0):
        """
        :param complete_binary_tree: 一个完全二叉树的列表，没节点部分用None表示；list
        :param index_tree：完全二叉树结点索引，int, [0, len(complete_binary_tree))
        :param tree_list: 一个表示树的列表,形如[[data, left_index, right_index]...]
        ，如无左/右结点，则用-1表示；根节点放在首位；如果输入此参数，则只需输入此参数
        :param index_tree_1: tree_list中该结点所在索引
        """
        if tree_list:
            try:
                self._get_tree(tree_list)
            except:
                print("输入树有误")
        else:
            self._tree = complete_binary_tree
            self._index_tree = index_tree

    @property
    def data(self):
        try:
            return self._tree[self._index_tree]
        except:
            return None

    @property
    def parent(self, index_tree=-1):
        """
        获得父节点
        :param index_tree: 当前树的索引， int
        :return: 父节点，SequenceListBinaryTree
        """
        index_parent = self.get_parent_index(index_tree)
        if index_parent != -1 and self._tree[index_parent] is not None:
            return SequenceListBinaryTree(self._tree, index_parent)
        else:
            return None

    @property
    def left(self, index_tree=-1):
        """
        获得左子树
        :param index_tree: 当前树的索引， int
        :return: 左子树 SequenceListBinaryTree
        """
        index_left = self.get_left_index(index_tree)
        if index_left != -1 and self._tree[index_left] is not None:
            return SequenceListBinaryTree(self._tree, index_left)
        else:
            return None

    @property
    def right(self, index_tree=-1):
        """
        获得右子树
        :param index_tree: 当前树的索引， int
        :return: 右子树 SequenceListBinaryTree
        """
        index_right = self.get_right_index(index_tree)
        if index_right != -1 and self._tree[index_right] is not None:
            return SequenceListBinaryTree(self._tree, index_right)
        else:
            return None

    @property
    def height(self):
        """
        求树的高度；堆栈实现
        :return: 树的高度，int
        """
        node_stack = [self]
        node = self
        height = 0
        while node_stack:
            if node.left:
                node = node.left
                node_stack.append(node)
            elif node.right:
                node = node.right
                node_stack.append(node)
            else:
                height = max(len(node_stack), height)
                node_stack.pop()
                while node_stack:
                    node_temp = node_stack.pop()
                    if node_temp.right == node or node_temp.right is None:
                        node = node_temp
                    else:
                        node_stack.append(node_temp)
                        node = node_temp.right
                        node_stack.append(node)
                        break
        return height

    def _get_tree(self, tree_list):
        """
        将tree_list转成二叉树顺序存储;利用队列解决
        :param tree_list: tree_list: 一个表示树的列表，[[data, int, int]]
        """
        node_queue = deque([[0, tree_list[0]]])
        self._index_tree = 0
        self._tree = []
        while node_queue:
            node = node_queue.popleft()
            try:
                self._tree[node[0]] = node[1][0]
            except IndexError:
                self._tree.extend([None] * (node[0]-len(self._tree) + 1))
                self._tree[node[0]] = node[1][0]
            if node[1][1] != -1:
                node_queue.append([2 * node[0] + 1, tree_list[node[1][1]]])
            if node[1][2] != -1:
                node_queue.append([2 * node[0] + 2, tree_list[node[1][2]]])

    def get_parent_index(self, index_tree=-1):
        """
        获得父节点索引
        :param index_tree: 当前树的索引， int
        :return: 父节点索引, int
        """
        if index_tree == -1:
            index_tree = self._index_tree
        index_parent = (index_tree-1) // 2
        return index_parent if (0 <= index_parent < len(self._tree)) else -1

    def get_left_index(self, index_tree=-1):
        """
        获得左子树索引
        :param index_tree: 当前树的索引， int
        :return: 左子树索引, int
        """
        if index_tree == -1:
            index_tree = self._index_tree
        index_left = 2 * index_tree + 1
        return index_left if 0 <= index_left < len(self._tree) else -1

    def get_right_index(self, index_tree=-1):
        """
        获得右子树索引
        :param index_tree: 当前树的索引， int
        :return: 右子树索引, int
        """
        if index_tree == -1:
            index_tree = self._index_tree
        index_right = 2 * index_tree + 2
        return index_right if 0 <= index_right < len(self._tree) else -1

    def link2sequence(self, link_list):
        """
        链式存储的二叉树转为顺序存储,队列实现
        :param link_list:一个链式存储的二叉树类， LinkListBinaryTree
        :return: 一个顺序存储二叉树类， SequenceListBinaryTree
        """
        if self._index_tree is None:
            self._index_tree = 0
        self._tree = []
        node_queue = deque([[0, link_list]])
        while node_queue:
            node = node_queue.popleft()
            try:
                self._tree[node[0]] = node[1].data
            except IndexError:
                self._tree.extend([None] * (node[0] - len(self._tree) + 1))
                self._tree[node[0]] = node[1].data
            if node[1].left is not None:
                node_queue.append([2 * node[0] + 1, node[1].left])
            if node[1].right is not None:
                node_queue.append([2 * node[0] + 2, node[1].right])

        # if self._index_tree is None:
        #     self._index_tree = 0
        # self._tree = []
        # try:
        #     self._tree[self._index_tree] = link_list.data
        # except IndexError:
        #     self._tree.extend([None] * (self._index_tree + 1 - len(self._tree)))
        #     self._tree[self._index_tree] = link_list.data
        #
        # if link_list.left is not None:
        #     left_tree = SequenceListBinaryTree(self._tree, 2 * self._index_tree + 1)
        #     left_tree.link2sequence(link_list.left)
        # if link_list.right is not None:
        #     right_tree = SequenceListBinaryTree(self._tree, 2 * self._index_tree + 2)
        #     right_tree.link2sequence(link_list.right)

    def pre_order_traversal(self):
        """
        先序遍历：根左右；堆栈实现
        :return: 遍历结果的列表，list
        """
        tree = []
        node = self
        node_stack = []
        while node_stack or node:
            if node:
                tree.append(node.data)
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                node = node.right
        return tree

    def in_order_traversal(self):
        """
        中序遍历：左根右；堆栈实现
        :return: 遍历结果的列表，list
        """
        tree = []
        node = self
        node_stack = []
        while node_stack or node:
            if node:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                tree.append(node.data)
                node = node.right
        return tree

    def post_order_traversal(self):
        """
        后序遍历：左右根；堆栈实现
        :return: 遍历结果的列表，list
        """
        tree = []
        node = self
        node_stack = []
        while node_stack or node:
            while node:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            if node.right:
                node_stack.append(node)
                node = node.right
            else:
                tree.append(node.data)
                while node_stack:
                    node_temp = node_stack.pop()
                    if node_temp.right == node or node_temp.right is None:
                        node = node_temp
                        tree.append(node.data)
                    else:
                        node_stack.append(node_temp)
                        node = node_temp.right
                        break
                else:
                    break
        return tree

    def level_order_traversal(self):
        """
        层次遍历：从左到右，从上到下；队列实现
        :return: 遍历结果的列表，list
        """
        tree = []
        nodes_list = deque([self])
        while nodes_list:
            node = nodes_list.popleft()
            tree.append(node.data)
            if node.left:
                nodes_list.append(node.left)
            if node.right:
                nodes_list.append(node.right)
        return tree

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        try:
            return self._tree == other._tree and self._index_tree == other._index_tree
        except:
            return False

    def __getitem__(self, item):
        return self._tree[item] if 0 <= item < len(self._tree) else None


if __name__ == "__main__":
    sequence_tree = SequenceListBinaryTree([1, 2, 3, None, 5, 6, 7, None, None, 10, None, 12, 13, 14])
    link_tree = LinkListBinaryTree()
    link_tree.sequence2link(sequence_tree)
    print(link_tree.pre_order_traversal())
    print(link_tree.in_order_traversal())
    print(link_tree.post_order_traversal())
    print(link_tree.level_order_traversal())
    print(link_tree.height)
    sequence_tree = SequenceListBinaryTree()
    sequence_tree.link2sequence(link_tree)
    print(sequence_tree.pre_order_traversal())
    print(sequence_tree.in_order_traversal())
    print(sequence_tree.post_order_traversal())
    print(sequence_tree.level_order_traversal())
    print(sequence_tree.height)
    tree_list = [[1, 1, 2], [3, 3, 4], [2, 5, -1], [6, 6, 7], [7, -1, 8],
                 [5, 9, -1], [13, -1, -1], [12, -1, -1], [14, -1, -1], [10, -1, -1]]
    link_tree_1 = LinkListBinaryTree(tree_list=tree_list)
    sequence_tree_1 = SequenceListBinaryTree(tree_list=tree_list)
    # print(link_tree_1.pre_order_traversal())
    # print(link_tree_1.in_order_traversal())
    # print(link_tree_1.post_order_traversal())
    # print(link_tree_1.level_order_traversal())
    # print(link_tree_1.height)
    # sequence_tree_1 = SequenceListBinaryTree()
    # sequence_tree_1.link2sequence(link_tree)
    # sequence_tree_1 = SequenceListBinaryTree(tree_list=tree_list)

    a = 1
    pass
