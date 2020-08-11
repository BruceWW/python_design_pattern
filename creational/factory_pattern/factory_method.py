#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/10
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational import Phone
from creational.factory_pattern.example import iPhoneKit, SamsungS20Kit, HuaweiMate30Kit


class Product(object):
    """
    工厂模式
    """

    @staticmethod
    def product(phone_name: str) -> Phone.__subclasses__():
        """
        根据传入的型号名称，返回对应型号的类
        :param phone_name:
        :return:
        """
        if phone_name == 'iphone':
            return iPhoneKit
        elif phone_name == 'samsung':
            return SamsungS20Kit
        elif phone_name == 'huawei':
            return HuaweiMate30Kit
        else:
            return None
