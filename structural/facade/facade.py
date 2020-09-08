#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/24
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from structural.facade.example.facade import AccountManager


class ViMaPay(object):
    def __init__(self, account_mapping: AccountManager, banks: dict):
        self._account_mapping = account_mapping
        self._banks = banks

    def create_account(self, account_name: str, amount: int, bank: str) -> bool:
        """
        创建账户
        :param account_name: 账户名
        :param amount: 账户金额
        :param bank: 银行名
        :return:
        """
        if bank not in self._banks or amount < 0:
            return False
        else:
            if self._banks[bank].add_account(account_name, amount):
                self._account_mapping.add_account_mapping(account_name, self._banks[bank])
                return True
        return False

    def query(self, account_name: str) -> int:
        """
        查询账户余额
        :param account_name:
        :return:
        """
        bank = self._account_mapping.get_bank_by_account(account_name)
        if bank:
            return bank.get_surplus(account_name)
        else:
            return -1

    def trans(self, source_account: str, target_account: str, amount: int) -> bool:
        """
        执行转账
        门面方法，只需要转出数据和转入数据以及转账金额，不需要知道里面具体的银行类、央行类、用户类的操作接口
        :param source_account: 转出账户
        :param target_account: 转入账户
        :param amount: 转账金额
        :return:
        """
        # 去央行获取用户账户所在银行
        source_bank = self._account_mapping.get_bank_by_account(source_account)
        target_bank = self._account_mapping.get_bank_by_account(target_account)
        # 检查用户所在银行的余额及交易状态
        source_pre = source_bank.pre_trans_in(source_account, amount)
        target_pre = target_bank.pre_trans_out(source_account, amount)
        # 执行交易
        if source_pre and target_pre:
            source_bank.confirm(source_account)
            target_bank.confirm(target_account)
            return True
        else:
            return False
