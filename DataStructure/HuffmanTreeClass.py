"""
带权路径长度(WPL)：设二叉树有n个叶子结点，每个叶子结点带有权值Wk，从根节点到每个叶子结点的长度为Lk，
                  则每个叶子结点的带权路径长度之和为WPL=sum(Wk * LK)
最优二叉树（哈夫曼树）：WPL最小的二叉树
"""


class TreeNode:
    def __init__(self, data=None, weight=None, left=None, right=None):
        self.data = data
        self.weight = weight
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.data) + "," + str(self.weight) + ")"


class HuffmanTree:

    def __init__(self, val_insert):
        """
        :param val_insert: [[val, weight]...]生成哈夫曼树的元素和权重
        """
        tree_node_all = []
        for data, weight in val_insert:
            tree_node_all.append(TreeNode(data, weight))
        self._huffman_tree = None
        while tree_node_all:
            tree_node_all.sort(reverse=True, key=lambda x: x.weight)
            node_left = tree_node_all.pop()
            if tree_node_all:
                node_right = tree_node_all.pop()
                tree_node_all.append(TreeNode(node_left.data + node_right.data, node_left.weight + node_right.weight,
                                              node_left, node_right))
            else:
                self._huffman_tree = node_left

    @property
    def huffman_tree(self):
        return self._huffman_tree

    def __repr__(self):
        tree_node_level = [self._huffman_tree]
        result = ""
        while tree_node_level:
            tree_node_level_next = []
            for tree_node in tree_node_level:
                if tree_node is not None:
                    result += str(tree_node.data)
                    if tree_node.left is not None:
                        result += "->" + str(tree_node.left.data) + "," + str(tree_node.right.data)
                        tree_node_level_next.append(tree_node.left)
                        tree_node_level_next.append(tree_node.right)
                    result += ";"
            result += "\n"
            tree_node_level = tree_node_level_next
        return result


def main():
    val_insert = []
    for i in range(1, 10):
        val_insert.append([i, i])
    huffman_tree = HuffmanTree(val_insert)
    print(huffman_tree)


if __name__ == "__main__":
    main()
