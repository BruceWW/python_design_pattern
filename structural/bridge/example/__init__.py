#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/17
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import abstractmethod
import sys


class ProgramAbstraction(object):
    def __init__(self):
        self._imp = None
        self._view = None

    def _get_imp(self) -> None:
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


class Implementor(object):
    def __init__(self):
        pass

    @abstractmethod
    def get_location(self):
        pass
