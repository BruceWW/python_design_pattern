#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/17
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import abstractmethod
import sys


class Implementor(object):
    def __init__(self):
        pass

    @abstractmethod
    def get_location(self) -> (float, float):
        pass


class ProgramAbstraction(object):
    def __init__(self):
        self._imp = None

    @abstractmethod
    def _get_imp(self) -> Implementor:
        """
        这里做了单例处理
        :return:
        """
        if not self._imp:
            platform = sys.platform
            # 判断当前操作系统
            if platform == 'darwin':
                # mac
                pass
            elif platform == 'win32':
                # windows
                pass
            elif platform == 'linux':
                # linux
                pass
            else:
                # 其他
                pass

        return self._imp

    @abstractmethod
    def upload(self):
        pass


def mac_system_location() -> (str, str):
    """
    模拟mac系统返回坐标的系统api
    :return: tuple对象，一共两个对象，第一个为lon，第二个为lat，类型为字符串
    """
    print('this is mac location api')
    print('return a tuple object, and the type of element is string')
    return '120.1', '30.1'


def linux_system_location() -> str:
    """
    模拟linux系统返回坐标的系统api
    :return: 字符串对象，将lon和lat通过半角都好拼接
    """
    print('this is linux location api')
    print("return a string object")
    return '120.1,30.1'


def windows_system_location() -> (float, float):
    """
    模拟windows系统返回坐标的系统api
    :return: tuple对象，一共两个对象，第一个为lon，第二个为lat，类型为浮点
    """
    print('this is windows location api')
    print('return a tuple object, and the type of element is float')
    return 120.1, 30.1
