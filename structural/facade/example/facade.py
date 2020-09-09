#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/9/8
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com


class Bank(object):
    """银行类，管理下属账户"""

    def __init__(self, accounts: dict):
        self._accounts = accounts

    def get_surplus(self, account: str):
        """
        获取余额
        :param account:
        :return:
        """
        if account in self._accounts:
            return self._accounts[account]['surplus']

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
            self._accounts[account] = {'surplus': surplus, 'locked': 0}
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
        if account in self._accounts:
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
        if account in self._accounts:
            # 检查余额是否大于转账金额及是否有未完成的转账
            if self._accounts[account]['surplus'] >= amount and self._accounts[account]['locked'] == 0:
                self._accounts[account]['locked'] -= amount
                return True
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
    """账户管理类，类似于央行，记录每个人的信息在哪些银行"""

    def __init__(self, accounts: dict):
        self._accounts = accounts

    def add_account_mapping(self, account: str, bank: Bank) -> bool:
        """
        添加账户记录
        :param account:
        :param bank:
        :return:
        """
        if account in self._accounts:
            return False
        else:
            self._accounts[account] = bank

    def get_bank_by_account(self, account: str) -> Bank:
        """
        获取账户所在银行
        :param account:
        :return:
        """
        if account in self._accounts:
            return self._accounts[account]


class ViMaPay(object):
    def __init__(self, account_mapping: AccountManager, banks: dict):
        """

        :param account_mapping:
        :param banks:
        """
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
        target_pre = target_bank.pre_trans_out(target_account, amount)
        # 执行交易
        if source_pre and target_pre:
            source_bank.confirm(source_account)
            target_bank.confirm(target_account)
            return True
        else:
            return False


def init():
    obj = ViMaPay(AccountManager({}), {'citi_bank': Bank({}), 'wells_fargo': Bank({})})
    obj.create_account('Bruce', 100, 'citi_bank')
    obj.create_account('Walk', 200, 'citi_bank')
    obj.create_account('Frank', 300, 'wells_fargo')
    obj.create_account('Catty', 400, 'wells_fargo')
    return obj


if __name__ == '__main__':
    obj = init()
    # 转账成功
    print(f"Catty's surplus before trans: {obj.query('Catty')}")
    print(f"Frank's surplus before trans: {obj.query('Frank')}")
    res = obj.trans('Catty', 'Frank', 300)
    print(f'trans result: {res}')
    print(f"Catty's surplus after trans: {obj.query('Catty')}")
    print(f"Frank's surplus after trans: {obj.query('Frank')}")

    print()
    # 余额不足，转账失败
    print(f"Walk's surplus before trans: {obj.query('Walk')}")
    print(f"Bruce's surplus before trans: {obj.query('Bruce')}")
    res = obj.trans('Walk', 'Bruce', 300)
    print(f'trans result: {res}')
    print(f"Walk's surplus after trans: {obj.query('Walk')}")
    print(f"Bruce's surplus after trans: {obj.query('Bruce')}")
