#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/16
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import abstractmethod
from structural.adapter.example import ProgramAdaptee


class AlphaTarget(object):
    """
    Alpha系统
    """

    @abstractmethod
    def upload(self, lon: str, lat: str) -> None:
        """
        alpha系统调用的函数名称为upload，入参是lon和lat，类型是字符串
        :param lon:
        :param lat:
        :return:
        """
        pass


class BetaTarget(object):
    """
    Beta系统
    """

    @abstractmethod
    def send(self, lonlat: str) -> None:
        """
        beta系统调用的函数名称为send，入参是lonlat，类型是字符串，由经度和维度组成，中间使用半角都好间隔
        :param lonlat:
        :return:
        """
        pass


class ProgramAlphaAdapter(ProgramAdaptee, AlphaTarget):
    """
    Alpha系统的适配器，继承两个类
    Program类为适配器的被适配方（adaptee），提供数据上传服务
    AlphaTarget为适配器的目标方（target），提供被调用的接口，并重写接口的逻辑来调用被适配方的函数
    """

    def upload(self, lon: str, lat: str) -> None:
        """
        Alpha系统调用的接口传入的经纬度为字符串类型，需要修改类型后再调用adaptee的方法
        重写target的方法，实现类型的转换以打到适配器的目的
        :param lon:
        :param lat:
        :return:
        """
        # 将字符串转为浮点型，并调用_location方法
        print('system Alpha method upload called')
        print(f'the original value is {lon} and {lat}, and original type is {type(lon)} and {type(lat)}, '
              'adapter trans string type data into float type.')
        self._location(float(lon), float(lat))


class ProgramBetaAdapter(ProgramAdaptee, BetaTarget):
    """
    Beta系统的适配器，继承两个类
    Program类为适配器的被适配方，提供数据上传服务
    BetaTarget为适配器的目标方，提供被调用的接口，并重写接口的逻辑来调用被适配方的函数
    """

    def send(self, lonlat: str) -> None:
        """
        Beta系统调用的接口传入的经纬度是一个组合的字符串，需要进行解析并转换类型后再调用adapterr的方法
        重写target的方法，实现类型的转换以打到适配器的目的
        :param lonlat:
        :return:
        """
        print('system Beta method send called')
        # 对传入的经纬度字符串进行解析
        print(f'the original value is: {lonlat} and the original type is {type(lonlat)}, '
              'adapter splits lonlat and trans string type into float type.')
        lon, lat = lonlat.split(',')
        # 调用adaptee的方法
        self._location(float(lon), float(lat))


if __name__ == '__main__':
    # 客户端alpha实例化了一个Alpha的适配器，并调用upload方法
    client_alpha = ProgramAlphaAdapter('Frankee', 18)
    client_alpha.upload('120', '30')
    print()
    # 客户端beta实例化了一个Beta的适配器，并调用send方法
    client_beta = ProgramBetaAdapter('Jon', 56)
    client_beta.send('120,30')
