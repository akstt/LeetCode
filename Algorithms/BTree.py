"""
一颗B树T是具有一下性质的有根树：
1. 每个结点x有下面的属性：
    1. x.n，当前存储在结点x中关键字的个数。
    2. 结点中的关键字以非降序排列
    3. x.leaf,一个布尔值，判断x是否为叶子结点
2. 每个内部结点x还包含x.n + 1 个指向其孩子的指针x.c(1),...,x.c(x.n+1)，叶节点没有孩子
3. 关键字x.key(i)对存储在各子树中的关键字范围加以分割。
4. 每个叶子结点具有相同的深度，及树的高度h。
5. 每个结点所包含的关键字个数有上界和下界。用一个被称为B树的最小度数的固定整数t>=2来表示这些界。
    1. 除了根节点以外的每个结点至少有t-1个关键字。如果树非空，根节点至少有一个关键字
    2. 每个结点至多可以有2t-1个关键字。当一个结点恰好有2t-1个关键字时，则称该节点是满的。

B树的高度 h >= logt((n+1)/2)

"""


# 该树不会出现相同关键字,也不会出现任何对磁盘的操作，每个树结点都相当于以各磁盘页
# 部分细节处理较为随意
class BTree:

    def __init__(self, min_degree):
        """
        :param min_degree: B树的最小度数 >=1,即每个节点至少有min_degree个关键字
        """
        if min_degree >= 1:
            self._min_degree = min_degree
            self._tree = BTreeNode(min_degree, True)
        else:
            print("参数设置错误")

    @property
    def min_degree(self):
        return self._min_degree

    def search(self, key):
        return self._tree.search(key)

    def insert(self, key):
        """
        插入
        :param key: 插入的key
        :return 新的根节点
        """
        self._tree = self._tree.insert(key)

    def delete(self, key):
        self._tree = self._tree.delete(key)

    def level_order_traversal(self):
        """
        层次遍历
        本来打算看看有没有哪不对，感觉有点难看出来
        :return:
        """
        trees_all = [[self._tree]]
        while trees_all:
            trees_all_temp = []
            for trees in trees_all:
                for tree in trees:
                    if tree.children:
                        trees_all_temp.append(tree.children)
                    print(tree, end="")
                print(end="***")
            print()
            trees_all = trees_all_temp

    def check(self):
        return self.height_check() and self._tree.check_tree_root()

    def height_check(self):
        """
        检查树是否一样高
        :return:
        """
        trees = [self._tree]
        while trees:
            trees_temp = []
            for tree in trees:
                if tree.leaf:
                    break
                else:
                    trees_temp.extend(tree.children)
            else:
                trees = trees_temp
                continue
            for tree in trees:
                if not tree.leaf:
                    return False
            return True


