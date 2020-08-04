#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/4
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import ABCMeta, abstractmethod

from creational import Phone


class PhoneBuilder(metaclass=ABCMeta):
    """
    生成器的抽象类，里面提供了所需的抽象方法
    继承了抽象工厂类的子类，需要实现所有抽象方法
    生成器在于一步步进行装配，然后最后返回创建的对象
    """

    def __init__(self):
        """
        在类进行初始化时，就创建一个具体的手机实例，用于装配
        """
        self._phone = Phone()

    @abstractmethod
    def add_cpu(self) -> None:
        """
        向手机实例中装配cpu
        :return:
        """
        pass

    @abstractmethod
    def add_os(self) -> None:
        """
        向手机实例中装配os
        :return:
        """
        pass

    @abstractmethod
    def add_name(self) -> None:
        """
        向手机实例装配置信息
        :return:
        """
        pass

    def get_phone(self):
        """
        返回手机配置完的手机实例
        :return:
        """
        return self._phone


class ConcretePhoneBuilder(PhoneBuilder):
    """
    具体实现生成器的手机类
    """
    def add_os(self):
        """
        生成os，并直接在手机实例中装配os
        :return:
        """
        self._phone.os = 'os'

    def add_cpu(self):
        """
        生成cpu，并直接在手机实例中装配cpu
        :return:
        """
        self._phone.cpu = 'cpu'

    def add_name(self):
        """
        生成手机信息，并直接在手机实例中配置手机信息
        :return:
        """
        self._phone.name = 'name'
