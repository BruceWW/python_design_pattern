#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/6
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import ABCMeta, abstractmethod

from creational.example.component import MotherBoard, CpuHigh, CpuLow, MemoryHigh, MemoryLow, \
    StorageHigh, StorageLow, MotherBoardLow, MotherBoardHigh


class SupplierBuilder(metaclass=ABCMeta):
    def __init__(self):
        self._mother_board = None

    @abstractmethod
    def add_cpu(self) -> None:
        pass

    @abstractmethod
    def add_memory(self) -> None:
        pass

    @abstractmethod
    def add_storage(self) -> None:
        pass

    def get_mother_board(self) -> MotherBoard:
        return self._mother_board


class SupplierAlpha(SupplierBuilder):
    def __init__(self):
        super(SupplierAlpha, self).__init__()
        self._mother_board = MotherBoardHigh()

    def add_cpu(self) -> None:
        cpu = CpuHigh()
        self._mother_board.cpu = cpu

    def add_memory(self) -> None:
        memory = MemoryHigh()
        self._mother_board.memory = memory

    def add_storage(self) -> None:
        storage = StorageHigh()
        self._mother_board.storage = storage


class SupplierBeta(SupplierBuilder):
    def __init__(self):
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
