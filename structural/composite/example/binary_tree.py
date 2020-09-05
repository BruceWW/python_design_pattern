#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/24
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from structural.composite.example import Node, print_node


class NodeWithParent(Node):
    """
    我们对leetcode原始的类进行改进
    添加parent属性，表示父节点
    """

    def __init__(self, val: int = None, left: Node.__subclasses__() = None, right: Node.__subclasses__() = None,
                 parent: Node.__subclasses__() = None):
        """
        在Node类的基础上增加parent属性
        :param val:
        :param left:
        :param right:
        :param parent:
        """
        super(NodeWithParent, self).__init__(val, left, right)
        self.parent = parent


if __name__ == '__main__':
    # 以查询二叉树为例
    # 生成根结点
    root = NodeWithParent(3)
    # 生成根结点直属的左右子节点，并直接为它配置父节点
    level_1_left = NodeWithParent(1, parent=root)
    level_1_right = NodeWithParent(5, parent=root)
    # 为根结点设置左右子节点
    root.left = level_1_left
    root.right = level_1_right
    # 生成四个叶子节点
    level_2_left_1 = NodeWithParent(0, parent=level_1_left)
    level_2_left_2 = NodeWithParent(4, parent=level_1_right)
    level_2_right_1 = NodeWithParent(2, parent=level_1_left)
    level_2_right_2 = NodeWithParent(6, parent=level_1_right)
    # 将叶子节点配置到根结点的左右子节点中
    level_1_left.left = level_2_left_1
    level_1_left.right = level_2_right_1
    level_1_right.left = level_2_left_2
    level_1_right.right = level_2_right_2
    print_node(root)
