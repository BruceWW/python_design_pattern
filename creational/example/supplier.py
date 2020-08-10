#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/6
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import ABCMeta, abstractmethod

from creational.example.component import MotherBoard, CpuHigh, CpuLow, MemoryHigh, MemoryLow, \
    StorageHigh, StorageLow, MotherBoardLow, MotherBoardHigh


class SupplierBuilder(metaclass=ABCMeta):
    """
    主板供应商基类
    这是个生成器方法
    """
    def __init__(self):
        self._mother_board = None

    @abstractmethod
    def add_cpu(self) -> None:
        """
        添加cpu
        :return:
        """
        pass

    @abstractmethod
    def add_memory(self) -> None:
        """
        添加内存
        :return:
        """
        pass

    @abstractmethod
    def add_storage(self) -> None:
        """
        添加闪存
        :return:
        """
        pass

    def get_mother_board(self) -> MotherBoard:
        """
        返回制造完毕的主板
        :return:
        """
        return self._mother_board


class SupplierAlpha(SupplierBuilder):
    """
    Alpha供应商，主要提供高端主板
    """
    def __init__(self):
        """
        继承主板生成器类
        同时添加新属性_mother_board
        """
        super(SupplierAlpha, self).__init__()
        self._mother_board = MotherBoardHigh()

    def add_cpu(self) -> None:
        """
        实例化具体的cpu，并添加到主板上
        :return:
        """
        cpu = CpuHigh()
        self._mother_board.cpu = cpu

    def add_memory(self) -> None:
        """
        实例化具体的内存，并添加到主板上
        :return:
        """
        memory = MemoryHigh()
        self._mother_board.memory = memory

    def add_storage(self) -> None:
        """
        实例化具体的闪存，并添加到主板上
        :return:
        """
        storage = StorageHigh()
        self._mother_board.storage = storage


class SupplierBeta(SupplierBuilder):
    """
    beta供应商，主要提供低端主板
    """
    def __init__(self):
        """
        继承主板生成器类
        同时添加新属性_mother_board
        """
        super(SupplierBeta, self).__init__()
        self._mother_board = MotherBoardLow()

    def add_cpu(self) -> None:
        cpu = CpuLow()
        self._mother_board.cpu = cpu

    def add_memory(self) -> None:
        memory = MemoryLow()
        self._mother_board.memory = memory

    def add_storage(self) -> None:
        storage = StorageLow()
        self._mother_board.storage = storage
