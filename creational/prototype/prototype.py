#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/3
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import abstractmethod, ABCMeta


class Prototype(metaclass=ABCMeta):
    """
    原型对象使用的基类
    """

    def __init__(self, info: str):
        self._info = info

    @abstractmethod
    def clone(self):
        """
        原型对象使用的copy方法，需要用户进行实现
        :return:
        """
        pass


class Logo(Prototype):
    """
    logo类，继承了原型原型基类
    """
    def __init__(self, info):
        super(Logo, self).__init__(info)

    def clone(self):
        """
        实现clone方法
        :return:
        """
        logo = Logo(self._info)
        return logo


class OS(Prototype):
    """
    os类，实现克隆基类
    """
    def __init__(self, info):
        super(OS, self).__init__(info)

    def clone(self):
        """
        实现clone方法
        :return:
        """
        os = OS(self._info)
        return os