class BTreeNode:

    def __init__(self, min_degree, leaf, keys=None, children=None):
        """
        :param min_degree: 最小度数
        :param leaf: 是否为叶子结点
        :param keys:
        :param children:
        """
        self.t = min_degree
        # 每个节点最大关键字个数
        self.max_count = min_degree * 2 + 1
        self.leaf = leaf
        if keys:
            self.keys = keys
            self.n = len(keys)
        else:
            self.keys = []
            self.n = 0
        if self.leaf:
            self.children = None
        elif children:
            self.children = children
        else:
            self.children = []

    def binary_search(self, key):
        """
        二分查找
        :param key: 查找的值
        """
        index_start = 0
        index_end = self.n - 1
        while index_start <= index_end:
            index_middle = (index_start + index_end) // 2
            if self.keys[index_middle] > key:
                index_end = index_middle - 1
            elif self.keys[index_middle] < key:
                index_start = index_middle + 1
            else:
                return index_middle
        return index_start

    def search(self, key):
        """
        查找
        :param key: 需要查找的元素
        :return: 需要查找的元素，如果没有则返回None
        """
        # 二分查找
        index_1 = self.binary_search(key)

        # 线性查找
        # index_1 = 0
        # while index_1 < self._n and self._keys[index_1] < key:
        #     index_1 += 1

        if index_1 < self.n and self.keys[index_1] == key:
            return self.keys[index_1]
        elif self.leaf:
            return None
        else:
            return self.children[index_1].search(key)

    def split_node(self, i):
        """
        :param i:分割结点
        :return: 将该节点第i个子节点（满结点）分为两个结点，
        """
        child = self.children[i]

        self.keys.insert(i, child.keys[self.t])
        self.n += 1
        keys_right = child.keys[self.t+1:]
        child.keys = child.keys[: self.t]
        if not child.leaf:
            child_right = child.children[self.t + 1:]
            child.children = child.children[: self.t+1]
        else:
            child_right = None
        child.n = self.t
        right = BTreeNode(self.t, child.leaf, keys_right, child_right)
        self.children.insert(i+1, right)

    def insert_not_full(self, key):
        """
        递归的调用这段代码，将值找到合适的位置插入
        :param key:需要插入的值
        :return:
        """
        index_1 = self.binary_search(key)
        if index_1 < self.n and self.keys[index_1] == key:
            print(str(key) + "已经插入, 不能重复插入")
        elif self.leaf:
            self.keys.insert(index_1, key)
            self.n += 1
        else:
            if self.children[index_1].n == self.children[index_1].max_count:
                self.split_node(index_1)
                if self.keys[index_1] < key:
                    index_1 += 1
            self.children[index_1].insert_not_full(key)

    def insert(self, key):
        """
        :param key: 需要插入的键
        :return: 根节点
        """
        if self.n == self.max_count:
            new_root = BTreeNode(self.t, False, children=[self])
            new_root.split_node(0)
            new_root.insert(key)
            return new_root
        else:
            self.insert_not_full(key)
            return self

    def merge_node(self, i):
        """
        :param i:需要移动的结点的索引
        """

        child_1 = self.children[i]
        child_2 = self.children[i + 1]

        child_1.keys.append(self.keys[i])
        child_1.keys.extend(child_2.keys)
        self.keys.pop(i)

        child_1.n += (child_2.n + 1)
        self.n -= 1
        if not child_1.leaf:
            child_1.children.extend(child_2.children)

        self.children.pop(i + 1)

    # 寻找最大值
    def find_max_key(self):
        if self.leaf:
            return self.keys[-1]
        else:
            return self.children[-1].find_max_key()

    # 寻找最小值
    def find_min_key(self):
        if self.leaf:
            return self.keys[0]
        else:
            return self.children[0].find_min_key()

    def move_key(self, i):
        """
        :param i: 移动对应子树的元素，使 self.children[i].n > self.children[i].t
        """
        child_1 = self.children[i]
        if child_1.n == child_1.t:
            if i - 1 >= 0 and self.children[i-1].n > self.children[i-1].t:
                child_2 = self.children[i-1]

                child_1.keys.insert(0, self.keys[i - 1])
                self.keys[i - 1] = child_2.keys[-1]
                child_2.keys.pop()

                if not child_1.leaf:
                    child_1.children.insert(0, child_2.children[-1])
                    child_2.children.pop()

                child_1.n += 1
                child_2.n -= 1

            elif i + 1 <= self.n and self.children[i+1].n > self.children[i+1].t:
                child_2 = self.children[i + 1]

                child_1.keys.append(self.keys[i])
                self.keys[i] = child_2.keys[0]
                child_2.keys.pop(0)

                if not child_1.leaf:
                    child_1.children.append(child_2.children[0])
                    child_2.children.pop(0)

                child_1.n += 1
                child_2.n -= 1

            else:
                if i - 1 >= 0:
                    i = i - 1
                self.merge_node(i)
        return i

    def delete_not_leaf(self, i, key):
        """
        删除非叶子结点的值
        :param i:
        """
        child_1 = self.children[i]
        child_2 = self.children[i+1]
        if child_1.n > child_1.t:
            child_1_max_key = child_1.find_max_key()
            self.keys[i] = child_1_max_key
            child_1.delete_not_empty(child_1_max_key)
        elif child_2.n > child_2.t:
            child_2_min_key = child_2.find_min_key()
            self.keys[i] = child_2_min_key
            child_2.delete_not_empty(child_2_min_key)
        else:
            self.merge_node(i)
            self.children[i].delete_not_empty(key)

    def delete_not_empty(self, key):
        """
        递归的主体部分, 虽然是not_empty，但其实是满足self.n>self.t
        :param key: 需要删除的key
        """
        index_1 = self.binary_search(key)
        if self.leaf:
            if index_1 < self. n and self.keys[index_1] == key:
                self.keys.pop(index_1)
                self.n -= 1
            else:
                print("删除出错")
        else:
            if index_1 < self. n and self.keys[index_1] == key:
                self.delete_not_leaf(index_1, key)
            else:
                index_1 = self.move_key(index_1)
                self.children[index_1].delete_not_empty(key)

    def delete(self, key):
        """
        :param key:需要删除的关键字
        :return:
        """
        # 判断key是否存在，不先判断，也是可以的
        if_exit = self.search(key)
        if if_exit is None:
            print(str(key) + "关键字不存在")
        else:
            self.delete_not_empty(key)
            if not self.leaf and self.n == 0:
                return self.children[0]
        return self

    # 检察树构建的对不对
    def check_tree_root(self):
        if self.n == 0 and self.leaf and len(self.keys) == 0 and self.children is None:
            return True
        if self.n < 1:
            return False
        return self.check_all()

    def check_all(self):
        if not self.leaf and len(self.keys) != len(self.children) - 1:
            return False
        if self.n != len(self.keys):
            return False
        for i in range(1, self.n):
            if self.keys[i-1] > self.keys[i]:
                return False
        if self.leaf:
            return True
        for i in range(self.n+1):
            if i == 0:
                min_num = float("-inf")
            else:
                min_num = self.keys[i - 1]
            if i == self.n:
                max_num = float("inf")
            else:
                max_num = self.keys[i]
            if not self.children[i].check_tree(min_num, max_num):
                return False
        return True

    def check_tree(self, min_num, max_num):
        if self.n < self.t or self.n > self.max_count:
            return False
        if self.keys[0] < min_num or self.keys[self.n-1] > max_num:
            return False
        return self.check_all()

    def __repr__(self):
        return self.keys.__repr__()


import random


def main():
    b_tree = BTree(5)
    nums = [i for i in range(1000)]
    nums_2 = [i for i in range(20, 30)]
    nums.extend(nums_2)
    random.shuffle(nums)
    print(nums)
    for i in nums:
        b_tree.insert(i)
        if not b_tree.check():
            print(str(i) + "插入失败")
            break
    b_tree.level_order_traversal()
    random.shuffle(nums)
    for i in nums:
        b_tree.delete(i)
        if not b_tree.check():
            print(str(i) + "删除失败")
            break


if __name__ == '__main__':
    main()
