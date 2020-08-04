#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/2
# @Author : Bruce Liu / Lin Luo
# @Mail   : 15869300264@163.com
class Phone(object):
    """
    公共的手机类
    作为各种创建模式的创建目标
    存储了手机的os、cpu以及名称等属性
    为了简化模型，所有属性都采用字符串进行表示
    """

    def __init__(self):
        self._os = None
        self._cpu = None
        self._name = None

    @property
    def os(self) -> str:
        return self._os

    @os.setter
    def os(self, os: str) -> None:
        self._os = os

    @property
    def cpu(self) -> str:
        return self._cpu

    @cpu.setter
    def cpu(self, cpu: str) -> None:
        self._cpu = cpu

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def information(self) -> str:
        """
        返回手机信息
        :return:
        """
        return f"this is {self._name}, it's cpu is {self._cpu} and it's os is {self._os}"
