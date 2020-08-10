#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/10
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational import Phone
from creational.factory_method.example import iPhoneKit, SamsungS20Kit, HuaweiMate30Kit


class Product(object):
    @staticmethod
    def produce(phone_name: str) -> Phone.__subclasses__():
        if phone_name == 'iphone':
            return iPhoneKit
        elif phone_name == 'samsung':
            return SamsungS20Kit
        elif phone_name == 'huawei':
            return HuaweiMate30Kit
        else:
            return None
