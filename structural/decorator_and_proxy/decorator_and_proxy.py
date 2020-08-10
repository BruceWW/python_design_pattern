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
            func(*inner_args, **inner_kwargs)

        return inner

    return wrapper

