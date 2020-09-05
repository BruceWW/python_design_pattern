#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/9/4
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com


class Bank(object):
    def __init__(self, accounts: dict):
        self._accounts = accounts

    def add_account(self, account: str, surplus: int) -> bool:
        """
        添加账户
        :param account: 账户
        :param surplus: 余额
        :return:
        """
        if account in self._accounts:
            return False
        else:
            self._accounts[account] = {'surplus': surplus}
            return True

    def check_account(self, account) -> bool:
        """
        检查账户是否存在
        :param account:
        :return:
        """
        return account in self._accounts

    def check_surplus(self, account: str, surplus: int) -> int:
        """
        校验account账户是否存在，且余额是否大于检测额度
        :param account: 账户名
        :param surplus: 检测额度
        :return:
        """
        if account in self._accounts:
            if surplus >= self._accounts[account]['surplus']:
                return 0
            else:
                return 1
        else:
            return 3

    def pre_trans_in(self, account: str, amount: int) -> bool:
        """
        转入准备
        :param account:
        :param amount:
        :return:
        """
        # 检查转账金额是否大于0
        if amount <= 0:
            return False
        # 检查账户是否存在
        if account is self._accounts:
            #  检查账户是否有未完成的转账
            if self._accounts[account]['locked'] != 0:
                return False
            else:
                # 转账款冻结
                self._accounts[account]['locked'] = amount
                return True
        else:
            return False

    def pre_trans_out(self, account: str, amount: int) -> bool:
        """
        转出准备
        :param account:
        :param amount:
        :return:
        """
        # 检查转账金额是否大于0
        if amount <= 0:
            return False
        # 检查账户是否存在
        if account is self._accounts:
            # 检查余额是否大于转账金额及是否有未完成的转账
            if self._accounts[account]['surplus'] >= amount and self._accounts[account]['locked'] == 0:
                self._accounts[account]['locked'] -= amount
            else:
                return False
        else:
            return False

    def confirm(self, account: str) -> bool:
        """
        完成转账
        :param account:
        :return:
        """
        if account in self._accounts:
            self._accounts[account]['surplus'] += self._accounts[account]['locked']
            self._accounts[account]['locked'] = 0
            return True
        else:
            return False


class AccountManager(object):
    def __init__(self, accounts: dict):
        self._accounts = accounts

    def add_account_mapping(self, account: str, bank: Bank) -> bool:
        if account in self._accounts:
            return False
        else:
            self._accounts[account] = bank

    def get_bank_by_account(self, account: str) -> Bank:
        if account in self._accounts:
            return self._accounts[account]
