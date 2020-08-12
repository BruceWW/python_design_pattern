#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/6
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from creational.example.contract import Contract
from creational.example.component import MotherBoardHigh, OsNew, LogoAlpha, Mould, MotherBoardLow, OsPre, LogoBeta

if __name__ == '__main__':
    """
    这个例子里涉及了我们讲到的五种创建模式的使用
    我们继续扮演一个黑心小作坊老板
    """
    # 今天运气不错，签了一个10000台高配机器的订单
    print('get a contract')
    # 生成订单信息
    contract_alpha = Contract('alpha', 'Glory', 10000, MotherBoardHigh, OsNew, LogoAlpha, Mould)
    # 试制产品
    contract_alpha.trial_produce()
    # 进行量产
    contract_alpha.produce()

    print()
    # 又签了20000台低配机器的订单
    print('get another contract')
    contract_beta = Contract('beta', 'Glory', 20000, MotherBoardLow, OsPre, LogoBeta, Mould)
    contract_beta.trial_produce()
    contract_beta.produce()
