#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/2
# @Author : Bruce Liu / Lin Luo
# @Mail   : 15869300264@163.com


class Nation(object):
    """
    国家类
    这里可以将Nation定义为一个抽象类，但是由于我们在metaclass.py中使用了元类来实现单例，这里继承抽象类会导致元类冲突，所以没有使用抽象类
    meatclass=ABCMeta
    """

    def __init__(self, name: str = None):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


class Citizen(object):
    """
    公民类
    每个人只能隶属于一个国家实体
    """

    def __init__(self, name: str, nation: Nation = None):
        self._name = name
        self._nation = nation

    @property
    def name(self) -> str:
        return self._name

    @property
    def nation(self) -> Nation:
        return self._nation

    @nation.setter
    def nation(self, nation: Nation) -> None:
        self._nation = nation

    def nation_name(self) -> str:
        return self._nation.name


def test(citizen_one_name: str, citizen_two_name: str, nation_class: Nation.__subclasses__()) -> None:
    """
    测试函数
    :param citizen_one_name: 公民一的名字
    :param citizen_two_name: 共鸣二的名字
    :param nation_class: 已实现单例的国家类的子类
    :return:
    """
    # 创建公民一
    citizen_one = Citizen(citizen_one_name)
    # 创建一个国家实例
    nation_one = nation_class()
    citizen_one.nation = nation_one
    # 创建公民二
    citizen_two = Citizen(citizen_two_name)
    # 创建另一个国家实例
    nation_two = nation_class()
    citizen_two.nation = nation_two
    # 显示两个公民的国籍
    print(f"Citizen: {citizen_one.name}'s nation is {citizen_one.nation_name()}")
    print(f"Citizen: {citizen_two.name}'s nation is {citizen_two.nation_name()}")
    # 显示两次实例化生成的国家id
    print(f"citizen_one's nation id is {id(citizen_one.nation)}")
    print(f"citizen_two's nation id is {id(citizen_two.nation)}")
    # 判断两次实例化的国家是否为同一个对象
    print(f"citizen_one's nation are same with citizen_two's nation? {citizen_one.nation is citizen_two.nation}")
