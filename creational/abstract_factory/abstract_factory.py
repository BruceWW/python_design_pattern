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
        """
        直接返回一个新建的手机实例
        可以理解为一个空手机
        :return:
        """
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


class ConcretePhone(PhoneFactory):
    """
    具体实现抽象工厂的手机类
    可以理解为一个具体的手机
    """

    def os(self) -> str:
        """
        返回concrete phone的操作系统，（返回的操作系统是一个已经实现的整体）
        :return:
        """
        return 'os'

    def cpu(self) -> str:
        """
        返回concrete phone的cpu，（返回的cpu是一个已经实现的整体）
        :return:
        """
        return 'cpu'

    def name(self) -> str:
        """
        返回concrete phone的信息，（返回的手机信息是一个已经实现的整体）
        :return:
        """
        return 'name'
