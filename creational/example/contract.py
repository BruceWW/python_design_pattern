#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/10
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational.example.component import Os, Logo, Mould, MotherBoard, MotherBoardHigh
from creational.example.pipeline import Pipeline
from creational.example.supplier import SupplierBuilder, SupplierAlpha, SupplierBeta


class Contract(object):
    def __init__(self, first_part: str, second_part: str, num: int, mother_board: MotherBoard.__subclasses__(),
                 os: Os.__subclasses__(), logo: Logo.__subclasses__(), mould: Mould.__class__):
        """
        合同模版
        同时带有试制和量产的操作
        某种意义上，合同类也是个工厂方法
        :param first_part: 甲方
        :param second_part: 乙方
        :param num: 订单数量
        :param mother_board: 主板
        :param os: 操作系统
        :param logo: logo
        :param mould: 模具厂
        """
        self._first_part = first_part
        self._second_part = second_part
        self._num = num
        self._supplier = self._mother_board_supplier(mother_board)
        self._os = os
        self._logo = logo
        self._mould = mould
        self._pipeline = Pipeline()

    @staticmethod
    def _mother_board_supplier(mother_board: MotherBoard.__subclasses__()) -> SupplierBuilder.__subclasses__():
        """
        主板供应商选择
        :param mother_board: 主板型号
        :return:
        """
        # 根据主板型号，获取供应商
        # 这里有更优雅的写法，大家可以去修改优化
        if issubclass(mother_board, MotherBoardHigh):
            # 高端主板供应商
            return SupplierAlpha
        else:
            # 低端主板供应商
            return SupplierBeta

    def trial_produce(self):
        """
        试制
        显示手机制造的整个过程及信息
        :return:
        """
        print('begin to trial produce')
        phone = self._pipeline.produce_phone(supplier=self._supplier, os=self._os, logo=self._logo,
                                             mould=self._mould)
        print('trial produce complete')
        return phone

    def produce(self):
        """
        量产
        这里不进行具体展示
        :return:
        """
        print('begin to produce')
        pass
        print(f'{self._num} products produced completed')
