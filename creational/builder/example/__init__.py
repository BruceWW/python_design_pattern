#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/4
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from abc import ABCMeta, abstractmethod

from creational import Phone


class PhoneBuilder(metaclass=ABCMeta):
    def __init__(self):
        self._phone = Phone()

    @abstractmethod
    def add_cpu(self):
        pass

    @abstractmethod
    def add_os(self):
        pass

    @abstractmethod
    def add_name(self):
        pass

    def get_phone(self):
        return self._phone
