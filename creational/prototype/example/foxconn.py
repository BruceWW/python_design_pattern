#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/7
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational import Phone
from creational.prototype.example import Prototype, compare


class Logo(Prototype):
    """
    logo类，继承了原型原型基类
    """

    def __init__(self, info):
        super(Logo, self).__init__(info)

    def clone(self):
        """
        实现clone方法
        :return:
        """
        logo = Logo(self._info)
        return logo


class OS(Prototype):
    """
    os类，实现克隆基类
    """

    def __init__(self, info):
        super(OS, self).__init__(info)

    def clone(self):
        """
        实现clone方法
        :return:
        """
        # 返回一个os对象，被返回的对象与原始对象所有属性都一样，但是是两个不同的实例
        os = OS(self._info)
        return os


class Foxconn(object):
    """
    以富士康为例，创建一个富士康类
    """

    @staticmethod
    def package(phone: Phone, os: OS, logo: Logo):
        """
        静态方法，用于给一个已经生产完的手机添加操作系统和logo
        :param phone:
        :param os:
        :param logo:
        :return:
        """
        # 为手机添加一份克隆的os，类似cv
        phone.os = os.clone()
        # 为手机添加一个克隆的logo贴纸，类似复印
        # 偷懒使用了猴子补丁给phone对象添加属性
        setattr(phone, 'logo', logo.clone())
        print('os and logo had been add to the phone')
        print(f"it's logo is {phone.logo.info}")
        print(f"it's os is {phone.os.info}")


if __name__ == '__main__':
    foxconn = Foxconn()
    # 实例化一部手机
    phone1 = Phone()
    # 实例化一个iOS的系统
    os1 = OS('ios')
    # 实例化一个苹果的图标
    logo1 = Logo('apple')
    # 实例化另一部手机
    phone2 = Phone()
    # 实例化一个安卓系统
    os2 = OS('andriod')
    # 实例化一个三星的图标
    logo2 = Logo('samsung')
    # 在工厂中，给手机1装上os，并贴上图标
    foxconn.package(phone1, os1, logo1)
    # 比较原来的系统与被装上的系统之间的差别
    compare(os1, phone1.os)
    compare(logo1, phone1.logo)
    foxconn.package(phone2, os2, logo2, )
    compare(os2, phone2.os)
    compare(logo2, phone2.logo)
