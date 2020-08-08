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

    @property
    def info(self) -> str:
        return self._info

    @info.setter
    def info(self, info: str) -> None:
        self._info = info

    @abstractmethod
    def clone(self):
        """
        原型对象使用的copy方法，需要用户进行实现
        :return:
        """
        pass


def compare(obj1, obj2):
    print(f"the info of original obj is '{obj1.info}', and the info of obj on phone is '{obj2.info}'")
    print(f"the id of original obj is '{id(obj1)}', and the id of obj on phone is '{id(obj2)}'")
