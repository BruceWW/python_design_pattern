#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/25
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
class Component(object):
    def __init__(self, name: str, price: int, sub_components: iter = None):
        if sub_components:
            self.sub_components = sub_components
        else:
            self.sub_components = []
        self.name = name
        self.price = price

    def add_sub_components(self, sub_component: object) -> None:
        """
        添加子组件
        :param sub_component:
        :return:
        """
        self.sub_components.append(sub_component)

    def get_sub_components_obj(self):
        """
        获取子组件的迭代器
        :return:
        """
        yield self.sub_components

    def get_sub_component_info(self, level: int = 1) -> None:
        """
        获取子节点组件信息
        :param level:
        :return:
        """
        for sub_component in self.sub_components:
            sub_component.get_info(level + 1)

    def get_info(self, level: int = 0) -> None:
        """
        获取设备信息，同时获取子节点信息
        :param level:
        :return:
        """
        space = '\t' * level
        print(f'{space} component name: {self.name}')
        print(f'{space} component price: {self.price}')
        if self.sub_components:
            print(f'{space} here are the sub components of {self.name}')
            self.get_sub_component_info(level)


def make_pro_composites():
    """
    组合模式样例1
    :return:
    """
    phone_pro = Component('phone pro', 4999)
    screen_national = Component('national 2k screen', 300)
    camera = Component('leica adjusted camera', 250)
    mother_board = Component('pro mother board', 400)
    soc = Component('990', 200)
    memory = Component('64G', 80)
    battery = Component('5000mah', 300)
    phone_pro.sub_components = [screen_national, camera, mother_board, battery]
    mother_board.sub_components = [soc, memory]
    return phone_pro


def make_composites():
    """
    组合模式样例1
    :return:
    """
    phone = Component('phone', 3999)
    screen_national = Component('true 2k screen', 500)
    camera = Component('leica adjusted camera', 250)
    mother_board = Component('mother board', 300)
    soc = Component('990', 200)
    memory = Component('64G', 80)
    battery = Component('4000mah', 240)
    phone.sub_components = [screen_national, camera, mother_board, battery]
    mother_board.sub_components = [soc, memory]
    return phone


if __name__ == '__main__':
    phone_pro = make_pro_composites()
    print('this is the pro module info')
    phone_pro.get_info()
    phone = make_composites()
    print()
    print('this is the normal module info')
    phone.get_info()
