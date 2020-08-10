#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/6
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com

from creational.example.supplier import SupplierBuilder
from creational.example.component import Os, Logo, Mould, Product


class SingletonPipeline(object):
    """
    单例模式流水线基类
    无论外面刮风下雨，打雷吹逼，我始终如一，一，一
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


class Pipeline(SingletonPipeline):
    """
    流水线类，继承了单例的基类
    """

    def produce_phone(self, supplier: SupplierBuilder.__subclasses__(), os: Os.__subclasses__(),
                      logo: Logo.__subclasses__(), mould: Mould.__subclasses__()) -> Product:
        """
        手机制造方法，使用工厂模式，传入对应的类进行查u你更加爱你
        :param supplier: 供应商类
        :param os: 操作系统类
        :param logo: logo类
        :param mould: 模具类
        :return:
        """
        print(f'this is pipeline with id: {id(self)}')
        print('begin to produce a phone')
        print(f'stage 1: create the phone mould, model: {mould.__name__}')
        phone = mould()
        print(f'stage 2: order a mother board from supplier: {supplier.__name__}')
        mother_board_supplier = supplier()
        print(f'\t mother board supplier begin to build up the mother board')
        mother_board_supplier.add_cpu()
        mother_board_supplier.add_memory()
        mother_board_supplier.add_storage()
        print(f'\t mother board build up complete')
        print(f'\t get mother board from supplier')
        mother_board = mother_board_supplier.get_mother_board()
        print(f'stage 3: get a copy of os and logo from os:{os.__name__} and logo:{logo.__name__}')
        os_copy = os().clone()
        logo_copy = logo().clone()
        print(f'stage 4: install os into mother_board')
        mother_board.storage.os = os_copy
        print(f'stage 5: add the mother board into mould')
        phone.mother_board = mother_board
        print(f'stage 6: paste logo on the phone')
        phone.logo = logo_copy
        print('the phone had benn produced')
        print('here are the information:')
        phone.information()
        product = Product()
        product.mould = phone
        return product
