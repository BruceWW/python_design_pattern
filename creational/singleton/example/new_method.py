#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/2
# @Author : Bruce Liu / Lin Luo
# @Mail   : 15869300264@163.com
from creational.singleton.example import Nation, test


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


class China(Nation, SingletonByNewMethod):
    """
    继承国家类和单例类
    """

    def __init__(self, name: str = '中国'):
        super().__init__(name)


if __name__ == '__main__':
    print('using __new__ method to create singleton')
    test('Bruce', 'Clerk', China)
