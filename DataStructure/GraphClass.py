"""
图（Graph）:表示多对多的关系，包括：
    1.一组顶点：通常V（Vertex）表示顶点集合
    2.一组边：通常用E(Edge)表示边的集合
        1.边是定点对：（v, w）属于E，其中v和w属于V
        2.有向边<v, w>表示v指向w的边
        3.不考虑重边和自回路
数据对象集：G(V,E)由非空的有限顶点集合V和一个有限边集合E组成
操作集：creat()：建立图
        insertVertex(v) 插入v
        insertEdge(e) 插入e
        DFS(v) 从v开始深度优先遍历
        BFS(v) 从v开始广度优先遍历
        shortestPath(v) 计算v到其它顶点的最短路径
        MST() 计算最小生成树
常见术语：无向图；有向图；网络（带权图）...
连通：如果v到w存在一条（无向）路径，则称v和w是连通的
路径：v到w的路径是一系列顶点{v,...,w}的集合，相邻顶点间有图中的边
路径长度：路径边数（如果带权，则为权重和）
简单路径：路径中所有顶点都不同
回路：起点等于终点的路径
连通图：图中任意两顶点均连通
连通分量： 无向图的极大连通图（极大顶点数，极大边数）
强连通：有向图v和w之间存在双向路径
强连通图：任意两顶点均强连通
强连通分量：有向图的极大强连通子图
"""

"""
邻接矩阵表示图
优点：1. 直观，简单，好理解
      2. 方便检查任意一对顶点间是否存在边
      3. 方便找任意顶点的所有邻接点
      4. 方便计算顶点的度
缺点：稀疏图浪费空间和时间
"""

"""
邻接表表示图：
优点：1. 方便找任一顶点的所有临接点
      2. 适合表示稀疏图
      3. 方便计算无向图的度,和有向图的出度；需要构造“逆邻接表”计算入度
缺点：不方便检查任意一对顶点间是否存在边
"""

"""
遍历：深度优先搜索（类似于树的先序遍历），广度优先搜索（类似于树的层次遍历）
"""
from collections import deque


# 有向图的邻接矩阵表示
class MatrixGraph:

    def __init__(self, vertex_num=0, edge=None):
        """
        用>=0的整数表示各个顶点，可以使用vertex_num*vertex_num的列表表示图
        :param vertex_num 顶点数目
        :param edge 形如[[v1, v2],...]表示v1到v2的边
        """
        self._vertex_num = 0
        self._graph = []
        self._search_num = 1
        self._if_search = []
        self.insert_vertex(vertex_num)
        if edge is not None:
            self.insert_edge(edge)

    @property
    def vertex_num(self):
        return self._vertex_num

    @property
    def graph(self):
        return self._graph

    def insert_vertex(self, n=1):
        """
        :param n: 插入顶点数量
        """
        self._vertex_num += n
        for vertex in self._graph:
            vertex.extend([0] * n)
        for i in range(n):
            self._graph.append([0]*self._vertex_num)
            self._if_search.append(self._search_num)

    def insert_edge(self, edges):
        """
        :param edges: 插入边
        """
        for start_vertex, end_vertex in edges:
            self._graph[start_vertex][end_vertex] = 1

    def DFT(self):
        """
        深度优先遍历
        """
        self._search_num = -self._search_num
        for i in range(self._vertex_num):
            if self._if_search[i] != self._search_num:
                self._DFT_each_vertex(i)

    def _DFT_each_vertex(self, vertex_index):
        """
        :param vertex_index: 以vertex_index为起点，递归遍历图
        """
        print(vertex_index)
        self._if_search[vertex_index] = self._search_num
        for i in range(self._vertex_num):
            if self._graph[vertex_index][i] == 1 and self._if_search[i] != self._search_num:
                self._DFT_each_vertex(i)

    def BFT(self):
        """
        广度优先遍历
        """
        self._search_num = -self._search_num
        for i in range(self._vertex_num):
            if self._if_search[i] != self._search_num:
                self._BFT_each_vertex(i)

    def _BFT_each_vertex(self, vertex_index):
        """
        :param vertex_index: 以vertex_index为起点，循环遍历图
        """
        vertex_level = deque()
        vertex_level.append(vertex_index)
        self._if_search[vertex_index] = self._search_num
        while vertex_level:
            vertex_index_get = vertex_level.popleft()
            print(vertex_index_get)
            for i in range(self._vertex_num):
                if self._graph[vertex_index_get][i] == 1 and self._if_search[i] != self._search_num:
                    vertex_level.append(i)
                    self._if_search[i] = self._search_num

    def shortest_path(self, vertex_index):
        """
        :param vertex_index:
        :return: 获得vertex_index该顶点到其他顶点的最短路径及其长度
        """
        vertex_length = dict()
        path = dict()
        for i in range(self._vertex_num):
            vertex_length[i] = -1
        vertex_deque = deque()
        vertex_deque.append(vertex_index)
        vertex_length[vertex_index] = 0
        while vertex_deque:
            index_1 = vertex_deque.popleft()
            for index_2 in range(self._vertex_num):
                if self._graph[index_1][index_2] == 1 and vertex_length[index_2] == -1:
                    vertex_length[index_2] = vertex_length[index_1] + 1
                    path[index_2] = index_1
                    vertex_deque.append(index_2)
        return vertex_length, path


