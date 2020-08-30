#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/4
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from functools import wraps


def function_decorator(func):
    """
    函数修饰器，修饰器不接受其他参数
    :param func:
    :return:
    """

    # 使用wraps修饰器，将被修饰函数的属性赋予修饰器
    @wraps(func)
    def inner(*args, **kwargs):
        """
        修饰器内部函数
        :param args:
        :param kwargs:
        :return:
        """
        # 修饰器添加的相关逻辑
        func(*args, **kwargs)
        # 修饰器添加的相关逻辑

    return inner


def function_decorator_with_params(*args, **kwargs):
    """
    修饰器函数，修饰器接受其他参数
    :param args:
    :param kwargs:
    :return:
    """

    def wrapper(func):
        # 使用wraps修饰器，将被修饰函数的属性赋予修饰器
        @wraps(func)
        def inner(*inner_args, **inner_kwargs):
            """
            修饰器内部函数
            :param inner_args:
            :param inner_kwargs:
            :return:
            """
            # 修饰器添加的相关逻辑
            func(*inner_args, **inner_kwargs)
            # 修饰器添加的相关逻辑

        return inner

    return wrapper


class Card(object):
    """
    卡片类
    """

    def __init__(self, name: str, limited: bool = False, limited_num: int = 100000, surplus: int = 0):
        """
        初始化一张卡
        :param limited: 是否限额
        :param limited_num: 限额数量
        :param surplus: 余额
        """
        self.name = name
        # 是否限额
        self.limited = limited
        # 限额总数
        self.limited_num = limited_num
        # 余额
        self.surplus = surplus
        # 本次操作的金额
        self.operator_num = 0

    def __add__(self, other) -> bool:
        """
        将other中本次操作的金额转移到self对象中
        即从other中划一部分钱到本卡
        :param other:
        :return:
        """
        # 判断是否可以转账
        if (self.limited and self.surplus + other.operator_num > self.limited_num) or other.surplus - other.operator_num < 0:
            return False
        else:
            # 可以转入
            self.surplus += other.operator_num
            other.surplus -= other.operator_num
            other.operator_num = 0
            return True

    def __sub__(self, other) -> bool:
        """
        将本卡中的一部分钱转到otehr中
        :param other:
        :return:
        """
        # 判断是否可以转账
        if self.surplus - self.operator_num >= 0 and (
                not other.limited or other.surplus + self.operator_num <= other.limited_num):
            self.surplus -= self.operator_num
            other.surplus += self.operator_num
            self.operator_num = 0
            return True
        else:
            return False
