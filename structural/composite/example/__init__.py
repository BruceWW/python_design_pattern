#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/20
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
class Node(object):
    """
    这是一个leetcode常用的模型，表示一个二叉树节点
    val是二叉树的值
    left是二叉树的左子节点
    right是二叉树的右子节点
    """

    def __init__(self, val: int = None, left=None, right=None):
        """

        :param val:
        :param left:
        :param right:
        """
        self.val = val
        self.left = left
        self.right = right


def tree_2_array(root):
    """
    将二叉树转换为数组
    :param root:
    :return:
    """
    if not root:
        return []
    res = []
    cur_layer = [root]
    while cur_layer:
        cur_list = []
        next_layer = []
        for node in cur_layer:
            if node == '.':
                cur_list.append('.')
            else:
                cur_list.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                else:
                    next_layer.append('.')
                if node.right:
                    next_layer.append(node.right)
                else:
                    next_layer.append('.')
        res.append(cur_list)
        cur_layer = next_layer
    return res


def print_node(root: Node.__subclasses__()):
    """
    将二叉树打印成树状徒刑
    :param root:
    :return:
    """
    # 先将二叉树转换为数组
    t = tree_2_array(root)
    n = len(t) - 1
    for i in range(1, n - 1):
        for j in range(2 * i):
            if t[i][j] == '.':
                t[i + 1].insert(j + 1, '.')
                t[i + 1].insert(j + 1, '.')
    result = ['   {}   '.format(t[0][0]), '  / \\  ', ' {}   {} '.format(t[1][0], t[1][1]), '/ \\ / \\',
              '{} {} {} {}'.format(*t[2])]
    for i in result[:2 * n - 1]:
        print(i)
    pass
