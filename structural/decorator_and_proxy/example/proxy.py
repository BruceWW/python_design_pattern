#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/30
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
class Card(object):
    """
    卡片类
    """

    def __init__(self, name: str, limited: bool = False, limited_num: int = 100000, surplus: int = 0):
        """
        初始化一张卡
        :param limited: 是否限额
        :param limited_num: 限额数量
        :param surplus: 余额
        """
        self.name = name
        # 是否限额
        self.limited = limited
        # 限额总数
        self.limited_num = limited_num
        # 余额
        self.surplus = surplus
        # 本次操作的金额
        self.operator_num = 0

    def __add__(self, other) -> bool:
        """
        将other中本次操作的金额转移到self对象中
        即从other中划一部分钱到本卡
        :param other:
        :return:
        """
        # 判断是否可以转账
        if (
                self.limited and self.surplus + other.operator_num > self.limited_num) or other.surplus - other.operator_num < 0:
            return False
        else:
            # 可以转入
            self.surplus += other.operator_num
            other.surplus -= other.operator_num
            other.operator_num = 0
            return True

    def __sub__(self, other) -> bool:
        """
        将本卡中的一部分钱转到otehr中
        :param other:
        :return:
        """
        # 判断是否可以转账
        if self.surplus - self.operator_num >= 0 and (
                not other.limited or other.surplus + self.operator_num <= other.limited_num):
            self.surplus -= self.operator_num
            other.surplus += self.operator_num
            self.operator_num = 0
            return True
        else:
            return False


def trans(source_card: Card, target_card: Card, trans_num: int):
    """
    执行转账
    :param source_card: 转出卡
    :param target_card: 转入卡
    :param trans_num: 转账金额
    :return:
    """
    print(f'trans 100 from {source_card.name} to {target_card.name}')
    print(f'surplus of source_card: {source_card.name} before trans: {source_card.surplus}')
    print(f'surplus of target_card: {target_card.name} before trans: {target_card.surplus}')
    source_card.operator_num = trans_num
    res = target_card + source_card
    print(f'transfer result: {res}')
    print(f'surplus of source_card: {source_card.name} after trans: {source_card.surplus}')
    print(f'surplus of target_card: {target_card.name} after trans: {target_card.surplus}')


if __name__ == '__main__':
    # 实例化三张卡
    # 第一张不限额，且有10000余额
    card_1 = Card('card_1', False, 100000, 10000)
    # 第二张限额1000，余额为0
    card_2 = Card('card_2', True, 1000, 0)
    # 第三章限额10000，余额为100
    card_3 = Card('card_3', True, 10000, 100)

    # 从第二张卡转100到第一张卡
    trans(card_2, card_1, 100)
    print()

    # 从第一张卡转2000到第三张卡
    trans(card_1, card_3, 2000)
    print()

    # 从第一张卡转999到第三张卡
    trans(card_1, card_2, 999)
    print()

    # 从第一张卡转2到第三张卡
    trans(card_1, card_2, 2)
    print()

    # 从第三张卡转10000到第一张卡
    trans(card_3, card_1, 10000)

