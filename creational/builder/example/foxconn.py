#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/4
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational.builder.example import PhoneBuilder


class iPhoneBuilder(PhoneBuilder):
    """
    具体的iphone生成器
    """

    def add_os(self) -> None:
        """
        生成os，并装配到手机上
        :return:
        """
        self._phone.os = 'ios'

    def add_cpu(self) -> None:
        """
        生成cpu，并装配到手机上
        :return:
        """
        self._phone.cpu = 'a13'

    def add_name(self) -> None:
        """
        生成手机信息，并配置到手机上
        :return:
        """
        self._phone.name = 'iphone 11'


class SamsungS20Builder(PhoneBuilder):
    def add_os(self) -> None:
        self._phone.os = 'android'

    def add_cpu(self) -> None:
        self._phone.cpu = 'adreno650'

    def add_name(self) -> None:
        self._phone.name = 'samsung s20'


class HuaweiMate30Builder(PhoneBuilder):
    def add_os(self) -> None:
        self._phone.os = 'android'

    def add_cpu(self) -> None:
        self._phone.cpu = 'kirin 990'

    def add_name(self) -> None:
        self._phone.name = 'huawei 990'


class Foxconn(object):
    """
    以富士康为例，创建一个富士康类
    """
    @staticmethod
    def produce(phone_builder: PhoneBuilder.__subclasses__()):
        """
        静态方法，用于实例化生成器，并调用生成器的方法进行组装
        :param phone_builder: 手机的生成器类
        :return:
        """
        # 实例化一个手机生成器
        builder = phone_builder()
        # 装配os
        builder.add_os()
        # 装配cpu
        builder.add_cpu()
        # 配置手机信息
        builder.add_name()
        print(f'a phone was produced and the phone builder is {builder.__class__.__name__}')
        print(builder.get_phone().information())
        print()


if __name__ == '__main__':
    # 这里可以不进行实例化，直接调用静态方法
    foxconn_line = Foxconn()
    foxconn_line.produce(iPhoneBuilder)
    foxconn_line.produce(SamsungS20Builder)
    foxconn_line.produce(HuaweiMate30Builder)
