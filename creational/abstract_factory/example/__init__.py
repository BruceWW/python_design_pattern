#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/3
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import ABCMeta, abstractmethod

from creational import Phone


class PhoneFactory(metaclass=ABCMeta):
    """
    抽象工厂类，里面提供了所需的抽象方法
    继承了抽象工厂类的子类，需要实现所有抽象方法
    抽象工厂着重于一个系列的产品创建，创建的对象直接返回
    """

    @staticmethod
    def phone():
        return Phone()

    @abstractmethod
    def os(self) -> str:
        """
        操作系统
        :return:
        """
        pass

    @abstractmethod
    def cpu(self) -> str:
        """
        手机cpu
        :return:
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """
        手机名称
        :return:
        """
        pass
