#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/6
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com


class SingletonPipeline(object):
    """
    单例模式流水线基类
    """

    def __new__(cls, *args, **kwargs):
        # 判断类变量中是否有singleton属性
        if not hasattr(cls, '_instance'):
            # 如果没有singleton属性，则调用super方法，创建一个实例并赋予singleton属性
            cls._instance = super().__new__(cls)
            print('return instance by created')
            return cls._instance
        else:
            print('return instance from class attribute')
            return cls._instance


class Pipeline(SingletonPipeline):
    """
    流水线类，继承了单例的基类
    """

    def produce_phone(self):
        """
        工厂方法
        :return:
        """
