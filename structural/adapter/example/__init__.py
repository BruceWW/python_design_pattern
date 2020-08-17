#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/16
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
class ProgramAdaptee(object):
    """
    被适配的接口
    模拟一个程序用于获取用户信息并向服务器上传数据
    适配器被调用的方法一般使用私有函数，避免被用户直接调用
    """

    def __init__(self, user: str, age: int):
        """
        程序初始化，获取用户信息
        :param user:
        :param age:
        """
        self._user = user
        self._age = age

    def _location(self, lon: float, lat: float) -> None:
        """
        获取用户位置，并向服务器上传
        :param lon: 经度
        :param lat: 纬度
        :return:
        """
        print(f"the lon: {lon} it's type is {type(lon)} and lat is: {lat} it's type is {type(lat)}")
        self._post(lon, lat)

    def _post(self, lon: float, lat: float) -> None:
        """
        向服务器上传用户信息及位置
        :param lon: 经度
        :param lat: 维度
        :return:
        """
        print(f"post user info to server. "
              f"user'name: {self._user}, user's age: {self._age}, user's location: {lon},{lat}")
