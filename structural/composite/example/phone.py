#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/25
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
class Component(object):
    def __init__(self, name: str, price: int, sub_components: iter = None):
        self.sub_components = sub_components
        self.name = name
        self.price = price

    def get_sub_component_info(self):
        """

        :return:
        """
        for sub_component in self.sub_components:
            print(f'\t {sub_component}')
