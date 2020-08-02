#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/2
# @Author : Bruce Liu / Lin Luo
# @Mail   : 15869300264@163.com


class SingletonByNewMethod(object):
    """
    使用构造函数实现单例
    所有继承的子类在执行构造函数时，自动执行单例创建　
    这里的思路使用了懒汉模式
    """

    def __new__(cls, *args, **kwargs):
        # 判断类变量中是否有singleton属性
        if not hasattr(cls, '_instance'):
            # 如果没有singleton属性，则调用super方法，创建一个实例并赋予singleton属性
            cls._instance = super().__new__(cls)
            print('return instance by created')
            return cls._instance
        else:
            print('return instance from class attribute')
            return cls._instance


def singleton_proxy(cls):
    """
    函数装饰器
    这里使用了python的修饰器方法，但实际上这个属于代理模式，所以使用proxy命名
    同时python的修饰器方法，使用了典型的面向函数变成闭包思想
    :param cls: 需要实例化的类
    :return:
    """
    # 用于存储已实例话的对象
    _instances = {}

    def inner(*args, **kwargs):
        # 调用外部函数的变量判断传入的类是否已经被实例化
        if cls in _instances:
            print('return instance from outer attribute')
            return _instances[cls]
        else:
            _instances[cls] = cls(*args, **kwargs)
            print('return instance by created')
            return _instances[cls]

    return inner


class SingletonProxy(object):
    """
    类装饰器
    这里使用了python的修饰器方法，但实际上这个属于代理模式，所以使用proxy命名
    """

    def __init__(self, cls):
        """
        类装饰器初始化函数
        :param cls: 需要实例化的类
        """
        self._cls = cls
        self._instances = {}

    def __call__(self, *args, **kwargs):
        """
        类装饰器需要实现__call__方法，用于自身的调用
        :param args:
        :param kwargs:
        :return:
        """
        if self._cls in self._instances:
            print('return instance from class proxy attribute')
            return self._instances[self._cls]
        else:
            self._instances[self._cls] = self._cls(*args, **kwargs)
            print('return instance by created')
            return self._instances[self._cls]


class SingletonMetaClass(type):
    """
    元类，即创建类的类
    使用元类在对象实例化时实现单例操作
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print('return instance by created')
            cls._instances[cls] = super().__call__(cls, *args, **kwargs)
            return cls._instances[cls]
        else:
            print('return instance from metaclass')
            return cls._instances[cls]
