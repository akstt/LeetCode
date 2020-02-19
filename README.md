# LeetCode
1. 所有解法都是自己写的，如果和优秀题解的思路相比时间复杂度差不多，基本不会修改
2. 所有的解法都能经过测试，部分解法由于时间复杂度的原因可能无法通过leetcode的检验
3. 本来想写一些解题时的想法，但是看了leetcode上别人写的题解（图文并茂，思路清晰，种类齐全）后，确实有云泥之别，有兴趣的可以看leetcode上热门题解
4. 我不赞成在解题时，主要逻辑利用语言中自带的方法
# DataStructure
一些自己写的关于数据结构的类
## 线性表
1. [线性表的顺序存储和链式存储](./DataStructure/LinearList.py)
2. [队列的顺序存储和链式存储](./DataStructure/QueueClass.py)
3. [堆栈的顺序存储和链式存储](./DataStructure/StackClass.py)  
在写链式存储类的时候，我把结点类和存储类分开作为两个类。之后我感觉其实可以把这两个类合并成一个类

## 树
1. [二叉树的顺序存储和链式存储](.\\DataStructure\\TreeClass.py)  
二叉树的链式存储内部方法用递归实现；二叉树的顺序存储用循环实现（利用循环判断是否同构的方法暂时没想到简单好用的实现方法）
2. [二叉搜索树的链式存储](.\\DataStructure\\BinarySearchTreeClass.py)  
在以前链式存储类中如果结点的数据为None时，则会用None替代该结点（根节点除外）；但是在该类中当结点的数据为None时，则不会用None代替，值为None的结点代表空结点  
3. [堆的顺序存储](.\\DataStructure\\HeapClass.py)
4. [哈夫曼树的链式存储](.\\DataStructure\\HuffmanTreeClass.py)  
在构造哈夫曼树时，可以利用最小堆，不过需要对原来的堆类进行修改，暂时不适用堆来生成哈夫曼树
5. [集合的顺序存储](.\\DataStructure\\SetClass.py)  
只有固定几个元素的集合的查找和并操作