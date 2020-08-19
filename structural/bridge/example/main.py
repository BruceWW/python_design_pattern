#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/19
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
import sys

from structural.bridge.example import ProgramAbstraction, Implementor, mac_system_location, linux_system_location, \
    windows_system_location


class MacImp(Implementor):
    """
    模拟一个mac的implementor
    """

    def get_location(self) -> (float, float):
        """
        mac系统中获取坐标信息
        假设mac系统返回坐标的api为mac_sysytem_location
        返回的坐标为lon和lat，类型为字符串
        :return:
        """
        lon, lat = mac_system_location()
        return float(lon), float(lat)


class LinuxImp(Implementor):
    """
    模拟一个Linux系统的implementor
    """

    def get_location(self) -> (float, float):
        """
        linux系统中获取坐标的信息
        假设linux系统返回坐标的api为linux_system_location
        返回的坐标为一个字符串
        :return:
        """
        lon, lat = linux_system_location().split(',')
        return float(lon), float(lat)


class WindowsImp(Implementor):
    """
    模拟一个Windows系统的Implementor
    """

    def get_location(self) -> (float, float):
        """
        windows系统中获取坐标的信息
        假设windoes系统返回坐标的api为windows_system_location
        返回的坐标为一个字符串
        :return:
        """
        return windows_system_location()


class Program(ProgramAbstraction):
    def __init__(self):
        super(Program, self).__init__()
        self._get_imp()

    def _get_imp(self) -> Implementor:
        """

        :return:
        """
        if not self._imp:
            platform = sys.platform
            # 判断当前操作系统
            if platform == 'darwin':
                # mac
                print('system: mac')
                self._imp = MacImp()
            elif platform == 'win32':
                # windows
                print('system: windows')
                self._imp = WindowsImp()
            elif platform == 'linux':
                # linux
                print('system: linux')
                self._imp = LinuxImp()
            else:
                # 其他
                pass
        return self._imp

    def upload(self):
        lon, lat = self._get_imp().get_location()
        # 执行上传操作
        print(f'get location info lon:{lon}, lat:{lat}')


if __name__ == '__main__':
    # 生成一个程序，然后执行, 后去当前系统，并生成对应imp
    obj = Program()
    print('upload info')
    # 调用imp对象，获取系统的坐标信息，并上传
    obj.upload()
