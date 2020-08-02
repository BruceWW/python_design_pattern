#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/2
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational.singleton.example import Nation, test


class SingletonMetaClass(type):
    """
    元类，即创建类的类
    使用元类在对象实例化时实现单例操作
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
        else:
            return cls._instances[cls]


class China(Nation, metaclass=SingletonMetaClass):
    def __init__(self, name: str = '中国'):
        super().__init__(name)


if __name__ == '__main__':
    print('using metaclass to create singleton')
    test('Bruce', 'Clerk', China)
