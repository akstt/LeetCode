"""
集合的查找和并操作
"""


class SetClass:
    def __init__(self, val_insert):
        """
        :param val_insert: [[val, parent_index]...]如果为根节点，则parent_index为该集合的size的相反数
        """
        self._set = val_insert

    def find(self, val):
        """
        :param val: 需要查找的值
        :return: val所在集合根节点的索引
        """
        index_target = -1
        for index_val in range(0, len(self._set)):
            if self._set[index_val] == val:
                index_target = index_val
                break
        if index_target == -1:
            return -1
        else:
            while self._set[index_target][1] > 0:
                index_target = self._set[index_target][1]
            return index_target

    def union(self, val_1, val_2):
        """
        :param val_1: 需要并操作的集合中的值
        :param val_2: 需要并操作的集合中的值
        """
        index_1 = self.find(val_1)
        index_2 = self.find(val_2)
        if index_1 != index_2:
            if self._set[index_1][1] < self._set[index_2][1]:
                self._set[index_1][1] += self._set[index_2][1]
                self._set[index_2][1] = index_1
            else:
                self._set[index_2][1] += self._set[index_1][1]
                self._set[index_1][1] = index_2
