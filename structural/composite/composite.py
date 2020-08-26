#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/20
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from structural.composite.example import Node


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