# 有向图的邻接表表示
class ListGraph:

    def __init__(self, vertex_num=0, edge=None):
        """
        用>=0的整数表示各个顶点，可以使用vertex_num的列表表示图,列表中的元素为链表，表示该顶点指向的顶点，为了方便，使用列表代替链表
        :param vertex_num 顶点数目
        :param edge 形如[[v1, v2],...]表示v1到v2的边
        """
        self._vertex_num = 0
        self._graph = []
        self._search_num = 1
        self._if_search = []

        self.insert_vertex(vertex_num)
        if edge is not None:
            self.insert_edge(edge)



    @property
    def vertex_num(self):
        return self._vertex_num

    @property
    def graph(self):
        return self._graph

    def insert_vertex(self, n=1):
        """
        :param n: 插入顶点数量
        """
        self._vertex_num += n
        for i in range(n):
            self._graph.append([])
            self._if_search.append(self._search_num)

    def insert_edge(self, edges):
        """
        :param edges: 插入边
        """
        for start_vertex, end_vertex in edges:
            if end_vertex not in self._graph[start_vertex]:
                self._graph[start_vertex].append(end_vertex)

    def DFT(self):
        """
        深度优先遍历
        """
        self._search_num = -self._search_num
        for i in range(self._vertex_num):
            if self._if_search[i] != self._search_num:
                self._DFT_each_vertex(i)

    def _DFT_each_vertex(self, vertex_index):
        """
        :param vertex_index: 以vertex_index为起点，递归遍历图
        """
        print(vertex_index)
        self._if_search[vertex_index] = self._search_num
        for i in self._graph[vertex_index]:
            if self._if_search[i] != self._search_num:
                self._DFT_each_vertex(i)

    def BFT(self):
        """
        广度优先遍历
        """
        self._search_num = -self._search_num
        for i in range(self._vertex_num):
            if self._if_search[i] != self._search_num:
                self._BFT_each_vertex(i)

    def _BFT_each_vertex(self, vertex_index):
        """
        :param vertex_index: 以vertex_index为起点，循环遍历图
        """
        vertex_level = deque()
        vertex_level.append(vertex_index)
        self._if_search[vertex_index] = self._search_num
        while vertex_level:
            vertex_index_get = vertex_level.popleft()
            print(vertex_index_get)

            for i in self._graph[vertex_index_get]:
                if self._if_search[i] != self._search_num:
                    vertex_level.append(i)
                    self._if_search[i] = self._search_num

    def shortest_path(self, vertex_index):
        """
        :param vertex_index:
        :return: 获得vertex_index该顶点到其他顶点的最短路径及其长度
        """
        vertex_length = dict()
        path = dict()
        for i in range(self._vertex_num):
            vertex_length[i] = -1
        vertex_deque = deque()
        vertex_deque.append(vertex_index)
        vertex_length[vertex_index] = 0
        while vertex_deque:
            index_1 = vertex_deque.popleft()
            for index_2 in self._graph[index_1]:
                if vertex_length[index_2] == -1:
                    vertex_length[index_2] = vertex_length[index_1] + 1
                    path[index_2] = index_1
                    vertex_deque.append(index_2)
        return vertex_length, path

def test():
    # graph = ListGraph(5, [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 1], [4, 1], [4, 2], [4, 3]])
    graph = MatrixGraph(5, [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 1], [4, 1], [4, 2], [4, 3]])
    graph.insert_vertex()
    graph.insert_edge([[5, 1], [5, 2], [1, 5]])
    # graph.DFT()
    print("===")
    # graph.BFT()
    length, path = graph.shortest_path(1)
    print(length)
    print(path)

if __name__ == "__main__":
    test()
