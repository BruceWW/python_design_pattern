#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/24
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com


class ViMaPay(object):
    def __init__(self):
        self._account_mapping = None

    def system_init(self):
        """

        :return:
        """
        pass

    def trans(self, source_account: str, target_account: str, amount: int) -> bool:
        """
        执行转账
        :param source_account: 转出账户
        :param target_account: 转入账户
        :param amount: 转账金额
        :return:
        """
        source_bank = self._account_mapping.get_bank_by_account(source_account)
        target_bank = self._account_mapping.get_bank_by_account(target_account)
        source_pre = source_bank.pre_trans_in(source_account, amount)
        target_pre = target_bank.pre_trans_out(source_account, amount)
        if source_pre and target_pre:
            source_bank.confirm(source_account)
            target_bank.confirm(target_account)
            return True
        else:
            return False
