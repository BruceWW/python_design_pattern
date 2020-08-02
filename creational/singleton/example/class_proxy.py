#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/2
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational.singleton.example import Nation, test


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


@SingletonProxy
# 使用修饰器，在执行类的实例化时实现单例
class China(Nation):
    def __init__(self, name: str = '中国'):
        super().__init__(name)
        # 使用修饰器会由于修饰器的调用，China会变成装饰器对象而不是原来的China类，导致调用失败
        # 解决方式为在修饰器的代码中植入一段内容，将被修饰的类的属性赋予修饰器对象
        # super(China, self).__init__(name)


if __name__ == '__main__':
    print('using class proxy to create singleton')
    test('Bruce', 'Clerk', China)
