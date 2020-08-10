#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/6
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import abstractmethod
from copy import deepcopy


class Component(object):
    """
    基础组建类
    包括了三个属性，名称、版本和信息
    """

    def __init__(self):
        self._name = None
        self._version = None
        self._info = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        self._version = version

    @property
    def info(self) -> str:
        return self._info

    @info.setter
    def info(self, info: str) -> None:
        self._info = info


class Prototype(object):
    """
    原型基类，提供了clone函数
    """

    @abstractmethod
    def clone(self):
        pass


class Os(Component, Prototype):
    """
    操作系统基类，继承了基础组建类和原型基类
    """

    def __init__(self):
        super(Os, self).__init__()
        self._name = 'android'
        self._version = '4.0'
        self._info = 'android operation system ver 4.0'

    def clone(self):
        """
        实现克隆方法，返回克隆的操作系统对象
        这里偷懒使用了python自带的deepcopy函数，也可以自行实例化一个Os类，然后将属性赋给新实例化的对象
        :return:
        """
        return deepcopy(self)


class OsPre(Os):
    """
    老版操作系统
    """

    def __init__(self):
        super(OsPre, self).__init__()


class OsNew(Os):
    """
    新版操作系统，
    在初始化时，修改了版本号和信息的内容
    """

    def __init__(self):
        super(OsNew, self).__init__()
        self._version = '6.0'
        self._info = 'android operation system ver 6.0'


class Cpu(Component):
    """
    cpu基类，继承了基础组建类
    """
    pass


class CpuLow(Cpu):
    """
    低端cpu类
    """

    def __init__(self):
        super(CpuLow, self).__init__()
        self._name = 'KR'
        self._version = '3000'
        self._info = 'cpu KR 3000'


class CpuHigh(Cpu):
    """
    高端cpu类
    """

    def __init__(self):
        super(CpuHigh, self).__init__()
        self._name = 'QT'
        self._version = '600'
        self._info = 'cpu QT 600'


class Memory(Component):
    """
    内存基类，继承了基础组建类
    """
    pass


class MemoryLow(Memory):
    """
    低端内存类
    """

    def __init__(self):
        super(MemoryLow, self).__init__()
        self._name = 'KTS 1'
        self._version = 'DDR3'
        self._info = 'KST 1 DDR3 2G'


class MemoryHigh(Memory):
    """
    高端内存类
    """

    def __init__(self):
        super(MemoryHigh, self).__init__()
        self._name = 'KTS 2'
        self._version = 'DDR4'
        self._info = 'KST 2 DDR4 4G'


class Logo(Component, Prototype):
    """
    logo基类，继承了基础组建类和原型基类
    """

    def __init__(self):
        """
        在基础组建类基础上增加了pic属性
        """
        super(Logo, self).__init__()
        self._pic = None

    @property
    def pic(self) -> str:
        return self._pic

    @pic.setter
    def pic(self, pic: str) -> None:
        self._pic = pic

    def clone(self):
        """
        实现clone方法
        :return:
        """
        return deepcopy(self)


class LogoAlpha(Logo):
    """
    具体logo类，定义了pic属性的值
    """

    def __init__(self):
        super(LogoAlpha, self).__init__()
        self._pic = 'alpha'


class LogoBeta(Logo):
    """
    具体logo类，定义了pic属性的值
    """

    def __init__(self):
        super(LogoBeta, self).__init__()
        self._pic = 'beta'


class Storage(Component):
    """
    闪存基类，继承了基础组建类
    """

    def __init__(self):
        """
        在基础组建类的基础上添加了os属性，即在闪存中存储的os
        """
        super(Storage, self).__init__()
        self._os = None

    @property
    def os(self) -> Os:
        return self._os

    @os.setter
    def os(self, os: Os) -> None:
        self._os = os


class StorageLow(Storage):
    """
    低端闪存类
    """

    def __init__(self):
        super(StorageLow, self).__init__()
        self._name = 'SS 1'
        self._version = 'eMMc'
        self._info = 'SS 1 eMMc 64G'


class StorageHigh(Storage):
    """
    高端闪存类
    """

    def __init__(self):
        super(StorageHigh, self).__init__()
        self._name = 'SS 2'
        self._version = 'UFS'
        self._info = 'SS 2 UFS 64G'


class MotherBoard(Component):
    """
    主板基类，继承了基础组建类
    """

    def __init__(self):
        """
        在基础组建类的基础上，增加了内存、cpu、闪存等属性
        """
        super().__init__()
        self._memory = None
        self._cpu = None
        self._storage = None

    @property
    def cpu(self) -> Cpu:
        return self._cpu

    @cpu.setter
    def cpu(self, cpu: Cpu) -> None:
        self._cpu = cpu

    @property
    def memory(self) -> Memory:
        return self._memory

    @memory.setter
    def memory(self, memory: Memory) -> None:
        self._memory = memory

    @property
    def storage(self) -> Storage:
        return self._storage

    @storage.setter
    def storage(self, storage: Storage) -> None:
        self._storage = storage


class MotherBoardLow(Component):
    """
    低端主板类
    """

    def __init__(self):
        super(MotherBoardLow, self).__init__()
        self._name = 'b350'
        self._version = '1.0'
        self._info = 'mother board b350'


class MotherBoardHigh(Component):
    """
    高端主板类
    """

    def __init__(self):
        super(MotherBoardHigh, self).__init__()
        self._name = 'h370'
        self._version = '1.0'
        self._info = 'mother board b370'


class Mould(Component):
    """
    基础模具类，继承了基础组建类
    """

    def __init__(self):
        """
        在基础组建类的基础上，增加了logo和主板
        """
        super(Mould, self).__init__()
        self._mother_board = None
        self._logo = None

    @property
    def mother_board(self) -> MotherBoard:
        return self._mother_board

    @mother_board.setter
    def mother_board(self, mother_board):
        self._mother_board = mother_board

    @property
    def logo(self) -> Logo:
        return self._logo

    @logo.setter
    def logo(self, logo: Logo) -> None:
        self._logo = logo

    def information(self):
        print(f'logo: {self.logo.pic}')
        print(f'mother board: {self.mother_board.info}')
        print(f'os: {self.mother_board.storage.os.info}')
        print(f'cpu: {self.mother_board.cpu.info}')
        print(f'memory: {self.mother_board.memory.info}')
        print(f'storage: {self.mother_board.storage.info}')


class Product(Component):
    """
    产品类
    """
    def __init__(self):
        super(Product, self).__init__()
        self._mould = None

    @property
    def mould(self) -> Mould:
        return self._mould

    @mould.setter
    def mould(self, mould: Mould) -> None:
        self._mould = mould
