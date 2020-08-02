#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/2
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational.singleton.example import Nation, test


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


@singleton_proxy
# 使用修饰器，在执行类的实例化时实现单例
class China(Nation):
    def __init__(self, name: str = '中国'):
        super().__init__(name)
        # 使用修饰器会由于修饰器的调用，China会变成装饰器对象而不是原来的China类，导致调用失败
        # 解决方式为在修饰器的代码中植入一段内容，将被修饰的类的属性赋予修饰器对象
        # super(China, self).__init__(name)


if __name__ == '__main__':
    print('using method proxy to create singleton')
    test('Bruce', 'Clerk', China)
