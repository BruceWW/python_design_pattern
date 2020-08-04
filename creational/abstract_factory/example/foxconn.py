#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/3
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational.abstract_factory.example import PhoneFactory


class iPhoneKit(PhoneFactory):
    """
    具体的iphone抽象工厂
    """

    def os(self) -> str:
        """
        返回操作系统实例
        :return:
        """
        return 'ios'

    def cpu(self) -> str:
        """
        返回cpu实例
        :return:
        """
        return 'a13'

    def name(self) -> str:
        """
        返回手机信息实例
        :return:
        """
        return 'iphone 11'


class SamsungS20Kit(PhoneFactory):
    def os(self) -> str:
        return 'android'

    def cpu(self) -> str:
        return 'adreno650'

    def name(self) -> str:
        return 'samsung s20'


class HuaweiMate30Kit(PhoneFactory):
    def os(self) -> str:
        return 'android'

    def cpu(self) -> str:
        return 'kirin990'

    def name(self) -> str:
        return 'huawei mate30'


class Foxconn(object):
    """
    以富士康为例，创建一个富士康类
    """
    @staticmethod
    def produce(abstract_factory: PhoneFactory.__subclasses__()):
        """
        静态方法，用于生产手机，及其部件并进行组装
        :param abstract_factory: 手机的抽象工厂类
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


if __name__ == '__main__':
    # 这里可以不进行实例化，直接调用静态方法
    foxconn_line = Foxconn
    foxconn_line.produce(iPhoneKit)
    foxconn_line.produce(SamsungS20Kit)
    foxconn_line.produce(HuaweiMate30Kit)
