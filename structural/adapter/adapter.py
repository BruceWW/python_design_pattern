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
    def upload(self, lon: str, lat: str):
        """
        alpha系统调用的函数名称为upload，入参是lon和lat，类型是字符串
        :param lon:
        :param lat:
        :return:
        """
        pass


class ProgramAlphaAdapter(ProgramAdaptee, AlphaTarget):
    """
    Alpha系统的适配器，继承两个类
    Program类为适配器的被适配方（adaptee），提供数据上传服务
    AlphaTarget为适配器的目标方（target），提供被调用的接口，并重写接口的逻辑来调用被适配方的函数
    """

    def upload(self, lon: str, lat: str):
        """
        Alpha系统调用的接口传入的经纬度为字符串类型，需要修改类型后再调用adaptee的方法
        重写target的方法，实现类型的转换以打到适配器的目的
        :param lon:
        :param lat:
        :return:
        """
        # 将字符串转为浮点型，并调用_location方法
        self._location(float(lon), float(lat))
