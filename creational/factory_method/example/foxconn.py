#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/10
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational import Phone
from creational.factory_method.example import PhoneFactory
from creational.factory_method.example import iPhoneKit, SamsungS20Kit, HuaweiMate30Kit


class Product(object):
    """
    工厂模式类
    """

    @staticmethod
    def produce(phone_name: str) -> Phone.__subclasses__():
        """
        根据传入的数据返回对应的手机类
        :param phone_name:
        :return:
        """
        if phone_name == 'iphone':
            print('input string "iphone" and return iphone class')
            return iPhoneKit
        elif phone_name == 'samsung':
            print('input string "samsung" and return samsung class')
            return SamsungS20Kit
        elif phone_name == 'huawei':
            print('input string "huawei" and return huawei class')
            return HuaweiMate30Kit
        else:
            return None


class Foxconn(object):
    """
    以富士康为例，创建一个富士康类
    """

    @staticmethod
    def produce(abstract_factory: PhoneFactory.__subclasses__()):
        """
        静态方法，用于生产手机，及其部件并进行组装
        :param abstract_factory: 手机类（这个类是个抽象工厂）
        :return:
        """
        # 创建一个手机实例
        factory = abstract_factory()
        # 生产一个手机空壳
        phone = factory.phone()
        # 生产一个手机系统，并装配到手机上
        phone.os = factory.os()
        # 生产一个手机cpu，并装配到手机上
        phone.cpu = factory.cpu()
        # 生产一个手机信息，并配置到手机上
        phone.name = factory.name()
        print(f'a phone was produced and the phone factory is {factory.__class__.__name__}')
        print(phone.information())
        print()


if __name__ == '__main__':
    # 获取一个富士康，可以不进行实例化
    foxconn = Foxconn()
    # 调用工厂方法，获取iphone类
    iphone = Product.produce('iphone')
    # 成产一台iphone
    foxconn.produce(iphone)
    samsung = Product.produce('samsung')
    foxconn.produce(samsung)
    huawei = Product.produce('huawei')
    foxconn.produce(huawei)
