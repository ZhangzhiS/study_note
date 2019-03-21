"""
二叉查找树（英语：Binary Search Tree），也称为二叉搜索树、有序二叉树（ordered binary tree）或排序二叉树（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：
    1. 若任意节点的左子树不空，则左子树上所有节点的值都小于他的根节点的值。
    2. 若任意节点的右子树不空，则右子树上所有节点的值都大于他的根节点的值。
    3. 任意节点的左右子树也分别为二叉查找树。
    4. 没有键值相等的节点
二叉查找树于其他数据结构的优势在于查找、插入的时间复杂度较低。为O(log n)。
来源于：https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
"""


class Node(object):
    """
    节点类
    """

    def __init__(self, data=None):
        self.data = data
        self.l_child = None
        self.r_child = None


class BinarySearchTree(object):
    """
    二叉搜索树
    """

    def __init__(self, li=None):
        self.root = None
        # if li:
        #     self.root = self.insert(self.root, li[0])
        #     for value in li[1:]:
        #         self.insert(self.root, value)

    def insert(self, root, value):
        """数据的插入"""
        # print(root, value)
        if root is None:
            # 如果根节点为None，则初始化根节点
            root = Node(value)
        elif value < root.data:
            # 如果要插入的值小于根节点的值，则插入左子树中
            root.l_child = self.insert(root.l_child, value)
        else:
            # 如果要插入的值大于根节点的值，则插入右子树中
            root.r_child = self.insert(root.r_child, value)
        return root

    def in_order(self, root):
        if root:
            self.in_order(root.l_child)
            print(root.data, end=", ")
            self.in_order(root.r_child)


if __name__ == '__main__':
    lis = [62, 58, 88, 47, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 48, 50]
    btree = BinarySearchTree()
    for i in lis:
        if btree.root is None:
            btree.root = Node(lis[0])
        else:
            btree.insert(btree.root, i)
    btree.in_order(btree.root)